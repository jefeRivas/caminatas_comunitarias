class Equipamiento:
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

    descripcion: str = None

    def GetDescripcion(self) -> str:
        return self.descripcion
    def SetDescripcion(self, value: str) -> None:
        self.descripcion = value

    cantidad_disponible: int = None

    def GetCantidad_disponible(self) -> int:
        return self.cantidad_disponible
    def SetCantidad_disponible(self, value: int) -> None:
        self.cantidad_disponible = value
