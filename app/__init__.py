import os
from dotenv import load_dotenv
from flask import Flask
from app.routes.tasks import tasks_bp
from app.routes.user_routes import user_bp
from flask_jwt_extended import JWTManager

load_dotenv()

def create_app():
    app = Flask(__name__)

    #Configuracion JWT
    app.config['JWT_SECRET_KEY'] =  os.getenv("JWT_SECRET_KEY")
    jwt = JWTManager(app)

    #Registrar rutas
    app.register_blueprint(tasks_bp)
    app.register_blueprint(user_bp, url_prefix='/api/users')


    return app
