import json
# Librerías externas
from flask import Flask #Framework Flask
from flask import jsonify
from flask_cors import CORS # Manejar cors de conexión// Para enviar un paquete en pequeñas porciones.
from waitress import serve # Para dejar la app disponible // Ordena qué puertos va a usar Flask


app = Flask(__name__) # Creación de una app Flask
cors = CORS(app) # Cors se conecta con la app para manejar los cors de conexión.

@app.route("/", methods=['GET'])
def home():
    response = {"message": "Bienvenid@ a los servicios académicos del grupo G10"}
    return jsonify(response)


#=========== CONFIG AND EXECUTION CODE ===========
def load_file_config():
    with open("config.json", "r") as config:
        data = json.load(config)
    return data


if __name__ == '__main__':
    data_config = load_file_config()
    print("Server running: http://" + data_config.get("url-backend") + ":" + str(data_config.get("port")))
    serve(app, host=data_config.get("url-backend"), port=data_config.get("port"))