"""
Módulo con la lógica para invertir el orden de las palabras de una frase usando POO y pilas.
Contiene:
- Stack: estructura de datos LIFO genérica.
- WordInverter: clase que usa Stack para invertir frases.
"""

class Stack:
    """Implementación sencilla de una pila."""
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not self._items

    def push(self, item):
        """Añade un elemento al tope de la pila."""
        self._items.append(item)

    def pop(self):
        """Extrae y devuelve el tope de la pila. Error si está vacía."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """Devuelve el elemento tope sin extraerlo, o None si está vacía."""
        return self._items[-1] if self._items else None


class WordInverter:
    """Invierte el orden de las palabras de una frase usando una pila."""
    def __init__(self, stack_class=Stack):
        # Permite inyección de dependencia para pruebas
        self.stack_class = stack_class

    def invert(self, sentence: str) -> str:
        """Devuelve la frase con el orden de palabras invertido."""
        stack = self.stack_class()
        # Separar por espacios, conservar palabras no vacías
        words = [w for w in sentence.strip().split(' ') if w]
        for word in words:
            stack.push(word)

        inverted = []
        while not stack.is_empty():
            inverted.append(stack.pop())

        return ' '.join(inverted)
