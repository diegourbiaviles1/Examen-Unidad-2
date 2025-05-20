# Problema 2: Verificación de paréntesis balanceados
# Version: 1.0
# Fecha: 21/05/2025
# Autor: Diego Urbina, Julio Delgadillo, Emmanuel Aguilar

from reproductor import ListaReproduccion

def mostrar_menu():
    print("""
=== Reproductor de Musica ===
1. Agregar cancion
2. Eliminar cancion actual
3. Reproducir siguiente cancion
4. Reproducir cancion anterior
5. Mostrar lista de reproduccion
6. Salir
""")


def main():
    lista = ListaReproduccion()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opcion (1-6): ").strip()

        if opcion == "1":
            nombre = input("Nombre de la cancion: ").strip()
            if nombre:
                lista.agregar_cancion(nombre)
            else:
                print("-> Nombre invalido.")
        elif opcion == "2":
            lista.eliminar_cancion_actual()
        elif opcion == "3":
            lista.siguiente_cancion()
        elif opcion == "4":
            lista.anterior_cancion()
        elif opcion == "5":
            lista.mostrar_lista()
        elif opcion == "6":
            print("-> Saliendo del reproductor.")
            break
        else:
            print("-> Opcion invalida. Intenta de nuevo.")

        print("-" * 40)

if __name__ == "__main__":
    main()
