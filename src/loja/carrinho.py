from .produto import Produto


class Carrinho:
    """Carrinho de compras com regras simples para uso em testes unitarios."""

    def __init__(self):
        self._itens = []

    def adicionar_produto(self, produto: Produto, quantidade: int):
        if quantidade <= 0:
            raise ValueError("A quantidade deve ser maior que zero.")

        self._itens.append({
            "produto": produto,
            "quantidade": quantidade
        })

    def total_itens(self):
        return sum(item["quantidade"] for item in self._itens)

    def calcular_total(self):
        return sum(
            item["produto"].preco * item["quantidade"]
            for item in self._itens
        )

    def aplicar_desconto(self, percentual: float):
        if percentual < 0 or percentual > 100:
            raise ValueError("O desconto deve estar entre 0 e 100.")

        total = self.calcular_total()
        return total - (total * percentual / 100)

    def esta_vazio(self):
        return len(self._itens) == 0
