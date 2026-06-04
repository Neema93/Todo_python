from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import psycopg2

app = FastAPI()
#create middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
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
    cursor.execute("SELECT id, name, checked FROM task")
    rows = cursor.fetchall()

    return [
        {
            "id": row[0],
            "name": row[1],
            "checked": row[2]
        }
        for row in rows
    ]
# get task by id
@app.get("/task/{task_id}")
def get_task(task_id: int):
    cursor.execute("SELECT * FROM task WHERE id=%s", (task_id,))
    task = cursor.fetchone()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    return {
        "id": task[0],
        "name": task[1],
        "checked": task[2]
    }

# add new tasks
@app.post("/task")
def add_task(task: Task):
    cursor.execute(
        "INSERT INTO task (name, checked) VALUES (%s, %s)",
        (task.name, task.checked)
    )
    conn.commit()
    return {
    "name": task.name,
    "checked": task.checked
}
#check 
def task_exists(task_id: int):
    cursor.execute("SELECT id FROM task WHERE id=%s", (task_id,))
    return cursor.fetchone() is not None
#update task
@app.put("/task/{task_id}")
def update_task(task_id: int, task: Task):
    if not task_exists(task_id):
        raise HTTPException(status_code=404, detail="Task not found")

    cursor.execute(
        "UPDATE task SET name=%s, checked=%s WHERE id=%s",
        (task.name, task.checked, task_id)
    )
    conn.commit()

    return {
        "id": task_id,
        "name": task.name,
        "checked": task.checked
    }

#delete task
@app.delete("/task/{task_id}")
def delete_task(task_id: int):
   

    if not task_exists(task_id):
        raise HTTPException(status_code=404, detail="Task not found")

    cursor.execute("DELETE FROM task WHERE id=%s", (task_id,))
    conn.commit()

    return {"message": "Task deleted successfully"}