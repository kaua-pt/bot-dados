from func.Jogadas.Dadoslen2 import Dadoslen2
from func.Jogadas.Dadoslen4 import Dadoslen4
from func.Jogadas.Moeda import Moeda


class Separar:
    """A Classe Separar.
        Realiza a filtração das mensagens, caso ela seja compatível com o
    input estipulado nas regras do bot.

        Métodos:
        Verificar_lista(minhaLista): Recebe uma lista e após a chamada de
    outro método, retorna um valor.
    """

    def Verificar_Lista(minhaLista):

        print("Dentro da função", minhaLista)

        # Verifica se é uma chamada de bot
        if minhaLista[0] == "=d":

            # Moeda
            if minhaLista[1] == "m":
                print("Indo para a moeda")
                return Moeda.moeda()

            else:
                # Dado com operação
                if len(minhaLista) > 3:
                    print("Condicional 1 :", minhaLista)
                    print("Retornando Segunda lista")
                    return Dadoslen4.Jogar(minhaLista[1:5])

                # Dado sem operação
                else:
                    print("Excessão :", minhaLista)
                    print("Retornando Segunda lista")
                    return Dadoslen2.Jogar(minhaLista[1:3])

        else:
            print("____________________________________")
            print("Mensagem não referente ao Bot ou um Erro")
            pass
