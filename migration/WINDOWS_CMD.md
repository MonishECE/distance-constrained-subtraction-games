# Safe replacement in Windows CMD

Use a **new, empty working folder**, Git for Windows and Python 3.10+. Extract the download first. Set PACKAGE to the extracted folder containing README.md, src and migration. Change the example paths below to yours. These commands are for CMD, not PowerShell.

```cmd
set "PACKAGE=C:\Users\YOURNAME\Downloads\distance-constrained-subtraction-games"
set "CHECKOUT=C:\Users\YOURNAME\Documents\distance-games-clean-review"
git clone https://github.com/MonishECE/distance-constrained-subtraction-games.git "%CHECKOUT%"
cd /d "%CHECKOUT%"
git fetch origin
git switch -c cleanup/consolidated-research-2026-10-10 origin/main
git status --short
python "%PACKAGE%\src\verify_package.py"
python "%PACKAGE%\migration\replace_repository.py" --repo "%CHECKOUT%"
```

Read `DELETION_AUDIT.csv` and `PROVENANCE.md` in the package. The dry run changes nothing. The tool refuses a dirty checkout, untracked/ignored files, an unexpected repository, an unaudited commit, or an original branch. If GitHub has advanced beyond the recorded snapshot, stop and refresh the audit; do not bypass the guard.

When the audit and dry run are acceptable:

```cmd
python "%PACKAGE%\migration\replace_repository.py" --repo "%CHECKOUT%" --apply
python src\verify_package.py
git add -A
git diff --cached --stat
git diff --cached --name-status
git diff --cached -- README.md src/verify_theorems_ab.py
git status --short
```

The replacement tool creates a complete Git bundle **beside** the checkout before changing any tracked files. It preserves `.git`, remotes and history. It removes old tracked files individually and copies the consolidated contents. Old content remains in the ZIP's archives and Git history. It does not stage, commit, push, merge, delete branches, or call GitHub. No `rmdir`, wildcard deletion or `git clean` is needed. Empty old folders may remain locally; Git does not track them.

If the staged changes look correct, finish on the review branch:

```cmd
git commit -m "Consolidate research sources, evidence and migration audit"
git push -u origin cleanup/consolidated-research-2026-10-10
```

Open a pull request to main and review it before merging. Keep the research branch and backup until the migration is accepted; the package does not recommend deleting research history. To cancel before committing, leave the review clone alone and use your original checkout. To recover elsewhere, `git clone "C:\path\to\the-backup.bundle" "C:\path\to\recovered"`. Avoid destructive reset commands if you added new work.

## Audit interpretation

Every tracked file at each branch head has a CSV row with its exact original hash and retained destination. `retain_same_path` keeps an identical root path, `replace_at_same_path` overwrites a root path while preserving its original, and `remove_old_path_preserve_content` removes an obsolete/nested path with byte-for-byte content retained elsewhere. This is a proposed local migration, not evidence of remote deletion. Hidden .gitignore files are included. No existing LICENSE was present; none is invented.

## Keep after migration

Keep the single root, paper, overleaf, src, all evidence folders, archives and migration records. The three old nested package directories are represented by the audit and archives; do not import them as additional active copies. Historical manuals may refer to unavailable row-interval artifacts. Use the new root README and reproducibility instructions.
