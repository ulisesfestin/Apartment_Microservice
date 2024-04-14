from flask import Flask
import os
from app.config import config
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    config_name = os.getenv('FLASK_ENV')
      
    f = config.factory(config_name if config_name else 'development')
    app.config.from_object(f)

    f.init_app(app)
    db.init_app(app)

    from app.controllers import apartment
    app.register_blueprint(apartment, url_prefix='/api/v1/apartment')

    @app.shell_context_processor
    def ctx():
        return {"app": app, "db": db}
    
    return app