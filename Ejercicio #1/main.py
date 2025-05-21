from funciones_inversion import WordInverter


def main():
    inverter = WordInverter()  # creamos el invertidor
    print("Invertidor de palabras usando pilas")
    print("Escribe 'salir' para terminar.")
    while True: 
        frase = input("Ingresa una frase: ") # pide la frase
        if frase.lower() == 'salir':
            print("¡Hasta luego!")
            break
        try:
            resultado = inverter.invert(frase)  # invierte y muestra
            print(f"Invertido: {resultado}\n")
        except Exception as e:
            print(f"Error: {e}\n")

if __name__ == '__main__':
    main()
