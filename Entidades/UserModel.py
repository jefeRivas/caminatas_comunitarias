import datetime

class User:
    def __init__(self, id=0, nombre="", correo="", contrasena="", rol="voluntario", fecha_registro=None):
        self._id = id
        self._nombre = nombre
        self._correo = correo
        self._contrasena = contrasena
        self._rol = rol
        self._fecha_registro = fecha_registro or datetime.datetime.now()

    def get_id(self): return self._id
    def set_id(self, id): self._id = id

    def get_nombre(self): return self._nombre
    def set_nombre(self, nombre): self._nombre = nombre

    def get_correo(self): return self._correo
    def set_correo(self, correo): self._correo = correo

    def get_contrasena(self): return self._contrasena
    def set_contrasena(self, contrasena): self._contrasena = contrasena

    def get_rol(self): return self._rol
    def set_rol(self, rol): self._rol = rol

    def get_fecha_registro(self): return self._fecha_registro
    def set_fecha_registro(self, fecha_registro): self._fecha_registro = fecha_registro
