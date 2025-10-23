class configuracion:
    def __init__(self, id, nombre, descripcion):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.lista_recursos = []

    def to_dict(self):

        return {
            'id': self.id,
            'nombre': self.nombre,
            'descripcion': self.descripcion,
            'recursos': self.lista_recursos
        }