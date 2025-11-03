import os
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
jwt = JWTManager()
bcrypt = Bcrypt()

def create_app():
    app = Flask(__name__)
    allowed_origins = os.environ.get('CORS_ALLOWED_ORIGINS', '*').split(',')
    CORS(app, resources={r"/*": {"origins": allowed_origins}})

    app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)

    from auth.routes import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')

    from trips.routes import trips_bp
    app.register_blueprint(trips_bp, url_prefix='/trips')

    @app.route('/')
    def home():
        return jsonify({"message": "Welcome to PlanVenture API"})

    @app.route('/health')
    def health_check():
        try:
            # Attempt to connect to the database
            db.session.execute(db.text('SELECT 1'))
            return jsonify({"status": "operational"})
        except Exception as e:
            return jsonify({"status": "degraded", "details": str(e)}), 503

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)