from Clases.empleado import Empleado
from Clases.inventario import Inventario
from Clases.fecha import Fecha
from Clases.solicitud import Solicitud

class Investigador(Empleado):

    def __str__(self):
        super().__str__()
    
    def solicitar_agregar_equipo(self, empleado):
        while True:
            print("Ingrese los datos del equipo que desee agregar")
            nombre = input("Nombre del equipo: ")
            while True:
                numero_placa = input("Número de placa del equipo: ")
                if numero_placa.isdigit() and len(numero_placa) == 8: 
                    break
                else:
                    print("Número de placa inválido, debe ser de 8 dígitos.") 
            fecha_compra = str(input("Fecha de compra del quipo (DD/MM/AAAA): "))
            linea = fecha_compra.split("/")
            fecha = Fecha(linea[0],linea[1],linea[2])
            valor_compra = int(input("valor de compra de quipo: "))

            equipo = Inventario.buscar(numero_placa)
            if equipo == -1 or equipo.get_fecha_compra() != fecha or equipo.get_valor_compra() != valor_compra:
                print("Los datos del equipo son incorrectos. Ingreselos de nuevo para que su solicitud pueda ser tramitada.")
            
            else:
                solicitud = Solicitud(empleado, "Agregar", equipo)
                print(f"Su solicitud quedo tramitada correctamente con los siguientes datos:\n{solicitud}")
                break



        
        
        
        
        
    










    #solicitar_agregar_equipo(equipo Equipo): Boolean
    #solicitar_eliminar_equipo(p int, razon String):Boolean
    #consultar_estado_solicitudes(): List<Solicitud>