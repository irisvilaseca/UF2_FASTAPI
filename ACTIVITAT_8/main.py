from fastapi import FastAPI, HTTPException
import json
app = FastAPI()

# Emmagatzament en memòria
users= [{"id":1,"nom": "Iris Vilaseca", "email": "iris@example.com", "edat": 26},
    {"id":2,"nom": "Natalia Casanellas", "email": "natalia@example.com", "edat": 33},
    {"id":3,"nom": "Roger Sobrino", "email": "roger@example.com", "edat": 45}]


@app.post("/users")
async def create_user(nom: str, email: str, edat: int):
    # Verificar si l'email ja existeix
    for user in users:
        if user["email"]==email:
            print("No s'ha pogut crear l'usuari nou perquè el correu ja està registrat")
            return

    # Crear un nou usuari
    nou_id = len(users) + 1
    new_user = {"id": nou_id, "nom": nom, "email": email, "edat": edat}
    users.append(new_user)
    return new_user

# Read All - Obtenir tots els usuarios
@app.get("/users")
async def get_users():
    json_object=json.dumps(users,indent=4)
    return json_object

# Read - Obtenir un usuari per ID
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    for user in users:
        if user["id"]==user_id:
            return user
    print("No existeix aquest usuari")
    return

# Update - Actualitzar un usuari existent
@app.put("/users/{user_id}")
async def update_user(user_id: int, nom: str, email: str = None, edat: int = None):
    user = get_user(user_id)
    if not user:
        print("No s'ha trobat cap usuari amb aquest id")

    # Actualizar nom si es proporciona
    if nom:
        user['nom'] = nom

    # Validar i actualitzar email si es proporciona
    if email:
        for user in users.values():
            if user['email'] == email and user['id'] != user_id:
                print("El correu proporcionat ja existeix")
        user['email'] = email

    # Validar i actualitzar edat si es proporciona
    if edat:
        if edat <= 0:
            print("L'edat introduïda no pot ser menor a zero")
        else:
            user["edat"]=edat
    return user

# Delete - Eliminar un usuari per ID
@app.delete("/users/{user_id}")
async def delete_user(user_id: int):
    # Filtrar fora la id que hem decidit
    updated_users = [user for user in users if user["id"] != user_id]

    # Si la llista no s'ha actualitzat, vol dir que l'usuari no s'ha trobat
    if len(updated_users) == len(users):
        print("No s'ha trobat l'usuari")

    # Actualitzem la llista original
    users[:] = updated_users

    return {"message": f"L'usuari amb ID {user_id} ha estat esborrat."}