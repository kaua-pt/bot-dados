from func.Dados import Dados


class Separar:
    def Verificar_Lista(self, minhaLista):

        print("Dentro da função")
        print(minhaLista)

        if minhaLista[0] == "=d":
            try:
                segundaLista = Dados.Jogar(minhaLista[1:4], minhaLista[1:4])
                print("Retornando Segunda lista")
                return segundaLista

            except IndexError:
                segundaLista = Dados.Jogar(minhaLista[1:2], minhaLista[1:4])

                print("Retornando Segunda lista")
                return segundaLista
