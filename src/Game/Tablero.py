import numpy;

# La clase Tablero es el tablero del buscaminas:
# Se compone de la siguiente información:
# dimension_x: Dimension en casillas horizontales del tablero
# dimension_y: Dimension en casillas verticales del tablero

#  El board constará de una matriz de enteros: cada entero representa la siguiente casilla:
#  0 : casilla sin mina y con 0 minas a su alrededor.
#  1 : casilla sin mina y con 1 mina a su alrededor.
#  ...
#  8 : casilla sin mina y con 8 minas a su alrededor.
# -1 : casilla con mina

# El visual_tablero (v_tablero)es el tablero que se muestra por pantalla y con el que interacciona el usuario.
# El v_tablero tiene los siguientes valores
# 0 : casilla sin descubir
# 1 : casilla descubierta
# En función de este estado, se visualizarán o no los valores del tablero en el v_tablero

class Tablero:
    # constructor del tablero. Se construye a partir de dos dimensiones dadas por parámetro.

    def __init__(self, dimension_x, dimension_y):

        self.s_tablero = [0]*dimension_x            # Declaro un [0] y lo "multiplico" x veces
        for i in range(dimension_x):                # Por cada una de esas X veces
            self.s_tablero[i] = [0] * dimension_y   # Cada [0] se convierte en [[0]*y]

        self.v_tablero = [0]*dimension_x
        for i in range(dimension_x):
            self.v_tablero[i] = [0] * dimension_y        #numpy.zeros(dimension_x, dimension_y) // INCORRECTO

    def print_s_tablero(self):
        print('SOURCE_TABLERO')
        for index_x in range(len(self.s_tablero[0])):
            print(self.s_tablero[index_x])
        #       for index_y in self.dimension_y:
        #           print '|', self.board[index_x][index_y]

    def print_v_tablero(self):
        print('VISUAL TABLERO')
        for index_x in range(len(self.v_tablero[0])):
            print(self.v_tablero[index_x])

    def set_tablero_visible(self):
        for index_x in range (len(self.v_tablero[0])):
            for index_y in range(len(self.v_tablero[index_x])):
                self.v_tablero[index_x][index_y] = 1







