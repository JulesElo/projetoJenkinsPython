import pytest

from loja import Produto, Carrinho


def test_carrinho_deve_iniciar_vazio():
    carrinho = Carrinho()

    assert carrinho.esta_vazio() is True
    assert carrinho.total_itens() == 0
    assert carrinho.calcular_total() == 0


def test_deve_adicionar_produto_no_carrinho():
    produto = Produto(1, "Mouse", 80.00)
    carrinho = Carrinho()

    carrinho.adicionar_produto(produto, 2)

    assert carrinho.esta_vazio() is False
    assert carrinho.total_itens() == 2
    assert carrinho.calcular_total() == 160.00


def test_deve_calcular_total_com_varios_produtos():
    teclado = Produto(1, "Teclado", 120.00)
    mouse = Produto(2, "Mouse", 80.00)
    carrinho = Carrinho()

    carrinho.adicionar_produto(teclado, 1)
    carrinho.adicionar_produto(mouse, 2)

    assert carrinho.total_itens() == 3
    assert carrinho.calcular_total() == 280.00


def test_deve_aplicar_desconto():
    produto = Produto(1, "Monitor", 1000.00)
    carrinho = Carrinho()

    carrinho.adicionar_produto(produto, 1)

    assert carrinho.aplicar_desconto(10) == 900.00


def test_nao_deve_adicionar_quantidade_invalida():
    produto = Produto(1, "Mouse", 80.00)
    carrinho = Carrinho()

    with pytest.raises(ValueError, match="quantidade"):
        carrinho.adicionar_produto(produto, 0)


def test_nao_deve_aplicar_desconto_invalido():
    produto = Produto(1, "Monitor", 1000.00)
    carrinho = Carrinho()
    carrinho.adicionar_produto(produto, 1)

    with pytest.raises(ValueError, match="desconto"):
        carrinho.aplicar_desconto(120)
