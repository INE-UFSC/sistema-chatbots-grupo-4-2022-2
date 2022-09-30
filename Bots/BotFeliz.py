from Bots.Bot import Bot

class BotFeliz(Bot):
    def __init__(self,nome):
        super().__init__(nome,
                         comandos={"Bom dia": "Que lindo dia para falar com uma pessoa legal!",
                                   "Qual é o seu nome?": f"Meu nome é {nome} e mal te conheci e já te amooo!",
                                   "Conselho": ["Ajeite a postura.",
                                                "Ligue para a sua mãe.",
                                                "Diga saude quando alguem espirrar.",
                                                "Beba água."],
                                   "Adeus": "Auf wiedersehen! Até mais ver, sentirei saudades."})
  
    def apresentacao(self):
        return f"Me chamo {self.nome}, prazer em conhecer você!"

    def boas_vindas(self):
        return "Ainda bem que você me escolheu!"

    def despedida(self):
        return "Ahhh que pena, queria conversar mais contigo. Ate a proxima!"