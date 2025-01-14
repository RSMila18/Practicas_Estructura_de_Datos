class DoubleNode:
    def __init__(self, data = None, _next = None, prev = None):
        self._data = data
        self._next = _next
        self._prev = prev

    def set_Data(self, object_):
        self._data = object_
    
    def set_Next(self, doubleNode):
        self._next = doubleNode

    def set_Prev(self, doubleNode):
        self._prev = doubleNode
    
    def get_Data(self):
        return self._data
    
    def get_Next(self):
        return self._next
    
    def get_Prev(self):
        return self._prev
    
    def __str__(self):
        return self._data