from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
class User(BaseModel):
    id:int
    nom:str
    cognom:str
    email:str
    telefon:int
    edat:int | None = None

app = FastAPI()

@app.post("/users/")
async def create_user(user: User):
    return user

