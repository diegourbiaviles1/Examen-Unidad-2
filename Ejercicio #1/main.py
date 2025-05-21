from funciones_inversion import WordInverter


def main():
    inverter = WordInverter()
    print("Invertidor de palabras usando pilas")
    print("Escribe 'salir' para terminar.")
    while True:
        frase = input("Ingresa una frase: ")
        if frase.lower() == 'salir':
            print("¡Hasta luego!")
            break
        try:
            resultado = inverter.invert(frase)
            print(f"Invertido: {resultado}\n")
        except Exception as e:
            print(f"Error al invertir la frase: {e}\n")


if __name__ == '__main__':
    main()