class cliente:
    def __init__(self, nit, nombre, usuario, clave, direccion, correo):
        self.nit = nit
        self.nombre = nombre
        self.usuario = usuario
        self.clave = clave
        self.direccion = direccion 
        self.correo = correo
        self.lista_instancias = []

    def to_dict(self):

        return {
            'nit': self.nit,
            'nombre': self.nombre,
            'usuario': self.usuario,
            'clave': self.clave,
            'direccion': self.direccion,
            'correo': self.correo,
            'instancias': [instancia.to_dict() for instancia in self.lista_instancias]           
        }