from fastapi import FastAPI, HTTPException

app = FastAPI()

# Almacenamiento en memoria simulado
users= [{"id":1,"nom": "Iris Vilaseca", "email": "iris@example.com", "edat": 26},
    {"id":2,"nom": "Natalia Casanellas", "email": "natalia@example.com", "edat": 33},
    {"id":3,"nom": "Roger Sobrino", "email": "roger@example.com", "edat": 45}]

# Read - Obtenir un usuari per ID i sinó, llançar resposta
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    for user in users:
        if user["id"]==user_id:
            return user
    return {"status": 404, "message": "Usuari no trobat"}
