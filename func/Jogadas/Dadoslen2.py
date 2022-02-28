import random


class Dadoslen2:
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
