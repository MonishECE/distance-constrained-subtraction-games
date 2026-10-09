# Push the formal Theorems A/B update to the existing repository

Target: https://github.com/MonishECE/distance-constrained-subtraction-games

**Important:** A GitHub integration 403 error prevented the assistant from writing to the repository. The ZIP is prepared locally; nothing in this update has been pushed by the assistant.

The GitHub repository already has an outer `distance-constrained-subtraction-games/` directory containing its paper and sources. The provided ZIP has exactly that same top directory. **Do not add an extra enclosing directory** when copying.

## Safe Git command workflow

1. Clone your existing repo (or open a verified local clone):

```bash
git clone https://github.com/MonishECE/distance-constrained-subtraction-games.git
cd distance-constrained-subtraction-games
git pull --ff-only origin main
git switch -c research/formal-theorems-a-b
```

2. Extract the **changes-only ZIP** directly into this Git repository root. It contains paths prefixed by `distance-constrained-subtraction-games/`; merge/replace only those paths. Avoid deleting unrelated repository directories.

3. Inspect and stage:

```bash
git status
git diff --stat
git add distance-constrained-subtraction-games
git diff --cached --stat
```

4. Commit and push:

```bash
git commit -m "Formalize Theorems A/B and update computer-assisted proof paper"
git push -u origin research/formal-theorems-a-b
```

5. Open a pull request to `main` on GitHub, review the diff, and merge only when your team confirms the theorem statements and citations.

## Fast verification

From the GitHub repo root:

```bash
cd distance-constrained-subtraction-games
python src/verify_theorems_ab.py
python src/row_interval_classifier.py self-test
python src/affine_region_extractor.py self-test
```

You should see 21 verified Theorem B rows and passing self-tests. The program regenerates a deterministic CSV and SHA summary.

## Main changed files

- `paper/main.tex`, `paper/main.pdf`, `paper/generated/certificate_rows.tex`
- `paper/references.tex`, `paper/references.bib`, `paper/WORKS_CITED.md`
- `paper/PROOF_AUDIT.md`, `paper/README.md`
- `paper/archive/main_initial_2026-10-04.tex` (unaltered historical source)
- `src/verify_theorems_ab.py`
- `data/certificates/theorem_B_audit.csv`, `data/certificates/theorem_B_audit.json`
- `RESEARCH_UPDATE_CONCLUSION.md`, `README.md`, `CHANGELOG.md`, `MANIFEST_SHA256.txt`

**GitHub permissions:** An integration able to read a repository may still lack permission to create branches or modify files. If you want ChatGPT to push instead of running commands, grant the appropriate GitHub integration **Contents: read and write** access for this repository, then explicitly retry the action.
