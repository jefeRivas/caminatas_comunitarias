# View/UserView.py
from Controller.UserController import UserController  

def menu():
    controller = UserController()
    while True:
        print("\n--- Menú de Usuarios ---")
        print("1. Crear usuario")
        print("2. Listar usuarios")
        print("3. Editar usuario")
        print("4. Eliminar usuario")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            correo = input("Correo: ")
            contrasena = input("Contraseña: ")
            rol = input("Rol (admin/voluntario): ")
            controller.crear_usuario(nombre, correo, contrasena, rol)

        elif opcion == "2":
            usuarios = controller.listar_usuarios()
            for u in usuarios:
                print(f"[{u.get_id()}] {u.get_nombre()} | {u.get_correo()} | {u.get_rol()}")

        elif opcion == "3":
            id = int(input("ID del usuario a editar: "))
            nombre = input("Nuevo nombre: ")
            correo = input("Nuevo correo: ")
            contrasena = input("Nueva contraseña: ")
            rol = input("Nuevo rol: ")
            controller.editar_usuario(id, nombre, correo, contrasena, rol)

        elif opcion == "4":
            id = int(input("ID del usuario a eliminar: "))
            controller.eliminar_usuario(id)

        elif opcion == "5":
            break

        else:
            print("Opción no válida")

if __name__ == "__main__":
    menu()
