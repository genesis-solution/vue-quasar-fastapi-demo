from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import pymysql

connection = pymysql.connect(
  host="127.0.0.1",
  user="root",
  password="",
  database="quasar_db"
)
# Create a cursor object

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:8080",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class SignIN(BaseModel):
    email: str
    password: str


class SignUP(BaseModel):
    first_name: str
    last_name: str
    email: str
    password: str

class ChangePassword(BaseModel):
    user_id: str
    password: str
    new_password: str


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/signin/")
async def post_signin(item: SignIN):
    cursor = connection.cursor()
    sql = "SELECT * FROM users WHERE email = '"+item.email+"' AND password = '" + item.password + "'";
    cursor.execute(sql)
    result = cursor.fetchall()

    if len(result) > 0:
        return {"status": 200, "data": result[0]}
    else:
        return {"status": 401}


@app.post("/signup/")
async def post_signup(item: SignUP):
    cursor = connection.cursor()
    sql = "INSERT INTO users (first_name, last_name, email, password) VALUES (%s, %s, %s, %s)"
    val = (item.first_name, item.last_name, item.email, item.password)
    cursor.execute(sql, val)
    connection.commit()
    return { "status": 200, "data": item }


@app.post("/changepassword/")
async def post_changepassword(item: ChangePassword):
    cursor = connection.cursor()
    sql = "SELECT * FROM users WHERE id = '"+item.user_id+"' AND password = '" + item.password + "'";
    cursor.execute(sql)
    result = cursor.fetchall()

    if len(result) > 0:
        sql = "UPDATE users SET password = %s WHERE id = %s"
        values = (item.new_password, item.user_id)
        cursor.execute(sql, values)
        connection.commit()
        return {"status": 200, "data": "changed"}
    else:
        return {"status": 401}