# Quick Action Plan - Do This In Order

## ⚡ 5-Minute Quick Start

### Step 1: Create Project Files (5 min)
```bash
# In your project root: c:\Users\HP\OneDrive\Desktop\dso_assignment_4\

# Create Flask app
# File: app.py
# File: test_app.py
# File: requirements.txt

# Create workflows folder
mkdir -p .github\workflows

# Create workflow file
# File: .github\workflows\ci.yml
```

---

## 📋 Exact Files You Need to Create

### 1️⃣ `app.py`
```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return {'message': 'Hello, World!', 'status': 'success'}

@app.route('/api/add/<int:a>/<int:b>')
def add(a, b):
    return {'result': a + b}

if __name__ == '__main__':
    app.run(debug=True, port=5000)
```

### 2️⃣ `test_app.py`
```python
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.json['status'] == 'success'

def test_add(client):
    response = client.get('/api/add/10/5')
    assert response.status_code == 200
    assert response.json['result'] == 15
```

### 3️⃣ `requirements.txt`
```
flask==2.3.0
pytest==7.3.0
```

### 4️⃣ `.github/workflows/ci.yml`
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
      run: echo "Deploying to Render... Tests passed!"
```

### 5️⃣ `.gitignore`
```
__pycache__/
*.pyc
.pytest_cache/
*.egg-info/
.env
.venv
venv/
```

### 6️⃣ `README.md`
```markdown
# CI/CD Assignment - Flask App

## What is This?
A simple Flask application with automated CI/CD pipeline using GitHub Actions.

## Project Files
- `app.py` - The Flask application
- `test_app.py` - Unit tests
- `requirements.txt` - Dependencies
- `.github/workflows/ci.yml` - CI/CD pipeline

## How to Run Locally
```bash
pip install -r requirements.txt
python app.py
```

## How to Run Tests
```bash
pytest
```

## CI/CD Pipeline
✅ Runs tests automatically on every push  
✅ Deploys to Render if tests pass  
✅ Live app: [Your Render URL]

## Submission Checklist
- [ ] GitHub repository created and public
- [ ] All 6 files committed and pushed
- [ ] GitHub Actions shows passing tests
- [ ] Deployed to Render and working
```

---

## 🔧 Deployment Setup (Render)

### Step 1: Create Render Account
- Go to https://render.com
- Sign up with GitHub

### Step 2: Create Web Service
1. Click "New +" → "Web Service"
2. Select your GitHub repo
3. Settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `python app.py`
   - **Environment:** Add `PYTHON_VERSION=3.9`
4. Click "Create Web Service"
5. Wait for deployment (2-3 minutes)
6. Copy the URL (e.g., https://your-app-xyz.onrender.com)

### Step 3: Setup Auto-Deployment
1. In Render → Your Service → Settings
2. Find "Deploy Hook" section
3. Copy the webhook URL

4. In GitHub:
   - Settings → Secrets and variables → Actions
   - New secret: `RENDER_DEPLOY_HOOK`
   - Paste the webhook URL

5. Update `.github/workflows/ci.yml` with:
```yaml
- name: Deploy to Render
  run: curl ${{ secrets.RENDER_DEPLOY_HOOK }}
```

---

## ✅ Complete Execution Order

1. **Create 6 files** (app.py, test_app.py, requirements.txt, ci.yml, .gitignore, README.md)
2. **Test locally:**
   ```bash
   pip install -r requirements.txt
   pytest
   python app.py
   ```
3. **Commit and push to GitHub:**
   ```bash
   git add .
   git commit -m "Initial commit: Flask app with CI/CD"
   git push origin main
   ```
4. **Check GitHub Actions:**
   - Go to your repo → Actions tab
   - Should see workflow running
   - Should show ✅ all tests passed

5. **Create Render deployment**
   - Create service
   - Get webhook URL
   - Add GitHub secret
   - Update ci.yml
   - Push again

6. **Verify live app:**
   - Copy Render URL
   - Test in browser
   - Update README with URL

7. **Submit:**
   - GitHub repo link
   - Render URL
   - Screenshot of passing tests
   - README with explanation

---

## 🚀 Expected Timeline

- **File creation:** 5 minutes
- **Local testing:** 5 minutes
- **GitHub setup:** 2 minutes
- **GitHub Actions running:** 2 minutes
- **Render setup:** 10 minutes
- **Testing deployment:** 5 minutes
- **Documentation:** 5 minutes

**Total: ~35 minutes**

---

## 🎯 Marks Breakdown

- **Project Structure** (2 marks) - Your 6 files organized correctly ✅
- **CI Pipeline** (3 marks) - `.github/workflows/ci.yml` works and shows passing builds ✅
- **Tests** (2 marks) - `test_app.py` has tests, all passing ✅
- **Deployment** (2 marks) - Render auto-deployment works ✅
- **Documentation** (1 mark) - Good README explaining everything ✅

**All 10 marks achievable by following this plan!**
