class Caminata:
    def __init__(self):
        self._id: Optional[int] = None
        self._fecha: Optional[datetime] = None
        self._ubicacion: Optional[str] = None
        self._descripcion: Optional[str] = None

    def get_id(self): return self._id
    def set_id(self, value): self._id = value

    def get_fecha(self): return self._fecha
    def set_fecha(self, value): self._fecha = value

    def get_ubicacion(self): return self._ubicacion
    def set_ubicacion(self, value): self._ubicacion = value

    def get_descripcion(self): return self._descripcion
    def set_descripcion(self, value): self._descripcion = value