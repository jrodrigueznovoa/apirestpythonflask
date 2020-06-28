from flask_restful import Resource, reqparse
from flask import Flask, request, jsonify
import constantes
import requests
from flask_jwt import JWT, jwt_required

class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password
    
    def getIdUsuario(self):
        return self.id 

    def setIdUsuario(self, id):
        self.idUsuario = id

    def getUsername(self):
        return self.username 

    def setUsername(self, username):
        self.username = username

    def getPassword(self):
        return self.password 

    def setPassword(self, password):
        self.password = password

class RegistrarAgente(Resource):
    
    #@app.route('/register', methods=['POST'])
    @jwt_required()
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user',
            type=str,
            required=True,
            help="Este campo no puede ir en blanco!"
        )

        parser.add_argument('password',
            type=str,
            required=True,
            help="Este campo no puede ir en blanco!"
        )

        request_data = parser.parse_args()
        #request_data = request.get_json()
        response = requests.post(f"{constantes.ENDPOINT}/agent", json=request_data)
        return response.json()
    
    #@app.route('/agent', methods=['GET'])
    @jwt_required()
    def get(self):
        response = requests.get(f"{constantes.ENDPOINT}/agent").json()
        
        if len(response) > 0:
            return jsonify(response)
        else:
            return jsonify({'mensaje': 'no encontrado'}), 404


    
    