from flask import Blueprint, jsonify, request
from src.models.xmlReader import xmlReader
from src.models.recurso import recurso
from src.models.categoria import categoria
from src.models.cliente import cliente

funciones_bp = Blueprint('servicios',__name__)

datos_globales = None

@funciones_bp.route('/servicios/consultarDatos', methods=['GET'])
def consultar_datos():
    global datos_globales

    if datos_globales is None:
        return {'error': 'No hay datos cargados'}, 404
    
    try:

        return jsonify({
            'mensaje': 'Datos completos',
            'recursos': [r.to_dict() for r in datos_globales.recursos],
            'categorias': [c.to_dict() for c in datos_globales.categorias],
            'clientes': [cl.to_dict() for cl in datos_globales.clientes]
        }),200
    
    except Exception as e:

        return {'error': f'Error al consultar los datos: {str(e)}'},500

@funciones_bp.route('/servicios/crearRecurso', methods=['POST'])
def crear_recurso():
    global datos_globales

    if datos_globales is None:
        return {'error': 'No hay datos cargados'}, 400
    
    data = request.get_json()

    nuevo_recurso = recurso(
        id=data['id'],
        nombre=data['nombre'],
        abreviatura=data['abreviatura'], 
        metrica=data['metrica'],
        tipo=data['tipo'],
        valor_hora=data['valorXhora']
    )

    if datos_globales.agregar_recurso(nuevo_recurso):
        return {'mensaje': 'Recurso creado', 'recurso': nuevo_recurso.to_dict()}, 201
    else:
        return {'error': 'Error al crear recurso'}, 500


@funciones_bp.route('/servicios/crearCategoria', methods=['POST'])
def crear_categoria():
    global datos_globales

    if datos_globales is None:
        return {'error': 'No hay datos cargados'}, 400
    
    data = request.get_json()

    nueva_categoria = categoria(
        id=data['id'],
        nombre=data['nombre'],
        descripcion=data['descripcion'],
        carga=data['cargaTrabajo']
    )

    if datos_globales.agregar_categoria(nueva_categoria):
        return {
            'mensaje': 'Categoria creada exitosamente',
            'categoria': nueva_categoria.to_dict()
        }, 201
    
    else:
        return {'error': 'Error al crear categoria'}, 500

@funciones_bp.route('/servicios/crearConfiguracion', methods=['POST'])
def crear_configuracion():
    return {'mensaje': 'las configuraciones estan en desarrollo'}

@funciones_bp.route('/servicios/crearCliente', methods=['POST'])
def crear_cliente():
    global datos_globales

    if datos_globales is None:
        return {'error': 'No hay datos cargados'}, 400
    
    data = request.get_json()

    nuevo_cliente = cliente(
        nit=data['nit'],
        nombre=data['nombre'],
        usuario=data['usuario'],
        clave=data['clave'],
        direccion=data['direccion'],
        correo=data['correoElectronico']
    )

    if datos_globales.agregar_cliente(nuevo_cliente):
        return {
            'mensaje': 'Cliente creado exitosamente', 
            'cliente': nuevo_cliente.to_dict()
        }, 201
    
    else:
        return {'error': 'Error al crear cliente'}, 500

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
        
        datos_globales = xmlReader()

        if datos_globales.leer_xml(archivo):
            datos_globales.nombre_archivo = archivo.filename
            return{
                'mensaje': 'Se cargó el XML exitosamente',
                'recursos': len(datos_globales.recursos),
                'categorias': len(datos_globales.categorias),
                'clientes': len(datos_globales.clientes)
            }    
        
        else:
            return{'error': 'Error al procesar el archivo XML'}, 500
        
    except Exception as e:
        return {'error': f'Error interno del servidor: {str(e)}'}, 500

