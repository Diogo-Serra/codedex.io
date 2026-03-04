# Codedex.io – Git & GitHub Course

<img src="../public/bannergit_github.gif" alt="Banner" width="800"/>

My solutions and exercises from the [Codedex](https://www.codedex.io) Git & GitHub course.

## About

This folder tracks my progress through the Codedex Git & GitHub course, learning version control fundamentals and collaborative workflows using Git and GitHub.

## Topics Covered

- Introduction to Version Control & Git
- Setting up a repository (`git init`, `git clone`)
- Staging & committing changes (`git add`, `git commit`)
- Branching & merging (`git branch`, `git merge`)
- Remote repositories (`git push`, `git pull`, `git fetch`)
- Pull Requests & code reviews on GitHub
- Resolving merge conflicts
- GitHub features: Issues, Actions, and Pages

## Getting Started

No special setup required — exercises are command-line based. Make sure Git is installed:

```bash
git --version
```

## Chapter Notes

### 01 – Gitting Started

In 2005, **Linus Torvalds** (creator of Linux) built **Git** to solve the chaos of managing multiple versions of code. It's a **version control system** — it tracks every change made to a project over time.

A few years later, **GitHub** launched (founded by Tom Preston-Werner, Chris Wanstrath, and PJ Hyett in San Francisco). Often called the _"Google Drive for code"_, it became the standard platform for storing, sharing, and collaborating on code — now with 150 million+ users.

**Key concepts introduced:**
- A **repository** (repo) is a project folder tracked by Git.
- Git lives on your machine; GitHub lives in the cloud.
- Every project, from "Hello World" to a portfolio piece, is worth pushing.

**Verify Git is installed:**

```bash
git --version
# e.g. git version 2.39.3
```

> If not installed: [git-scm.com](https://git-scm.com) for Mac/Windows installers.

### 02 – GitHub Repos

**Git vs GitHub — the key difference:**

| | Git | GitHub |
|---|---|---|
| What it is | Version control tool | Web platform / host |
| Where it runs | Your local machine | The cloud |
| Relationship | The engine | Built on top of Git |

> You can use Git without GitHub, but not GitHub without Git.

A **repository (repo)** is like a project folder on GitHub — it stores all your code files and assets (images, videos, fonts, etc.).

**Notable profiles to explore:**
- [@codedex-io](https://github.com/codedex-io) — the team
- [@exrlla](https://github.com/exrlla) — community user
- [@juanpflores](https://github.com/juanpflores) — community user

### 03 – Remote & Local

There are two types of repos that work together:

| | Type | Where |
|---|---|---|
| ☁️ Remote | GitHub repo | Internet (latest version) |
| 🏡 Local | Git repo | Your own computer (drafts) |

**Workflow to connect them:**

**1. Initialize a local repo** — turns a normal folder into a Git-tracked project:
```bash
git init
# → Initialized empty Git repository in /path/to/project/.git
```

**2. Link local → remote** — connects your local repo to the GitHub URL:
```bash
git remote add origin <repository_url>
# e.g. git remote add origin https://github.com/username/my-repo.git
```
- `origin` — a nickname for the remote URL (convention, not required)
- `<repository_url>` — the `.git` URL from your GitHub repo page

**3. Rename the branch to `main`:**
```bash
git branch -M main
# -M = move/rename the branch
```

**4. Verify everything:**
```bash
pwd          # confirm you're in the right folder
git branch   # should output: * main
```

### 04 – Working Directory & Staging

Three areas code moves through before reaching GitHub:

| Area | Description | Command |
|---|---|---|
| 💻 Working directory | Your project folder — where you edit files | — |
| 📋 Staging area | Files prepped for the next commit | `git add` |
| 🗄️ Local repo | Saved snapshots of your project history | `git commit` |

**`git add` — stage changes:**

```bash
git add example.txt   # stage one file
git add .             # stage all changed files
git add *.html        # stage all files with a specific extension
```

**`git commit` — save a snapshot:**

```bash
git commit -m 'Your commit message here'
# -m = message flag
```

A successful commit outputs something like:
```
[main 09f4acd] Updated index.html with a new line
 1 file changed, 1 insertion(+)
```

**Good commit message examples:**
- `'Initial commit'`
- `'Add navigation bar to homepage'`
- `'Fix login button alignment'`

> Think of commit messages as journal entries — short, clear, and descriptive, especially when working on a team.

### 05 – Local Push

**`git status` — check what's going on before pushing:**

```bash
git status
```

Tells you the state of every file in your working directory:

| State | Meaning |
|---|---|
| Staged | Ready to be committed |
| Unstaged | Changed but not yet staged |
| Untracked | New file Git hasn't seen before |

Example output:
```
On branch main

No commits yet

Untracked files:
  .DS_Store
  test.py
  output.gif
```

> Use `git status` anytime you're unsure about the state of your repo.

**`git push` — send local commits to GitHub:**

```bash
# First time pushing a branch:
git push -u origin main
# -u sets the upstream link so future pushes remember the target

# Every time after:
git push
```

After pushing, refresh your GitHub repo URL — your files will be live. 🎉

**Full workflow summary:**

```bash
git init
git remote add origin <repository_url>
git branch -M main
git add .
git commit -m 'Initial commit'
git push -u origin main
```

---

## Course

[codedex.io/courses/git-and-github](https://www.codedex.io/courses/git-and-github)
