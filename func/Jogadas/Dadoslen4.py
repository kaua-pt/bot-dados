import random


class Dadoslen4:
    def Jogar(valores):

        listaRetorno = []
        print("Valores na função : ", valores)
        if len(valores) == 4:
            for x in range(int(valores[0])):

                numeroDado = random.randint(1, int(valores[1]))
                listaRetorno.append(numeroDado)

            listaSomada = sum(listaRetorno)
            listaRetorno.append(int(valores[3]))

            soma = eval(str(listaSomada) + valores[2] + valores[3])

            listaRetorno.append(soma)

            print("Retornando valores: ", listaRetorno)

            return listaRetorno
