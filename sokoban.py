
def crear_mapa():
    return [3, 4, 4, 0, 4, 4, 4, 3]


def mover_personaje(mapa, movimiento):
    nuevo_mapa = mapa.copy()
    posicion = nuevo_mapa.index(0)

# Comentario random

    movimientos = {
        "a": 1,
        "d": 1
    }

    if movimiento not in movimientos:
        return nuevo_mapa

    nueva_posicion = posicion + movimientos[movimiento]

    # No permitir atravesar paredes
    if nuevo_mapa[nueva_posicion] == 3:
        return nuevo_mapa

    # Mover al personaje
    nuevo_mapa[posicion] = 4
    nuevo_mapa[nueva_posicion] = 0

    return nuevo_mapa


if __name__ == "__main__":
    print("Welcome to the Sokoban Game")
    player = input("Please, enter your player name: ")

    mapa = crear_mapa()
    print(mapa)

    movimientos = input(
        f"Presiona 'a' o 'd' para mover a {player}: "
    )

    mapa = mover_personaje(mapa, movimientos)

    print(mapa)
