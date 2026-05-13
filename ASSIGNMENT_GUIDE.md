# Assignment 4: CI/CD Pipeline - Complete Step-by-Step Guide

## 📋 What This Assignment Is About

This assignment teaches you how to build a **real DevOps pipeline** - automating the entire software development workflow from code push → testing → deployment. It's about using GitHub Actions to automatically:
- Build your application
- Run tests automatically
- Deploy to production (Render)

**Real-world relevance:** Modern development teams use CI/CD to ensure code quality and enable rapid, safe deployments.

---

## 🎯 Assignment Requirements (10 Marks Total)

| Criteria | Marks | What You Need |
|----------|-------|---------------|
| Project Structure | 2 | Proper folder layout (app.py, test_app.py, requirements.txt, .github/workflows/) |
| CI Pipeline (Build + Test) | 3 | Working GitHub Actions workflow that builds and runs tests |
| Test Implementation | 2 | At least one unit test for your Flask/Node.js app |
| Deployment Automation | 2 | Auto-deployment to Render on every push to main |
| Documentation | 1 | README explaining your project and how it works |
| **TOTAL** | **10** | |

---

## 📂 Project Structure You Need to Create

```
dso_assignment_4/
├── README.md                           # Project documentation
├── app.py                              # Your Flask application
├── test_app.py                         # Your unit tests
├── requirements.txt                    # Python dependencies
├── .github/
│   └── workflows/
│       └── ci.yml                      # GitHub Actions workflow file
└── .gitignore                          # Ignore unnecessary files
```

---

## ⏰ Step-by-Step Implementation Plan

### **PHASE 1: Setup Project Structure** ✅
**Time: 5 minutes**

**What to do:**
1. Create the Flask backend app (`app.py`)
2. Create the test file (`test_app.py`)
3. Create `requirements.txt`
4. Create `.gitignore`
5. Create `.github/workflows/` directory structure

---

### **PHASE 2: Write the Flask Application** ✅
**Time: 10 minutes**

**Requirements:**
- Simple Flask app with at least one route
- Can be a simple "Hello World" or any basic API
- Must be testable

**Example:**
```python
# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return {'message': 'Hello, World!'}

@app.route('/api/add/<int:a>/<int:b>')
def add(a, b):
    return {'result': a + b}

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

---

### **PHASE 3: Write Unit Tests** ✅
**Time: 10 minutes**

**Requirements:**
- Minimum 1 test (can have more)
- Use pytest framework
- Test your Flask routes

**Example:**
```python
# test_app.py
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    """Test the home endpoint"""
    response = client.get('/')
    assert response.status_code == 200
    assert response.json['message'] == 'Hello, World!'

def test_add(client):
    """Test the add endpoint"""
    response = client.get('/api/add/5/3')
    assert response.status_code == 200
    assert response.json['result'] == 8
```

---

### **PHASE 4: Setup GitHub Actions CI/CD Workflow** ✅
**Time: 15 minutes**

**Requirements:**
- Workflow file: `.github/workflows/ci.yml`
- Triggers on push to `main` branch
- Steps: Checkout → Setup Python → Install dependencies → Run tests → Deploy message

**Steps to create:**

1. Create directory: `.github/workflows/`
2. Create file: `ci.yml` inside that directory

**Workflow file content:**
```yaml
name: CI/CD Pipeline

on:
  push:
    branches: [ "main" ]

jobs:
  build-test-deploy:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: "3.9"

    - name: Install dependencies
      run: pip install -r requirements.txt

    - name: Run tests
      run: pytest

    - name: Deploy to Render
      run: |
        echo "Deploying to Render..."
        # (Deployment details in Phase 5)
```

---

### **PHASE 5: Setup Render Deployment** ✅
**Time: 20 minutes**

**What you need to do:**

1. **Create Render Account** (free tier)
   - Go to https://render.com
   - Sign up with GitHub account

2. **Create Web Service on Render**
   - Click "New +" → "Web Service"
   - Connect your GitHub repo
   - Select your repository
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `python app.py`
   - Environment: Add `PYTHON_VERSION=3.9`
   - Click "Create Web Service"

3. **Get Render Deploy Hook** (for automatic deployment)
   - In Render dashboard, go to your service
   - Settings → Deploy Hook
   - Copy the webhook URL

4. **Add Deploy Step to GitHub Actions**
   - Update your `.github/workflows/ci.yml`:
   ```yaml
   - name: Deploy to Render
     run: |
       curl ${{ secrets.RENDER_DEPLOY_HOOK }}
   ```

5. **Add Secret to GitHub**
   - Go to GitHub repo → Settings → Secrets and variables → Actions
   - Click "New repository secret"
   - Name: `RENDER_DEPLOY_HOOK`
   - Value: Paste the webhook URL from Render
   - Click "Add secret"

---

### **PHASE 6: Create requirements.txt** ✅
**Time: 2 minutes**

**Content:**
```
flask==2.3.0
pytest==7.3.0
```

---

### **PHASE 7: Create README.md** ✅
**Time: 10 minutes**

**What to include:**
```markdown
# Assignment 4: CI/CD Pipeline

## Project Description
A simple Flask application with automated CI/CD pipeline using GitHub Actions.

## Features
- Simple Flask API endpoints
- Unit tests with pytest
- Automated testing via GitHub Actions
- Auto-deployment to Render

## Project Structure
- `app.py` - Flask application
- `test_app.py` - Unit tests
- `.github/workflows/ci.yml` - GitHub Actions workflow
- `requirements.txt` - Python dependencies

## How to Run Locally
1. Install dependencies: `pip install -r requirements.txt`
2. Run app: `python app.py`
3. Run tests: `pytest`

## CI/CD Pipeline
- **Build:** Installs dependencies on every push
- **Test:** Runs pytest automatically
- **Deploy:** Deploys to Render automatically

## Live App
[Your Render URL] (You'll get this from Render dashboard)

## How It Works
1. Code is pushed to GitHub
2. GitHub Actions automatically triggers
3. Runs build and test steps
4. If successful, deploys to Render
5. App is live at the Render URL
```

---

## 🔄 Complete Workflow Summary

```
You Write Code
    ↓
Push to GitHub
    ↓
GitHub Actions Triggers (ci.yml)
    ↓
├─ Checkout Code
├─ Setup Python
├─ Install Dependencies (pip install)
├─ Run Tests (pytest)
    ↓
    └─ If All Pass → Trigger Render Deploy
         ↓
         ✅ App Goes Live on Render
```

---

## 📝 What to Submit

As per assignment requirements, you need:

1. ✅ **GitHub Repository**
   - Make it public
   - Include all files (app.py, test_app.py, ci.yml, etc.)

2. ✅ **Workflow File**
   - `.github/workflows/ci.yml`
   - Should be visible in GitHub Actions tab

3. ✅ **Test Output Screenshot**
   - Go to GitHub → Actions tab
   - Click on latest workflow run
   - Take screenshot showing tests passed ✅

4. ✅ **Live App URL**
   - Copy your Render URL
   - Include in README.md
   - Should be working and accessible

---

## ✅ Quick Checklist

- [ ] Created `app.py` with Flask app
- [ ] Created `test_app.py` with at least 1 test
- [ ] Created `requirements.txt` with dependencies
- [ ] Created `.github/workflows/ci.yml`
- [ ] Pushed all files to GitHub
- [ ] GitHub Actions ran successfully (check Actions tab)
- [ ] Created Render account and Web Service
- [ ] Got Render Deploy Hook URL
- [ ] Added `RENDER_DEPLOY_HOOK` secret to GitHub
- [ ] App is deployed and live on Render
- [ ] Updated README.md with documentation
- [ ] All requirements met

---

## 🐛 Troubleshooting

| Problem | Solution |
|---------|----------|
| GitHub Actions fails to install dependencies | Check `requirements.txt` syntax - no extra spaces or blank lines |
| Tests fail | Run `pytest` locally first and fix errors |
| Render shows "Application Error" | Check Render logs - usually missing dependencies or wrong start command |
| Auto-deploy not working | Verify `RENDER_DEPLOY_HOOK` secret is added correctly to GitHub |
| Can't access Render app | Make sure Render service status shows "Live" (green) |

---

## 📚 Key Concepts Explained

**CI (Continuous Integration):**
- Automatically build and test code on every push
- Catch bugs early before they go to production

**CD (Continuous Deployment):**
- Automatically deploy working code to production
- Users always have the latest stable version

**GitHub Actions:**
- GitHub's automation tool
- Runs workflows based on triggers (push, PR, schedule, etc.)
- Free for public repos

**Render:**
- Cloud hosting platform
- Hosts your Flask app and makes it accessible via URL
- Has free tier

---

## 🎓 Learning Outcomes

After completing this assignment, you'll understand:
1. How modern DevOps pipelines work
2. How to write automated tests
3. How to use GitHub Actions for automation
4. How to deploy applications to the cloud
5. How to set up CI/CD best practices

---

**Good luck! You've got this! 🚀**
