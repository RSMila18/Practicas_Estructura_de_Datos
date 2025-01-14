from Clases.empleado import Empleado
class Sistema:    

    def menu_administrador(self, id_):
        while True:
            print("\n--- Menú Administrador ---")
            print("1. Crear nuevo usuario")
            print("2. Eliminar usuario")
            print("3. Cambiar contraseña")
            print("4. Ver solicitudes")
            print("5. Aprobar o rechazar solicitudes")
            print("6. Consultar inventario de un usuario")
            print("7. Generar reportes")
            print("8. Salir")

            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                self.crear_usuario()
            elif opcion == "2":
                self.eliminar_usuario()
            elif opcion == "3":
                self.cambiar_contraseña()
            elif opcion == "4":
                self.ver_solicitudes()
            elif opcion == "5":
                self.gestionar_solicitudes()
            elif opcion == "6":
                self.consultar_inventario_admin()
            elif opcion == "7":
                self.generar_reportes()
            elif opcion == "8":
                self.guardar_archivos()
                break
            else:
                print("Opción no válida.")

    def menu_investigador(self, id_):
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
                self.consultar_inventario(id_)
            elif opcion == "2":
                self.solicitar_agregar_equipo(id_)
            elif opcion == "3":
                self.solicitar_eliminar_equipo(id_)
            elif opcion == "4":
                self.consultar_solicitudes(id_)
            elif opcion == "5":
                self.generar_reporte_investigador(id_)
            elif opcion == "6":
                self.guardar_archivos()
                break
            else:
                print("Opción no válida.")