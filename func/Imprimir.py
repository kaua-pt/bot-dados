import discord
import os
from func.Formatar import Formatar


class Imprimir:

    """Classe Imprimir.

        Classe responsável pela impressão de resultados
    no Chat do canal do Discord.
        Métodos:

        chat(message,valores) : Realiza a impressão dos dados
    recebidos, o parâmetro "message" serve para a identificação
    do canal e do expeditor da mensagem, já o parâmetro "valores"
    são os valores a serem impressos em forma de lista ou String.
    """

    async def chat(message, valores):

        print("Dentro da função assincrona")

        # Caso seja uma string, teremos que o usuário quer a função moeda
        if type(valores) == str:
            await message.channel.send(
                f"{message.author.mention}{os.linesep}Você: {valores}"
            )

        # caso seja uma lista, teremos os 2 casos abaixo
        elif len(valores) == 2:

            combinacao = "  ".join(Formatar.formatar(valores))
            await message.channel.send(
                f"{message.author.mention}{os.linesep}Resultado: {valores[0]}"
            )

        else:

            combinacao = "  ".join(Formatar.formatar(valores))
            await message.channel.send(
                f"{message.author.mention}{os.linesep}Resultado: {valores[-1]} {os.linesep}Combinação: {combinacao[:-2]}"
            )

        print("____________________________________")
