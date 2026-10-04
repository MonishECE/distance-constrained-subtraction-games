```
distance_subtraction_research.cpp:23:21: error: ‘filesystem’ is not a namespace-name; did you mean ‘system’?
   23 | namespace fs = std::filesystem;
      |                     ^~~~~~~~~~
      |                     system
distance_subtraction_research.cpp:44:10: error: ‘optional’ in namespace ‘std’ does not name a template type
   44 |     std::optional<int> preperiod;
      |          ^~~~~~~~
distance_subtraction_research.cpp:44:5: note: ‘std::optional’ is only available from C++17 onwards
   44 |     std::optional<int> preperiod;
      |     ^~~
distance_subtraction_research.cpp:45:10: error: ‘optional’ in namespace ‘std’ does not name a template type
   45 |     std::optional<int> period;
      |          ^~~~~~~~
distance_subtraction_research.cpp:45:5: note: ‘std::optional’ is only available from C++17 onwards
   45 |     std::optional<int> period;
      |     ^~~
distance_subtraction_research.cpp:46:10: error: ‘optional’ in namespace ‘std’ does not name a template type
   46 |     std::optional<double> p_density;
      |          ^~~~~~~~
distance_subtraction_research.cpp:46:5: note: ‘std::optional’ is only available from C++17 onwards
   46 |     std::optional<double> p_density;
      |     ^~~
distance_subtraction_research.cpp:51:10: error: ‘optional’ in namespace ‘std’ does not name a template type
   51 |     std::optional<int> exact_state_preperiod_upper_bound;
      |          ^~~~~~~~
distance_subtraction_research.cpp:51:5: note: ‘std::optional’ is only available from C++17 onwards
   51 |     std::optional<int> exact_state_preperiod_upper_bound;
      |     ^~~
distance_subtraction_research.cpp:52:10: error: ‘optional’ in namespace ‘std’ does not name a template type
   52 |     std::optional<int> exact_state_period;
      |          ^~~~~~~~
distance_subtraction_research.cpp:52:5: note: ‘std::optional’ is only available from C++17 onwards
   52 |     std::optional<int> exact_state_period;
      |     ^~~
distance_subtraction_research.cpp:98:34: error: ‘optional’ in namespace ‘std’ does not name a template type
   98 | static string opt_int(const std::optional<int>& x) {
      |                                  ^~~~~~~~
distance_subtraction_research.cpp:98:29: note: ‘std::optional’ is only available from C++17 onwards
   98 | static string opt_int(const std::optional<int>& x) {
      |                             ^~~
distance_subtraction_research.cpp:98:42: error: expected ‘,’ or ‘...’ before ‘<’ token
   98 | static string opt_int(const std::optional<int>& x) {
      |                                          ^
distance_subtraction_research.cpp: In function ‘std::string opt_int(int)’:
distance_subtraction_research.cpp:99:12: error: ‘x’ was not declared in this scope
   99 |     return x ? std::to_string(*x) : "";
      |            ^
distance_subtraction_research.cpp: At global scope:
distance_subtraction_research.cpp:102:37: error: ‘optional’ in namespace ‘std’ does not name a template type
  102 | static string opt_double(const std::optional<double>& x) {
      |                                     ^~~~~~~~
distance_subtraction_research.cpp:102:32: note: ‘std::optional’ is only available from C++17 onwards
  102 | static string opt_double(const std::optional<double>& x) {
      |                                ^~~
distance_subtraction_research.cpp:102:45: error: expected ‘,’ or ‘...’ before ‘<’ token
  102 | static string opt_double(const std::optional<double>& x) {
      |                                             ^
distance_subtraction_research.cpp: In function ‘std::string opt_double(int)’:
distance_subtraction_research.cpp:103:10: error: ‘x’ was not declared in this scope
  103 |     if (!x) return "";
      |          ^
distance_subtraction_research.cpp:105:38: error: ‘x’ was not declared in this scope
  105 |     oss << std::setprecision(12) << *x;
      |                                      ^
distance_subtraction_research.cpp: At global scope:
distance_subtraction_research.cpp:196:6: error: ‘optional’ in namespace ‘std’ does not name a template type
  196 | std::optional<std::pair<int,int>> detect_eventual_period(
      |      ^~~~~~~~
distance_subtraction_research.cpp:196:1: note: ‘std::optional’ is only available from C++17 onwards
  196 | std::optional<std::pair<int,int>> detect_eventual_period(
      | ^~~
distance_subtraction_research.cpp:246:6: error: ‘optional’ in namespace ‘std’ does not name a template type
  246 | std::optional<std::pair<int,int>> detect_exact_full_state_cycle(
      |      ^~~~~~~~
distance_subtraction_research.cpp:246:1: note: ‘std::optional’ is only available from C++17 onwards
  246 | std::optional<std::pair<int,int>> detect_exact_full_state_cycle(
      | ^~~
distance_subtraction_research.cpp: In function ‘ScanResult period_description(const GameComputation&, int, int)’:
distance_subtraction_research.cpp:292:16: error: ‘detect_eventual_period’ was not declared in this scope
  292 |     auto det = detect_eventual_period(comp.start_p, max_period, min_repeats);
      |                ^~~~~~~~~~~~~~~~~~~~~~
distance_subtraction_research.cpp:297:7: error: ‘struct ScanResult’ has no member named ‘preperiod’
  297 |     r.preperiod = pre;
      |       ^~~~~~~~~
distance_subtraction_research.cpp:298:7: error: ‘struct ScanResult’ has no member named ‘period’
  298 |     r.period = p;
      |       ^~~~~~
distance_subtraction_research.cpp:319:7: error: ‘struct ScanResult’ has no member named ‘p_density’
  319 |     r.p_density = static_cast<double>(ones) / static_cast<double>(p);
      |       ^~~~~~~~~
distance_subtraction_research.cpp: In constructor ‘Rational::Rational(long long int, long long int)’:
distance_subtraction_research.cpp:337:28: error: ‘gcd’ is not a member of ‘std’
  337 |         long long g = std::gcd(std::llabs(n), d);
      |                            ^~~
distance_subtraction_research.cpp: In function ‘std::vector<std::__cxx11::basic_string<char> > mine_affine_period_laws(const std::vector<ScanResult>&, int, int)’:
distance_subtraction_research.cpp:361:17: error: ‘const struct ScanResult’ has no member named ‘period’
  361 |         if (row.period) by_m[row.m].push_back(&row);
      |                 ^~~~~~
distance_subtraction_research.cpp:367:16: warning: structured bindings only available with ‘-std=c++17’ or ‘-std=gnu++17’ [-Wc++17-extensions]
  367 |     for (auto& [m, rows] : by_m) {
      |                ^
distance_subtraction_research.cpp:368:48: error: use of ‘auto’ in lambda parameter declaration only available with ‘-std=c++14’ or ‘-std=gnu++14’
  368 |         std::sort(rows.begin(), rows.end(), [](auto* a, auto* b){ return a->k < b->k; });
      |                                                ^~~~
distance_subtraction_research.cpp:368:57: error: use of ‘auto’ in lambda parameter declaration only available with ‘-std=c++14’ or ‘-std=gnu++14’
  368 |         std::sort(rows.begin(), rows.end(), [](auto* a, auto* b){ return a->k < b->k; });
      |                                                         ^~~~
distance_subtraction_research.cpp: In lambda function:
distance_subtraction_research.cpp:368:77: error: request for member ‘k’ in ‘* a’, which is of non-class type ‘int’
  368 |         std::sort(rows.begin(), rows.end(), [](auto* a, auto* b){ return a->k < b->k; });
      |                                                                             ^
distance_subtraction_research.cpp:368:84: error: request for member ‘k’ in ‘* b’, which is of non-class type ‘int’
  368 |         std::sort(rows.begin(), rows.end(), [](auto* a, auto* b){ return a->k < b->k; });
      |                                                                                    ^
distance_subtraction_research.cpp: In function ‘std::vector<std::__cxx11::basic_string<char> > mine_affine_period_laws(const std::vector<ScanResult>&, int, int)’:
distance_subtraction_research.cpp:378:33: error: ‘const struct ScanResult’ has no member named ‘period’
  378 |                 Rational a(*x2->period - *x1->period, x2->k - x1->k);
      |                                 ^~~~~~
distance_subtraction_research.cpp:378:47: error: ‘const struct ScanResult’ has no member named ‘period’
  378 |                 Rational a(*x2->period - *x1->period, x2->k - x1->k);
      |                                               ^~~~~~
distance_subtraction_research.cpp:379:56: error: ‘const struct ScanResult’ has no member named ‘period’
  379 |                 Rational b(static_cast<long long>(*x1->period) * a.den - a.num * x1->k, a.den);
      |                                                        ^~~~~~
distance_subtraction_research.cpp:383:56: error: ‘const struct ScanResult’ has no member named ‘period’
  383 |                     if (!equals_period(a, b, x->k, *x->period)) { good = false; break; }
      |                                                        ^~~~~~
distance_subtraction_research.cpp:390:60: error: ‘const struct ScanResult’ has no member named ‘period’
  390 |                         if (!equals_period(a, b, x->k, *x->period)) { all_rows_obey = false; break; }
      |                                                            ^~~~~~
distance_subtraction_research.cpp: In function ‘std::vector<std::__cxx11::basic_string<char> > mine_contiguous_affine_regimes(const std::vector<ScanResult>&, int)’:
distance_subtraction_research.cpp:417:41: error: ‘const struct ScanResult’ has no member named ‘period’
  417 |     for (const auto& r : results) if (r.period) by_m[r.m].push_back(&r);
      |                                         ^~~~~~
distance_subtraction_research.cpp:420:16: warning: structured bindings only available with ‘-std=c++17’ or ‘-std=gnu++17’ [-Wc++17-extensions]
  420 |     for (auto& [m, rows] : by_m) {
      |                ^
distance_subtraction_research.cpp:421:48: error: use of ‘auto’ in lambda parameter declaration only available with ‘-std=c++14’ or ‘-std=gnu++14’
  421 |         std::sort(rows.begin(), rows.end(), [](auto* a, auto* b){ return a->k < b->k; });
      |                                                ^~~~
distance_subtraction_research.cpp:421:57: error: use of ‘auto’ in lambda parameter declaration only available with ‘-std=c++14’ or ‘-std=gnu++14’
  421 |         std::sort(rows.begin(), rows.end(), [](auto* a, auto* b){ return a->k < b->k; });
      |                                                         ^~~~
distance_subtraction_research.cpp: In lambda function:
distance_subtraction_research.cpp:421:77: error: request for member ‘k’ in ‘* a’, which is of non-class type ‘int’
  421 |         std::sort(rows.begin(), rows.end(), [](auto* a, auto* b){ return a->k < b->k; });
      |                                                                             ^
distance_subtraction_research.cpp:421:84: error: request for member ‘k’ in ‘* b’, which is of non-class type ‘int’
  421 |         std::sort(rows.begin(), rows.end(), [](auto* a, auto* b){ return a->k < b->k; });
      |                                                                                    ^
distance_subtraction_research.cpp: In function ‘std::vector<std::__cxx11::basic_string<char> > mine_contiguous_affine_regimes(const std::vector<ScanResult>&, int)’:
distance_subtraction_research.cpp:425:47: error: ‘const struct ScanResult’ has no member named ‘period’
  425 |             long long slope_num = *rows[i+1]->period - *rows[i]->period;
      |                                               ^~~~~~
distance_subtraction_research.cpp:425:66: error: ‘const struct ScanResult’ has no member named ‘period’
  425 |             long long slope_num = *rows[i+1]->period - *rows[i]->period;
      |                                                                  ^~~~~~
distance_subtraction_research.cpp:428:57: error: ‘const struct ScanResult’ has no member named ‘period’
  428 |             Rational b(static_cast<long long>(*rows[i]->period) * a.den - a.num * rows[i]->k, a.den);
      |                                                         ^~~~~~
distance_subtraction_research.cpp:432:66: error: ‘const struct ScanResult’ has no member named ‘period’
  432 |                    equals_period(a, b, rows[j+1]->k, *rows[j+1]->period)) {
      |                                                                  ^~~~~~
distance_subtraction_research.cpp: In function ‘std::vector<std::__cxx11::basic_string<char> > unusual_cases(const std::vector<ScanResult>&, int)’:
distance_subtraction_research.cpp:465:16: error: ‘const struct ScanResult’ has no member named ‘period’
  465 |         if (!r.period) {
      |                ^~~~~~
distance_subtraction_research.cpp:469:57: error: ‘const struct ScanResult’ has no member named ‘period’
  469 |             const double ratio = static_cast<double>(*r.period) / std::max(1, r.k);
      |                                                         ^~~~~~
distance_subtraction_research.cpp:475:19: error: ‘const struct ScanResult’ has no member named ‘preperiod’
  475 |             if (r.preperiod && *r.preperiod >= 4 * r.k) {
      |                   ^~~~~~~~~
distance_subtraction_research.cpp:475:35: error: ‘const struct ScanResult’ has no member named ‘preperiod’
  475 |             if (r.preperiod && *r.preperiod >= 4 * r.k) {
      |                                   ^~~~~~~~~
distance_subtraction_research.cpp:476:63: error: ‘const struct ScanResult’ has no member named ‘preperiod’
  476 |                 score += std::min(4.0, static_cast<double>(*r.preperiod) / std::max(1, 4 * r.k));
      |                                                               ^~~~~~~~~
distance_subtraction_research.cpp:477:75: error: ‘const struct ScanResult’ has no member named ‘preperiod’
  477 |                 reasons.push_back("large preperiod (" + std::to_string(*r.preperiod) + ")");
      |                                                                           ^~~~~~~~~
distance_subtraction_research.cpp: At global scope:
distance_subtraction_research.cpp:508:11: error: ‘fs’ does not name a type
  508 |     const fs::path& out_dir,
      |           ^~
distance_subtraction_research.cpp:508:19: error: expected unqualified-id before ‘&’ token
  508 |     const fs::path& out_dir,
      |                   ^
distance_subtraction_research.cpp:508:19: error: expected ‘)’ before ‘&’ token
  508 |     const fs::path& out_dir,
      |                   ^
      |                   )
distance_subtraction_research.cpp:507:24: note: to match this ‘(’
  507 | void write_scan_outputs(
      |                        ^
distance_subtraction_research.cpp:508:21: error: expected initializer before ‘out_dir’
  508 |     const fs::path& out_dir,
      |                     ^~~~~~~
distance_subtraction_research.cpp: In function ‘int cmd_single(const Args&)’:
distance_subtraction_research.cpp:700:22: error: ‘detect_exact_full_state_cycle’ was not declared in this scope
  700 |         auto exact = detect_exact_full_state_cycle(comp, args.exact_cycle_max_n);
      |                      ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
distance_subtraction_research.cpp:702:20: error: ‘struct ScanResult’ has no member named ‘exact_state_preperiod_upper_bound’
  702 |             result.exact_state_preperiod_upper_bound = exact->first;
      |                    ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
distance_subtraction_research.cpp:703:20: error: ‘struct ScanResult’ has no member named ‘exact_state_period’
  703 |             result.exact_state_period = exact->second;
      |                    ^~~~~~~~~~~~~~~~~~
distance_subtraction_research.cpp:711:17: error: ‘struct ScanResult’ has no member named ‘period’
  711 |     if (!result.period) {
      |                 ^~~~~~
distance_subtraction_research.cpp:714:55: error: ‘struct ScanResult’ has no member named ‘preperiod’
  714 |         cout << "candidate P-preperiod = " << *result.preperiod << '\n';
      |                                                       ^~~~~~~~~
distance_subtraction_research.cpp:715:55: error: ‘struct ScanResult’ has no member named ‘period’
  715 |         cout << "candidate P-period    = " << *result.period << '\n';
      |                                                       ^~~~~~
distance_subtraction_research.cpp:716:93: error: ‘struct ScanResult’ has no member named ‘p_density’
  716 |         cout << "P-density in period   = " << std::fixed << std::setprecision(6) << *result.p_density << '\n';
      |                                                                                             ^~~~~~~~~
distance_subtraction_research.cpp:722:21: error: ‘struct ScanResult’ has no member named ‘exact_state_period’
  722 |         if (!result.exact_state_period) cout << "exact full-state cycle: not found within requested range\n";
      |                     ^~~~~~~~~~~~~~~~~~
distance_subtraction_research.cpp:723:67: error: ‘struct ScanResult’ has no member named ‘exact_state_period’
  723 |         else cout << "exact full-state cycle: period=" << *result.exact_state_period
      |                                                                   ^~~~~~~~~~~~~~~~~~
distance_subtraction_research.cpp:724:51: error: ‘struct ScanResult’ has no member named ‘exact_state_preperiod_upper_bound’
  724 |                   << ", preperiod <= " << *result.exact_state_preperiod_upper_bound << '\n';
      |                                                   ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
distance_subtraction_research.cpp: In function ‘int cmd_scan(const Args&)’:
distance_subtraction_research.cpp:756:30: error: ‘detect_exact_full_state_cycle’ was not declared in this scope
  756 |                 auto exact = detect_exact_full_state_cycle(comp, args.exact_cycle_max_n);
      |                              ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
distance_subtraction_research.cpp:758:28: error: ‘struct ScanResult’ has no member named ‘exact_state_preperiod_upper_bound’
  758 |                     result.exact_state_preperiod_upper_bound = exact->first;
      |                            ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
distance_subtraction_research.cpp:759:28: error: ‘struct ScanResult’ has no member named ‘exact_state_period’
  759 |                     result.exact_state_period = exact->second;
      |                            ^~~~~~~~~~~~~~~~~~
distance_subtraction_research.cpp:764:25: error: ‘struct ScanResult’ has no member named ‘period’
  764 |             if (!result.period) {
      |                         ^~~~~~
distance_subtraction_research.cpp:767:49: error: ‘struct ScanResult’ has no member named ‘preperiod’
  767 |                 cout << "\n    pre=" << *result.preperiod << ", p=" << *result.period
      |                                                 ^~~~~~~~~
distance_subtraction_research.cpp:767:80: error: ‘struct ScanResult’ has no member named ‘period’
  767 |                 cout << "\n    pre=" << *result.preperiod << ", p=" << *result.period
      |                                                                                ^~~~~~
distance_subtraction_research.cpp:768:87: error: ‘struct ScanResult’ has no member named ‘p_density’
  768 |                      << ", density=" << std::fixed << std::setprecision(4) << *result.p_density << '\n';
      |                                                                                       ^~~~~~~~~
distance_subtraction_research.cpp:776:5: error: ‘fs’ has not been declared
  776 |     fs::path out_dir(args.out);
      |     ^~
distance_subtraction_research.cpp:777:24: error: ‘out_dir’ was not declared in this scope
  777 |     write_scan_outputs(out_dir, results, affine, contiguous, unusual);
      |                        ^~~~~~~
distance_subtraction_research.cpp:777:5: error: ‘write_scan_outputs’ was not declared in this scope
  777 |     write_scan_outputs(out_dir, results, affine, contiguous, unusual);
      |     ^~~~~~~~~~~~~~~~~~
distance_subtraction_research.cpp: In function ‘int cmd_test_period_formula(const Args&)’:
distance_subtraction_research.cpp:822:21: error: ‘struct ScanResult’ has no member named ‘period’
  822 |         if (!result.period || *result.period != expected) {
      |                     ^~~~~~
distance_subtraction_research.cpp:822:39: error: ‘struct ScanResult’ has no member named ‘period’
  822 |         if (!result.period || *result.period != expected) {
      |                                       ^~~~~~
distance_subtraction_research.cpp:826:56: error: ‘struct ScanResult’ has no member named ‘period’
  826 |                  << "  detected period  = " << (result.period ? std::to_string(*result.period) : string("none")) << '\n'
      |                                                        ^~~~~~
distance_subtraction_research.cpp:826:88: error: ‘struct ScanResult’ has no member named ‘period’
  826 |                  << "  detected period  = " << (result.period ? std::to_string(*result.period) : string("none")) << '\n'
      |                                                                                        ^~~~~~
distance_subtraction_research.cpp:827:58: error: ‘struct ScanResult’ has no member named ‘preperiod’
  827 |                  << "  detected preperiod = " << (result.preperiod ? std::to_string(*result.preperiod) : string("none")) << '\n'
      |                                                          ^~~~~~~~~
distance_subtraction_research.cpp:827:93: error: ‘struct ScanResult’ has no member named ‘preperiod’
  827 |                  << "  detected preperiod = " << (result.preperiod ? std::to_string(*result.preperiod) : string("none")) << '\n'
      |                                                                                             ^~~~~~~~~
distance_subtraction_research.cpp: In function ‘int cmd_self_test()’:
distance_subtraction_research.cpp:870:18: warning: structured bindings only available with ‘-std=c++17’ or ‘-std=gnu++17’ [-Wc++17-extensions]
  870 |             auto [slow_g, slow_start] = slow(k, m, N);
      |                  ^
In file included from /nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/stl_algobase.h:71,
                 from /nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/algorithm:60,
                 from distance_subtraction_research.cpp:1:
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/predefined_ops.h: In instantiation of ‘bool __gnu_cxx::__ops::_Iter_comp_iter<_Compare>::operator()(_Iterator1, _Iterator2) [with _Iterator1 = __gnu_cxx::__normal_iterator<const ScanResult**, std::vector<const ScanResult*> >; _Iterator2 = __gnu_cxx::__normal_iterator<const ScanResult**, std::vector<const ScanResult*> >; _Compare = mine_affine_period_laws(const std::vector<ScanResult>&, int, int)::<lambda(int*, int*)>]’:
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/stl_algo.h:1777:14:   required from ‘void std::__insertion_sort(_RandomAccessIterator, _RandomAccessIterator, _Compare) [with _RandomAccessIterator = __gnu_cxx::__normal_iterator<const ScanResult**, vector<const ScanResult*> >; _Compare = __gnu_cxx::__ops::_Iter_comp_iter<mine_affine_period_laws(const std::vector<ScanResult>&, int, int)::<lambda(int*, int*)> >]’
 1777 |           if (__comp(__i, __first))
      |               ~~~~~~^~~~~~~~~~~~~~
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/stl_algo.h:1817:25:   required from ‘void std::__final_insertion_sort(_RandomAccessIterator, _RandomAccessIterator, _Compare) [with _RandomAccessIterator = __gnu_cxx::__normal_iterator<const ScanResult**, vector<const ScanResult*> >; _Compare = __gnu_cxx::__ops::_Iter_comp_iter<mine_affine_period_laws(const std::vector<ScanResult>&, int, int)::<lambda(int*, int*)> >]’
 1817 |           std::__insertion_sort(__first, __first + int(_S_threshold), __comp);
      |           ~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/stl_algo.h:1908:31:   required from ‘void std::__sort(_RandomAccessIterator, _RandomAccessIterator, _Compare) [with _RandomAccessIterator = __gnu_cxx::__normal_iterator<const ScanResult**, vector<const ScanResult*> >; _Compare = __gnu_cxx::__ops::_Iter_comp_iter<mine_affine_period_laws(const std::vector<ScanResult>&, int, int)::<lambda(int*, int*)> >]’
 1908 |           std::__final_insertion_sort(__first, __last, __comp);
      |           ~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/stl_algo.h:4805:18:   required from ‘void std::sort(_RAIter, _RAIter, _Compare) [with _RAIter = __gnu_cxx::__normal_iterator<const ScanResult**, vector<const ScanResult*> >; _Compare = mine_affine_period_laws(const std::vector<ScanResult>&, int, int)::<lambda(int*, int*)>]’
 4805 |       std::__sort(__first, __last, __gnu_cxx::__ops::__iter_comp_iter(__comp));
      |       ~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
distance_subtraction_research.cpp:368:18:   required from here
  368 |         std::sort(rows.begin(), rows.end(), [](auto* a, auto* b){ return a->k < b->k; });
      |         ~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/predefined_ops.h:158:30: error: no match for call to ‘(mine_affine_period_laws(const std::vector&, int, int)::) (const ScanResult*&, const ScanResult*&)’
  158 |         { return bool(_M_comp(*__it1, *__it2)); }
      |                       ~~~~~~~^~~~~~~~~~~~~~~~
distance_subtraction_research.cpp:368:45: note: candidate: ‘mine_affine_period_laws(const std::vector&, int, int)::’
  368 |         std::sort(rows.begin(), rows.end(), [](auto* a, auto* b){ return a->k < b->k; });
      |                                             ^
distance_subtraction_research.cpp:368:45: note:   no known conversion for argument 1 from ‘const ScanResult*’ to ‘int*’
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/predefined_ops.h: In instantiation of ‘bool __gnu_cxx::__ops::_Iter_comp_iter<_Compare>::operator()(_Iterator1, _Iterator2) [with _Iterator1 = __gnu_cxx::__normal_iterator<const ScanResult**, std::vector<const ScanResult*> >; _Iterator2 = __gnu_cxx::__normal_iterator<const ScanResult**, std::vector<const ScanResult*> >; _Compare = mine_contiguous_affine_regimes(const std::vector<ScanResult>&, int)::<lambda(int*, int*)>]’:
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/stl_algo.h:1777:14:   required from ‘void std::__insertion_sort(_RandomAccessIterator, _RandomAccessIterator, _Compare) [with _RandomAccessIterator = __gnu_cxx::__normal_iterator<const ScanResult**, vector<const ScanResult*> >; _Compare = __gnu_cxx::__ops::_Iter_comp_iter<mine_contiguous_affine_regimes(const std::vector<ScanResult>&, int)::<lambda(int*, int*)> >]’
 1777 |           if (__comp(__i, __first))
      |               ~~~~~~^~~~~~~~~~~~~~
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/stl_algo.h:1817:25:   required from ‘void std::__final_insertion_sort(_RandomAccessIterator, _RandomAccessIterator, _Compare) [with _RandomAccessIterator = __gnu_cxx::__normal_iterator<const ScanResult**, vector<const ScanResult*> >; _Compare = __gnu_cxx::__ops::_Iter_comp_iter<mine_contiguous_affine_regimes(const std::vector<ScanResult>&, int)::<lambda(int*, int*)> >]’
 1817 |           std::__insertion_sort(__first, __first + int(_S_threshold), __comp);
      |           ~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/stl_algo.h:1908:31:   required from ‘void std::__sort(_RandomAccessIterator, _RandomAccessIterator, _Compare) [with _RandomAccessIterator = __gnu_cxx::__normal_iterator<const ScanResult**, vector<const ScanResult*> >; _Compare = __gnu_cxx::__ops::_Iter_comp_iter<mine_contiguous_affine_regimes(const std::vector<ScanResult>&, int)::<lambda(int*, int*)> >]’
 1908 |           std::__final_insertion_sort(__first, __last, __comp);
      |           ~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/stl_algo.h:4805:18:   required from ‘void std::sort(_RAIter, _RAIter, _Compare) [with _RAIter = __gnu_cxx::__normal_iterator<const ScanResult**, vector<const ScanResult*> >; _Compare = mine_contiguous_affine_regimes(const std::vector<ScanResult>&, int)::<lambda(int*, int*)>]’
 4805 |       std::__sort(__first, __last, __gnu_cxx::__ops::__iter_comp_iter(__comp));
      |       ~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
distance_subtraction_research.cpp:421:18:   required from here
  421 |         std::sort(rows.begin(), rows.end(), [](auto* a, auto* b){ return a->k < b->k; });
      |         ~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/predefined_ops.h:158:30: error: no match for call to ‘(mine_contiguous_affine_regimes(const std::vector&, int)::) (const ScanResult*&, const ScanResult*&)’
  158 |         { return bool(_M_comp(*__it1, *__it2)); }
      |                       ~~~~~~~^~~~~~~~~~~~~~~~
distance_subtraction_research.cpp:421:45: note: candidate: ‘mine_contiguous_affine_regimes(const std::vector&, int)::’
  421 |         std::sort(rows.begin(), rows.end(), [](auto* a, auto* b){ return a->k < b->k; });
      |                                             ^
distance_subtraction_research.cpp:421:45: note:   no known conversion for argument 1 from ‘const ScanResult*’ to ‘int*’
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/predefined_ops.h: In instantiation of ‘bool __gnu_cxx::__ops::_Val_comp_iter<_Compare>::operator()(_Value&, _Iterator) [with _Value = const ScanResult*; _Iterator = __gnu_cxx::__normal_iterator<const ScanResult**, std::vector<const ScanResult*> >; _Compare = mine_affine_period_laws(const std::vector<ScanResult>&, int, int)::<lambda(int*, int*)>]’:
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/stl_algo.h:1757:20:   required from ‘void std::__unguarded_linear_insert(_RandomAccessIterator, _Compare) [with _RandomAccessIterator = __gnu_cxx::__normal_iterator<const ScanResult**, vector<const ScanResult*> >; _Compare = __gnu_cxx::__ops::_Val_comp_iter<mine_affine_period_laws(const std::vector<ScanResult>&, int, int)::<lambda(int*, int*)> >]’
 1757 |       while (__comp(__val, __next))
      |              ~~~~~~^~~~~~~~~~~~~~~
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/stl_algo.h:1785:36:   required from ‘void std::__insertion_sort(_RandomAccessIterator, _RandomAccessIterator, _Compare) [with _RandomAccessIterator = __gnu_cxx::__normal_iterator<const ScanResult**, vector<const ScanResult*> >; _Compare = __gnu_cxx::__ops::_Iter_comp_iter<mine_affine_period_laws(const std::vector<ScanResult>&, int, int)::<lambda(int*, int*)> >]’
 1785 |             std::__unguarded_linear_insert(__i,
      |             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~
 1786 |                                 __gnu_cxx::__ops::__val_comp_iter(__comp));
      |                                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/stl_algo.h:1817:25:   required from ‘void std::__final_insertion_sort(_RandomAccessIterator, _RandomAccessIterator, _Compare) [with _RandomAccessIterator = __gnu_cxx::__normal_iterator<const ScanResult**, vector<const ScanResult*> >; _Compare = __gnu_cxx::__ops::_Iter_comp_iter<mine_affine_period_laws(const std::vector<ScanResult>&, int, int)::<lambda(int*, int*)> >]’
 1817 |           std::__insertion_sort(__first, __first + int(_S_threshold), __comp);
      |           ~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/stl_algo.h:1908:31:   required from ‘void std::__sort(_RandomAccessIterator, _RandomAccessIterator, _Compare) [with _RandomAccessIterator = __gnu_cxx::__normal_iterator<const ScanResult**, vector<const ScanResult*> >; _Compare = __gnu_cxx::__ops::_Iter_comp_iter<mine_affine_period_laws(const std::vector<ScanResult>&, int, int)::<lambda(int*, int*)> >]’
 1908 |           std::__final_insertion_sort(__first, __last, __comp);
      |           ~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/stl_algo.h:4805:18:   required from ‘void std::sort(_RAIter, _RAIter, _Compare) [with _RAIter = __gnu_cxx::__normal_iterator<const ScanResult**, vector<const ScanResult*> >; _Compare = mine_affine_period_laws(const std::vector<ScanResult>&, int, int)::<lambda(int*, int*)>]’
 4805 |       std::__sort(__first, __last, __gnu_cxx::__ops::__iter_comp_iter(__comp));
      |       ~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
distance_subtraction_research.cpp:368:18:   required from here
  368 |         std::sort(rows.begin(), rows.end(), [](auto* a, auto* b){ return a->k < b->k; });
      |         ~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/predefined_ops.h:240:30: error: no match for call to ‘(mine_affine_period_laws(const std::vector&, int, int)::) (const ScanResult*&, const ScanResult*&)’
  240 |         { return bool(_M_comp(__val, *__it)); }
      |                       ~~~~~~~^~~~~~~~~~~~~~
distance_subtraction_research.cpp:368:45: note: candidate: ‘mine_affine_period_laws(const std::vector&, int, int)::’
  368 |         std::sort(rows.begin(), rows.end(), [](auto* a, auto* b){ return a->k < b->k; });
      |                                             ^
distance_subtraction_research.cpp:368:45: note:   no known conversion for argument 1 from ‘const ScanResult*’ to ‘int*’
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/predefined_ops.h: In instantiation of ‘bool __gnu_cxx::__ops::_Val_comp_iter<_Compare>::operator()(_Value&, _Iterator) [with _Value = const ScanResult*; _Iterator = __gnu_cxx::__normal_iterator<const ScanResult**, std::vector<const ScanResult*> >; _Compare = mine_contiguous_affine_regimes(const std::vector<ScanResult>&, int)::<lambda(int*, int*)>]’:
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/stl_algo.h:1757:20:   required from ‘void std::__unguarded_linear_insert(_RandomAccessIterator, _Compare) [with _RandomAccessIterator = __gnu_cxx::__normal_iterator<const ScanResult**, vector<const ScanResult*> >; _Compare = __gnu_cxx::__ops::_Val_comp_iter<mine_contiguous_affine_regimes(const std::vector<ScanResult>&, int)::<lambda(int*, int*)> >]’
 1757 |       while (__comp(__val, __next))
      |              ~~~~~~^~~~~~~~~~~~~~~
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/stl_algo.h:1785:36:   required from ‘void std::__insertion_sort(_RandomAccessIterator, _RandomAccessIterator, _Compare) [with _RandomAccessIterator = __gnu_cxx::__normal_iterator<const ScanResult**, vector<const ScanResult*> >; _Compare = __gnu_cxx::__ops::_Iter_comp_iter<mine_contiguous_affine_regimes(const std::vector<ScanResult>&, int)::<lambda(int*, int*)> >]’
 1785 |             std::__unguarded_linear_insert(__i,
      |             ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~
 1786 |                                 __gnu_cxx::__ops::__val_comp_iter(__comp));
      |                                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/stl_algo.h:1817:25:   required from ‘void std::__final_insertion_sort(_RandomAccessIterator, _RandomAccessIterator, _Compare) [with _RandomAccessIterator = __gnu_cxx::__normal_iterator<const ScanResult**, vector<const ScanResult*> >; _Compare = __gnu_cxx::__ops::_Iter_comp_iter<mine_contiguous_affine_regimes(const std::vector<ScanResult>&, int)::<lambda(int*, int*)> >]’
 1817 |           std::__insertion_sort(__first, __first + int(_S_threshold), __comp);
      |           ~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/stl_algo.h:1908:31:   required from ‘void std::__sort(_RandomAccessIterator, _RandomAccessIterator, _Compare) [with _RandomAccessIterator = __gnu_cxx::__normal_iterator<const ScanResult**, vector<const ScanResult*> >; _Compare = __gnu_cxx::__ops::_Iter_comp_iter<mine_contiguous_affine_regimes(const std::vector<ScanResult>&, int)::<lambda(int*, int*)> >]’
 1908 |           std::__final_insertion_sort(__first, __last, __comp);
      |           ~~~~~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/stl_algo.h:4805:18:   required from ‘void std::sort(_RAIter, _RAIter, _Compare) [with _RAIter = __gnu_cxx::__normal_iterator<const ScanResult**, vector<const ScanResult*> >; _Compare = mine_contiguous_affine_regimes(const std::vector<ScanResult>&, int)::<lambda(int*, int*)>]’
 4805 |       std::__sort(__first, __last, __gnu_cxx::__ops::__iter_comp_iter(__comp));
      |       ~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
distance_subtraction_research.cpp:421:18:   required from here
  421 |         std::sort(rows.begin(), rows.end(), [](auto* a, auto* b){ return a->k < b->k; });
      |         ~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/predefined_ops.h:240:30: error: no match for call to ‘(mine_contiguous_affine_regimes(const std::vector&, int)::) (const ScanResult*&, const ScanResult*&)’
  240 |         { return bool(_M_comp(__val, *__it)); }
      |                       ~~~~~~~^~~~~~~~~~~~~~
distance_subtraction_research.cpp:421:45: note: candidate: ‘mine_contiguous_affine_regimes(const std::vector&, int)::’
  421 |         std::sort(rows.begin(), rows.end(), [](auto* a, auto* b){ return a->k < b->k; });
      |                                             ^
distance_subtraction_research.cpp:421:45: note:   no known conversion for argument 1 from ‘const ScanResult*’ to ‘int*’
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/predefined_ops.h: In instantiation of ‘bool __gnu_cxx::__ops::_Iter_comp_val<_Compare>::operator()(_Iterator, _Value&) [with _Iterator = __gnu_cxx::__normal_iterator<const ScanResult**, std::vector<const ScanResult*> >; _Value = const ScanResult*; _Compare = mine_affine_period_laws(const std::vector<ScanResult>&, int, int)::<lambda(int*, int*)>]’:
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/stl_heap.h:140:48:   required from ‘void std::__push_heap(_RandomAccessIterator, _Distance, _Distance, _Tp, _Compare&) [with _RandomAccessIterator = __gnu_cxx::__normal_iterator<const ScanResult**, vector<const ScanResult*> >; _Distance = long int; _Tp = const ScanResult*; _Compare = __gnu_cxx::__ops::_Iter_comp_val<mine_affine_period_laws(const std::vector<ScanResult>&, int, int)::<lambda(int*, int*)> >]’
  140 |       while (__holeIndex > __topIndex && __comp(__first + __parent, __value))
      |                                          ~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/stl_heap.h:247:23:   required from ‘void std::__adjust_heap(_RandomAccessIterator, _Distance, _Distance, _Tp, _Compare) [with _RandomAccessIterator = __gnu_cxx::__normal_iterator<const ScanResult**, vector<const ScanResult*> >; _Distance = long int; _Tp = const ScanResult*; _Compare = __gnu_cxx::__ops::_Iter_comp_iter<mine_affine_period_laws(const std::vector<ScanResult>&, int, int)::<lambda(int*, int*)> >]’
  247 |       std::__push_heap(__first, __holeIndex, __topIndex,
      |       ~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  248 |                        _GLIBCXX_MOVE(__value), __cmp);
      |                        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/stl_heap.h:356:22:   required from ‘void std::__make_heap(_RandomAccessIterator, _RandomAccessIterator, _Compare&) [with _RandomAccessIterator = __gnu_cxx::__normal_iterator<const ScanResult**, vector<const ScanResult*> >; _Compare = __gnu_cxx::__ops::_Iter_comp_iter<mine_affine_period_laws(const std::vector<ScanResult>&, int, int)::<lambda(int*, int*)> >]’
  356 |           std::__adjust_heap(__first, __parent, __len, _GLIBCXX_MOVE(__value),
      |           ~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  357 |                              __comp);
      |                              ~~~~~~~
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/stl_algo.h:1593:23:   required from ‘void std::__heap_select(_RandomAccessIterator, _RandomAccessIterator, _RandomAccessIterator, _Compare) [with _RandomAccessIterator = __gnu_cxx::__normal_iterator<const ScanResult**, vector<const ScanResult*> >; _Compare = __gnu_cxx::__ops::_Iter_comp_iter<mine_affine_period_laws(const std::vector<ScanResult>&, int, int)::<lambda(int*, int*)> >]’
 1593 |       std::__make_heap(__first, __middle, __comp);
      |       ~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/stl_algo.h:1868:25:   required from ‘void std::__partial_sort(_RandomAccessIterator, _RandomAccessIterator, _RandomAccessIterator, _Compare) [with _RandomAccessIterator = __gnu_cxx::__normal_iterator<const ScanResult**, vector<const ScanResult*> >; _Compare = __gnu_cxx::__ops::_Iter_comp_iter<mine_affine_period_laws(const std::vector<ScanResult>&, int, int)::<lambda(int*, int*)> >]’
 1868 |       std::__heap_select(__first, __middle, __last, __comp);
      |       ~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/stl_algo.h:1884:27:   required from ‘void std::__introsort_loop(_RandomAccessIterator, _RandomAccessIterator, _Size, _Compare) [with _RandomAccessIterator = __gnu_cxx::__normal_iterator<const ScanResult**, vector<const ScanResult*> >; _Size = long int; _Compare = __gnu_cxx::__ops::_Iter_comp_iter<mine_affine_period_laws(const std::vector<ScanResult>&, int, int)::<lambda(int*, int*)> >]’
 1884 |               std::__partial_sort(__first, __last, __last, __comp);
      |               ~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/stl_algo.h:1905:25:   required from ‘void std::__sort(_RandomAccessIterator, _RandomAccessIterator, _Compare) [with _RandomAccessIterator = __gnu_cxx::__normal_iterator<const ScanResult**, vector<const ScanResult*> >; _Compare = __gnu_cxx::__ops::_Iter_comp_iter<mine_affine_period_laws(const std::vector<ScanResult>&, int, int)::<lambda(int*, int*)> >]’
 1905 |           std::__introsort_loop(__first, __last,
      |           ~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~
 1906 |                                 std::__lg(__last - __first) * 2,
      |                                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 1907 |                                 __comp);
      |                                 ~~~~~~~
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/stl_algo.h:4805:18:   required from ‘void std::sort(_RAIter, _RAIter, _Compare) [with _RAIter = __gnu_cxx::__normal_iterator<const ScanResult**, vector<const ScanResult*> >; _Compare = mine_affine_period_laws(const std::vector<ScanResult>&, int, int)::<lambda(int*, int*)>]’
 4805 |       std::__sort(__first, __last, __gnu_cxx::__ops::__iter_comp_iter(__comp));
      |       ~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
distance_subtraction_research.cpp:368:18:   required from here
  368 |         std::sort(rows.begin(), rows.end(), [](auto* a, auto* b){ return a->k < b->k; });
      |         ~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/predefined_ops.h:196:30: error: no match for call to ‘(mine_affine_period_laws(const std::vector&, int, int)::) (const ScanResult*&, const ScanResult*&)’
  196 |         { return bool(_M_comp(*__it, __val)); }
      |                       ~~~~~~~^~~~~~~~~~~~~~
distance_subtraction_research.cpp:368:45: note: candidate: ‘mine_affine_period_laws(const std::vector&, int, int)::’
  368 |         std::sort(rows.begin(), rows.end(), [](auto* a, auto* b){ return a->k < b->k; });
      |                                             ^
distance_subtraction_research.cpp:368:45: note:   no known conversion for argument 1 from ‘const ScanResult*’ to ‘int*’
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/predefined_ops.h: In instantiation of ‘bool __gnu_cxx::__ops::_Iter_comp_val<_Compare>::operator()(_Iterator, _Value&) [with _Iterator = __gnu_cxx::__normal_iterator<const ScanResult**, std::vector<const ScanResult*> >; _Value = const ScanResult*; _Compare = mine_contiguous_affine_regimes(const std::vector<ScanResult>&, int)::<lambda(int*, int*)>]’:
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/stl_heap.h:140:48:   required from ‘void std::__push_heap(_RandomAccessIterator, _Distance, _Distance, _Tp, _Compare&) [with _RandomAccessIterator = __gnu_cxx::__normal_iterator<const ScanResult**, vector<const ScanResult*> >; _Distance = long int; _Tp = const ScanResult*; _Compare = __gnu_cxx::__ops::_Iter_comp_val<mine_contiguous_affine_regimes(const std::vector<ScanResult>&, int)::<lambda(int*, int*)> >]’
  140 |       while (__holeIndex > __topIndex && __comp(__first + __parent, __value))
      |                                          ~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/stl_heap.h:247:23:   required from ‘void std::__adjust_heap(_RandomAccessIterator, _Distance, _Distance, _Tp, _Compare) [with _RandomAccessIterator = __gnu_cxx::__normal_iterator<const ScanResult**, vector<const ScanResult*> >; _Distance = long int; _Tp = const ScanResult*; _Compare = __gnu_cxx::__ops::_Iter_comp_iter<mine_contiguous_affine_regimes(const std::vector<ScanResult>&, int)::<lambda(int*, int*)> >]’
  247 |       std::__push_heap(__first, __holeIndex, __topIndex,
      |       ~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  248 |                        _GLIBCXX_MOVE(__value), __cmp);
      |                        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/stl_heap.h:356:22:   required from ‘void std::__make_heap(_RandomAccessIterator, _RandomAccessIterator, _Compare&) [with _RandomAccessIterator = __gnu_cxx::__normal_iterator<const ScanResult**, vector<const ScanResult*> >; _Compare = __gnu_cxx::__ops::_Iter_comp_iter<mine_contiguous_affine_regimes(const std::vector<ScanResult>&, int)::<lambda(int*, int*)> >]’
  356 |           std::__adjust_heap(__first, __parent, __len, _GLIBCXX_MOVE(__value),
      |           ~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  357 |                              __comp);
      |                              ~~~~~~~
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/stl_algo.h:1593:23:   required from ‘void std::__heap_select(_RandomAccessIterator, _RandomAccessIterator, _RandomAccessIterator, _Compare) [with _RandomAccessIterator = __gnu_cxx::__normal_iterator<const ScanResult**, vector<const ScanResult*> >; _Compare = __gnu_cxx::__ops::_Iter_comp_iter<mine_contiguous_affine_regimes(const std::vector<ScanResult>&, int)::<lambda(int*, int*)> >]’
 1593 |       std::__make_heap(__first, __middle, __comp);
      |       ~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/stl_algo.h:1868:25:   required from ‘void std::__partial_sort(_RandomAccessIterator, _RandomAccessIterator, _RandomAccessIterator, _Compare) [with _RandomAccessIterator = __gnu_cxx::__normal_iterator<const ScanResult**, vector<const ScanResult*> >; _Compare = __gnu_cxx::__ops::_Iter_comp_iter<mine_contiguous_affine_regimes(const std::vector<ScanResult>&, int)::<lambda(int*, int*)> >]’
 1868 |       std::__heap_select(__first, __middle, __last, __comp);
      |       ~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/stl_algo.h:1884:27:   required from ‘void std::__introsort_loop(_RandomAccessIterator, _RandomAccessIterator, _Size, _Compare) [with _RandomAccessIterator = __gnu_cxx::__normal_iterator<const ScanResult**, vector<const ScanResult*> >; _Size = long int; _Compare = __gnu_cxx::__ops::_Iter_comp_iter<mine_contiguous_affine_regimes(const std::vector<ScanResult>&, int)::<lambda(int*, int*)> >]’
 1884 |               std::__partial_sort(__first, __last, __last, __comp);
      |               ~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/stl_algo.h:1905:25:   required from ‘void std::__sort(_RandomAccessIterator, _RandomAccessIterator, _Compare) [with _RandomAccessIterator = __gnu_cxx::__normal_iterator<const ScanResult**, vector<const ScanResult*> >; _Compare = __gnu_cxx::__ops::_Iter_comp_iter<mine_contiguous_affine_regimes(const std::vector<ScanResult>&, int)::<lambda(int*, int*)> >]’
 1905 |           std::__introsort_loop(__first, __last,
      |           ~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~~~~~~
 1906 |                                 std::__lg(__last - __first) * 2,
      |                                 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
 1907 |                                 __comp);
      |                                 ~~~~~~~
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/stl_algo.h:4805:18:   required from ‘void std::sort(_RAIter, _RAIter, _Compare) [with _RAIter = __gnu_cxx::__normal_iterator<const ScanResult**, vector<const ScanResult*> >; _Compare = mine_contiguous_affine_regimes(const std::vector<ScanResult>&, int)::<lambda(int*, int*)>]’
 4805 |       std::__sort(__first, __last, __gnu_cxx::__ops::__iter_comp_iter(__comp));
      |       ~~~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
distance_subtraction_research.cpp:421:18:   required from here
  421 |         std::sort(rows.begin(), rows.end(), [](auto* a, auto* b){ return a->k < b->k; });
      |         ~~~~~~~~~^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/nix/store/k6gpflj398qaxzx4bmqhnnj4l328vabk-gcc-14.3.0/include/c++/14.3.0/bits/predefined_ops.h:196:30: error: no match for call to ‘(mine_contiguous_affine_regimes(const std::vector&, int)::) (const ScanResult*&, const ScanResult*&)’
  196 |         { return bool(_M_comp(*__it, __val)); }
      |                       ~~~~~~~^~~~~~~~~~~~~~
distance_subtraction_research.cpp:421:45: note: candidate: ‘mine_contiguous_affine_regimes(const std::vector&, int)::’
  421 |         std::sort(rows.begin(), rows.end(), [](auto* a, auto* b){ return a->k < b->k; });
      |                                             ^
distance_subtraction_research.cpp:421:45: note:   no known conversion for argument 1 from ‘const ScanResult*’ to ‘int*’
```