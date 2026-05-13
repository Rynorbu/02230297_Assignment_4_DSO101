# Assignment 4: CI/CD Pipeline - Flask Application

## 📋 Project Overview

This is a **complete CI/CD pipeline implementation** for the DSO101 Bachelor's of Engineering in Software Engineering assignment. The project demonstrates:

✅ Automated Build Pipeline  
✅ Continuous Testing  
✅ Automated Deployment  
✅ GitHub Actions Workflow  
✅ Live Web Application  

---

## 🎯 Project Requirements Met

| Requirement | Status | Details |
|-------------|--------|---------|
| Project Structure | ✅ | Proper folder layout with app.py, test_app.py, requirements.txt, CI/CD workflow |
| CI Pipeline (Build + Test) | ✅ | GitHub Actions workflow builds and tests automatically |
| Unit Tests | ✅ | 6 comprehensive unit tests using pytest |
| Deployment Automation | ✅ | Auto-deployment to Render on successful tests |
| Documentation | ✅ | Complete README with setup and execution instructions |

---

## 📂 Project Structure

```
dso_assignment_4/
├── app.py                          # Flask application
├── test_app.py                     # Unit tests
├── requirements.txt                # Python dependencies
├── .gitignore                      # Git ignore rules
├── README.md                       # This file
├── ASSIGNMENT_GUIDE.md             # Detailed guide
├── QUICK_ACTION_PLAN.md            # Quick reference
└── .github/
    └── workflows/
        └── ci.yml                  # GitHub Actions workflow
```

---

## 🚀 Features

### Application Endpoints

The Flask application provides the following RESTful endpoints:

```
GET /                    # Home endpoint
GET /api/add/<a>/<b>    # Add two numbers
GET /api/subtract/<a>/<b> # Subtract two numbers
GET /health             # Health check
```

### Example Requests

```bash
# Home endpoint
curl http://localhost:5000/

# Add endpoint
curl http://localhost:5000/api/add/10/5
# Response: {"a": 10, "b": 5, "result": 15, "operation": "addition"}

# Subtract endpoint
curl http://localhost:5000/api/subtract/10/3
# Response: {"a": 10, "b": 3, "result": 7, "operation": "subtraction"}

# Health check
curl http://localhost:5000/health
# Response: {"status": "healthy"}
```

---

## 📦 Installation & Setup

### Prerequisites
- Python 3.9+
- pip (Python package manager)
- Git

### Local Installation

```bash
# Clone the repository
git clone https://github.com/Rynorbu/02230297_Assignment_4_DSO101.git
cd dso_assignment_4

# Create virtual environment (optional but recommended)
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

---

## 🧪 Testing

### Run Tests Locally

```bash
# Run all tests
pytest

# Run tests with verbose output
pytest -v

# Run specific test file
pytest test_app.py

# Run with coverage report
pytest --cov=app test_app.py
```

### Test Cases

The project includes 6 comprehensive unit tests:

1. **test_home** - Validates home endpoint returns correct response
2. **test_add** - Tests addition endpoint with positive numbers
3. **test_subtract** - Tests subtraction endpoint
4. **test_health** - Tests health check endpoint
5. **test_add_negative_numbers** - Tests addition with negative numbers
6. **test_subtract_negative_numbers** - Tests subtraction with negative numbers

---

## ▶️ Running the Application

### Local Execution

```bash
# Run the Flask application
python app.py

# Application will be available at:
# http://localhost:5000
```

### Using Flask CLI

```bash
# Set Flask app
export FLASK_APP=app.py
export FLASK_ENV=development

# Run application
flask run
```

---

## 🔄 CI/CD Pipeline Workflow

The GitHub Actions pipeline automatically:

1. **Triggers** on push to `main` branch
2. **Checks out** the latest code
3. **Sets up** Python 3.9 environment
4. **Installs** dependencies from requirements.txt
5. **Runs** all unit tests with pytest
6. **Reports** test results
7. **Deploys** to Render (if tests pass)

### Workflow File Location
```
.github/workflows/ci.yml
```

### Pipeline Status
Check the status in GitHub repository:
- Go to: **Actions** tab
- View: Latest workflow run
- Status: Shows ✅ Pass or ❌ Fail

---

## 🌐 Deployment to Render

### Live Application URL
```
https://dso-assignment-4-ci-cd.onrender.com
```

### Deployment Setup

The application is deployed to Render with:
- **Build Command:** `pip install -r requirements.txt`
- **Start Command:** `python app.py`
- **Environment:** Python 3.9
- **Port:** 5000

### Auto-Deployment Trigger

```yaml
- name: Deploy to Render
  run: curl ${{ secrets.RENDER_DEPLOY_HOOK }}
```

---

## 📊 How It Works

```
Developer Code
    ↓
Push to GitHub (git push)
    ↓
GitHub Actions Triggers
    ↓
┌─────────────────────────┐
│  1. Checkout Code       │
│  2. Setup Python 3.9    │
│  3. Install Packages    │
│  4. Run pytest Tests    │
└─────────────────────────┘
    ↓
  Tests Pass? ✅
    ↓
  Deploy to Render
    ↓
  Live App Updated 🚀
```

---

## 🧑‍💻 Development Workflow

### Making Changes

1. Make code changes locally
2. Test locally: `pytest`
3. Commit changes: `git add .` and `git commit -m "message"`
4. Push to GitHub: `git push origin main`
5. GitHub Actions automatically:
   - Builds your code
   - Runs all tests
   - Deploys to Render
6. View live app at Render URL

### Example Workflow

```bash
# Make a change to app.py
nano app.py

# Test locally
pytest

# Commit and push
git add app.py
git commit -m "Add new endpoint"
git push origin main

# Wait 1-2 minutes
# Check GitHub Actions: All pass? ✅
# Check live app: New feature live? 🚀
```

---

## 🐛 Troubleshooting

### GitHub Actions Fails

**Problem:** Tests fail in GitHub Actions
- **Solution:** Run `pytest` locally first to fix errors before pushing

**Problem:** Dependency installation fails
- **Solution:** Check `requirements.txt` for typos or version conflicts

### Render Deployment Issues

**Problem:** App shows "Application Error"
- **Solution:** Check Render logs in dashboard for error details

**Problem:** Endpoint returns 404
- **Solution:** Verify start command in Render: `python app.py`

---

## 📋 Submission Checklist

- ✅ GitHub Repository created and made public
- ✅ All files committed (app.py, test_app.py, requirements.txt, ci.yml)
- ✅ GitHub Actions workflow running and passing
- ✅ Tests running: `pytest` shows all tests passed
- ✅ Deployed to Render and live
- ✅ README with documentation
- ✅ All endpoints working and tested

---

## 📚 Key Technologies

| Technology | Purpose |
|-----------|---------|
| **Flask** | Python web framework |
| **pytest** | Python testing framework |
| **GitHub Actions** | CI/CD automation |
| **Render** | Cloud deployment platform |
| **Git** | Version control |

---

## 🎓 Learning Outcomes

After completing this assignment, you understand:

1. ✅ How CI/CD pipelines automate software development
2. ✅ How to write and run unit tests
3. ✅ How to use GitHub Actions for automation
4. ✅ How to deploy applications to the cloud
5. ✅ How modern DevOps practices work
6. ✅ Best practices in software development

---

## 📝 References

- [Flask Documentation](https://flask.palletsprojects.com/)
- [pytest Documentation](https://docs.pytest.org/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Render Documentation](https://render.com/docs)

---

## 👨‍🎓 Student Information

- **Assignment:** DSO101 - Assignment 4: CI/CD Pipeline
- **Program:** Bachelor's of Engineering in Software Engineering
- **University:** Royal University of Bhutan
- **Date:** May 13, 2026
- **Submission Date:** May 13, 2026

---

## 📞 Support

For issues or questions:
1. Check the troubleshooting section above
2. Review ASSIGNMENT_GUIDE.md for detailed explanations
3. Check GitHub Issues
4. Review workflow logs in GitHub Actions

---

**All requirements met. Ready for submission! 🎉**
