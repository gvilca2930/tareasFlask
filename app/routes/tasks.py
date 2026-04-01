from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required

from app.services.tasks import (
    get_all_tasks,
    create_task,
    update_task,
    delete_task
)

tasks_bp = Blueprint("tasks", __name__)

@tasks_bp.route("/tasks", methods=["GET"])
@jwt_required()
def get_tasks():
    tasks = get_all_tasks()
    return jsonify(tasks)

@tasks_bp.route("/tasks", methods=["POST"])
@jwt_required()
def create():
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify ({"error": "Falta el campo 'title'"}), 400

    task = create_task(data["title"])
    return jsonify(task), 201

@tasks_bp.route("/tasks/<int:id>", methods=["PUT"])
@jwt_required()
def update(id):
    data = request.get_json()

    task = update_task(id, data)

    if not task:
        return jsonify({"error": "Tarea no encontrada"}), 404

    return jsonify(task)

@tasks_bp.route("/tasks/<int:id>", methods=["DELETE"])
@jwt_required()
def delete(id):
    success = delete_task(id)

    if not success:
        return jsonify({"error" : "Tarea no encontrada"}), 404

    return jsonify({"message": "Tarea eliminada"})








