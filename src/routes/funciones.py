from flask import Blueprint

funciones_bp = Blueprint('servicios',__name__)

@funciones_bp.route('/servicios/consultarDatos', methods=['GET'])
def consultar_datos():
    return {'mensaje': 'los datos estan en desarrollo'}

@funciones_bp.route('/servicios/crearRecurso', methods=['POST'])
def crear_recurso():
    return {'mensaje': 'crear esta en desarrollo'}

@funciones_bp.route('/servicios/crearCategoria', methods=['POST'])
def crear_categoria():
    return {'mensaje': 'las categorias estan en desarrollo'}

@funciones_bp.route('/servicios/crearConfiguracion', methods=['POST'])
def crear_configuracion():
    return {'mensaje': 'las configuraciones estan en desarrollo'}

@funciones_bp.route('/servicios/crearCliente', methods=['POST'])
def crear_cliente():
    return {'mensaje': 'los clientes estan en desarrollo'}

@funciones_bp.route('/servicios/crearInstancia', methods=['POST'])
def crear_instancia():
    return {'mensaje': 'las instancias estan en desarrollo'}

@funciones_bp.route('/servicios/generarFactura', methods=['POST'])
def crear_factura():
    return {'mensaje': 'las facturas estan en desarrollo'}

