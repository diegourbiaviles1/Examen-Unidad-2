from funciones import InfixToPostfixConverter, PostfixEvaluator


def main():
    converter = InfixToPostfixConverter()
    evaluator = PostfixEvaluator()
    print("Convertir y evaluar expresiones infija->postfija")
    while True:
        expr = input("Ingresa expresión infija (o 'salir'): ")
        if expr.lower() == 'salir':
            break
        try:
            postfija = converter.convert(expr)
            print(f"Postfija: {postfija}")
            resultado = evaluator.evaluate(postfija)
            print(f"Resultado: {resultado}\n")
        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == '__main__':
    main()