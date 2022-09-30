from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self,nome):
        super().__init__(nome,
                         comandos={"Bom dia": "Vai se lascar, você me acordou!",
                                   "Qual é o seu nome?": f"Não sabe ler? {nome}, seu analfabeto.",
                                   "Conselho": ["Conselho? Me pague.",
                                                "Digite -1 para ver um comando legal.",
                                                "Nada vem de graça, nem o pão, nem a cachaça, e nem o conselho.",
                                                "Beba corote na promoção."],
                                   "Adeus": "Já vai tarde."})

 
    def apresentacao(self):
        return f"Quê? Conversar? Mas eu estava dormindo! Nome? {self.nome}"

    def boas_vindas(self):
        return "Diabo de conversa o quê, me deixa em paz."

    def despedida(self):
        return "Aleluia! Vou voltar a dormir."