import random


class DadosMaiores:
    """Soma de dados.
        É realizado a soma de dados após a operação randomica.

        Método:
        SomarDados(valores) : Realiza a operação aleatória, Retornando uma lista com
    todos os valores que foram usados nas operações e a soma dos dados.
    """

    def SomarDados(valores):

        listaRetorno1 = []

        print("Valores dentro da função: ", valores)

        for y in range(len(valores)):
            # caso o número seja divisível por 3, ele irá ser identificado como número de dados
            if y % 3 == 0:
                for x in range(int(valores[y])):
                    listaRetorno1.append(random.randint(1, int(valores[y + 1])))

        soma = sum(listaRetorno1)
        listaRetorno1.append(soma)

        print("Lista retornando", listaRetorno1)

        return listaRetorno1
