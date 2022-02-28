import discord
import os
from func.Separar import Separar
import func.Imprimir as imp


class MyClient(discord.Client):
    """Classe inicial do Bot.

    Classe a qual realiza o inicio do bot, tal como
    indicar se ele está ativo no servidor e realizar
    algo caso alguma mensagem seja enviada no servidor.

    Metodos definidos:

    on_ready(self): Manda uma mensagem no terminal quando
    o Bot fica ativo no servidor.

    on_message(self, message): Realiza alguma ação ao ser enviado
    qualquer mensagem no servidor. Caso a mensagem seja coerente com
    os padrões, do bot, ele irá marcar a pessoa com a resposta.
        Para isso, podemos definir os seguintes comandos:

        1- =d X Y a Z -> Chama o bot de dados, com "X" sendo um real
    que indica o número de dados que serão jogados, "Y" o número máximo
    que o dado pode chegar, "a" sendo uma operação matemática de soma ou
    subtração caso necessário, e "Z" o número que será asssociado aos números
    aleatórios juntamente com "a". O output será:

       "
        @Caller
        "Resultado = "Somatório dos dados
        "Combinação = "Elementos
       "
    Exceto em caso de dado único, neste caso teremos:
       "
        @Caller
        "Resultado = "Número do dado.
       "
        2- =d m -> Decide se alguma pessoa morre ou vive. Teremos o output:
       "
        @Caller
        "Você : "Resultado
       "
    """

    async def on_ready(self):
        print("Nome do bot: {0}!".format(self.user))

    async def on_message(self, message):
        try:
            print("{0.author}: {0.content}".format(message))

            # Dividir a mensagem recebida, afim de facilitar o processamento da mesma
            mensagem = message.content.split(" ")

            # Imprime a mensagem
            await imp.Imprimir.chat(message, Separar.Verificar_Lista(mensagem))

        except AttributeError:
            pass
        except TypeError:
            pass


client = MyClient()
client.run("OTQ3MjQ0MjUwNDAyMjg3Njg2.Yhqb9A.Nn6G9VUlPnLmdgSNatau2S1Rjnw")
