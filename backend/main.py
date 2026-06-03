from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2

app = FastAPI()

# connect PostgreSQL
conn = psycopg2.connect(
    dbname="todo_db",
    user="heeya",
    password="heeya",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()
class Task(BaseModel):
    name: str
    checked: bool = False

#get all tasks
@app.get("/tasks")
def get_tasks():
    cursor.execute("SELECT * FROM task")
    rows = cursor.fetchall()
    return rows

# get task by id
@app.get("/task/{task_id}")
def get_task(task_id: int):
    cursor.execute("SELECT * FROM task WHERE id=%s", (task_id,))
    return cursor.fetchone()

# add new tasks
@app.post("/task")
def add_task(task: Task):
    cursor.execute(
        "INSERT INTO task (name, checked) VALUES (%s, %s)",
        (task.name, task.checked)
    )
    conn.commit()
    return {"message": "Task added"}

#update task
@app.put("/task/{task_id}")
def update_task(task_id: int, task: Task):
    cursor.execute(
        "UPDATE task SET name=%s, checked=%s WHERE id=%s",
        (task.name, task.checked, task_id)
    )
    conn.commit()
    return {"message": "Updated"}

#delete task
@app.delete("/task/{task_id}")
def delete_task(task_id: int):
    cursor.execute("DELETE FROM task WHERE id=%s", (task_id,))
    conn.commit()
    return {"message": "Deleted"}