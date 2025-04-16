class Refugios:
	id: int = 0;

	def GetId(self) -> int:
		return self.id;
	def SetId(self, value: int) -> None:
		self.id = value;

	nombre: str = None;

	def GetNombre(self) -> str:
		return self.nombre;
	def SetNombre(self, value: str) -> None:
		self.nombre = value;

    direccion: str = None;

    def GetDireccion(self) -> str:
        return self.direccion;
    def SetDireccion(self, value: str) -> None:
        self.direccion = value;

    telefono: str = None;

    def GetTelefono(self) -> str:
        return self.telefono;
    def SetTelefono(self, value:str) -> None:
        self.telefono = value;

    correo: str = None;

    def GetCorreo(self) -> str:
        return self.correo;
    def SetCorreo(self, value:str) -> None:
        self.correo = value;