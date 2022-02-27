import discord
from func.Separar import Separar


class MyClient(discord.Client):
    async def on_ready(self):
        print("Nome do bot: {0}!".format(self.user))

    async def on_message(self, message):
        print("{0.author}: {0.content}".format(message))

        mensagem = message.content.split(" ")

        valores = Separar.Verificar_Lista(mensagem, mensagem)

        await message.channel.send(f"{valores}")


client = MyClient()
client.run("OTQ3MjQ0MjUwNDAyMjg3Njg2.Yhqb9A.Nn6G9VUlPnLmdgSNatau2S1Rjnw")
