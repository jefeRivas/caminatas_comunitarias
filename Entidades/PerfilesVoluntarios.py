import Usuarios;

class PerfilesVoluntarios:
	id: int = 0;

	def GetId(self) -> int:
		return self.id;
	def SetId(self, value: int) -> None:
		self.id = value;

	telefono: str = None;

	def GetTelefono(self) -> str:
		return self.telefono;
	def SetTelefono(self, value: str) -> None:
		self.telefono = value;

    direccion: str = None;

    def GetDireccion(self) -> str:
        return self.direccion;
    def SetDireccion(self, value:str) -> None:
        self.direccion = value;

    usuario: int = None;

    def GetUsuario(self) -> int:
        return self.usuario;
    def SetUsuario(self, value:int) -> None:
        self.usuario = value;

    experiencia: str = None;

    def GetExperiencia(self) -> str:
        return self.experiencia;
    def SetExperiencia(self, value:str) -> None:
        self.experiencia = value;

    #Relación
    _usuario: Usuarios = None;

    def Get_Usuario(self) -> Usuarios:
        return self._usuario;
    def Set_Usuario(self, value: Usuarios) -> None:
        self._usuario = value;
