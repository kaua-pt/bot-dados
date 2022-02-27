import random


class Dados:
    def Jogar(self, valores):

        print(valores)
        listaRetorno = []

        if len(valores) == 2:
            for x in range(int(valores[0])):
                numeroDado = random.randint(1, int(valores[1]))
                listaRetorno.append(numeroDado)

            print("Retornando valores: ", listaRetorno)
            return listaRetorno

        if len(valores) == 4:
            for x in range(int(valores[0])):
                numeroDado = random.randint(1, int(valores[1]))
                listaRetorno.append(numeroDado)

            listaSomada = sum(listaRetorno)
            soma = eval(listaSomada + valores[3:4])
            listaRetorno.append(soma)

            print("Retornando valores: ", listaRetorno)

            return listaRetorno
