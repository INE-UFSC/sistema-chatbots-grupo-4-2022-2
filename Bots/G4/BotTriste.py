from Bots.Bot import Bot

class BotTriste(Bot):
    def __init__(self,nome):
        super().__init__(nome=nome,
                         comandos={"Bom dia": "Oi.",
                                   "Qual é o seu nome?": f"Ah, é {nome}.",
                                   "Conselho": "Nada está tão ruim que não possa piorar.",
                                   "Adeus": "Não se vá..."})

    def apresentacao(self):
        return f"Me chamo {self.nome}."

    def boas_vindas(self):
        return "Qual o motivo para comemorar uma vinda?"

    def despedida(self):
        return "Sozinho denovo..."
