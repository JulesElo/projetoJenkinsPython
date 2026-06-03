from loja import Produto, Carrinho


def main():
    teclado = Produto(1, "Teclado", 120.00)
    mouse = Produto(2, "Mouse", 80.00)

    carrinho = Carrinho()
    carrinho.adicionar_produto(teclado, 1)
    carrinho.adicionar_produto(mouse, 2)

    print("Resumo do pedido")
    print(f"Total de itens: {carrinho.total_itens()}")
    print(f"Valor total: R$ {carrinho.calcular_total():.2f}")
    print(f"Valor com 10% de desconto: R$ {carrinho.aplicar_desconto(10):.2f}")


if __name__ == "__main__":
    main()
