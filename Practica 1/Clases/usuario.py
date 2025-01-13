class Usuario:
    def __init__(self, nombre = None, identificaion = None, fecha_nacimiento = None, ciudad_nacimiento = None, telefono = None, email = None, direccion = None):
        self._nombre = nombre
        self._id = identificaion
        self._fecha_nacimiento = fecha_nacimiento
        self._ciudad_nacimiento = ciudad_nacimiento
        self._tel = telefono
        self._email = email
        self._dir = direccion
    
    def set_nombre(self, nombre):
        self._nombre = nombre
    def get_nombre(self):
        return self._nombre
    def set_id(self, identificacion):
        self._id = identificacion
    def get_id(self):
        return self._id
    def set_fecha_nacimiento(self, fecha_nacimiento):
        self._fecha_nacimiento = fecha_nacimiento
    def get_fecha_nacimiento(self):
        return self._fecha_nacimiento
    def set_ciudad_nacimiento(self, ciudad_nacimiento):
        self._ciudad_nacimiento = ciudad_nacimiento
    def get_ciudad_nacimiento(self):
        return self._ciudad_nacimiento
    def set_tel(self, telefono):
        self._tel = telefono
    def get_tel(self):
        return self._tel
    def set_email(self, email):
        self._email = email
    def get_email(self):
        return self._email
    def set_dir(self, direccion):
        self._dir = direccion
    def get_dir(self):
        return self._dir
    
    def __str__(self):
        return f'{self._nombre},{self._id},{self._fecha_nacimiento},{self._ciudad_nacimiento},{self._tel},{self._email},{self._dir}'
    