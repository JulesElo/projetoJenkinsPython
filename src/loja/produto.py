from dataclasses import dataclass


@dataclass
class Produto:
    """Representa um produto simples de uma loja."""

    codigo: int
    nome: str
    preco: float

    def __post_init__(self):
        if self.codigo <= 0:
            raise ValueError("O codigo do produto deve ser maior que zero.")
        if not self.nome.strip():
            raise ValueError("O nome do produto nao pode ser vazio.")
        if self.preco <= 0:
            raise ValueError("O preco do produto deve ser maior que zero.")
