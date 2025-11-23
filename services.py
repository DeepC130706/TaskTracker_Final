from src import models
from src.models import SessionLocal, User, Task
from sqlalchemy import func
from sqlalchemy.orm import Session
def create_user(username):
    db = SessionLocal()
    user = db.query(User).filter(User.username==username).first()
    if not user:
        user = User(username=username)
        db.add(user)
        db.commit()
    db.close()

def create_task(title, difficulty, priority):
    db = SessionLocal()
    t = Task(title=title, difficulty=difficulty, priority=priority, completed=False)
    db.add(t)
    db.commit()
    db.close()

def list_tasks():
    db = SessionLocal()
    tasks = db.query(Task).order_by(Task.id.desc()).all()
    db.close()
    return tasks

def complete_task(task_id, actual_time):
    db = SessionLocal()
    t = db.query(Task).filter(Task.id==task_id).first()
    if t:
        t.completed = True
        t.actual_time = actual_time
        db.commit()
    db.close()

def get_stats():
    db = SessionLocal()
    total = db.query(Task).count()
    completed = db.query(Task).filter(Task.completed==True).count()
    avg_time = db.query(Task).filter(Task.actual_time!=None).with_entities(func.avg(Task.actual_time)).scalar()
    db.close()
    return {"total": total, "completed": completed, "avg_time": avg_time}
