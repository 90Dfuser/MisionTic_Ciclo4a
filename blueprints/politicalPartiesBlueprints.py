import json
from flask import Blueprint
from flask import request
from controllers.political_parties_controller import PoliticalPartyController

political_parties_blueprints = Blueprint('political_parties_blueprints', __name__)
political_parties_controller = PoliticalPartyController()


@political_parties_blueprints.route("/political_parties/all", methods=['GET'])
def get_all_political_parties():
    response = political_parties_controller.index()
    return response, 200


@political_parties_blueprints.route("/political_parties/<string:id_>", methods=['GET'])
def get_political_party_by_id(id_):
    response = political_parties_controller.show(id_)
    return response, 200


@political_parties_blueprints.route("/political_parties/insert", methods=['POST'])
def insert_political_party():
    political_party = request.get_json()
    response = political_parties_controller.create(political_party)
    return response, 201


@political_parties_blueprints.route("/political__parties/update/<string:id_>", methods=['PATCH'])
def update_political_party(id_):
    political_party = request.get_json()
    response = political_parties_controller.update(id_, political_party)
    return response, 201


@political_parties_blueprints.route("/political_parties/delete/<string:id_>", methods=['DELETE'])
def delete_political_party(id_):
    response = political_parties_controller.delete(id_)
    return response, 204

