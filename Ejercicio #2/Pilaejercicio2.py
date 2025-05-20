class Pila:
    """
    Clase que implementa una estructura tipo pila (stack).
    Sigue el principio LIFO: el ultimo en entrar es el primero en salir.
    """

    def __init__(self):
        self.elementos = []  # Lista que almacena los datos

    def push(self, valor):
        """
        Agrega un elemento al tope de la pila.
        """
        self.elementos.append(valor)

    def pop(self):
        """
        Elimina y retorna el elemento del tope de la pila.
        Si la pila esta vacia, retorna None.
        """
        if not self.is_empty():
            return self.elementos.pop()
        return None

    def peek(self):
        """
        Retorna el elemento del tope sin eliminarlo.
        Si la pila esta vacia, retorna None.
        """
        if not self.is_empty():
            return self.elementos[-1]
        return None

    def is_empty(self):
        """
        Retorna True si la pila esta vacia, False en caso contrario.
        """
        return len(self.elementos) == 0
