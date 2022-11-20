
from flask import Blueprint
from flask import request
from controllers.result_controller import Result_controller

result_blueprints = Blueprint('result_blueprints', __name__)
result_controller = Result_controller()


@result_blueprints.route("/result/all", methods=['GET'])
def get_all_results():
    response = result_controller.index()
    return response, 200


@result_blueprints.route("/result/<string:id_>", methods=['GET'])
def get_result_by_id(id_):
    response = result_controller.show(id_)
    return response, 200


@result_blueprints.route("/result/candidate/<string:candidate_id>", methods=['GET'])
def get_result_by_candidate(candidate_id):
    response = result_controller.get_by_candidate(candidate_id)
    return response, 200


@result_blueprints.route("/result/insert/candidate/<string:candidate_id>/table/<string:table_id>", methods=['POST'])
def insert_result(candidate_id, table_id):
    result = request.get_json()
    response = result_controller.create(result, candidate_id, table_id)
    return response, 201


@result_blueprints.route("/result/update/<string:id_>", methods=['PATCH'])
def update_result(id_):
    result = request.get_jeson()
    response = result_controller.update(id_, result)
    return response, 201


@result_blueprints.route("/result/delete/<string:id_>", methods=['DELETE'])
def delete_result(id_):
    response = result_controller.delete(id_)
    return response, 204
