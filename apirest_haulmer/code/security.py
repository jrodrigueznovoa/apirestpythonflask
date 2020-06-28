from werkzeug.security import safe_str_cmp
from user import User
import requests
import constantes

"""
usersPrueba = [
    User(1, 'user1', '123456'),
    User(2, 'user2', '123456')
]

"""

def getUsuario():
    response = requests.get(f"{constantes.ENDPOINT}/agent")
    json_resp = response.json()
    return json_resp

users = getUsuario()
item1 = []

for item in users:
    idUsuario = item['id']
    usuario = item['user']
    password = item['password']
    item1.append(User(idUsuario, usuario, password))
    
username_mapping = {u.username: u for u in item1}
id_mapping = {u.id: u for u in item1}


def authenticate(username, password):
    user = username_mapping.get(username, None)
    if user and safe_str_cmp(user.password, password):
        return user

def identity(payload):
    user_id = payload['identity']
    return id_mapping.get(user_id, None)

