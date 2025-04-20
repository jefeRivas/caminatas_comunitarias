from typing import List
from Entidades.Usuarios import Usuarios
from Entidades.Perros import Perros
from Entidades.Horarios import Horarios
from Entidades.Rutas import Rutas

class Caminatas:
    id: int = 0
    fecha: str = None
    estado: str = None
    usuario: str = None
    usuarios: List[Usuarios] = []  # Lista de usuarios (voluntarios) en la caminata
    perro: Perros = None
    horario: Horarios = None
    ruta: Rutas = None

    def GetId(self) -> int:
        return self.id

    def SetId(self, value: int) -> None:
        self.id = value

    def GetFecha(self) -> str:
        return self.fecha

    def SetFecha(self, value: str) -> None:
        self.fecha = value

    def GetEstado(self) -> str:
        return self.estado

    def SetEstado(self, value: str) -> None:
        self.estado = value

    #def GetUsuarios(self) -> List[Usuarios]:
    #    return self.usuarios

    def GetUsuario(self) -> Usuarios:
        return self.usuario

    def SetUsuario(self, usuario: Usuarios) -> None:
        self.usuario = usuario

    def GetPerro(self) -> Perros:
        return self.perro

    def SetPerro(self, value: Perros) -> None:
        self.perro = value

    def GetHorario(self) -> Horarios:
        return self.horario

    def SetHorario(self, value: Horarios) -> None:
        self.horario = value

    def GetRuta(self) -> Rutas:
        return self.ruta

    def SetRuta(self, value: Rutas) -> None:
        self.ruta = value
