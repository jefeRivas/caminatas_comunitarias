class PreferenciasPerros:
    usuario_id: int = None

    def GetUsuario_id(self) -> int:
        return self.usuario_id
    def SetUsuario_id(self, value: int) -> None:
        self.usuario_id = value

    perro_id: int = None

    def GetPerro_id(self) -> int:
        return self.perro_id
    def SetPerro_id(self, value: int) -> None:
        self.perro_id = value

    preferencia: int = None

    def GetPreferencia(self) -> int:
        return self.preferencia
    def SetPreferencia(self, value: int) -> None:
        self.preferencia = value

    # Relaciones
    _usuario = None
    _perro = None

    def Get_Usuario(self):
        return self._usuario
    def Set_Usuario(self, value) -> None:
        self._usuario = value

    def Get_Perro(self):
        return self._perro
    def Set_Perro(self, value) -> None:
        self._perro = value
