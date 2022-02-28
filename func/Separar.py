from func.Jogadas.Dadoslen2 import Dadoslen2
from func.Jogadas.Dadoslen4 import Dadoslen4
from func.Jogadas.Moeda import Moeda


class Separar:
    def Verificar_Lista(minhaLista):

        print("Dentro da função", minhaLista)

        if minhaLista[0] == "=d":
            if minhaLista[1] == "m":
                print("Indo para a moeda")
                resultado = Moeda.moeda()
                return resultado

            else:
                if len(minhaLista) > 3:
                    print("Condicional 1 :", minhaLista)
                    segundaLista = Dadoslen4.Jogar(minhaLista[1:5])
                    print("Lista retornada: ", segundaLista)
                    print("Retornando Segunda lista")
                    return segundaLista

                else:
                    print("Excessão :", minhaLista)
                    segundaLista = Dadoslen2.Jogar(minhaLista[1:3])

                    print("Retornando Segunda lista")
                    return segundaLista

        else:
            print("____________________________________")
            print("Mensagem não referente ao Bot ou um Erro")
            pass
