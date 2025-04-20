class PreferenciasRutas:
    usuario_id: int = None

    def GetUsuario_id(self) -> int:
        return self.usuario_id
    def SetUsuario_id(self, value: int) -> None:
        self.usuario_id = value

    ruta_id: int = None

    def GetRuta_id(self) -> int:
        return self.ruta_id
    def SetRuta_id(self, value: int) -> None:
        self.ruta_id = value

    preferencia: int = None

    def GetPreferencia(self) -> int:
        return self.preferencia
    def SetPreferencia(self, value: int) -> None:
        self.preferencia = value

    # Relaciones
    _usuario = None
    _ruta = None

    def Get_Usuario(self):
        return self._usuario
    def Set_Usuario(self, value) -> None:
        self._usuario = value

    def Get_Ruta(self):
        return self._ruta
    def Set_Ruta(self, value) -> None:
        self._ruta = value
