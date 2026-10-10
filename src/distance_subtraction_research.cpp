#include <algorithm>
#include <cassert>
#include <chrono>
#include <cmath>
#include <cstdint>
#include <filesystem>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <limits>
#include <map>
#include <numeric>
#include <optional>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <tuple>
#include <unordered_map>
#include <utility>
#include <vector>

namespace fs = std::filesystem;
using std::cerr;
using std::cout;
using std::endl;
using std::string;
using std::vector;

struct GameComputation {
    int k = 0;
    int m = 0;
    int n_max = 0;
    vector<uint16_t> table;      // flat: (n * stride + previous_move)
    vector<uint16_t> start_sg;   // SG with no previous move
    vector<uint8_t> start_p;     // 1 iff start_sg[n] == 0
    int max_state_sg = 0;
};

struct ScanResult {
    int m = 0;
    int k = 0;
    int n_max = 0;
    std::optional<int> preperiod;
    std::optional<int> period;
    std::optional<double> p_density;
    string p_residues;
    string period_fingerprint;
    int max_start_sg = 0;
    int max_state_sg = 0;
    std::optional<int> exact_state_preperiod_upper_bound;
    std::optional<int> exact_state_period;
};

// -----------------------------------------------------------------------------
// Small helpers
// -----------------------------------------------------------------------------

static string to_hex64(uint64_t x) {
    std::ostringstream oss;
    oss << std::hex << std::setfill('0') << std::setw(16) << x;
    return oss.str();
}

static uint64_t fnv1a64(const uint8_t* data, size_t n) {
    uint64_t h = 1469598103934665603ULL;
    for (size_t i = 0; i < n; ++i) {
        h ^= static_cast<uint64_t>(data[i]);
        h *= 1099511628211ULL;
    }
    return h;
}

static uint64_t fnv1a64_u16(const uint16_t* data, size_t n) {
    uint64_t h = 1469598103934665603ULL;
    for (size_t i = 0; i < n; ++i) {
        uint16_t x = data[i];
        h ^= static_cast<uint8_t>(x & 0xff);
        h *= 1099511628211ULL;
        h ^= static_cast<uint8_t>((x >> 8) & 0xff);
        h *= 1099511628211ULL;
    }
    return h;
}

static string csv_escape(const string& s) {
    bool need_quotes = s.find_first_of(",\"\n\r") != string::npos;
    if (!need_quotes) return s;
    string out = "\"";
    for (char c : s) {
        if (c == '\"') out += "\"\"";
        else out += c;
    }
    out += '\"';
    return out;
}

static string opt_int(const std::optional<int>& x) {
    return x ? std::to_string(*x) : "";
}

static string opt_double(const std::optional<double>& x) {
    if (!x) return "";
    std::ostringstream oss;
    oss << std::setprecision(12) << *x;
    return oss.str();
}

// -----------------------------------------------------------------------------
// Core SG solver
// -----------------------------------------------------------------------------

GameComputation solve_game(int k, int m, int n_max) {
    if (k < 1) throw std::invalid_argument("k must be >= 1");
    if (m < 0) throw std::invalid_argument("m must be >= 0");
    if (n_max < 0) throw std::invalid_argument("n_max must be >= 0");
    if (k > 65534) throw std::invalid_argument("k is too large for uint16_t SG storage");

    const size_t stride = static_cast<size_t>(k + 1);
    const size_t total = static_cast<size_t>(n_max + 1) * stride;

    GameComputation comp;
    comp.k = k;
    comp.m = m;
    comp.n_max = n_max;
    comp.table.assign(total, 0);
    comp.start_sg.assign(static_cast<size_t>(n_max + 1), 0);
    comp.start_p.assign(static_cast<size_t>(n_max + 1), 0);
    comp.start_p[0] = 1;

    vector<uint16_t> children(static_cast<size_t>(k + 1), 0);
    vector<int> counts(static_cast<size_t>(k + 1), 0);
    vector<int> touched;
    touched.reserve(static_cast<size_t>(k + 1));

    for (int n = 1; n <= n_max; ++n) {
        const int limit = std::min(k, n);
        touched.clear();

        // Multiset of SG values reachable by unrestricted first moves.
        for (int r = 1; r <= limit; ++r) {
            uint16_t v = comp.table[static_cast<size_t>(n - r) * stride + static_cast<size_t>(r)];
            children[static_cast<size_t>(r)] = v;
            if (counts[static_cast<size_t>(v)] == 0) touched.push_back(static_cast<int>(v));
            ++counts[static_cast<size_t>(v)];
        }

        int global_mex = 0;
        while (global_mex <= k && counts[static_cast<size_t>(global_mex)] > 0) ++global_mex;

        comp.start_sg[static_cast<size_t>(n)] = static_cast<uint16_t>(global_mex);
        if (global_mex == 0) comp.start_p[static_cast<size_t>(n)] = 1;

        const size_t base = static_cast<size_t>(n) * stride;

        // For a fixed previous move s, only r in [s-m, s+m] become forbidden.
        // Removing options can only lower the mex, so after decrementing those
        // counts the local mex is min(global_mex, newly-missing SG values).
        for (int s = 1; s <= k; ++s) {
            const int lo = std::max(1, s - m);
            const int hi = std::min(limit, s + m);
            int local_mex = global_mex;

            if (lo <= hi) {
                for (int r = lo; r <= hi; ++r) {
                    const uint16_t v = children[static_cast<size_t>(r)];
                    int& c = counts[static_cast<size_t>(v)];
                    --c;
                    if (c == 0 && static_cast<int>(v) < local_mex) {
                        local_mex = static_cast<int>(v);
                    }
                }
            }

            comp.table[base + static_cast<size_t>(s)] = static_cast<uint16_t>(local_mex);
            comp.max_state_sg = std::max(comp.max_state_sg, local_mex);

            if (lo <= hi) {
                for (int r = lo; r <= hi; ++r) {
                    const uint16_t v = children[static_cast<size_t>(r)];
                    ++counts[static_cast<size_t>(v)];
                }
            }
        }

        for (int v : touched) counts[static_cast<size_t>(v)] = 0;
    }

    return comp;
}

// -----------------------------------------------------------------------------
// Period / exact state-cycle detection
// -----------------------------------------------------------------------------

std::optional<std::pair<int,int>> detect_eventual_period(
    const vector<uint8_t>& bits,
    int max_period,
    int min_repeats = 12,
    int min_tail = 300
) {
    const int L = static_cast<int>(bits.size());
    if (L < 3) return std::nullopt;

    const int max_p = std::min(max_period, std::max(1, L / std::max(2, min_repeats)));

    for (int p = 1; p <= max_p; ++p) {
        const int tail = std::max(min_tail, p * min_repeats);
        if (tail + p > L) continue;

        const int start = L - tail - p;
        bool tail_match = true;
        for (int i = L - p - 1; i >= start; --i) {
            if (bits[static_cast<size_t>(i)] != bits[static_cast<size_t>(i + p)]) {
                tail_match = false;
                break;
            }
        }
        if (!tail_match) continue;

        int last_mismatch = -1;
        for (int i = 0; i < L - p; ++i) {
            if (bits[static_cast<size_t>(i)] != bits[static_cast<size_t>(i + p)]) {
                last_mismatch = i;
            }
        }

        const int pre = last_mismatch + 1;
        if (L - pre >= p * min_repeats) return std::make_pair(pre, p);
    }

    return std::nullopt;
}

static bool equal_u16_window(
    const vector<uint16_t>& table,
    size_t a,
    size_t b,
    size_t len
) {
    return std::equal(table.begin() + static_cast<std::ptrdiff_t>(a),
                      table.begin() + static_cast<std::ptrdiff_t>(a + len),
                      table.begin() + static_cast<std::ptrdiff_t>(b));
}

std::optional<std::pair<int,int>> detect_exact_full_state_cycle(
    const GameComputation& comp,
    std::optional<int> max_end = std::nullopt
) {
    const int k = comp.k;
    const size_t stride = static_cast<size_t>(k + 1);
    const int n_max = std::min(comp.n_max, max_end.value_or(comp.n_max));
    const int first_end = 2 * k - 1;
    if (n_max < first_end) return std::nullopt;

    std::unordered_map<uint64_t, vector<int>> seen;
    const size_t block_len = static_cast<size_t>(k) * stride;

    for (int end = first_end; end <= n_max; ++end) {
        const int start = end - k + 1;
        const size_t left = static_cast<size_t>(start) * stride;
        const uint64_t digest = fnv1a64_u16(comp.table.data() + left, block_len);

        auto it = seen.find(digest);
        if (it != seen.end()) {
            for (int old_end : it->second) {
                const int old_start = old_end - k + 1;
                const size_t old_left = static_cast<size_t>(old_start) * stride;
                if (equal_u16_window(comp.table, old_left, left, block_len)) {
                    return std::make_pair(old_start, end - old_end);
                }
            }
        }
        seen[digest].push_back(end);
    }

    return std::nullopt;
}

ScanResult period_description(
    const GameComputation& comp,
    int max_period,
    int min_repeats
) {
    ScanResult r;
    r.m = comp.m;
    r.k = comp.k;
    r.n_max = comp.n_max;
    r.max_state_sg = comp.max_state_sg;
    r.max_start_sg = static_cast<int>(*std::max_element(comp.start_sg.begin(), comp.start_sg.end()));

    auto det = detect_eventual_period(comp.start_p, max_period, min_repeats);
    if (!det) return r;

    const int pre = det->first;
    const int p = det->second;
    r.preperiod = pre;
    r.period = p;

    int ones = 0;
    vector<uint8_t> word;
    word.reserve(static_cast<size_t>(p));
    std::ostringstream residues;
    residues << "{";
    bool first = true;

    for (int i = 0; i < p && pre + i <= comp.n_max; ++i) {
        uint8_t bit = comp.start_p[static_cast<size_t>(pre + i)];
        word.push_back(bit);
        if (bit) {
            ++ones;
            if (!first) residues << ",";
            residues << ((pre + i) % p);
            first = false;
        }
    }
    residues << "}";

    r.p_density = static_cast<double>(ones) / static_cast<double>(p);
    r.p_residues = residues.str();
    r.period_fingerprint = to_hex64(fnv1a64(word.data(), word.size()));
    return r;
}

// -----------------------------------------------------------------------------
// Rational helper for affine-law mining
// -----------------------------------------------------------------------------

struct Rational {
    long long num = 0;
    long long den = 1;

    Rational() = default;
    Rational(long long n, long long d = 1) {
        if (d == 0) throw std::invalid_argument("zero denominator");
        if (d < 0) { n = -n; d = -d; }
        long long g = std::gcd(std::llabs(n), d);
        num = n / g;
        den = d / g;
    }
};

static bool equals_period(const Rational& a, const Rational& b, int k, int period) {
    long long lhs = static_cast<long long>(period) * a.den * b.den;
    long long rhs = a.num * static_cast<long long>(k) * b.den + b.num * a.den;
    return lhs == rhs;
}

static string rational_string(const Rational& x) {
    if (x.den == 1) return std::to_string(x.num);
    return std::to_string(x.num) + "/" + std::to_string(x.den);
}

vector<string> mine_affine_period_laws(
    const vector<ScanResult>& results,
    int max_modulus = 12,
    int min_points = 5
) {
    std::map<int, vector<const ScanResult*>> by_m;
    for (const auto& row : results) {
        if (row.period) by_m[row.m].push_back(&row);
    }

    vector<string> messages;
    std::set<string> unique;

    for (auto& [m, rows] : by_m) {
        std::sort(rows.begin(), rows.end(), [](auto* a, auto* b){ return a->k < b->k; });

        for (int q = 1; q <= max_modulus; ++q) {
            for (int rem = 0; rem < q; ++rem) {
                vector<const ScanResult*> group;
                for (auto* x : rows) if (x->k % q == rem) group.push_back(x);
                if (static_cast<int>(group.size()) < min_points || group.size() < 2) continue;

                const auto* x1 = group[0];
                const auto* x2 = group[1];
                Rational a(*x2->period - *x1->period, x2->k - x1->k);
                Rational b(static_cast<long long>(*x1->period) * a.den - a.num * x1->k, a.den);

                bool good = true;
                for (auto* x : group) {
                    if (!equals_period(a, b, x->k, *x->period)) { good = false; break; }
                }
                if (!good) continue;

                if (q > 1) {
                    bool all_rows_obey = true;
                    for (auto* x : rows) {
                        if (!equals_period(a, b, x->k, *x->period)) { all_rows_obey = false; break; }
                    }
                    if (all_rows_obey) continue;
                }

                std::ostringstream oss;
                oss << "m=" << m << ", k ≡ " << rem << " (mod " << q << "), observed for "
                    << group.size() << " k-values from " << group.front()->k << " to " << group.back()->k
                    << ": period = (" << rational_string(a) << ")*k ";
                if (b.num >= 0) oss << "+";
                oss << rational_string(b);

                string msg = oss.str();
                if (unique.insert(msg).second) messages.push_back(msg);
            }
        }
    }

    return messages;
}

// Bonus improvement over the original Python: find contiguous affine regimes.
vector<string> mine_contiguous_affine_regimes(
    const vector<ScanResult>& results,
    int min_points = 5
) {
    std::map<int, vector<const ScanResult*>> by_m;
    for (const auto& r : results) if (r.period) by_m[r.m].push_back(&r);

    vector<string> out;
    for (auto& [m, rows] : by_m) {
        std::sort(rows.begin(), rows.end(), [](auto* a, auto* b){ return a->k < b->k; });
        size_t i = 0;
        while (i + 1 < rows.size()) {
            if (rows[i+1]->k != rows[i]->k + 1) { ++i; continue; }
            long long slope_num = *rows[i+1]->period - *rows[i]->period;
            long long slope_den = 1;
            Rational a(slope_num, slope_den);
            Rational b(static_cast<long long>(*rows[i]->period) * a.den - a.num * rows[i]->k, a.den);

            size_t j = i + 1;
            while (j + 1 < rows.size() && rows[j+1]->k == rows[j]->k + 1 &&
                   equals_period(a, b, rows[j+1]->k, *rows[j+1]->period)) {
                ++j;
            }

            if (static_cast<int>(j - i + 1) >= min_points) {
                std::ostringstream oss;
                oss << "m=" << m << ", contiguous k=" << rows[i]->k << ".." << rows[j]->k
                    << " (" << (j-i+1) << " points): period = (" << rational_string(a) << ")*k ";
                if (b.num >= 0) oss << "+";
                oss << rational_string(b);
                out.push_back(oss.str());
                i = j + 1;
            } else {
                ++i;
            }
        }
    }
    return out;
}

vector<string> unusual_cases(const vector<ScanResult>& results, int limit = 12) {
    std::map<std::pair<int,string>, int> fp_count;
    for (const auto& r : results) {
        if (!r.period_fingerprint.empty()) ++fp_count[{r.m, r.period_fingerprint}];
    }

    struct Item { double score; int m; int k; string text; };
    vector<Item> scored;

    for (const auto& r : results) {
        double score = 0.0;
        vector<string> reasons;

        if (!r.period) {
            score += 10.0;
            reasons.push_back("no period detected within search bound");
        } else {
            const double ratio = static_cast<double>(*r.period) / std::max(1, r.k);
            if (ratio >= 4.0) {
                score += std::min(5.0, ratio / 2.0);
                std::ostringstream x; x << std::fixed << std::setprecision(2) << ratio;
                reasons.push_back("large period/k ratio (" + x.str() + ")");
            }
            if (r.preperiod && *r.preperiod >= 4 * r.k) {
                score += std::min(4.0, static_cast<double>(*r.preperiod) / std::max(1, 4 * r.k));
                reasons.push_back("large preperiod (" + std::to_string(*r.preperiod) + ")");
            }
            if (fp_count[{r.m, r.period_fingerprint}] == 1) {
                score += 1.0;
                reasons.push_back("unique period fingerprint in this scan");
            }
        }

        if (!reasons.empty()) {
            std::ostringstream oss;
            oss << "m=" << r.m << ", k=" << r.k << ": ";
            for (size_t i = 0; i < reasons.size(); ++i) {
                if (i) oss << "; ";
                oss << reasons[i];
            }
            scored.push_back({score, r.m, r.k, oss.str()});
        }
    }

    std::sort(scored.begin(), scored.end(), [](const Item& a, const Item& b){
        if (a.score != b.score) return a.score > b.score;
        if (a.m != b.m) return a.m < b.m;
        return a.k < b.k;
    });

    vector<string> out;
    for (int i = 0; i < std::min(limit, static_cast<int>(scored.size())); ++i) out.push_back(scored[i].text);
    return out;
}

void write_scan_outputs(
    const fs::path& out_dir,
    const vector<ScanResult>& results,
    const vector<string>& affine_laws,
    const vector<string>& contiguous_laws,
    const vector<string>& unusual
) {
    fs::create_directories(out_dir);

    {
        std::ofstream f(out_dir / "scan_results.csv");
        if (!f) throw std::runtime_error("could not open scan_results.csv for writing");
        f << "m,k,n_max,preperiod,period,p_density,p_residues,period_fingerprint,max_start_sg,max_state_sg,exact_state_preperiod_upper_bound,exact_state_period\n";
        for (const auto& r : results) {
            f << r.m << ',' << r.k << ',' << r.n_max << ','
              << opt_int(r.preperiod) << ',' << opt_int(r.period) << ','
              << opt_double(r.p_density) << ',' << csv_escape(r.p_residues) << ','
              << csv_escape(r.period_fingerprint) << ',' << r.max_start_sg << ','
              << r.max_state_sg << ',' << opt_int(r.exact_state_preperiod_upper_bound) << ','
              << opt_int(r.exact_state_period) << '\n';
        }
    }

    {
        std::ofstream f(out_dir / "research_report.md");
        if (!f) throw std::runtime_error("could not open research_report.md for writing");
        f << "# Distance-Constrained Subtraction Game Scan\n\n";
        f << "**Warning:** this report identifies computational patterns only. It does not establish literature novelty.\n\n";

        f << "## Candidate affine period laws\n\n";
        if (affine_laws.empty()) f << "- None found under the current scan settings.\n";
        else for (const auto& x : affine_laws) f << "- " << x << '\n';

        f << "\n## Contiguous affine period regimes\n\n";
        if (contiguous_laws.empty()) f << "- None found under the current scan settings.\n";
        else for (const auto& x : contiguous_laws) f << "- " << x << '\n';

        f << "\n## Computationally unusual cases\n\n";
        if (unusual.empty()) f << "- None surfaced.\n";
        else for (const auto& x : unusual) f << "- " << x << '\n';

        f << "\n## Novelty checklist for any promising pattern\n\n";
        f << "1. Re-run the case with at least 5-10x larger n.\n"
          << "2. Extend the k range well beyond the discovery range.\n"
          << "3. Search for a counterexample before attempting a proof.\n"
          << "4. Prove the statement for an infinite family if possible.\n"
          << "5. Search the mathematical literature for the exact rule and equivalent formulations.\n"
          << "6. Distinguish clearly among proved theorems, finite computational evidence, and conjectures.\n";

        f << "\n## Suggested literature-search phrases\n\n"
          << "- \"repetition-free subtraction game\"\n"
          << "- \"dynamic subtraction game previous move\"\n"
          << "- \"distance constrained subtraction game\"\n"
          << "- \"Sprague-Grundy previous move restriction\"\n"
          << "- \"take-away game previous move difference\"\n"
          << "- \"subtraction game forbidden consecutive move sizes\"\n";
    }

    {
        std::ofstream f(out_dir / "literature_search_terms.txt");
        f << "\"repetition-free subtraction game\"\n"
          << "\"dynamic subtraction game\" \"previous move\"\n"
          << "\"distance constrained\" \"subtraction game\"\n"
          << "\"Sprague-Grundy\" \"previous move\" subtraction\n"
          << "\"take-away game\" \"previous move\" difference\n"
          << "\"subtraction game\" forbidden consecutive move sizes\n";
    }
}

// -----------------------------------------------------------------------------
// Simple command-line parser
// -----------------------------------------------------------------------------

struct Args {
    string command;
    int k = -1;
    int m = 1;
    int n = 50000;
    int max_period = 10000;
    int min_repeats = 12;
    int show_p = 40;
    bool exact_state_cycle = false;
    int exact_cycle_max_n = 20000;

    vector<int> m_values = {1};
    int k_min = 2;
    int k_max = 60;
    int max_modulus = 12;
    int min_family_points = 5;
    string out = "distance_game_results";
    int exact_cycle_k_max = 20;

    int a = 0;
    int b = 0;
    int q = 1;
    int r = 0;
    bool has_a = false;
    bool has_b = false;
    bool has_k_min = false;
    bool has_k_max = false;
};

static bool starts_with_dashdash(const string& s) {
    return s.size() >= 2 && s[0] == '-' && s[1] == '-';
}

static int parse_int(const string& s, const string& name) {
    try {
        size_t pos = 0;
        long long v = std::stoll(s, &pos);
        if (pos != s.size()) throw std::runtime_error("junk");
        if (v < std::numeric_limits<int>::min() || v > std::numeric_limits<int>::max()) throw std::runtime_error("range");
        return static_cast<int>(v);
    } catch (...) {
        throw std::runtime_error("invalid integer for " + name + ": " + s);
    }
}

static void print_help() {
    cout << "Distance-constrained dynamic subtraction game research engine (C++17)\n\n"
         << "Commands:\n"
         << "  self-test\n"
         << "  single --k K [--m M] [--n N] [--max-period P] [--min-repeats R]\n"
         << "         [--show-p C] [--exact-state-cycle] [--exact-cycle-max-n N]\n"
         << "  scan --m-values M1 M2 ... [--k-min A] [--k-max B] [--n N]\n"
         << "       [--max-period P] [--min-repeats R] [--max-modulus Q]\n"
         << "       [--min-family-points C] [--out DIR] [--exact-state-cycle]\n"
         << "       [--exact-cycle-k-max K] [--exact-cycle-max-n N]\n"
         << "  test-period-formula --m M --k-min A --k-max B --a A --b B\n"
         << "       [--q Q] [--r R] [--n N] [--max-period P] [--min-repeats R]\n";
}

Args parse_args(int argc, char** argv) {
    if (argc < 2) {
        print_help();
        throw std::runtime_error("missing command");
    }

    Args args;
    args.command = argv[1];

    for (int i = 2; i < argc; ++i) {
        string x = argv[i];
        auto need = [&](const string& opt) -> string {
            if (i + 1 >= argc) throw std::runtime_error("missing value after " + opt);
            return argv[++i];
        };

        if (x == "--k") args.k = parse_int(need(x), x);
        else if (x == "--m") args.m = parse_int(need(x), x);
        else if (x == "--n") args.n = parse_int(need(x), x);
        else if (x == "--max-period") args.max_period = parse_int(need(x), x);
        else if (x == "--min-repeats") args.min_repeats = parse_int(need(x), x);
        else if (x == "--show-p") args.show_p = parse_int(need(x), x);
        else if (x == "--exact-state-cycle") args.exact_state_cycle = true;
        else if (x == "--exact-cycle-max-n") args.exact_cycle_max_n = parse_int(need(x), x);
        else if (x == "--k-min") { args.k_min = parse_int(need(x), x); args.has_k_min = true; }
        else if (x == "--k-max") { args.k_max = parse_int(need(x), x); args.has_k_max = true; }
        else if (x == "--max-modulus") args.max_modulus = parse_int(need(x), x);
        else if (x == "--min-family-points") args.min_family_points = parse_int(need(x), x);
        else if (x == "--out") args.out = need(x);
        else if (x == "--exact-cycle-k-max") args.exact_cycle_k_max = parse_int(need(x), x);
        else if (x == "--a") { args.a = parse_int(need(x), x); args.has_a = true; }
        else if (x == "--b") { args.b = parse_int(need(x), x); args.has_b = true; }
        else if (x == "--q") args.q = parse_int(need(x), x);
        else if (x == "--r") args.r = parse_int(need(x), x);
        else if (x == "--m-values") {
            args.m_values.clear();
            while (i + 1 < argc && !starts_with_dashdash(argv[i+1])) {
                args.m_values.push_back(parse_int(argv[++i], "--m-values"));
            }
            if (args.m_values.empty()) throw std::runtime_error("--m-values needs at least one integer");
        }
        else if (x == "-h" || x == "--help") {
            print_help();
            std::exit(0);
        }
        else throw std::runtime_error("unrecognized argument: " + x);
    }

    return args;
}

// -----------------------------------------------------------------------------
// Commands
// -----------------------------------------------------------------------------

int cmd_single(const Args& args) {
    if (args.k < 1) throw std::runtime_error("single requires --k K");
    auto comp = solve_game(args.k, args.m, args.n);
    auto result = period_description(comp, args.max_period, args.min_repeats);

    if (args.exact_state_cycle) {
        auto exact = detect_exact_full_state_cycle(comp, args.exact_cycle_max_n);
        if (exact) {
            result.exact_state_preperiod_upper_bound = exact->first;
            result.exact_state_period = exact->second;
        }
    }

    cout << "D(k=" << args.k << ", m=" << args.m << "), computed through n=" << args.n << '\n';
    cout << "max starting SG = " << result.max_start_sg << '\n';
    cout << "max state SG    = " << result.max_state_sg << '\n';

    if (!result.period) {
        cout << "candidate P-period: not detected\n";
    } else {
        cout << "candidate P-preperiod = " << *result.preperiod << '\n';
        cout << "candidate P-period    = " << *result.period << '\n';
        cout << "P-density in period   = " << std::fixed << std::setprecision(6) << *result.p_density << '\n';
        cout << "P residues mod period = " << result.p_residues << '\n';
        cout << "period fingerprint    = " << result.period_fingerprint << '\n';
    }

    if (args.exact_state_cycle) {
        if (!result.exact_state_period) cout << "exact full-state cycle: not found within requested range\n";
        else cout << "exact full-state cycle: period=" << *result.exact_state_period
                  << ", preperiod <= " << *result.exact_state_preperiod_upper_bound << '\n';
    }

    cout << "\nFirst starting P-positions:\n[";
    int shown = 0;
    for (int n = 0; n <= comp.n_max && shown < args.show_p; ++n) {
        if (comp.start_p[static_cast<size_t>(n)]) {
            if (shown) cout << ", ";
            cout << n;
            ++shown;
        }
    }
    cout << "]\n";
    return 0;
}

int cmd_scan(const Args& args) {
    if (args.k_min > args.k_max) throw std::runtime_error("--k-min must be <= --k-max");

    vector<ScanResult> results;
    const int total = static_cast<int>(args.m_values.size()) * (args.k_max - args.k_min + 1);
    int done = 0;

    for (int m : args.m_values) {
        for (int k = args.k_min; k <= args.k_max; ++k) {
            ++done;
            cout << "[" << done << "/" << total << "] computing m=" << m << ", k=" << k << " ..." << std::flush;

            auto comp = solve_game(k, m, args.n);
            auto result = period_description(comp, args.max_period, args.min_repeats);

            if (args.exact_state_cycle && k <= args.exact_cycle_k_max) {
                auto exact = detect_exact_full_state_cycle(comp, args.exact_cycle_max_n);
                if (exact) {
                    result.exact_state_preperiod_upper_bound = exact->first;
                    result.exact_state_period = exact->second;
                }
            }

            results.push_back(result);
            if (!result.period) {
                cout << "\n    no candidate P-period found\n";
            } else {
                cout << "\n    pre=" << *result.preperiod << ", p=" << *result.period
                     << ", density=" << std::fixed << std::setprecision(4) << *result.p_density << '\n';
            }
        }
    }

    auto affine = mine_affine_period_laws(results, args.max_modulus, args.min_family_points);
    auto contiguous = mine_contiguous_affine_regimes(results, args.min_family_points);
    auto unusual = unusual_cases(results);
    fs::path out_dir(args.out);
    write_scan_outputs(out_dir, results, affine, contiguous, unusual);

    cout << "\n=== Candidate affine laws ===\n";
    if (affine.empty()) cout << "  none found\n";
    else {
        const size_t nshow = std::min<size_t>(50, affine.size());
        for (size_t i = 0; i < nshow; ++i) cout << "  " << affine[i] << '\n';
        if (affine.size() > nshow) cout << "  ... plus " << (affine.size() - nshow) << " more in the report\n";
    }

    cout << "\n=== Contiguous affine regimes ===\n";
    if (contiguous.empty()) cout << "  none found\n";
    else for (const auto& x : contiguous) cout << "  " << x << '\n';

    cout << "\n=== Computationally unusual cases ===\n";
    if (unusual.empty()) cout << "  none surfaced\n";
    else for (const auto& x : unusual) cout << "  " << x << '\n';

    cout << "\nWrote: " << (out_dir / "scan_results.csv").string() << '\n';
    cout << "Wrote: " << (out_dir / "research_report.md").string() << '\n';
    cout << "Wrote: " << (out_dir / "literature_search_terms.txt").string() << '\n';
    return 0;
}

int cmd_test_period_formula(const Args& args) {
    if (!args.has_k_min || !args.has_k_max) throw std::runtime_error("test-period-formula requires --k-min and --k-max");
    if (!args.has_a || !args.has_b) throw std::runtime_error("test-period-formula requires --a and --b");
    if (args.q <= 0) throw std::runtime_error("--q must be positive");

    int tested = 0;
    for (int k = args.k_min; k <= args.k_max; ++k) {
        if (((k % args.q) + args.q) % args.q != ((args.r % args.q) + args.q) % args.q) continue;
        const long long expected_ll = static_cast<long long>(args.a) * k + args.b;
        if (expected_ll <= 0 || expected_ll > std::numeric_limits<int>::max()) {
            cout << "Skipping k=" << k << ": predicted period " << expected_ll << " is not positive/valid.\n";
            continue;
        }
        const int expected = static_cast<int>(expected_ll);
        ++tested;
        cout << "testing k=" << k << ", m=" << args.m << "; expected p=" << expected << " ..." << std::flush;

        auto comp = solve_game(k, args.m, args.n);
        auto result = period_description(comp, args.max_period, args.min_repeats);
        cout << '\n';

        if (!result.period || *result.period != expected) {
            cout << "\nCOUNTEREXAMPLE / FAILURE OF CURRENT EVIDENCE\n"
                 << "  m=" << args.m << ", k=" << k << '\n'
                 << "  predicted period = " << expected << '\n'
                 << "  detected period  = " << (result.period ? std::to_string(*result.period) : string("none")) << '\n'
                 << "  detected preperiod = " << (result.preperiod ? std::to_string(*result.preperiod) : string("none")) << '\n'
                 << "\nThis does not automatically prove the formula false if no period was detected; increase --n and --max-period first.\n";
            return 1;
        }
    }

    cout << "\nNo counterexample found among " << tested << " tested k-values. This is evidence, not a proof.\n";
    return 0;
}

int cmd_self_test() {
    {
        auto c = solve_game(1, 0, 8);
        vector<uint8_t> expected = {1,0,0,0,0,0,0,0,0};
        if (c.start_p != expected) throw std::runtime_error("self-test failed for k=1,m=0");
    }

    auto slow = [](int k, int m, int N) {
        vector<vector<int>> g(static_cast<size_t>(N+1), vector<int>(static_cast<size_t>(k+1), 0));
        vector<int> start(static_cast<size_t>(N+1), 0);

        for (int n = 1; n <= N; ++n) {
            std::set<int> vals0;
            for (int r = 1; r <= std::min(k,n); ++r) vals0.insert(g[static_cast<size_t>(n-r)][static_cast<size_t>(r)]);
            int z = 0; while (vals0.count(z)) ++z;
            start[static_cast<size_t>(n)] = z;

            for (int s = 1; s <= k; ++s) {
                std::set<int> vals;
                for (int r = 1; r <= std::min(k,n); ++r) {
                    if (std::abs(r-s) > m) vals.insert(g[static_cast<size_t>(n-r)][static_cast<size_t>(r)]);
                }
                z = 0; while (vals.count(z)) ++z;
                g[static_cast<size_t>(n)][static_cast<size_t>(s)] = z;
            }
        }
        return std::make_pair(g, start);
    };

    for (int k = 1; k <= 7; ++k) {
        for (int m = 0; m <= 3; ++m) {
            const int N = 35;
            auto fast = solve_game(k, m, N);
            auto [slow_g, slow_start] = slow(k, m, N);
            const size_t stride = static_cast<size_t>(k+1);

            for (int n = 0; n <= N; ++n) {
                if (fast.start_sg[static_cast<size_t>(n)] != slow_start[static_cast<size_t>(n)]) {
                    throw std::runtime_error("self-test start SG mismatch");
                }
                for (int s = 1; s <= k; ++s) {
                    if (fast.table[static_cast<size_t>(n)*stride + static_cast<size_t>(s)] != slow_g[static_cast<size_t>(n)][static_cast<size_t>(s)]) {
                        throw std::runtime_error("self-test state SG mismatch");
                    }
                }
            }
        }
    }

    cout << "All self-tests passed.\n";
    return 0;
}

int main(int argc, char** argv) {
    try {
        Args args = parse_args(argc, argv);
        if (args.command == "self-test") return cmd_self_test();
        if (args.command == "single") return cmd_single(args);
        if (args.command == "scan") return cmd_scan(args);
        if (args.command == "test-period-formula") return cmd_test_period_formula(args);
        print_help();
        throw std::runtime_error("unknown command: " + args.command);
    } catch (const std::exception& e) {
        cerr << "error: " << e.what() << '\n';
        return 2;
    }
}
