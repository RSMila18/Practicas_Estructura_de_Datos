from Laboratorio_4.doble_node import DoubleNode

class DoubleList:
    def __init__(self, head = None, tail = None, size = 0):
        self._head = head
        self._tail = tail
        self._size = size

    def size(self):
        return self._size

    def is_Empty(self):
        if self._size == 0:
            return True
        else:
            return False

    def first(self):
        if self.is_Empty() == True:
            raise ValueError("Lista vacia")
        return self._head

    def last(self):
        if self.is_Empty() == True:
            raise ValueError("Lista vacia")
        return self._tail

    def add_first(self, data):
        new_node = DoubleNode(data)
        if self.is_Empty() == True:
            self._head = self._tail = new_node
        else:
            new_node.set_Next(self._head)
            self._head.set_Prev(new_node)
            self._head = new_node
        self._size += 1

    def add_last(self, data):
        new_node = DoubleNode(data)
        if self.is_Empty() == True:
            self._head = self._tail = new_node
        else:
            self._tail.set_Next(new_node)
            new_node.set_Prev(self._tail)
            self._tail = new_node
        self._size += 1

    def remove_first(self):
        if self.is_Empty() == True:
            return None
        else:
            removed_node = self._head
            self._head = removed_node.get_Next()
            removed_node.set_Next(None)
            self._head.set_Prev(None)
            self._size -= 1
    
            return removed_node.get_Data()

    def remove_last(self):
        if self.is_Empty() == True:
            return None
        else:
            removed_node = self._tail
            self._tail = removed_node.get_Prev()
            self._tail.set_Next(None)
            self._tail.set_Prev(None)
            self._size -= 1
            return removed_node.get_Data()

    def remove(self, node):
        if self.is_Empty() == True:
            return None
        elif node is self._head:
            return self.remove_first()
        elif node is self._tail:
            return self.remove_last()
        else:
            removed_node = node.get_Data()
            p = removed_node.get_Prev()
            nx = removed_node.get_Next()
            p.set_Next(nx)
            nx.set_Prev(p)
            removed_node.set_Nex(None)
            removed_node.set_Prev(None)
            return removed_node.get_Data()

    def add_after(self, node, data):
        if node is self._tail:
            self.add_last(data)
        else:
            new_node = DoubleNode(data)
            nx = node.get_Next()
            node.set_Next(new_node)
            new_node.set_Prev(node)
            new_node.set_Next(nx)
            nx.set_Prev(new_node)
            self._size += 1

    def add_before(self, node, data):
        if node is self._head:
            self.add_first(data)
        else:
            new_node = DoubleNode(data)
            p = node.get_Prev()
            p.set_Prev(new_node)
            new_node.set_Prev(p)
            new_node.set_Next(node)
            node.set_Prev(new_node)
            self._size += 1
            
    def __str__(self):
        if self.is_Empty() == True:
            return "[]"
        else:
            node = self._head
            elementos = []
            while node is not None:
                elementos.append(str(node.get_Data()))
                node = node.get_Next()
            return "[" + ",".join(elementos) + "]"    