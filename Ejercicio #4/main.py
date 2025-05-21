# Problema 4: Cola de Prioridad
# Version: 1.0
# Fecha: 21/05/2025
# Autor: Diego Urbina, Julio Delgadillo, Emmanuel Aguilar


from funciones_prioridad import PriorityQueue


# Interfaz de usuario para la cola de prioridad
def main():
    pq = PriorityQueue()  # crear cola
    print("--- Cola de Prioridad Interactiva ---")
    while True:
        # Mostrar menú
        print("\nOpciones:")
        print("1. Encolar elemento")
        print("2. Desencolar siguiente")
        print("3. Ver siguiente (peek)")
        print("4. Chequear si está vacía")
        print("5. Salir")
        opcion = input("Selecciona una opción: ").strip()

        if opcion == '1':
            # Pedir datos y encolar
            item = input("Elemento (nombre): ").strip()
            try:
                pr = int(input("Prioridad (menor = más urgente): ").strip())
                pq.enqueue(item, pr)
                print(f"Agregado '{item}' con prioridad {pr}")
            except ValueError:
                print("Prioridad inválida. Debe ser un número entero.")

        elif opcion == '2':
            # Desencolar elemento más urgente
            try:
                item, pr = pq.dequeue()
                print(f"Desencolado '{item}' con prioridad {pr}")
            except IndexError as e:
                print(f"Error: {e}")

        elif opcion == '3':
            # Ver siguiente elemento
            res = pq.peek()
            if res:
                print(f"Siguiente en cola: '{res[0]}' con prioridad {res[1]}")
            else:
                print("La cola está vacía.")

        elif opcion == '4':
            # Chequear estado de la cola
            estado = "vacía" if pq.is_empty() else f"no está vacía (tamaño={len(pq)})"
            print(f"La cola {estado}.")

        elif opcion == '5':
            # Salir del programa
            print("¡Hasta luego!")
            break

        else:
            # Opción no válida
            print("Opción no reconocida. Intenta otra vez.")

if __name__ == '__main__':
    main()
