class Horarios:
    id: int = 0

    def GetId(self) -> int:
        return self.id
    def SetId(self, value: int) -> None:
        self.id = value

    dia_semana: str = None

    def GetDia_semana(self) -> str:
        return self.dia_semana
    def SetDia_semana(self, value: str) -> None:
        self.dia_semana = value

    hora_inicio: str = None  # Puede ser datetime.time si prefieres

    def GetHora_inicio(self) -> str:
        return self.hora_inicio
    def SetHora_inicio(self, value: str) -> None:
        self.hora_inicio = value

    hora_fin: str = None  # Igual que arriba, puedes cambiarlo a time

    def GetHora_fin(self) -> str:
        return self.hora_fin
    def SetHora_fin(self, value: str) -> None:
        self.hora_fin = value

    max_voluntarios: int = 0

    def GetMax_voluntarios(self) -> int:
        return self.max_voluntarios
    def SetMax_voluntarios(self, value: int) -> None:
        self.max_voluntarios = value
