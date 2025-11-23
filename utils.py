import pandas as pd
from src.models import SessionLocal, Task
def export_tasks_csv(path='tasks_export.csv'):
    db = SessionLocal()
    tasks = db.query(Task).all()
    db.close()
    rows = [{'id':t.id, 'title':t.title, 'difficulty':t.difficulty, 'priority':t.priority, 'completed':t.completed, 'actual_time':t.actual_time} for t in tasks]
    df = pd.DataFrame(rows)
    df.to_csv(path, index=False)
    return path
