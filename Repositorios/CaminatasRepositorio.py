import pyodbc
from Entidades.Caminatas import Caminatas
from Entidades.Usuarios import Usuarios
from Entidades.Perros import Perros
from Entidades.Horarios import Horarios
from Entidades.Rutas import Rutas
from Utilidades.Configuracion import Configuracion

class CaminatasRepositorio:
    def __init__(self):
        # Usar pyodbc con la cadena de conexión definida
        self.conn = Configuracion.obtener_conexion()
        self.cursor = self.conn.cursor()

    def obtener_caminatas(self):
        query = """
            SELECT c.id, c.fecha, c.estado, 
                   u.nombre AS usuario_nombre, 
                   p.nombre AS perro_nombre, 
                   h.dia_semana, 
                   r.nombre AS ruta_nombre
            FROM caminatas c
            JOIN registro_caminatas rc ON rc.caminata_id = c.id
            JOIN usuarios u ON u.id = rc.usuario_id
            JOIN perros p ON p.id = rc.perro_id
            JOIN horarios h ON h.id = c.horario_id
            JOIN rutas r ON r.id = c.ruta_id
        """

        self.cursor.execute(query)
        results = self.cursor.fetchall()

        caminatas = []
        for row in results:
            caminata = Caminatas()
            caminata.SetId(row[0])
            caminata.SetFecha(row[1])
            caminata.SetEstado(row[2])
            
            usuario = Usuarios()
            usuario.SetNombre(row[3])
            caminata.SetUsuario(usuario)

            perro = Perros()
            perro.SetNombre(row[4])
            caminata.SetPerro(perro)

            horario = Horarios()
            horario.SetDia_semana(row[5])
            caminata.SetHorario(horario)

            ruta = Rutas()
            ruta.SetNombre(row[6])
            caminata.SetRuta(ruta)

            caminatas.append(caminata)

        return caminatas

    def cerrar_conexion(self):
        self.cursor.close()
        self.conn.close()

# Ejemplo de uso
if __name__ == "__main__":
    repo = CaminatasRepositorio()
    caminatas = repo.obtener_caminatas()

    for caminata in caminatas:
        print(f"Caminata {caminata.GetId()} - Fecha: {caminata.GetFecha()} - Estado: {caminata.GetEstado()}")
        print(f"Usuario: {caminata.GetUsuario().GetNombre()}")
        print(f"Perro: {caminata.GetPerro().GetNombre()}")
        print(f"Horario: {caminata.GetHorario().GetDia_semana()}")
        print(f"Ruta: {caminata.GetRuta().GetNombre()}")
        print("---")

    repo.cerrar_conexion()
