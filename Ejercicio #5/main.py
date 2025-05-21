from funciones_listaenlazada import LinkedList


def main():
    print("--- Búsqueda en Lista Enlazada ---")
    # Crear la lista a partir de entrada del usuario
    datos = input("Ingresa elementos separados por espacios: ").strip().split()
    ll = LinkedList()
    for d in datos:
        ll.append(d)

    print(f"Lista creada: {ll}")
    while True:
        objetivo = input("Valor a buscar (o 'salir'): ")
        if objetivo.lower() == 'salir':
            print("Fin de la búsqueda. ¡Adiós!")
            break
        pos = ll.search(objetivo)
        if pos >= 0:
            print(f"Valor '{objetivo}' encontrado en la posición {pos} (0-based).\n")
        else:
            print(f"Valor '{objetivo}' NO se encuentra en la lista.\n")

if __name__ == '__main__':
    main()