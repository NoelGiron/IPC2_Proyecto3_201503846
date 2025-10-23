from flask import Flask, jsonify, request
from models import xmlReader
from src.routes.funciones import funciones_bp

app = Flask(__name__)

app.register_blueprint(funciones_bp)

@app.route('/')
def inicio():
    lector = xmlReader()
    if lector.leer_xml('configuraciones_test.xml'):
        print("¡XML leído exitosamente!")
        print(f"Recursos: {len(lector.recursos)}")
        print(f"Categorías: {len(lector.categorias)}")
        print(f"Clientes: {len(lector.clientes)}")
    return{'mensaje': 'API funcionando'}

if __name__ == '__main__':
    app.run(debug=True)