class RequisitosPerros:
    perro_id: int = None

    def GetPerro_id(self) -> int:
        return self.perro_id
    def SetPerro_id(self, value: int) -> None:
        self.perro_id = value

    requisito: str = None

    def GetRequisito(self) -> str:
        return self.requisito
    def SetRequisito(self, value: str) -> None:
        self.requisito = value

    # Relación
    _perro = None

    def Get_Perro(self):
        return self._perro
    def Set_Perro(self, value) -> None:
        self._perro = value
