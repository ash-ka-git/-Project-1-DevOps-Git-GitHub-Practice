# DevOps Git & GitHub Practice Project

This is a DevOps practice project to get hands-on with Git, GitHub, branching strategies, GitHub Actions, and CI/CD basics.

## Features
- Frontend: Basic HTML
- Backend: Basic Python Flask App
- GitHub Actions for CI

## Git Branches
- `main` — stable branch
- `feature/frontend` — frontend development
- `feature/backend` — backend development

## How to Contribute
1. Fork the repo
2. Clone to your local system
3. Create a new branch for your feature
4. Commit and push changes
5. Raise a Pull Request



#Do you want help in performing this devops project? follow below steps


# Project: DevOps Git & GitHub Practice

## 📁 Folder Structure:

```
devops-git-practice/
├── service-frontend/
│   └── index.html
├── service-backend/
│   └── app.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── README.md
└── .gitignore
```

---

## 📝 README.md

```markdown
# DevOps Git & GitHub Practice Project

This is a DevOps practice project to get hands-on with Git, GitHub, branching strategies, GitHub Actions, and CI/CD basics.

## ✅ Goal
Simulate a real-world DevOps workflow using Git + GitHub + GitHub Actions.

## 🚀 Step-by-Step Process

### 🧱 Step 1: Create GitHub Repository
- Go to https://github.com
- Click on "New" to create a new repository.
- Repository Name: `devops-git-practice`
- Keep it Public or Private (your choice)
- Don’t initialize with README, .gitignore, or license — we’ll do that locally.
- Click **Create Repository**

### 💻 Step 2: Set Up Locally
Open terminal or Git Bash and run:
```bash
mkdir devops-git-practice
cd devops-git-practice
git init
```
Then, manually copy the folder structure and files from this project or use an editor like VS Code.

### 📄 Step 3: Add Files to Git and Push to GitHub
```bash
git add .
git commit -m "Initial commit with frontend, backend and CI setup"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/devops-git-practice.git
git push -u origin main
```
✅ You’ve now pushed your initial code to GitHub.

### 🌿 Step 4: Create and Work on Feature Branches
#### Frontend:
```bash
git checkout -b feature/frontend
# Make changes to service-frontend/index.html
git add .
git commit -m "Updated frontend page"
git push origin feature/frontend
```
Go to GitHub → Create Pull Request (PR) to merge `feature/frontend` into `main`.

#### Backend:
```bash
git checkout main
git checkout -b feature/backend
# Make changes to service-backend/app.py
git add .
git commit -m "Updated backend app"
git push origin feature/backend
```
Go to GitHub → Create Pull Request.

### 🔀 Step 5: Practice Merging & Conflict Resolution
Edit the **same line** in both `feature/frontend` and `feature/backend`, then try merging both into `main`. Git will ask you to resolve conflicts.

```bash
git pull origin main
# Resolve conflict manually
git add conflicted_file
git commit -m "Resolved merge conflict"
```

### ⚙️ Step 6: Enable GitHub Actions
You already have a GitHub Actions workflow in `.github/workflows/ci.yml`. It will trigger on any push or PR to `main`.
- Check the CI runs under the GitHub → Actions tab

### 🏁 Step 7: Tag and Release
Create a new version tag:
```bash
git tag v1.0
git push origin v1.0
```

## 📌 Summary of Git Commands
```bash
git init
git add .
git commit -m "..."
git remote add origin <repo_url>
git push -u origin main
git checkout -b feature/branch
git merge branch
git tag v1.0
```
```

---

## 🖥️ service-frontend/index.html

```html
<!DOCTYPE html>
<html>
<head>
    <title>DevOps Frontend</title>
</head>
<body>
    <h1>Hello from Frontend!</h1>
</body>
</html>
```

---

## 🐍 service-backend/app.py

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Backend!"

if __name__ == '__main__':
    app.run(debug=True)
```

---

## ⚙️ .github/workflows/ci.yml

```yaml
name: CI

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'
      - name: Run Dummy Build
        run: |
          echo "CI is running"
          python --version
```

---

## 📄 .gitignore

```
__pycache__/
*.pyc
.env
```

---

You can now initialize this as a Git repo, push to GitHub, and start practicing your DevOps Git skills!

Let me know if you'd like help setting it up locally or deploying it via GitHub Pages or Docker.

Kudos to your Devops Journey!!!!
