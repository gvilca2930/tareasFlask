from flask import Flask
from app.routes.tasks import tasks_bp
from app.routes.user_routes import user_bp
from app.db import init_db
from flask_jwt_extended import JWTManager


def create_app():
    app = Flask(__name__)

    #Configuracion JWT
    app.config['JWT_SECRET_KEY'] = 'supersecretkey'
    jwt = JWTManager(app)

    #Registrar rutas
    app.register_blueprint(tasks_bp)
    app.register_blueprint(user_bp, url_prefix='/api/users')

    #Inicializar base de datos
    init_db()

    return app
