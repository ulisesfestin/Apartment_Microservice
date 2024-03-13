from flask import Flask
# from flask_migrate import Migrate
# from flask_cors import CORS
# from app.config.database import db, FULL_URL_DB
# from flask_marshmallow import Marshmallow


# ma = Marshmallow()

def create_app():
    app = Flask(__name__)
    # CORS(app)
    # ma.init_app(app)

    # app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB

    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # db.init_app(app)

    # migrate = Migrate()
    # migrate.init_app(app, db)

    # from app.resources import home, user, role, apartment, booking, auth
    # app.register_blueprint(home, url_prefix='/api/v1/home')
    # app.register_blueprint(user, url_prefix='/api/v1/user')
    # app.register_blueprint(apartment, url_prefix='/api/v1/apartment')
    # app.register_blueprint(role, url_prefix='/api/v1/role')
    # app.register_blueprint(booking, url_prefix='/api/v1/booking')
    # app.register_blueprint(auth, url_prefix='/api/v1/auth')
    return app