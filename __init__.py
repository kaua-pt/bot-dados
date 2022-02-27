import discord
from func.Separar import Separar


class MyClient(discord.Client):
    async def on_ready(self):
        print("Nome do bot: {0}!".format(self.user))

    async def on_message(self, message):
        try:
            print("{0.author}: {0.content}".format(message))

            mensagem = message.content.split(" ")

            valores = Separar.Verificar_Lista(mensagem)
            print("Valores principais: ", valores)
            combinacao = "".join(str(valores[:-1]))

            if len(valores) == 2:
                await message.channel.send(f"Você tirou um {valores[0]} no dado")

            else:
                await message.channel.send(
                    f"Você tirou um {valores[-1]} no dado com : {''.join(combinacao)}"
                )

            print("____________________________________")

        except AttributeError:
            pass


client = MyClient()
client.run("OTQ3MjQ0MjUwNDAyMjg3Njg2.Yhqb9A.Nn6G9VUlPnLmdgSNatau2S1Rjnw")
