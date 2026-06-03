import pytest

from app.calculadora import Calculadora


def test_deve_somar_dois_numeros():
    calc = Calculadora()
    assert calc.somar(2, 3) == 5


def test_deve_subtrair_dois_numeros():
    calc = Calculadora()
    assert calc.subtrair(10, 4) == 6


def test_deve_multiplicar_dois_numeros():
    calc = Calculadora()
    assert calc.multiplicar(3, 4) == 12


def test_deve_dividir_dois_numeros():
    calc = Calculadora()
    assert calc.dividir(10, 2) == 5


def test_deve_lancar_erro_ao_dividir_por_zero():
    calc = Calculadora()

    with pytest.raises(ValueError):
        calc.dividir(10, 0)
