import json
from flask import Flask, jsonify
from flask_cors import CORS
from waitress import serve


from blueprints.candidate_blueprints import candidate_blueprints
from blueprints.political_parties_blueprints import political_parties_blueprints
from blueprints.result_blueprints import result_blueprints
from blueprints.table_blueprints import table_blueprints


app = Flask(__name__)
cors = CORS(app)
app.register_blueprint(Candidate_blueprints)
app.register_blueprint(Political_party_blueprints)
app.register_blueprint(Result_blueprints)
app.register_blueprint(Table_blueprints)


def load_file_config():
    with open("config.json", "r") as config:
        url_backend_connection = json.load(config)
    return url_backend_connection


@app.route("/", methods=['GET'])
def home():
    response = {
        "message": "First test"
    }
    return jsonify(response)


if __name__ == '__main__':
    data_config = load_file_config()
    print("Server running: http://" + data_config.get("url-backend") + ":" + str(data_config.get("port")))
    serve(app, host=data_config.get("url-backend"), port=data_config.get("port"))