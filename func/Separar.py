from func.Dados import Dados


class Separar:
    def Verificar_Lista(minhaLista):

        print("Dentro da função", minhaLista)

        if minhaLista[0] == "=d":
            try:
                print("Condicional 1 :", minhaLista)
                segundaLista = Dados.Jogar(minhaLista[1:5])
                print("Retornando Segunda lista")
                return segundaLista

            except IndexError:

                print("Excessão :", minhaLista)
                segundaLista = Dados.Jogar(minhaLista[1:2])

                print("Retornando Segunda lista")
                return segundaLista
        else:
            print("____________________________________")
            print("Mensagem não referente ao Bot ou um Erro")
            pass
