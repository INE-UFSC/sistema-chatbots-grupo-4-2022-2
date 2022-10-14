from Bots.Bot import Bot
from Bots.comando import Comando

class BotTriste(Bot):
    def __init__(self,nome):
        comandos={"Bom dia": "Oi.",
                                   "Qual é o seu nome?": f"Ah, é {nome}.",
                                   "Conselho": "Nada está tão ruim que não possa piorar.",
                                   "Adeus": "Não se vá..."}
        newcomandos = list()
        for i, c in enumerate(comandos.keys()):
            nc = Comando(i, c, comandos[c])
            newcomandos.append(nc)
        super().__init__(nome, newcomandos)

    def apresentacao(self):
        return f"Me chamo {self.nome}."

    def boas_vindas(self):
        return "Qual o motivo para comemorar uma vinda?"

    def despedida(self):
        return "Sozinho denovo..."
