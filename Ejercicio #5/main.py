# Problema 5: Buscar en Lista Enlazada
# Version: 1.0
# Fecha: 21/05/2025
# Autor: Diego Urbina, Julio Delgadillo, Emmanuel Aguilar
from funciones_listaenlazada import LinkedList
# Punto de entrada: crea y busca en la lista enlazada
def main():
    print("--- Búsqueda en Lista Enlazada ---")
    # Leer elementos separados por espacio
    datos = input("Ingresa elementos separados por espacios: ").strip().split()
    ll = LinkedList()
    for d in datos:
        ll.append(d)  # construir la lista

    print(f"Lista creada: {ll}")
    while True:
        # Pedir valor a buscar
        objetivo = input("Valor a buscar (o 'salir'): ")
        if objetivo.lower() == 'salir':
            print("Fin de la búsqueda. ¡Adiós!")
            break
        pos = ll.search(objetivo)
        if pos >= 0:
            print(f"'{objetivo}' encontrado en posición {pos}.")
        else:
            print(f"'{objetivo}' no está en la lista.")
        print()  # línea en blanco para legibilidad

if __name__ == '__main__':
    main()