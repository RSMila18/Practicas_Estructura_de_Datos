from Clases.empleado import Empleado
from Clases.equipo import Equipo


class Investigador(Empleado):

    def __str__(self):
        super().__str__()
    
    def solicitar_agregar_equipo(self):
        print("Ingrese los datos del equipo que desee agregar")
        nombre = input("Nombre del equipo: ")
        numero_placa = input("Numero de placa del equipo: ")
        fecha_compra = input("Fecha de compra del quipo: ")
        valor_compra = input("valor de compra de quipo (DD/MM/AAAA): ")
        equipo = Equipo(nombre, numero_placa, fecha_compra, valor_compra)
        
        if not isinstance(equipo, Equipo):
            print("El quipo solicitado no se encuentra")
            return False
    










    #solicitar_agregar_equipo(equipo Equipo): Boolean
    #solicitar_eliminar_equipo(p int, razon String):Boolean
    #consultar_estado_solicitudes(): List<Solicitud>