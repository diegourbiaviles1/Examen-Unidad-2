class Node:
    """Nodo de lista enlazada."""
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"

class LinkedList:
    """Lista enlazada simple."""
    def __init__(self):
        self.head = None

    def append(self, data):
        """Añade un nuevo nodo al final de la lista."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def search(self, target):
        """
        Busca el valor `target` en la lista.
        Devuelve la posición 0-based si lo encuentra, o -1 si no está.
        """
        current = self.head
        index = 0
        while current:
            if current.data == target:
                return index
            current = current.next
            index += 1
        return -1

    def __str__(self):
        """Representación de la lista como secuencia de datos."""
        valores = []
        current = self.head
        while current:
            valores.append(str(current.data))
            current = current.next
        return ' -> '.join(valores)