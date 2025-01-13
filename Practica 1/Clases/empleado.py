from Clases.usuario import Usuario

class Empleado(Usuario):
    
    def __init__(self, nombre = None, identificacion = None, fecha_nacimiento = None, ciudad_nacimiento = None, telefono = None, email = None, direccion = None, password = None, descripcion = None):
        super().__init__(nombre, identificacion, fecha_nacimiento, ciudad_nacimiento, telefono, email, direccion)
        self._password = password
        self._descripcion = descripcion
        

    def get_password(self):
        return self._password
    def set_password(self, csñ):
        self._password = csñ
    def get_descripcion(self):
        return self._descripcion
    def set_descripcion(self, tipo):
        self._descripcion = tipo

    def __str__(self):
        base_str = super().__str__()
        return f'{base_str},{self._password},{self._descripcion}'

    # Método para ingresar al sistema
    def ingresar_sistema(self, identificacion, password):
        if str(self._id) == str(identificacion) and self._password == password:
            print("Inicio de sesión exitoso.")
            return True
        else:
            print("Identificación y/o contraseña incorrecta.")
            return False

    #ingresar_sistema(id Int, password String): Bolean
    #consultar_inventario(): List<Equipo>
    