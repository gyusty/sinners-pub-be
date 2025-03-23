# 🐍 Sinners Pub - Backend

This is the backend for the **Sinners Pub** project, built with Python.  
Follow the steps below to run it locally on your machine.

---

## 🚀 Requirements

- [Python 3.9+](https://www.python.org/)
- [Git](https://git-scm.com/)
- pip (comes bundled with Python)
- Recommended: virtual environment using `venv`

---

## 🛠 Installation & Setup

### 1. Clone the repository

--- 
git clone https://github.com/gyusty/sinners-pub-fe.git
cd sinners-pub-fe

### 2. Create and activate virtual environment

python -m venv .venv

on Linux/macOS
    source .venv/bin/activate

on Windows CMD:
    .venv\Scripts\activate.bat

on Windows Powershell:
    .venv\Scripts\Activate.ps1


### 3. Install dependencies
    pip install -r requirements.txt


### 4. Start the aplication
    uvicorn main:app --reload
