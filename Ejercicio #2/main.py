# Problema 2: Verificación de paréntesis balanceados
# Version: 1.0
# Fecha: 21/05/2025
# Autor: Diego Urbina, Julio Delgadillo, Emmanuel Aguilar

from Pilaejercicio2 import Pila  # Importamos la estructura de pila

def esta_balanceado(cadena):
    """
    Verifica si los parentesis (), {}, [] en una cadena estan balanceados.
    Utiliza una pila para controlar las aperturas y cierres.
    """
    pila = Pila()
    pares = {')': '(', ']': '[', '}': '{'}  # Diccionario que relaciona cierres con aperturas

    for caracter in cadena:
        if caracter in "({[":
            # Si es un parentesis de apertura, lo apilamos
            pila.push(caracter)
        elif caracter in ")}]":
            # Si encontramos un cierre y la pila esta vacia, esta desbalanceado
            if pila.is_empty():
                return False
            # Si el ultimo abierto no corresponde con el cierre, esta mal emparejado
            if pila.pop() != pares[caracter]:
                return False

    # Si al final la pila esta vacia, todos los parentesis fueron cerrados correctamente
    return pila.is_empty()


def main():
    print("=== Verificador de parentesis balanceados ===")
    expresion = input("Ingrese una expresion: ").strip()

    if not expresion:
        print("→ La expresion esta vacia.")
    else:
        if esta_balanceado(expresion):
            print("→ Los parentesis estan balanceados.")
        else:
            print("→ Los parentesis NO estan balanceados.")


if __name__ == "__main__":
    main()
