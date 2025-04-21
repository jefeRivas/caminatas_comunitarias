from Repositorios.CaminatasRepositorio import CaminatasRepositorio
from Repositorios.UsuariosRepositorio import UsuariosRepositorio
from Entidades.Usuarios import Usuarios
import datetime

def mostrar_menu_principal():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Consultar Caminatas")
    print("2. Gestionar Usuarios (CRUD)")
    print("3. Salir")

def mostrar_menu_usuarios():
    print("\n--- GESTIÓN DE USUARIOS ---")
    print("1. Listar Usuarios")
    print("2. Agregar Usuario")
    print("3. Actualizar Usuario")
    print("4. Eliminar Usuario")
    print("5. Volver al menú principal")

def consultar_caminatas():
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

def gestionar_usuarios():
    repo = UsuariosRepositorio()
    
    while True:
        mostrar_menu_usuarios()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            usuarios = repo.obtener_usuarios()
            for u in usuarios:
                print(f"{u.GetId()} - {u.GetNombre()} | {u.GetCorreo()} | Rol: {u.GetRol()} | Registrado: {u.GetFecha_registro()}")
        
        elif opcion == "2":
            usuario = Usuarios()
            usuario.SetNombre(input("Nombre: "))
            usuario.SetCorreo(input("Correo: "))
            usuario.SetContrasenia(input("Contraseña: "))
            usuario.SetRol(input("Rol: "))
            usuario.SetFecha_registro(datetime.datetime.now())
            repo.insertar_usuario(usuario)
            print("✅ Usuario insertado con éxito.")

        elif opcion == "3":
            id_usuario = int(input("ID del usuario a actualizar: "))
            usuario = Usuarios()
            usuario.SetId(id_usuario)
            usuario.SetNombre(input("Nuevo nombre: "))
            usuario.SetCorreo(input("Nuevo correo: "))
            usuario.SetContrasenia(input("Nueva contraseña: "))
            usuario.SetRol(input("Nuevo rol: "))
            repo.actualizar_usuario(usuario)
            print("✅ Usuario actualizado correctamente.")
        
        elif opcion == "4":
            id_usuario = int(input("ID del usuario a eliminar: "))
            repo.eliminar_usuario(id_usuario)
            print("✅ Usuario eliminado.")
        
        elif opcion == "5":
            break
        else:
            print("❌ Opción no válida. Intente de nuevo.")
    
    repo.cerrar_conexion()

def main():
    while True:
        mostrar_menu_principal()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            consultar_caminatas()
        elif opcion == "2":
            gestionar_usuarios()
        elif opcion == "3":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
