import json
from flask import Flask
from flask_cors import CORS
from waitress import serve


from blueprints.candidateBlueprints import candidate_blueprints
from blueprints.politicalPartiesBlueprints import political_parties_blueprints
from blueprints.resultBlueprints import result_blueprints
from blueprints.tableBlueprints import table_blueprints

app = Flask(__name__)
cors = CORS(app)


app.register_blueprint(candidate_blueprints)
app.register_blueprint(political_parties_blueprints)
app.register_blueprint(result_blueprints)
app.register_blueprint(table_blueprints)


def load_file_config():
    with open("config.json", "r") as config:
        url_backend_connection = json.load(config)
    return url_backend_connection


@app.route("/", methods=['GET'])
def home():
    response = {
        "message": "First test"
    }
    return response


if __name__ == '__main__':
    data_config = load_file_config()
    print("Server running: http://" + data_config.get("url-backend") + ":" + str(data_config.get("port")))
    serve(app, host=data_config.get("url-backend"), port=data_config.get("port"))