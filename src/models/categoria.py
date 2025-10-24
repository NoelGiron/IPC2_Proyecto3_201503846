class categoria:
    def __init__(self, id, nombre, descripcion, carga):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.carga = carga
        self.configuraciones = []

    def to_dict(self):

        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'carga': self.carga,
            'configuracion': [config.to_dict() for config in self.configuraciones]
        }