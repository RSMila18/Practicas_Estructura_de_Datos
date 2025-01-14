class Node:
    def __init__(self, data=None, node = None):
        self._data = data
        self._next = node
        
    def set_Data(self, Object):
        self._data = Object
    
    def set_Next(self, node):
        self._next = node
    
    def get_Data(self):
        return self._data
    
    def get_Next(self):
        return self._next
    
    def __str__(self):
        return self.data