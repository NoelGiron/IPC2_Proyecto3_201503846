import xml.etree.ElementTree as ET

from .categoria import categoria
from .cliente import cliente
from .configuracion import configuracion
from .instancia import instancia
from .recurso import recurso
class xmlReader:
    def __init__(self):
        self.recursos = []
        self.categorias = []
        self.clientes = []
        self.nombre_archivo = None
        self.datos_cargados = False

    def leer_xml(self, archivo):
        try:
            tree = ET.parse(archivo)
            root = tree.getroot()

            self.leer_recursos(root.find('listaRecursos'))

            self.leer_categorias(root.find('listaCategorias'))

            self.leer_clientes(root.find('listaClientes'))

            self.datos_cargados = True

            return True
        
        except Exception as e:
            print(f"Error al leer el archivo: {e}")
            return False
        
    def leer_recursos(self, lista_recursos_element):
        
        if lista_recursos_element is None:
            return 
    
        for recurso_element in lista_recursos_element.findall('recurso'):
            recurso_id = recurso_element.get('id')
            nombre = self.obtener_texto(recurso_element.find('nombre'))
            abreviatura = self.obtener_texto(recurso_element.find('abreviatura'))
            metrica = self.obtener_texto(recurso_element.find('metrica'))
            tipo = self.obtener_texto(recurso_element.find('tipo'))
            valor_hora = self.obtener_texto(recurso_element.find('valorXhora'))
            nombre = self.obtener_texto(recurso_element.find('nombre'))
            abreviatura = self.obtener_texto(recurso_element.find('abreviatura'))
            metrica = self.obtener_texto(recurso_element.find('metrica'))
            tipo = self.obtener_texto(recurso_element.find('tipo'))
            valor_hora = self.obtener_texto(recurso_element.find('valorXhora'))

            try:
                valor_hora = float(valor_hora) if valor_hora else 0.0
            except ValueError:
                valor_hora = 0.0

            nuevo_recurso = recurso(recurso_id, nombre, abreviatura, metrica, tipo, valor_hora)

            self.recursos.append(nuevo_recurso)

    def leer_categorias(self, lista_categorias_element):
        
        if lista_categorias_element is None:
            return 
        
        for categoria_element in lista_categorias_element.findall('categoria'):
            categoria_id = categoria_element.get('id')
            nombre = self.obtener_texto(categoria_element.find('nombre'))
            descripcion = self.obtener_texto(categoria_element.find('descripcion'))
            carga_trabajo = self.obtener_texto(categoria_element.find('cargaTrabajo'))
            nombre = self.obtener_texto(categoria_element.find('nombre'))
            descripcion = self.obtener_texto(categoria_element.find('descripcion'))
            carga_trabajo = self.obtener_texto(categoria_element.find('cargaTrabajo'))

            nueva_categoria = categoria(categoria_id, nombre, descripcion, carga_trabajo)

            self.categorias.append(nueva_categoria)

    def leer_configuracion(self, lista_configuraciones_element, categoria_obj):

        if lista_configuraciones_element is None:
            return
        
        for config_element in lista_configuraciones_element.findall('configuracion'):
            config_id = config_element.get('id')
            nombre = self.obtener_texto(config_element.find('nombre'))
            descripcion = self.obtener_texto(config_element.find('descripcion'))
            nombre = self.obtener_texto(config_element.find('nombre'))
            descripcion = self.obtener_texto(config_element.find('descripcion'))

            nueva_config = configuracion(config_id, nombre, descripcion)

            self.leer_recursos_configuracion(config_element.find('recursosConfiguracion'), nueva_config)
            self.leer_recursos_configuracion(config_element.find('recursosConfiguracion'), nueva_config)
            
            categoria_obj.configuraciones.append(nueva_config)

    def leer_recursos_configuracion(self, recursos_config_element, config_obj):
        if recursos_config_element is None:
            return 
        
        if recursos_config_element is None:
            return
            
        for recurso_config_element in recursos_config_element.findall('recurso'):
            recurso_id = recurso_config_element.get('id')
            cantidad_texto = self.obtener_texto(recurso_config_element)
            cantidad_texto = self.obtener_texto(recurso_config_element)
            
            try:
                cantidad = float(cantidad_texto) if cantidad_texto else 0.0
            except ValueError:
                cantidad = 0.0
            
            # Agregar el recurso a la configuración (solo el ID y la cantidad)
            config_obj.lista_recursos.append({
                'id_recurso': recurso_id,
                'cantidad': cantidad
            })

    def leer_clientes(self, lista_clientes_element):
        if lista_clientes_element is None:
            return
        
        for cliente_element in lista_clientes_element.findall('cliente'):
            nit = cliente_element.get('nit')
            nombre = self.obtener_texto(cliente_element.find('nombre'))
            usuario = self.obtener_texto(cliente_element.find('usuario'))
            clave = self.obtener_texto(cliente_element.find('clave'))
            direccion = self.obtener_texto(cliente_element.find('direccion'))
            correo = self.obtener_texto(cliente_element.find('correoElectronico'))
            nombre = self.obtener_texto(cliente_element.find('nombre'))
            usuario = self.obtener_texto(cliente_element.find('usuario'))
            clave = self.obtener_texto(cliente_element.find('clave'))
            direccion = self.obtener_texto(cliente_element.find('direccion'))
            correo = self.obtener_texto(cliente_element.find('correoElectronico'))

            nuevo_cliente = cliente(nit, nombre, usuario, clave, direccion, correo)
            
            lista_instancias_element = cliente_element.find('listaInstancias')
            self.leer_instancias(lista_instancias_element, nuevo_cliente)
            
            self.clientes.append(nuevo_cliente)
            
    def leer_instancias(self, lista_instancias_element, cliente_obj):
        if lista_instancias_element is None:
            return
        
        for instancia_element in lista_instancias_element.findall('instancia'):
            instancia_id = instancia_element.get('id')
            id_configuracion = self.obtener_texto(instancia_element.find('idConfiguracion'))
            nombre_instancia = self.obtener_texto(instancia_element.find('nombre'))
            fecha_inicio = self.obtener_texto(instancia_element.find('fechaInicio'))
            estado = self.obtener_texto(instancia_element.find('estado'))
            fecha_final = self.obtener_texto(instancia_element.find('fechaFinal'))
            id_configuracion = self.obtener_texto(instancia_element.find('idConfiguracion'))
            nombre_instancia = self.obtener_texto(instancia_element.find('nombre'))
            fecha_inicio = self.obtener_texto(instancia_element.find('fechaInicio'))
            estado = self.obtener_texto(instancia_element.find('estado'))
            fecha_final = self.obtener_texto(instancia_element.find('fechaFinal'))

            nueva_instancia = instancia(instancia_id, id_configuracion, nombre_instancia, fecha_inicio, estado, fecha_final)

            cliente_obj.lista_instancias.append(nueva_instancia)

    def agregar_recurso(self, nuevo_recurso):
        self.recursos.append(nuevo_recurso)
        
    def obtener_texto(self, element):
        if element is not None and element.text is not None:
            return element.text.strip()
        return ""
    
    def obtener_datos(self):
        if not self.datos_cargados:
            return None
        
        return {
            'recursos': [recurso.to_dict() for recurso in self.recursos],
            'categoria': [categoria.to_dict() for categoria in self.categorias],
            'clientes': [cliente.to_dict() for cliente in self.clientes]
        }
    
    