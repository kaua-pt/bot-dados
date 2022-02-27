import discord
import os
from func.Separar import Separar
from func.Formatar import Formatar


class MyClient(discord.Client):
    async def on_ready(self):
        print("Nome do bot: {0}!".format(self.user))

    async def on_message(self, message):
        try:
            print("{0.author}: {0.content}".format(message))

            mensagem = message.content.split(" ")

            valores = Separar.Verificar_Lista(mensagem)
            print("Valores principais: ", valores)

            if type(valores) == str:
                await message.channel.send(
                    f"{message.author.mention}{os.linesep}Você: {valores}"
                )

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

        except AttributeError:
            pass
        except TypeError:
            pass


client = MyClient()
client.run("OTQ3MjQ0MjUwNDAyMjg3Njg2.Yhqb9A.Nn6G9VUlPnLmdgSNatau2S1Rjnw")
