class Rutas:
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

    distancia_km: float = None

    def GetDistancia_km(self) -> float:
        return self.distancia_km
    def SetDistancia_km(self, value: float) -> None:
        self.distancia_km = value

    dificultad: str = None

    def GetDificultad(self) -> str:
        return self.dificultad
    def SetDificultad(self, value: str) -> None:
        self.dificultad = value

    descripcion: str = None

    def GetDescripcion(self) -> str:
        return self.descripcion
    def SetDescripcion(self, value: str) -> None:
        self.descripcion = value

    puntos_referencia: str = None

    def GetPuntos_referencia(self) -> str:
        return self.puntos_referencia
    def SetPuntos_referencia(self, value: str) -> None:
        self.puntos_referencia = value

    tiempo_estimado_min: int = None

    def GetTiempo_estimado_min(self) -> int:
        return self.tiempo_estimado_min
    def SetTiempo_estimado_min(self, value: int) -> None:
        self.tiempo_estimado_min = value
