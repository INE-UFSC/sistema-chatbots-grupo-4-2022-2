from Bots.Bot import Bot
from Bots.comando import Comando

class BotFeliz(Bot):
    def __init__(self,nome):
        comandos={"Bom dia": "Que lindo dia para falar com uma pessoa legal!",
                                   "Qual é o seu nome?": f"Meu nome é {nome} e mal te conheci e já te amooo!",
                                   "Conselho": "Ajeite a postura.",
                                   "Adeus": "Auf wiedersehen! Até mais ver, sentirei saudades."}
                                   
        newcomandos = list()
        for i, c in enumerate(comandos.keys()):
            nc = Comando(i, c, comandos[c])
            newcomandos.append(nc)

        super().__init__(nome, newcomandos)
  
    def apresentacao(self):
        return f"Me chamo {self.nome}, prazer em conhecer você!"

    def boas_vindas(self):
        return "Ainda bem que você me escolheu!"

    def despedida(self):
        return "Ahhh que pena, queria conversar mais contigo. Ate a proxima!"
