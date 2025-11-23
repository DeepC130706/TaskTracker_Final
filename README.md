# TaskTracker

**TaskTracker** — A lightweight task management web application with analytics and a simple ML-based completion-time predictor.

## Project title
TaskTracker

## Overview
TaskTracker allows users to create, manage, and analyze tasks. It demonstrates web development concepts, database design, modular coding, and a simple ML model to predict task completion time.

## Features
- User management (register/login - demo)
- Task CRUD operations
- Analytics dashboard (counts, average completion time, completion rate)
- Export reports (CSV)
- ML predictor endpoint for estimated completion time

## Technologies / Tools used
- Python 3.10+
- Flask (web framework)
- SQLite (lightweight DB)
- SQLAlchemy (ORM)
- scikit-learn (model)
- pandas (data handling)
- Jinja2 (templating)
- pytest (testing)
- reportlab, Pillow (report & diagram generation)
- Git for version control

## Installation & Run
1. Create venv and install:
```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

2. Initialize database and train model:
```bash
python init_db.py
python train_model.py
```

3. Run the app:
```bash
export FLASK_APP=app.py
flask run
```
Open http://127.0.0.1:5000

## Testing
Run:
```bash
pytest -q
```

## Repository layout
- README.md
- statement.md
- requirements.txt
- src/ (application code)
- diagrams/ (UML and ER diagrams as PNG)
- project_report.pdf
- BuildYourOwnProject.pdf (uploaded guideline copy)
