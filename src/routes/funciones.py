from flask import Blueprint, jsonify, request
from src.models.xmlReader import xmlReader

funciones_bp = Blueprint('servicios',__name__)

datos_globales = None

@funciones_bp.route('/servicios/consultarDatos', methods=['GET'])
def consultar_datos():
    global datos_globales

    if datos_globales is None:
        return {'error': 'No hay datos cargados'}, 404
    
    try:
        datos = datos_globales.obtener_datos()

        return jsonify({
            'mensaje': 'Datos completos',
            'datos': datos
        }),200
    
    except Exception as e:

        return {'error': f'Error al consultar los datos: {str(e)}'},500

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

@funciones_bp.route('/servicios/cargarDatos', methods=['POST'])
def cargar_xml():

    global datos_globales

    try:
        if 'archivo' not in request.files:
            return {'error': 'No se envio ningun archivo'}, 400
        
        archivo = request.files['archivo']

        if archivo.filename == '':
            return {'error': 'No se selecciono ningun archivo'}, 400
        
        if not archivo.filename.lower().endswith('.xml'):
            return {'error': 'el archivo debe de ser XML'}, 400
        
        lector_xml = xmlReader()

        if lector_xml.leer_xml(archivo):
            datos_globales = lector_xml
            return {
                'mensaje': 'Se cargo el XML',
                'recursos': len(lector_xml.recursos),
                'categorias': len(lector_xml.categorias),
                'clientes': len(lector_xml.clientes)
            }, 200
        
        else:
            return{'error': 'Error al procesar el archivo XML'}, 500
        
    except Exception as e:
        return {'error': f'Error interno del servidor: {str(e)}'}, 500

