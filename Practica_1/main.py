from sistema import Sistema
from Clases.empleado import Empleado


if __name__ == "__main__":
    Empleado.import_empleados()
    Empleado.import_password()

    inicio = Sistema.ingresar_sistema()