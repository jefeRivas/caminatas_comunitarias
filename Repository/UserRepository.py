from Utilidades.Configuracion import get_connection
from Entidades.UserModel import User

from Utilidades.Configuracion import get_connection
from Entidades.UserModel import User

class UserRepository:
    def __init__(self):
        try:
            self.conn = get_connection()
            if self.conn is None:
                raise Exception("No se pudo establecer conexión a la base de datos")
        except Exception as e:
            print(f"Error al inicializar UserRepository: {e}")
            raise  # Relanza la excepción para que el llamador sepa que hubo un error

    def insertar_usuario(self, usuario: User):
        try:
            if self.conn is None:
                self.conn = get_connection()  # Intentar reconectar
                
            cursor = self.conn.cursor()
            cursor.execute(
                "INSERT INTO usuarios (nombre, correo, contrasena, rol) VALUES (?, ?, ?, ?)",
                (usuario.nombre, usuario.correo, usuario.contrasena, usuario.rol)
            )
            self.conn.commit()
            return cursor.lastrowid
        except Exception as e:
            print(f"Error al insertar usuario: {e}")
            if self.conn:
                self.conn.rollback()
            return None
        finally:
            if cursor:
                cursor.close()

    def obtener_usuarios(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM usuarios")
        rows = cursor.fetchall()
        usuarios = []
        for row in rows:
            usuario = User(row.id, row.nombre, row.correo, row.contrasena, row.rol, row.fecha_registro)
            usuarios.append(usuario)
        cursor.close()
        return usuarios

    def actualizar_usuario(self, usuario: User):
        cursor = self.conn.cursor()
        query = """
            UPDATE usuarios
            SET nombre=?, correo=?, contrasena=?, rol=?
            WHERE id=?
        """
        cursor.execute(query, (
            usuario.get_nombre(),
            usuario.get_correo(),
            usuario.get_contrasena(),
            usuario.get_rol(),
            usuario.get_id()
        ))
        self.conn.commit()
        cursor.close()

    def eliminar_usuario(self, usuario_id: int):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM usuarios WHERE id=?", (usuario_id,))
        self.conn.commit()
        cursor.close()
