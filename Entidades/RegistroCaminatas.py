class RegistroCaminatas:
    id: int = 0

    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value

    usuario_id: int = None

    def GetUsuario_id(self) -> int:
        return self.usuario_id
    def SetUsuario_id(self, value: int) -> None:
        self.usuario_id = value

    caminata_id: int = None

    def GetCaminata_id(self) -> int:
        return self.caminata_id
    def SetCaminata_id(self, value: int) -> None:
        self.caminata_id = value

    perro_id: int = None

    def GetPerro_id(self) -> int:
        return self.perro_id
    def SetPerro_id(self, value: int) -> None:
        self.perro_id = value

    fecha_registro: str = None

    def GetFecha_registro(self) -> str:
        return self.fecha_registro
    def SetFecha_registro(self, value: str) -> None:
        self.fecha_registro = value

    asistencia: bool = False

    def GetAsistencia(self) -> bool:
        return self.asistencia
    def SetAsistencia(self, value: bool) -> None:
        self.asistencia = value

    comentarios: str = None

    def GetComentarios(self) -> str:
        return self.comentarios
    def SetComentarios(self, value: str) -> None:
        self.comentarios = value

    # Relaciones
    _usuario = None
    _caminata = None
    _perro = None

    def Get_Usuario(self):
        return self._usuario
    def Set_Usuario(self, value) -> None:
        self._usuario = value

    def Get_Caminata(self):
        return self._caminata
    def Set_Caminata(self, value) -> None:
        self._caminata = value

    def Get_Perro(self):
        return self._perro
    def Set_Perro(self, value) -> None:
        self._perro = value
