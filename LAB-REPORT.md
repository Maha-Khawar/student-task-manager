# Lab Report

## 1. Git vs GitHub; add, commit, push
Git is a version control tool that runs on my computer and records the history of my code. GitHub is an online service that hosts Git repositories and adds collaboration features such as Issues, Pull Requests, and Actions. `git add` stages changes for the next commit, `git commit` saves the staged changes as a snapshot with a message, and `git push` uploads my local commits to GitHub.

## 2. Branches, Pull Requests, and merge conflicts
Branches let me build each feature separately so unfinished code does not break main. Pull Requests let changes be reviewed and discussed before they are merged into main. A merge conflict happens when two branches change the same line of the same file in different ways, so Git cannot choose which version to keep.

## 3. Fetch vs pull; merge vs rebase
`git fetch` downloads new commits from the remote but does not change my working files. `git pull` does a fetch and then merges the changes into my current branch. Merge combines two branches with a merge commit and keeps the full history. Rebase replays my commits on top of another branch, which gives a straight, linear history but rewrites commits.

## 4. GitHub Issues and Actions
Issues track features, bugs, and documentation tasks, so the team knows what needs to be done and who is doing it. GitHub Actions automatically runs workflows, such as the unit tests, on every push and Pull Request, so problems are caught early before code is merged.

## 5. A difficulty I faced
When I tried to open my project folder in PowerShell, the `cd` command failed because the path contained spaces. I solved it by putting the whole path in quotes.
