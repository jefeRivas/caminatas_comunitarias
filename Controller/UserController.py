from Repository.UserRepository import UserRepository
from Entidades.UserModel import User
# Controller/UserController.py


class UserController:
    def __init__(self):
        self.repo = UserRepository()

    def crear_usuario(self, nombre, correo, contrasena, rol="voluntario"):
        usuario = User(nombre=nombre, correo=correo, contrasena=contrasena, rol=rol)
        self.repo.insertar_usuario(usuario)

    def listar_usuarios(self):
        return self.repo.obtener_usuarios()

    def editar_usuario(self, id, nombre, correo, contrasena, rol):
        usuario = User(id=id, nombre=nombre, correo=correo, contrasena=contrasena, rol=rol)
        self.repo.actualizar_usuario(usuario)

    def eliminar_usuario(self, id):
        self.repo.eliminar_usuario(id)
