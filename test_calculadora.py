"""Pruebas unitarias de la calculadora."""

from calculadora import suma


def test_suma():
    """Comprueba que la suma de 2 y 3 sea 5."""
    assert suma(2, 3) == 5
