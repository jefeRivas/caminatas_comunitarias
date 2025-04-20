class PrestamoEquipamiento:
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

    equipamiento_id: int = None

    def GetEquipamiento_id(self) -> int:
        return self.equipamiento_id
    def SetEquipamiento_id(self, value: int) -> None:
        self.equipamiento_id = value

    cantidad: int = None

    def GetCantidad(self) -> int:
        return self.cantidad
    def SetCantidad(self, value: int) -> None:
        self.cantidad = value

    devuelto: bool = False

    def GetDevuelto(self) -> bool:
        return self.devuelto
    def SetDevuelto(self, value: bool) -> None:
        self.devuelto = value

    # Relaciones
    _registro_caminata = None
    _equipamiento = None

    def Get_RegistroCaminata(self):
        return self._registro_caminata
    def Set_RegistroCaminata(self, value) -> None:
        self._registro_caminata = value

    def Get_Equipamiento(self):
        return self._equipamiento
    def Set_Equipamiento(self, value) -> None:
        self._equipamiento = value
