import datetime

class Usuarios:
    id: int = 0

    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value

    nombre: str = None

    def GetNombre(self) -> str:
        return self.nombre
    def SetNombre(self, value: str) -> None:
        self.nombre = value

    correo: str = None

    def GetCorreo(self) -> str:
        return self.correo
    def SetCorreo(self, value: str) -> None:
        self.correo = value

    contrasenia: str = None

    def GetContrasenia(self) -> str:
        return self.contrasenia
    def SetContrasenia(self, value: str) -> None:
        self.contrasenia = value

    rol: str = None

    def GetRol(self) -> str:
        return self.rol
    def SetRol(self, value: str) -> None:
        self.rol = value

    fecha_registro: datetime.datetime = None

    def GetFecha_registro(self) -> datetime.datetime:
        return self.fecha_registro
    def SetFecha_registro(self, value: datetime.datetime) -> None:
        self.fecha_registro = value
