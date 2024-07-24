from typing import Optional, List
from pydantic import BaseModel
from fastapi import FastAPI, Path, Query

app = FastAPI()

users = []

class User(BaseModel):
    name: str
    password: str
    age: Optional[int]

@app.get("/get",response_model=dict)
def get_users():
    return {"data":users,"status":"Success","length":len(users)}

@app.post("/create")
async def create_users(user:User):
    users.append(user)
    return "Success"

@app.get("/user/{id}")
async def get_users_byId(
    id:int = Path(...,description="give id",gt=2),
    q:str = Query(None,max_length=5)
    ):
    return {"data":users[id],"query":q}