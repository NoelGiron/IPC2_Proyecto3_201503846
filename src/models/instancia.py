class instancia:
    def __init__(self, id, id_config, nombre, fecha_inicio, estado, fecha_fin):
        self.id = id
        self.id_config = id_config
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.estado = estado
        self.fecha_fin = fecha_fin

    def to_dict(self):

        return {
            'id': self.id,
            'id Configuracion': self.id_config,
            'nombre': self.nombre,
            'Fecha de inicio': self.fecha_inicio,
            'estado': self.estado,
            'Fecha de fin': self.fecha_fin           
        }