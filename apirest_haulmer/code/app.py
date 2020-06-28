import requests
import constantes
from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity

from security import authenticate, identity
from incidencias import Incidencia, Incidencias, IncidenciasA, IncidenciasB, CrearIncidencia
from user import RegistrarAgente

app = Flask(__name__)

app.secret_key = 'super-secret'
api = Api(app)

jwt = JWT(app, authenticate, identity) #/auth


api.add_resource(Incidencias, '/issues')
api.add_resource(IncidenciasA, '/issues/<string:id>')
api.add_resource(IncidenciasB, '/issues/<string:dia>/<string:mes>/<string:anio>')
api.add_resource(CrearIncidencia, '/issue')
api.add_resource(Incidencia, '/issue/<string:id>')
api.add_resource(RegistrarAgente, '/agente')

if __name__ == '__main__':
    app.run(port=constantes.puerto, debug=True)