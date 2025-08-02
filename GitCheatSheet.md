# GitHub Cheat Sheet

## 🛠️ Git Basics

| Command | Description |
|---------|-------------|
| `git init` | Initialize a new git repository |
| `git clone <repo-url>` | Clone a remote repo to your machine |
| `git status` | Show current changes and staged files |
| `git add <file>` | Stage file(s) for commit |
| `git commit -m "message"` | Commit staged files with message |
| `git log` | View commit history |
| `git diff` | Show changes in tracked files |
| `git config --global user.name "Name"` | Set global username |
| `git config --global user.email "email@example.com"` | Set global email |

---

## 🔀 Branching and Merging

| Command | Description |
|---------|-------------|
| `git branch` | List all branches |
| `git branch <name>` | Create a new branch |
| `git checkout <branch>` | Switch to a branch |
| `git merge <branch>` | Merge given branch into current branch |
| `git branch -d <branch>` | Delete a branch |

---

## 🌐 Remote Repositories

| Command | Description |
|---------|-------------|
| `git remote add origin <url>` | Add remote repository |
| `git push -u origin main` | Push main branch to remote (first time) |
| `git push` | Push local changes to remote |
| `git pull` | Fetch and merge changes from remote |
| `git fetch` | Fetch changes from remote (no merge) |

---

## 🧹 Undoing Changes

| Command | Description |
|---------|-------------|
| `git restore <file>` | Restore file to last commit |
| `git reset <file>` | Unstage file |
| `git reset --hard` | Reset working directory and index to last commit |
| `git revert <commit>` | Revert changes from a commit |

---

## 📁 .gitignore

- Create a `.gitignore` file to exclude files/directories from being tracked by Git.
- Example:
