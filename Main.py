class Main:

    def __init__(self):
        self.partida_ganada = False
        self.partida_perdida = False

if __name__ == '__main__':

    my_game = Main()
    print("Partida ganada {}.".format(my_game.partida_ganada))
    print("Partida perdida{}.".format(my_game.partida_perdida))
