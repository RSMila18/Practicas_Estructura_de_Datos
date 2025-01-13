class Fecha:
    def __init__(self, dia = None, mes = None, año = None):
        self._dd = dia
        self._mm = mes
        self._aa = año
    
    def set_dia(self,dia):
        self._dd=dia
    def get_dia(self):
        return self._dd
    def set_mes(self,mes):
        self._mm=mes
    def get_mes(self):
        return self._mm
    def set_A(self,año):
        self._aa=año
    def get_A(self):
        return self._aa
    
    def __str__(self):
        return f"{self._dd}-{self._mm}-{self._aa}"