from Bots.Bot import Bot
from Bots.comando import Comando

class BotZangado(Bot):
    def __init__(self,nome):
        comandos={"Bom dia": "Vai se lascar, você me acordou!",
                                   "Qual é o seu nome?": f"Não sabe ler? {nome}, seu analfabeto.",
                                   "Conselho": "Conselho? Me pague.",
                                   "Adeus": "Já vai tarde."}
        newcomandos = list()
        for i, c in enumerate(comandos.keys()):
            nc = Comando(i, c, comandos[c])
            newcomandos.append(nc)
        super().__init__(nome, newcomandos)

 
    def apresentacao(self):
        return f"Quê? Conversar? Mas eu estava dormindo! Nome? {self.nome}"

    def boas_vindas(self):
        return "Diabo de conversa o quê, me deixa em paz."

    def despedida(self):
        return "Aleluia! Vou voltar a dormir."
