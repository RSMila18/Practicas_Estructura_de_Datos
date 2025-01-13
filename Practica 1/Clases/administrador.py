from empleado import Empleado

class Administrador(Empleado):

    def crear_usuario(self, nombre = None, identificaion = None, fecha_nacimiento = None, ciudad_nacimiento = None, telefono = None, email = None, direccion = None, password = None, descripcion = None):
        super().__init__(nombre = None, identificaion = None, fecha_nacimiento = None, ciudad_nacimiento = None, telefono = None, email = None, direccion = None, password = None, descripcion = None)
    #crear_usuario( usuario Usuario): Boolean
    #eliminar_usuario( id Int): Boolean
    #cambiar_contraseña( id Int, csñ String): Boolean
    #responder_solicitud(id_s Int, action String): Boolean 