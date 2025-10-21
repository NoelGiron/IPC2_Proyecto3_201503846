from flask import Flask, jsonify, request
from src.routes.funciones import funciones_bp

app = Flask(__name__)

app.register_blueprint(funciones_bp)

@app.route('/')
def inicio():
    return{'mensaje': 'API funcionando'}

if __name__ == '__main__':
    app.run(debug=True)