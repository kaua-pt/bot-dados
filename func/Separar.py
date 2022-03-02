from func.Jogadas.Dadoslen2 import Dadoslen2
from func.Jogadas.Dadoslen4 import Dadoslen4
from func.Jogadas.Moeda import Moeda
from func.Jogadas.Somadados import DadosMaiores


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
                if len(minhaLista) == 5:
                    print("Condicional 1 :", minhaLista)
                    print("Retornando Segunda lista")
                    return Dadoslen4.Jogar(minhaLista[1:5])

                # Dado sem operação
                elif len(minhaLista) == 3:
                    print("Excessão :", minhaLista)
                    print("Retornando Segunda lista")
                    return Dadoslen2.Jogar(minhaLista[1:3])

                elif len(minhaLista) > 5:
                    print("Else :", minhaLista)
                    print("Indo para a soma de dados")
                    teste = DadosMaiores.SomarDados(minhaLista[1:])
                    print(teste)
                    return teste

        else:
            print("____________________________________")
            print("Mensagem não referente ao Bot ou um Erro")
            pass
