import numpy;
import random

# La clase Tablero es el tablero del buscaminas:
# Se compone de la siguiente información:
# dimension_x: Dimension en casillas horizontales del tablero
# dimension_y: Dimension en casillas verticales del tablero

#  El board constará de una matriz de enteros: cada entero representa la siguiente casilla:
#  0 : casilla sin mina y con 0 minas a su alrededor.
#  1 : casilla sin mina y con 1 mina a su alrededor.
#  ...
#  8 : casilla sin mina y con 8 minas a su alrededor.
#  M : casilla con mina
#  []: casilla sin descubrir

# El visual_tablero (v_tablero)es el tablero que se muestra por pantalla y con el que interacciona el usuario.
# El v_tablero tiene los siguientes valores
# 0 : casilla sin descubir
# 1 : casilla descubierta
# En función de este estado, se visualizarán o no los valores del tablero en el v_tablero

# Se establece la dificultad del juego con los posibles valores en función del tamaño del tablero:
# 1: Fácil: Número de minas (X + Y)
# 2: Intermedio: Número de minas (X + Y*2)
# 3: Difícil: (X + Y*3)

class Tablero:
    # constructor del tablero. Se construye a partir de dos dimensiones dadas por parámetro.

    def __init__(self, dimension_x, dimension_y, dificultad):

        self.s_tablero = [0]*dimension_x            # Declaro un [0] y lo "multiplico" x veces
        for i in range(dimension_x):                # Por cada una de esas X veces
            self.s_tablero[i] = [0] * dimension_y   # Cada [0] se convierte en [[0]*y]

        self.v_tablero = [0]*dimension_x
        for i in range(dimension_x):
            self.v_tablero[i] = [0] * dimension_y        # numpy.zeros(dimension_x, dimension_y) INCORRECTO

        self.dificultad = dificultad

        # Se inicializa el número de minas en función de la dificultad
        self.num_minas = self.calcular_minas()

    def print_s_tablero(self):
        print('SOURCE_TABLERO')
        len_x = len(self.s_tablero)
#        len_y = len(self.s_tablero[0])
        for i in range(len_x):
            print(self.s_tablero[i])
        #       for index_y in self.dimension_y:
        #           print '|', self.board[index_x][index_y]

    def print_v_tablero(self):
        print('VISUAL TABLERO')
        len_x = len(self.v_tablero)
        for i in range(len_x):
            print(self.v_tablero[i])

    def set_tablero_visible(self):
        len_x = len(self.s_tablero)
        len_y = len(self.s_tablero[0])
        for i in range(len_x):
            for j in range(len_y):
                self.v_tablero[i][j] = 1
    """
    Se calcula el número de minas en función de la dificultad establecida
    """
    def calcular_minas(self):
        len_x = len(self.s_tablero)
        len_y = len(self.s_tablero[0])

        # El número de minas es la media de las dos dimensiones.
        # Si el tablero fuera cuadrado
        if self.dificultad == 1:
            num_minas = int(len_x + len_y)
        elif self.dificultad == 2:
            num_minas = int(len_x + len_y * 2)
        elif self.dificultad == 3:
            num_minas = int(len_x + len_y * 3)
        else:
            print("Error al seleccionar la dificultad"
                  "Se establece dificultad intermedia")
            self.dificultad == 2
            num_minas = int(len_x + len_y * 2)
        return num_minas

    def colocar_minas (self, num_minas):
        len_x = len(self.s_tablero)
        len_y = len(self.s_tablero[0])
        while num_minas > 0:
            for i in range(len_x):
                for j in range(len_y):
                    if num_minas > 0 and self.s_tablero[i][j] == 0:
                        if random.randint(0, 100) > 80:
                            self.s_tablero[i][j] = 'M'
                            num_minas -= 1






