from Clases.administrador import Administrador
from Clases.investigador import Investigador
from Clases.empleado import Empleado
class Sistema:    
    
    def ingresar_sistema():

        print("Bienvenid@, por favor, a continuación ingrese sus credenciales para acceder al sistema.\n")
        while True:
            id_ = int(input("Ingrese su número de identificación(cédula): "))
            password = input("Ingrese su contraseña: ")

            empleado = Empleado.buscar(id_)
            if empleado is not None and empleado.get_password() == password:
                    Sistema.menu(empleado)
                    break
            else:
                print("Identificación y/o contraseña incorrecta.")
    @classmethod
    def menu(self, empleado):
        if empleado.get_descripcion() == "administrador":

            while True:
                print("\n--- Menú Administrador ---")
                print("1. Crear nuevo usuario")
                print("2. Buscar Usuario")
                print("3. Eliminar usuario")
                print("4. Cambiar contraseña")
                print("5. Responder solicitudes")
                print("6. Consultar inventario de un usuario")
                print("7. Salir")

                opcion = input("Seleccione una opción: ")
                if opcion == "1":
                    Administrador.crear_usuario()
                elif opcion == "2":
                    ident = input("Ingrese la identificación(cédula) del empleado que desea buscar: ")
                    emp = Administrador.buscar(int(ident))
                    if emp is not None and ident.isdigit():
                        print(emp)
                    else:
                        print("Empleado no encontrado.")
                    
                elif opcion == "3":
                    ident = input("Ingrese la identificación(cédula) del empleado que desea eliminar: ")
                    if ident.isdigit():
                        Administrador.eliminar_usuario(ident)
                elif opcion == "4":
                    Administrador.cambiar_contraseña()
                elif opcion == "5":
                    Administrador.responder_solicitudes()
                elif opcion == "6":
                    Administrador.consultar_inventario_E(empleado)
                elif opcion == "7":
                    print("Sesión cerrada")
                    break
                else:
                    print("Opción no válida.")

        elif empleado.get_descripcion() == "investigador": 

            while True:
                print("\n--- Menú Investigador ---")
                print("1. Consultar inventario")
                print("2. Solicitar agregar equipo")
                print("3. Solicitar eliminar equipo")
                print("4. Consultar estado de solicitudes")
                print("5. Salir")

                opcion = input("Seleccione una opción: ")
                if opcion == "1":
                    Investigador.consultar_inventario_E(empleado)
                elif opcion == "2":
                    Investigador.solicitar_agregar_equipo(empleado)
                elif opcion == "3":
                    Investigador.solicitar_eliminar_equipo(empleado)
                elif opcion == "4":
                    Investigador.consultar_estado_solicitudes(empleado)
                elif opcion == "5":
                    print("Sesión cerrada")
                    break
                else:
                    print("Opción no válida.")