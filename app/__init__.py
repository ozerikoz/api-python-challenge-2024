from flask import Flask
from app.config.config import Config
from app.db.db import init_db
from app.routes.usuarios_routes import usuarios_bp
from app.routes.veiculos_routes import veiculos_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    init_db(app)

    app.register_blueprint(usuarios_bp, url_prefix='/usuarios')
    app.register_blueprint(veiculos_bp, url_prefix='/veiculos')

    return app
