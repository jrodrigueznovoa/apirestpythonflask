import requests
from flask_jwt import JWT, jwt_required, current_identity
from flask import Flask, request, jsonify
import constantes
from security import authenticate, identity
from flask_restful import Resource, reqparse

class Incidencias(Resource):
    
    """
    Metodo GET para obtener las incidencias no requiere token
    http://<host>:<puerto/issues
    """

    #@app.route('/issues', methods=['GET'])
    def get(self):
        response = requests.get(f"{constantes.ENDPOINT}/issues").json()
        if len(response) > 0:
            return jsonify(response)
        else:
            return jsonify({'mensaje': 'no encontrado'}), 404

class IncidenciasA(Resource):
    
    """
    metodo GET para obener un filtro de un agente, requiere token
    http://<host>:<puerto/issues/srv1.agente2.com

    """
    #@app.route('/issues/<string:id>', methods=['GET'])
    @jwt_required()
    def get(self, id):
        response = requests.get(f"{constantes.ENDPOINT}/issues?filter={id}").json()
        if len(response) > 0:
            return jsonify(response)
        else:
            return jsonify({'mensaje': 'no encontrado'}), 404

class IncidenciasB(Resource):

    """
    metodo GET para obener un filtro con una fecha, requiere token
    se debe pasar por parametro dia, mes, año
    http://<host>:<puerto/issues/20/09/2020

    """

    #@app.route('/issues/<string:dia>/<string:mes>/<string:anio>', methods=['GET'])
    @jwt_required()
    def get(self, dia, mes, anio):
        fecha = f"{dia}/{mes}/{anio}"
        response = requests.get(f"{constantes.ENDPOINT}/issues?filter={fecha}").json()
        if len(response) > 0:
            return jsonify(response)
        else:
            return jsonify({'mensaje': 'no encontrado'}), 404


class Incidencia(Resource):

    """
    metodo GET para obener una incidencia filtrado con su codigo id, requiere token 
    http://<host>:<puerto>/issue/1  
    """
    #@app.route('/issue/<string:id>', methods=['GET'])
    def get(self, id):
        response = requests.get(f"{constantes.ENDPOINT}/issues").json()
        for item in response:
            if item['id'] == id:
                return jsonify(item)
        return jsonify({'mensaje': 'no encontrado'}), 404

class CrearIncidencia(Resource):
    
    """
    metodo POST para crear una incidencia  
    http://<host>:<puerto>/issue
    
    """

    #@app.route('/issue', methods=['POST'])
    @jwt_required()
    def post(self):
        #validaciones
        parser = reqparse.RequestParser()
        parser.add_argument('fecha',
            type=str,
            required=True,
            help="Este campo no puede ir en blanco!"
        )

        parser.add_argument('titulo',
            type=str,
            required=True,
            help="Este campo no puede ir en blanco!"
        )

        parser.add_argument('descripcion',
            type=str,
            required=True,
            help="Este campo no puede ir en blanco!"
        )

        parser.add_argument('agente',
            type=str,
            required=True,
            help="Este campo no puede ir en blanco!"
        )

        request_data = parser.parse_args()

        #request_data = request.get_json()
        response = requests.post(f"{constantes.ENDPOINT}/issues", json=request_data)

        return response.json()

