from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from app.services.user_services import create_user, check_user, update_password

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if create_user(username, password):
        return jsonify({"message": "Usuario creado"}), 201
    return jsonify({"message": "Usuario ya existe"}), 400

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user_id = check_user(username, password)
    if not user_id:
        return jsonify({"message": "Usuario o password incorrectos"}), 401
    access_token = create_access_token(identity=str(user_id))
    return jsonify(access_token=access_token)

@user_bp.route('/update', methods=['POST'])
def update():
    data = request.get_json()

    success = update_password(
        data['username'],
        data['current_password'],
        data['new_password']
    )

    if success:
        return jsonify({"message" : "Password actualizado"})
    return jsonify({"message" : "Credenciales Incorrectas"}), 400
