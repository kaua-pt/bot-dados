import random


class Moeda:
    def moeda():
        valor = random.randint(0, 1)
        print("Temos o valor ", valor)

        if valor == 0:
            return "Vive"
        else:
            return "Morre"
