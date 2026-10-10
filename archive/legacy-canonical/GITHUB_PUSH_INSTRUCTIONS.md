# Push This Project to GitHub

These instructions assume the repository folder has been
downloaded/extracted to your computer.

## Option A: Git Bash / terminal

First create a **new empty repository** on GitHub. Do not initialize it
with a README, `.gitignore`, or license, because this folder already
contains repository files.

Then open Git Bash or a terminal inside the extracted project folder.

### 1. Initialize Git

``` bash
git init -b main
```

If your installed Git is too old for `-b main`, use:

``` bash
git init
git branch -M main
```

### 2. Check what will be committed

``` bash
git status
```

Before pushing, make sure no passwords, API keys, tokens, personal
credentials, or other secrets are present.

### 3. Stage the repository

``` bash
git add .
```

### 4. Create the first commit

``` bash
git commit -m "Initial computational research repository"
```

### 5. Connect the local folder to GitHub

Copy the HTTPS repository URL from the empty GitHub repository. It will
look like:

``` text
https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Then run:

``` bash
git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
git remote -v
```

### 6. Push

``` bash
git push -u origin main
```

After the first push, future updates are normally:

``` bash
git add .
git commit -m "Describe the research update"
git push
```

## Option B: GitHub CLI

If GitHub CLI (`gh`) is installed and authenticated:

``` bash
git init -b main
git add .
git commit -m "Initial computational research repository"
gh repo create --source=. --private --remote=origin --push
```

Replace `--private` with `--public` only when you intentionally want the
research repository publicly visible.

## Suggested repository name

A clear name would be:

``` text
distance-constrained-subtraction-games
```

or

``` text
dynamic-subtraction-game-research
```

## Suggested commit workflow during the project

Make commits at meaningful research checkpoints, for example:

``` bash
git add .
git commit -m "Add exact full-state certificate verifier"
git push
```

``` bash
git add .
git commit -m "Add affine region extraction experiment"
git push
```

``` bash
git add .
git commit -m "Update conjecture after boundary tests"
git push
```

This preserves the chronological development of the research rather than
replacing old results silently.

## If `origin` already exists

Check:

``` bash
git remote -v
```

If it points to the wrong repository:

``` bash
git remote set-url origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

Then:

``` bash
git push -u origin main
```

## Recommended visibility while the research is unfinished

A private repository is useful while the theorem, authorship record, and
competition submission are still being developed. Visibility can be
changed later if the team decides to release the code and data publicly.
