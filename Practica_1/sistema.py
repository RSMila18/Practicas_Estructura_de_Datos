from Clases.administrador import Administrador
from Clases.investigador import Investigador
class Sistema:    

    def ingresar_sistema():
        Administrador.import_empleados()
        Investigador.import_password()

        print("Bienvenid@, por favor, a continuación ingrese sus credenciales para accder al sistema.\n")
        id_ = input("Ingrese su número de identificación(cédula): ")
        password = input("Ingrese su contraseña: ")

        empleado = Administrador.buscar(id_)
        if empleado != -1 and empleado.get_password() == password:
                Sistema.menu(empleado)
        else:
            print("Identificación y/o contraseña incorrecta.")


    def menu(self, empleado):
        if empleado.get_descripcion() == "administrador":

            while True:
                print("\n--- Menú Administrador ---")
                print("1. Crear nuevo usuario")
                print("2. Eliminar usuario")
                print("3. Cambiar contraseña")
                print("4. Responder solicitudes")
                print("5. Consultar inventario de un usuario")
                print("6. Salir")

                opcion = input("Seleccione una opción: ")
                if opcion == "1":
                    Administrador.crear_usuario()
                elif opcion == "2":
                    ident = input("Ingrese la identificación(cédula) del empleado que desea eliminar: ")
                    Administrador.eliminar_usuario(ident)
                elif opcion == "3":
                    Administrador.cambiar_contraseña()
                elif opcion == "4":
                    Administrador.responder_solicitudes()
                elif opcion == "5":
                    Administrador.consultar_inventario(empleado)
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
                print("5. Generar reporte de inventario y solicitudes")
                print("6. Salir")

                opcion = input("Seleccione una opción: ")
                if opcion == "1":
                    self.consultar_inventario(empleado)
                elif opcion == "2":
                    self.solicitar_agregar_equipo(empleado)
                elif opcion == "3":
                    self.solicitar_eliminar_equipo(empleado)
                elif opcion == "4":
                    self.consultar_solicitudes(empleado)
                elif opcion == "5":
                    self.generar_reporte_investigador(empleado)
                elif opcion == "6":
                    self.guardar_archivos()
                    break
                else:
                    print("Opción no válida.")
            
            else:
                print("Ingreso invalido")