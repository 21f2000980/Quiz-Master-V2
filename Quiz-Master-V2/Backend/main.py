from flask import Flask
from config import Config
from models import db, User
from flask_jwt_extended import JWTManager
from flask_cors import CORS
# from flask_caching import Cache
from werkzeug.security import generate_password_hash
from api import api_bp



# cache = Cache()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    db.init_app(app)  # ✅ Initialize SQLAlchemy with app
    jwt = JWTManager(app)

    # ✅ Initialize Redis Cache
    # cache.init_app(app)

    app.register_blueprint(api_bp, url_prefix='/api')

    with app.app_context():
        db.create_all()  # ✅ Ensure tables are created
        

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

