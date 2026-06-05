# Todo App

A full-stack Todo application built with FastAPI, PostgreSQL, and React.

## Features

* Create tasks
* View all tasks
* View a task by ID
* Update tasks
* Delete tasks
* PostgreSQL database
* React frontend
* FastAPI backend

---

## Project Structure

```text
todo-project/
│
├── backend/
│   ├── main.py
│   ├── requirements.txt
│   └── venv/
│
└── frontend/
    ├── src/
    ├── public/
    └── package.json
```

---

## Backend Setup

### Create Virtual Environment

```bash
python3 -m venv venv
```

### Activate Virtual Environment

macOS/Linux:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run FastAPI Server

```bash
uvicorn main:app --reload
```

Backend URL:

```text
http://localhost:8000
```

Swagger Documentation:

```text
http://localhost:8000/docs
```

---

## PostgreSQL Setup

Create database:

```sql
CREATE DATABASE todo_db;
```

Create table:

```sql
CREATE TABLE task (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    checked BOOLEAN DEFAULT FALSE
);
```

Update PostgreSQL credentials in `main.py`:

```python
conn = psycopg2.connect(
    dbname="todo_db",
    user="your_username",
    password="your_password",
    host="localhost",
    port="5432"
)
```

---

## Frontend Setup

Navigate to frontend folder:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start React application:

```bash
npm start
```

Frontend URL:

```text
http://localhost:3000
```

---

## API Endpoints

### Get All Tasks

```http
GET /tasks
```

### Get Task By ID

```http
GET /task/{task_id}
```

### Create Task

```http
POST /task
```

Request Body:

```json
{
  "name": "Learn FastAPI",
  "checked": false
}
```

### Update Task

```http
PUT /task/{task_id}
```

Request Body:

```json
{
  "name": "Updated Task",
  "checked": true
}
```

### Delete Task

```http
DELETE /task/{task_id}
```

---

## Generate requirements.txt

```bash
pip freeze > requirements.txt
```

---

## Technologies Used

* FastAPI
* PostgreSQL
* psycopg2
* Pydantic
* React
* Axios
* SCSS
* Node.js
* npm

```
```
