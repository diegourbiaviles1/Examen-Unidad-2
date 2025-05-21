# Módulo para invertir palabras de una frase usando pila

class Stack:
    # Pila LIFO sencilla
    def __init__(self):
        self._items = []

    def is_empty(self):
        # Retorna True si no hay nada
        return not self._items

    def push(self, item):
        # Agrega un elemento arriba
        self._items.append(item)

    def pop(self):
        # Saca y devuelve el último elemento
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        # Mira el último sin sacar
        return self._items[-1] if self._items else None

class WordInverter:
    # Invierte el orden de las palabras en una frase
    def __init__(self, stack_class=Stack):
        self.stack_class = stack_class

    def invert(self, sentence: str) -> str:
        # Asegura que sea texto
        if not isinstance(sentence, str):
            raise ValueError("La frase debe ser texto")
        stack = self.stack_class()
        # Mete cada palabra en la pila
        for word in sentence.strip().split():
            stack.push(word)
        # Saca para invertir el orden
        inverted = []
        while not stack.is_empty():
            inverted.append(stack.pop())
        return ' '.join(inverted)



