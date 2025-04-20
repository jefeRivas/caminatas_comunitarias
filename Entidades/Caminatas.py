class Caminatas:
    id: int = 0

    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value

    fecha: str = None

    def GetFecha(self) -> str:
        return self.fecha
    def SetFecha(self, value: str) -> None:
        self.fecha = value

    horario_id: int = None

    def GetHorario_id(self) -> int:
        return self.horario_id
    def SetHorario_id(self, value: int) -> None:
        self.horario_id = value

    ruta_id: int = None

    def GetRuta_id(self) -> int:
        return self.ruta_id
    def SetRuta_id(self, value: int) -> None:
        self.ruta_id = value

    estado: str = "pendiente"

    def GetEstado(self) -> str:
        return self.estado
    def SetEstado(self, value: str) -> None:
        self.estado = value

    # Relaciones
    _horario = None
    _ruta = None

    def Get_Horario(self):
        return self._horario
    def Set_Horario(self, value) -> None:
        self._horario = value

    def Get_Ruta(self):
        return self._ruta
    def Set_Ruta(self, value) -> None:
        self._ruta = value
