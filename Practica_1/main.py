from sistema import Sistema
from Clases.empleado import Empleado
from Clases.equipo import Equipo
from Clases.solicitud import Solicitud
from Clases.control_cambios import ControlCambios

#   Investigador               Administrador
#   d13go1979.*                c4100l485Cal$
#   34568910                   2345902
#Juan-Perez 24567898 12 10 1980 Medellin 3003233234 juanperez@edl.edu.co kr74 4T-35 Boston Medellin null null

if __name__ == "__main__":
    Empleado.import_empleados()
    Empleado.import_password()
    Equipo.import_equipos()
    Solicitud.import_solicitud("Agregar", "Solicitudes_agregar.txt")
    Solicitud.import_solicitud("Editar", "Solicitudes_editar.txt")
    ControlCambios.import_control()


    inicio = Sistema.ingresar_sistema()