import Game.Tablero as gt


class Main:

    def __init__(self):
        self.partida_ganada = False


if __name__ == '__main__':

    tablero = gt.Tablero(10, 10, 2)
    tablero.colocar_minas(tablero.num_minas)
    tablero.coloca_numeros()
    turno = 0
    print("========================================")
    print("======== BIENVENIDO A PYSWEEPER ========")
    print("========================================")

    while True:

        print("Turno ", turno)
        str_x, str_y = input("Inserte la altura y anchura de la casilla "
                             "a descubrir separada por comas\n").split(',')
        posicion_x = int(str_x)
        posicion_y = int(str_y)
        tablero.v_tablero[posicion_x][posicion_y] = 1
        if tablero.s_tablero[posicion_x][posicion_y] == chr(77):
            print("Has pisado una mina en la posición ", posicion_x, ", ", posicion_y, " :,( ")
            tablero.set_tablero_visible()
            tablero.print_s_tablero()
            break

        if tablero.comprueba_ganada():
            print("HAS GANADO!!!!!  :D")
            tablero.set_tablero_visible()
            tablero.print_s_tablero()
            break

        tablero.print_s_tablero()
        turno += 1




