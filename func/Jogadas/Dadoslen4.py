import random


class Dadoslen4:

    """Dados com operações aritméticas.
        Dado no qual é realizado operações aritméticas como soma, subtração
    Multiplicação e divisão caso necessário.

        Método:
        Jogar(valores): Realiza a operação aleatória, Retornando uma lista com
    todos os valores que foram usados nas operações e a soma dos mesmos.
    """

    def Jogar(valores):

        listaRetorno = []
        print("Valores na função : ", valores)
        if len(valores) == 4:
            for x in range(int(valores[0])):

                numeroDado = random.randint(1, int(valores[1]))
                listaRetorno.append(numeroDado)

            listaSomada = sum(listaRetorno)
            listaRetorno.append(int(valores[3]))

            # Realiza a conta das strings: Método eval()
            soma = eval(str(listaSomada) + valores[2] + valores[3])

            listaRetorno.append(soma)

            print("Retornando valores: ", listaRetorno)

            return listaRetorno
