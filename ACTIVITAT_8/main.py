from fastapi import FastAPI, HTTPException

app = FastAPI()

# Almacenamiento en memoria simulado
users= [{"id":1,"nom": "Iris Vilaseca", "email": "iris@example.com", "edat": 26},
    {"id":2,"nom": "Natalia Casanellas", "email": "natalia@example.com", "edat": 33},
    {"id":3,"nom": "Roger Sobrino", "email": "roger@example.com", "edat": 45}]


@app.post("/users")
async def create_user(nom: str, email: str, edat: int):
    # Verificar si el email ya existe
    for user in users:
        if user["email"]==email:
            print("No s'ha pogut crear l'usuari nou perquè el correu ja està registrat")
            return

    # Crear un nuevo usuario
    nou_id = len(users) + 1
    new_user = {"id": nou_id, "nom": nom, "email": email, "edat": edat}
    users.append(new_user)
    return new_user

# Read All - Obtener todos los usuarios
@app.get("/users")
async def get_users():
    return users

# Read - Obtener un usuario por ID
@app.get("/users/{user_id}")
async def get_user(user_id: int):
    for user in users:
        if user["id"]==user_id:
            return user
    print("No existeix aquest usuari")
    return

# Update - Actualizar un usuario existente
@app.put("/users/{user_id}")
async def update_user(user_id: int, nom: str, email: str = None, edat: int = None):
    user = users.get(user_id)
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

# Delete - Eliminar un usuario por ID
def delete_user(users, user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)  # Eliminem l'usuari
            return f"Usuario eliminado: {user}"

    # Si no trobem l'usuari, no esborrem res
    return f"Error: No se encontró un usuario con ID {user_id}."