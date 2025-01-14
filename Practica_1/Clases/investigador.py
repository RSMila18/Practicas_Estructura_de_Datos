from Clases.empleado import Empleado
from Clases.equipo import Equipo
from Clases.solicitud import Solicitud

class Investigador(Empleado):

    def __str__(self):
        super().__str__()
    
    def solicitar_agregar_equipo(self):
        print("Ingrese los datos del equipo que desee agregar")
        nombre = input("Nombre del equipo: ")
        while True:
            numero_placa = input("Número de placa del equipo: ")
            if numero_placa.isdigit() and len(numero_placa) == 8: 
                break
            else:
                print("Número de placa inválido, debe ser de 8 dígitos.") 
        fecha_compra = input("Fecha de compra del quipo (DD/MM/AAAA): ")
        valor_compra = input("valor de compra de quipo: ")
        
        equipo_agregar = Equipo(nombre, numero_placa, fecha_compra, valor_compra)
        
        solicitudes.add_Last((equipo_agregar))
        
        if not isinstance(equipo, Equipo):
            print("El quipo solicitado no se encuentra")
            return False
    










    #solicitar_agregar_equipo(equipo Equipo): Boolean
    #solicitar_eliminar_equipo(p int, razon String):Boolean
    #consultar_estado_solicitudes(): List<Solicitud>