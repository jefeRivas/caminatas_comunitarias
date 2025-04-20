# model/UsuariosModel.py
from datetime import datetime

class UserModel:
    def __init__(self, id=0, nombre=None, correo=None, contrasena=None, rol="voluntario", fecha_registro=None):
        self._id = id
        self._nombre = nombre
        self._correo = correo
        self._contrasena = contrasena
        self._rol = rol
        self._fecha_registro = fecha_registro if fecha_registro else datetime.now()

    def get_id(self): return self._id
    def set_id(self, value): self._id = value

    def get_nombre(self): return self._nombre
    def set_nombre(self, value): self._nombre = value

    def get_correo(self): return self._correo
    def set_correo(self, value): self._correo = value

    def get_contrasena(self): return self._contrasena
    def set_contrasena(self, value): self._contrasena = value

    def get_rol(self): return self._rol
    def set_rol(self, value): self._rol = value

    def get_fecha_registro(self): return self._fecha_registro
    def set_fecha_registro(self, value): self._fecha_registro = value

    def to_tuple_insert(self):
        return (self._nombre, self._correo, self._contrasena, self._rol, self._fecha_registro)

    def to_tuple_update(self):
        return (self._nombre, self._correo, self._contrasena, self._rol, self._fecha_registro, self._id)
