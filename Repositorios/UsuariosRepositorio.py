import pyodbc
from Entidades.Usuarios import Usuarios
from Utilidades.Configuracion import Configuracion
import datetime

class UsuariosRepositorio:
    def __init__(self):
        self.conn = Configuracion.obtener_conexion()
        self.cursor = self.conn.cursor()

    def obtener_usuarios(self):
        self.cursor.execute("{CALL obtener_usuarios()}")
        results = self.cursor.fetchall()
        usuarios = []

        for row in results:
            usuario = Usuarios()
            usuario.SetId(row[0])
            usuario.SetNombre(row[1])
            usuario.SetCorreo(row[2])
            usuario.SetContrasenia(row[3])
            usuario.SetRol(row[4])
            usuario.SetFecha_registro(row[5])
            usuarios.append(usuario)

        return usuarios

    def insertar_usuario(self, usuario: Usuarios):
        self.cursor.execute("{CALL insertar_usuario (?, ?, ?, ?, ?)}", 
            usuario.GetNombre(),
            usuario.GetCorreo(),
            usuario.GetContrasenia(),
            usuario.GetRol(),
            usuario.GetFecha_registro() or datetime.datetime.now()
        )
        self.conn.commit()

    def actualizar_usuario(self, usuario: Usuarios):
        self.cursor.execute("{CALL actualizar_usuario (?, ?, ?, ?, ?)}", 
            usuario.GetId(),
            usuario.GetNombre(),
            usuario.GetCorreo(),
            usuario.GetContrasenia(),
            usuario.GetRol()
        )
        self.conn.commit()

    def eliminar_usuario(self, usuario_id: int):
        self.cursor.execute("{CALL eliminar_usuario(?)}", usuario_id)
        self.conn.commit()

    def cerrar_conexion(self):
        self.cursor.close()
        self.conn.close()
