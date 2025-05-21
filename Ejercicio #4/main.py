from funciones_prioridad import PriorityQueue


def main():
    pq = PriorityQueue()
    print("--- Cola de Prioridad Interactiva ---")
    while True:
        print("\nOpciones:")
        print("1. Encolar elemento")
        print("2. Desencolar siguiente")
        print("3. Ver siguiente (peek)")
        print("4. Chequear si está vacía")
        print("5. Salir")
        opcion = input("Selecciona una opción: ").strip()

        if opcion == '1':
            item = input("Elemento (nombre): ").strip()
            try:
                pr = int(input("Prioridad (entero, menor = mayor prioridad): ").strip())
                pq.enqueue(item, pr)
                print(f"Agregado '{item}' con prioridad {pr}")
            except ValueError:
                print("Prioridad inválida. Debe ser un número entero.")

        elif opcion == '2':
            try:
                item, pr = pq.dequeue()
                print(f"Desencolado '{item}' con prioridad {pr}")
            except IndexError as e:
                print(f"Error: {e}")

        elif opcion == '3':
            res = pq.peek()
            if res:
                print(f"Siguiente en cola: '{res[0]}' con prioridad {res[1]}")
            else:
                print("La cola está vacía.")

        elif opcion == '4':
            estado = "vacía" if pq.is_empty() else f"no está vacía (tamaño={len(pq)})"
            print(f"La cola {estado}.")

        elif opcion == '5':
            print("¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intenta de nuevo.")


if __name__ == '__main__':
    main()
