import os
from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

db = SQLAlchemy(app)
jwt = JWTManager(app)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to PlanVenture API"})

@app.route('/health')
def health_check():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(debug=True)
