import random


class Moeda:
    """Moeda.
        Classe na qual apenas deve ser chamada
    para escolher um valor entre 0 e 1 e converte-la
    em string.

        Retorno: String "Vive" ou String "Morre"
    """

    def moeda():
        valor = random.randint(0, 1)
        print("Temos o valor ", valor)

        if valor == 0:
            return "Vive"
        else:
            return "Morre"
