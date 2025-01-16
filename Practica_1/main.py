from sistema import Sistema
from Clases.empleado import Empleado

#   Investigador               Administrador
#   d13go1979.*                c4100l485Cal$
#   34568910                   2345902

if __name__ == "__main__":
    Empleado.import_empleados()
    Empleado.import_password()

    inicio = Sistema.ingresar_sistema()