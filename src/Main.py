import Game.Tablero as gt

class Main:

    def __init__(self):
        self.partida_ganada = False
        self.partida_perdida = False

if __name__ == '__main__':

    print('hola hola')
    print("hola2")

    tablero = gt.Tablero(10, 10, 2)
    tablero.colocar_minas(tablero.num_minas)
    tablero.print_s_tablero()

    tablero.set_tablero_visible()

    tablero.print_v_tablero()

    print(tablero.num_minas)

"""
    a = array([['Roy', 80, 75, 85, 90, 95],
               ['John', 75, 80, 75, 85, 100],
               ['Dave', 80, 80, 80, 90, 95]])
    a = delete(a, [1], 0)
    print(a)
"""

#print("Partida ganada {}.".format(True))




