# functions.py
"""
Módulo con la lógica de conversión y evaluación de expresiones aritméticas.
Contiene la implementación de:
- Stack
- InfixToPostfixConverter
- PostfixEvaluator
"""

class Stack:
    """Implementación sencilla de una pila."""
    def __init__(self):
        self._items = []

    def is_empty(self):
        return not self._items

    def push(self, item):
        """Inserta un elemento en la pila."""
        self._items.append(item)

    def pop(self):
        """Elimina y devuelve el elemento tope. Lanza IndexError si está vacía."""
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """Devuelve el elemento tope sin quitarlo, o None si está vacía."""
        return self._items[-1] if self._items else None


class InfixToPostfixConverter:
    """Convierte expresiones infijas a notación postfija."""
    def __init__(self):
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
        self.assoc = {'+': 'L', '-': 'L', '*': 'L', '/': 'L', '^': 'R'}

    def tokenize(self, expr):
        tokens, i = [], 0
        while i < len(expr):
            c = expr[i]
            if c.isspace():
                i += 1; continue
            if c.isalnum() or c == '.':
                j = i
                while j < len(expr) and (expr[j].isalnum() or expr[j] == '.'):
                    j += 1
                tokens.append(expr[i:j]); i = j
            elif c in '()+-*/^':
                tokens.append(c); i += 1
            else:
                raise ValueError(f"Token no válido: {c}")
        return tokens

    def convert(self, expr):
        output, stack = [], Stack()
        for token in self.tokenize(expr):
            if token.replace('.', '', 1).isdigit() or token.isalpha():
                output.append(token)
            elif token == '(':
                stack.push(token)
            elif token == ')':
                while not stack.is_empty() and stack.peek() != '(':
                    output.append(stack.pop())
                if stack.is_empty(): raise ValueError("Paréntesis desbalanceados")
                stack.pop()
            else:
                # operador
                while (not stack.is_empty() and stack.peek() != '(' and
                       ((self.assoc[token]=='L' and self.precedence[token]<=self.precedence.get(stack.peek(),0)) or
                        (self.assoc[token]=='R' and self.precedence[token]<self.precedence.get(stack.peek(),0)))):
                    output.append(stack.pop())
                stack.push(token)
        while not stack.is_empty():
            if stack.peek() == '(':
                raise ValueError("Paréntesis desbalanceados")
            output.append(stack.pop())
        return ' '.join(output)


class PostfixEvaluator:
    """Evalúa expresiones en notación postfija."""
    def __init__(self):
        self.operators = {
            '+': lambda a,b: a+b,
            '-': lambda a,b: a-b,
            '*': lambda a,b: a*b,
            '/': lambda a,b: a/b,
            '^': lambda a,b: a**b,
        }

    def evaluate(self, postfix_expr):
        stack = Stack()
        for token in postfix_expr.split():
            if token.replace('.', '', 1).isdigit():
                stack.push(float(token))
            elif token in self.operators:
                b = stack.pop(); a = stack.pop()
                stack.push(self.operators[token](a,b))
            else:
                raise ValueError(f"Token inválido: {token}")
        if stack.is_empty(): raise ValueError("Expresión inválida")
        result = stack.pop()
        if not stack.is_empty(): raise ValueError("Operandos sobrantes")
        return result