from Repositorios.CaminatasRepositorio import CaminatasRepositorio

def main():
    repo = CaminatasRepositorio()
    caminatas = repo.obtener_caminatas()

    for caminata in caminatas:
        print(f"\n--- Caminata ID: {caminata.id} ---")
        print(f"Fecha: {caminata.fecha}")
        print(f"Estado: {caminata.estado}")
        print(f"Usuario: {caminata.usuario.nombre}")
        print(f"Perro: {caminata.perro.nombre}")
        print(f"Día: {caminata.horario.dia_semana}")
        print(f"Ruta: {caminata.ruta.nombre}")
    
    repo.cerrar_conexion()

if __name__ == "__main__":
    main()
