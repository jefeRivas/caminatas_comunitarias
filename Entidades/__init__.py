# Importar todos los modelos para facilitar el acceso
from .UserModel import UserModel
from .perfiles_voluntarios import PerfilesVoluntarios
from .refugios import Refugios
from .perros import Perros
from .rutas import Rutas
from .horarios import Horarios
from .caminatas import Caminatas
from .registros_caminatas import RegistrosCaminatas
from .preferencias_perros import PreferenciasPerros
from .preferencias_rutas import PreferenciasRutas
from .historial_caminatas import HistorialCaminatas
from .requisitos_perros import RequisitosPerros
from .equipamiento import Equipamiento
from .prestamos_equipamiento import PrestamosEquipamiento

__all__ = [
    'Usuarios',
    'PerfilesVoluntarios',
    'Refugios',
    'Perros',
    'Rutas',
    'Horarios',
    'Caminatas',
    'RegistrosCaminatas',
    'PreferenciasPerros',
    'PreferenciasRutas',
    'HistorialCaminatas',
    'RequisitosPerros',
    'Equipamiento',
    'PrestamosEquipamiento'
]