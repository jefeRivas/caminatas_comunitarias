class HistorialCaminatas:
    id: int = 0

    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value

    registro_caminata_id: int = None

    def GetRegistro_caminata_id(self) -> int:
        return self.registro_caminata_id
    def SetRegistro_caminata_id(self, value: int) -> None:
        self.registro_caminata_id = value

    duracion_real_min: int = None

    def GetDuracion_real_min(self) -> int:
        return self.duracion_real_min
    def SetDuracion_real_min(self, value: int) -> None:
        self.duracion_real_min = value

    distancia_real_km: float = None

    def GetDistancia_real_km(self) -> float:
        return self.distancia_real_km
    def SetDistancia_real_km(self, value: float) -> None:
        self.distancia_real_km = value

    comportamiento_perro: str = None

    def GetComportamiento_perro(self) -> str:
        return self.comportamiento_perro
    def SetComportamiento_perro(self, value: str) -> None:
        self.comportamiento_perro = value

    observaciones: str = None

    def GetObservaciones(self) -> str:
        return self.observaciones
    def SetObservaciones(self, value: str) -> None:
        self.observaciones = value

    # Relación
    _registro_caminata = None

    def Get_RegistroCaminata(self):
        return self._registro_caminata
    def Set_RegistroCaminata(self, value) -> None:
        self._registro_caminata = value
