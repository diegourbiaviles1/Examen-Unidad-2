class Node:
    # Nodo que almacena un dato y apunta al siguiente nodo
    def __init__(self, data):
        self.data = data  # valor guardado
        self.next = None  # referencia al siguiente nodo, None si no hay

    def __repr__(self):
        # Permite ver el contenido al imprimir el nodo
        return f"Node({self.data})"

class LinkedList:
    # Lista enlazada simple, permite append y búsqueda
    def __init__(self):
        self.head = None  # inicio de la lista

    def append(self, data):
        # Crea un nuevo nodo al final con el dato dado
        new_node = Node(data)
        if not self.head:
            # Si la lista está vacía, head apunta al nuevo nodo
            self.head = new_node
            return
        current = self.head
        # Recorrer hasta llegar al último nodo
        while current.next:
            current = current.next
        # Enlazar el nuevo nodo al final
        current.next = new_node

    def search(self, target):
        # Busca `target` y devuelve su posición (0-based)
        current = self.head
        index = 0
        # Recorrer nodos hasta encontrar o llegar al final
        while current:
            if current.data == target:
                return index  # encontrado
            current = current.next
            index += 1
        return -1  # no encontrado en toda la lista

    def __str__(self):
        # Devuelve los valores de la lista separados por flechas
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return ' -> '.join(values)
