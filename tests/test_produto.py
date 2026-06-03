import pytest

from loja import Produto


def test_deve_criar_produto_valido():
    produto = Produto(1, "Notebook", 3500.00)

    assert produto.codigo == 1
    assert produto.nome == "Notebook"
    assert produto.preco == 3500.00


def test_nao_deve_criar_produto_com_codigo_invalido():
    with pytest.raises(ValueError, match="codigo"):
        Produto(0, "Notebook", 3500.00)


def test_nao_deve_criar_produto_com_nome_vazio():
    with pytest.raises(ValueError, match="nome"):
        Produto(1, "   ", 3500.00)


def test_nao_deve_criar_produto_com_preco_invalido():
    with pytest.raises(ValueError, match="preco"):
        Produto(1, "Notebook", 0)
