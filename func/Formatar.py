class Formatar:
    """Classe formatar.

        Apenas realiza operações com a lista afim
    de padroniza-la para fins estéticos no output.
    """

    def formatar(lista):
        listaFormatada = []

        for x in lista:
            listaFormatada.append(str(x))

        return listaFormatada
