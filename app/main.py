from app.calculadora import Calculadora


def executar_aplicacao() -> None:
    calc = Calculadora()

    print("Aplicação Python iniciada com sucesso!")
    print("Exemplo de operações:")
    print(f"10 + 5 = {calc.somar(10, 5)}")
    print(f"10 - 5 = {calc.subtrair(10, 5)}")
    print(f"10 * 5 = {calc.multiplicar(10, 5)}")
    print(f"10 / 5 = {calc.dividir(10, 5)}")


if __name__ == "__main__":
    executar_aplicacao()
