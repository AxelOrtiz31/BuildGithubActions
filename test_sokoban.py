
import pytest
from sokoban import crear_mapa, mover_personaje


# PRUEBA 1: Verificar la creación del mapa
def test_crear_mapa():
    mapa = crear_mapa()

    assert mapa == [3, 4, 4, 0, 4, 4, 4, 3]


# PRUEBA 2: Movimiento hacia la izquierda
def test_mover_izquierda():
    mapa = crear_mapa()

    nuevo_mapa = mover_personaje(mapa, "a")

    assert nuevo_mapa == [3, 4, 0, 4, 4, 4, 4, 3]


# PRUEBA 3: Movimiento hacia la derecha
def test_mover_derecha():
    mapa = crear_mapa()

    nuevo_mapa = mover_personaje(mapa, "d")

    assert nuevo_mapa == [3, 4, 4, 4, 0, 4, 4, 3]


# PRUEBA 4: Movimiento inválido
def test_movimiento_invalido():
    mapa = crear_mapa()

    nuevo_mapa = mover_personaje(mapa, "x")

    assert nuevo_mapa == mapa


# PRUEBA 5: No atravesar la pared izquierda
def test_no_atraviesa_pared_izquierda():
    mapa = [3, 0, 4, 4, 4, 4, 4, 3]

    nuevo_mapa = mover_personaje(mapa, "a")

    assert nuevo_mapa == mapa


# PRUEBA 6: No atravesar la pared derecha
def test_no_atraviesa_pared_derecha():
    mapa = [3, 4, 4, 4, 4, 4, 0, 3]

    nuevo_mapa = mover_personaje(mapa, "d")

    assert nuevo_mapa == mapa


# PRUEBA 7: El mapa original no debe modificarse
def test_mapa_original_no_se_modifica():
    mapa = crear_mapa()
    copia_original = mapa.copy()

    mover_personaje(mapa, "a")

    assert mapa == copia_original


