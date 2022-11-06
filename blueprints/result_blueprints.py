import json
from flask import Blueprint
from flask import request
from controllers.result_controller import ResultController

result_blueprints = Blueprint('result_blueprint', __name__)
result_controller = ResultController()


@result_blueprints.route("/result/all", methods=['GET'])
def get_all_results():
    response = result_controller.index()
    return response, 200


@result_blueprints.route("/result/<string: id_>", methods=['GET'])
def get_result_by_id(id_):
    response = result_controller.show(id_)
    return response, 200


@result_blueprints.route("/result/insert", methods=['POST'])
def insert_result():
    result = request.get_json()
    response = result_controller.create(result)
    return response, 201


@result_blueprints.route("/result/update/<string: id_>", methods=['PATCH'])
def update_result(id_):
    result = request.get_jeson()
    response = result_controller.update(id_, result)
    return response, 201


@result_blueprints.route("/result/delete/<string: id_>")
def delete_result(id_):
    response = result_controller.delete(id_)
    return response, 204
