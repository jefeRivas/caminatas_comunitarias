from Entidades.Refugios import Refugios

class Perros:
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

    edad: int = None

    def GetEdad(self) -> int:
        return self.edad
    def SetEdad(self, value: int) -> None:
        self.edad = value

    raza: str = None

    def GetRaza(self) -> str:
        return self.raza
    def SetRaza(self, value: str) -> None:
        self.raza = value

    tamanio: str = None

    def GetTamanio(self) -> str:
        return self.tamanio
    def SetTamanio(self, value: str) -> None:
        self.tamanio = value

    energia: str = None

    def GetEnergia(self) -> str:
        return self.energia
    def SetEnergia(self, value: str) -> None:
        self.energia = value

    descripcion: str = None

    def GetDescripcion(self) -> str:
        return self.descripcion
    def SetDescripcion(self, value: str) -> None:
        self.descripcion = value

    estado: str = None

    def GetEstado(self) -> str:
        return self.estado
    def SetEstado(self, value: str) -> None:
        self.estado = value

    refugio: int = None

    def GetRefugio(self) -> int:
        return self.refugio
    def SetRefugio(self, value: int) -> None:
        self.refugio = value

    # Relación:
    _refugio: Refugios = None

    def Get_Refugio(self) -> Refugios:
        return self._refugio
    def Set_Refugio(self, value: Refugios) -> None:
        self._refugio = value
