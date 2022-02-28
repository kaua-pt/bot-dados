import random


class Dadoslen2:

    """Dados sem operações aritméticas.
        É jogado um dado puro pela função random.

        Método:
        Jogar(valores): Realiza a operação aleatória, Retornando uma lista com
    todos os valores que foram usados e a soma dos mesmos.
    """

    def Jogar(valores):

        print("Função dado :", valores)

        listaRetorno = []

        if len(valores) == 2:
            for x in range(int(valores[0])):

                numeroDado = random.randint(1, int(valores[1]))
                listaRetorno.append(numeroDado)

            print("Retornando valores: ", listaRetorno)
            soma = sum(listaRetorno)

            if valores[0] != 1:
                listaRetorno.append(soma)
            return listaRetorno
