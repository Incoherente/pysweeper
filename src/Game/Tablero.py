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

        len_x = len(self.s_tablero)
        len_y = len(self.s_tablero[0])
        for i in range(len_x):
            if i == 0:
                print("", end="   ")
                for k in range(len_y):
                    print(k, end=" ")
                print()
                if i < 10:
                    print("", end="   ")
                elif i >= 10:
                    print("", end="    ")
                for k in range(len_y):
                    print("_", end=" ")
                print()
            if i < 10:
                print(i, end=" | ")
            elif i >= 10:
                print(i, end="| ")
            for j in range(len_y):
                if self.v_tablero[i][j] == 1:
                    print(self.s_tablero[i][j], end=" ")
                else:
                    print("?", end=" ")
            print()

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
            num_minas = int(len_x + len_y * 2)
        return num_minas

    def colocar_minas(self, num_minas):
        len_x = len(self.s_tablero)
        len_y = len(self.s_tablero[0])
        while num_minas > 0:
            for i in range(len_x):
                for j in range(len_y):
                    if num_minas > 0 and self.s_tablero[i][j] == 0:
                        if random.randint(0, 100) > 80:
                            self.s_tablero[i][j] = chr(77)
                            num_minas -= 1

    def coloca_numeros(self):
        len_x = len(self.s_tablero)
        len_y = len(self.s_tablero[0])
        for i in range(len_x):
            for j in range(len_y):
               # print(str(i)+" "+str(j))
                total = 0
                if self.s_tablero[i][j] != chr(77):
                    if i == 0:
                        if j == 0:    # ESQUINA SUPERIOR IZQUIERDA
                            total += self.comprueba_esi(i, j)
                        elif j > 0 and j < len_y - 1:  # BORDE SUPERIOR
                            total += self.comprueba_bs(i, j)
                        elif j == len_y - 1:   # ESQUINA SUPERIOR DERECHA
                            total += self.comprueba_esd(i, j)
                    elif i < len_x - 1:
                        if j == 0:              # BORDE IZQUIERDO
                            total += self.comprueba_bi(i, j)
                        elif j > 0 and j < len_y - 1:       # CENTRO
                            total += self.comprueba_centro(i, j)
                        elif j == len_y -1:        #BORDE DERECHO
                            total += self.comprueba_bd(i, j)
                    elif i == len_x - 1:
                        if j == 0:  # ESQUINA INFERIOR IZQUIERDA
                            total += self.comprueba_eii(i, j)
                        elif j > 0 and j < len_y - 1:  # BORDE INFERIOR
                            total += self.comprueba_bin(i, j)
                        elif j == len_y - 1 :  # ESQUINA INFERIOR DERECHA
                            total += self.comprueba_eid(i, j)
                    self.s_tablero[i][j] = total



    # Compureba la [E]squina [S]Superior [I]Izquierda
    def comprueba_esi(self, i, j):
        total = 0
        if self.s_tablero[i][j + 1] == chr(77):
            total += 1
        if self.s_tablero[i + 1][j + 1] == chr(77):
            total += 1
        if self.s_tablero[i + 1][j - 1] == chr(77):
            total += 1
        return total

    # Comprueba Esquina Inferior Izquierda
    def comprueba_eii(self, i, j):
        total = 0
        if self.s_tablero[i - 1][j] == chr(77):
            total += 1
        if self.s_tablero[i-1][j+1] == chr(77):
            total += 1
        if self.s_tablero[i][j + 1] == chr(77):
            total += 1
        return total

    # Comprueba Esquina Superior Derecha
    def comprueba_esd(self, i, j):
        total = 0
        if self.s_tablero[i][j - 1] == chr(77):
            total += 1
        if self.s_tablero[i + 1][j-1] == chr(77):
            total += 1
        if self.s_tablero[i + 1][j] == chr(77):
            total += 1
        return total

    # Comprueba Esquina Inferior Derecha
    def comprueba_eid(self, i, j):
        total = 0
        if self.s_tablero[i][j - 1] == chr(77):
            total += 1
        if self.s_tablero[i - 1][j - 1] == chr(77):
            total += 1
        if self.s_tablero[i - 1][j] == chr(77):
            total += 1
        return total

    # Comprueba Borde Izquierdo
    def comprueba_bi(self, i, j):
        total = 0
        if self.s_tablero[i-1][j] == chr(77):
            total += 1
        if self.s_tablero[i-1][j+1] == chr(77):
            total += 1
        if self.s_tablero[i][j+1] == chr(77):
            total += 1
        if self.s_tablero[i+1][j+1] == chr(77):
            total += 1
        if self.s_tablero[i+1][j] == chr(77):
            total += 1
        return total

    # Comprueba Borde Derecho
    def comprueba_bd(self, i, j):
        total = 0
        if self.s_tablero[i - 1][j] == chr(77):
            total += 1
        if self.s_tablero[i - 1][j - 1] == chr(77):
            total += 1
        if self.s_tablero[i][j - 1] == chr(77):
            total += 1
        if self.s_tablero[i + 1][j - 1] == chr(77):
            total += 1
        if self.s_tablero[i + 1][j] == chr(77):
            total += 1
        return total

    # Comprueba Borde Superior
    def comprueba_bs(self, i, j):
        total = 0
        if self.s_tablero[i][j-1] == chr(77):
            total += 1
        if self.s_tablero[i + 1][j - 1] == chr(77):
            total += 1
        if self.s_tablero[i + 1][j] == chr(77):
            total += 1
        if self.s_tablero[i + 1][j + 1] == chr(77):
            total += 1
        if self.s_tablero[i][j+1] == chr(77):
            total += 1
        return total

    # Comprueba Borde Inferior
    def comprueba_bin(self, i, j):
        total = 0
        if self.s_tablero[i][j-1] == chr(77):
            total += 1
        if self.s_tablero[i - 1][j - 1] == chr(77):
            total += 1
        if self.s_tablero[i - 1][j] == chr(77):
            total += 1
        if self.s_tablero[i - 1][j + 1] == chr(77):
            total += 1
        if self.s_tablero[i][j+1] == chr(77):
            total += 1
        return total

    def comprueba_centro(self, i, j):
        total = 0
        if self.s_tablero[i][j-1] == chr(77):
            total += 1
        if self.s_tablero[i - 1][j - 1] == chr(77):
            total += 1
        if self.s_tablero[i - 1][j] == chr(77):
            total += 1
        if self.s_tablero[i - 1][j + 1] == chr(77):
            total += 1
        if self.s_tablero[i][j+1] == chr(77):
            total += 1
        if self.s_tablero[i + 1][j+1] == chr(77):
            total += 1
        if self.s_tablero[i + 1][j] == chr(77):
            total += 1
        if self.s_tablero[i + 1][j - 1] == chr(77):
            total += 1
        return total

    def comprueba_ganada(self):
        len_x = len(self.s_tablero)
        len_y = len(self.s_tablero[0])
        ganada = True

        for i in range(len_x):
            for j in range(len_y):
                if self.v_tablero[i][j] == 0:
                    if self.s_tablero[i][j] != chr(77):
                        ganada = False
        return ganada

