from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2

app = FastAPI()

# connect PostgreSQL
conn = psycopg2.connect(
    dbname="todo_list",
    user="heeya",
    password="heeya",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()