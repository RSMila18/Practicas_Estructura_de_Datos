from sistema import Sistema
from Clases.empleado import Empleado
from Clases.equipo import Equipo
from Clases.solicitud import Solicitud

#   Investigador               Administrador
#   d13go1979.*                c4100l485Cal$
#   34568910                   2345902

if __name__ == "__main__":
    Empleado.import_empleados()
    Empleado.import_password()
    Equipo.import_equipos()
    Solicitud.import_solicitud("Agregar", "Solicitudes_agregar.txt")
    Solicitud.import_solicitud("Editar", "Solicitudes_editar.txt")


    inicio = Sistema.ingresar_sistema()