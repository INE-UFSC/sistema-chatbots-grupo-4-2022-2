from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self,nome):
        comandos={"Bom dia": "Vai se lascar, você me acordou!",
                                   "Qual é o seu nome?": f"Não sabe ler? {nome}, seu analfabeto.",
                                   "Conselho": "Conselho? Me pague.",
                                   "Adeus": "Já vai tarde."}
        super().__init__(nome=nome, )

 
    def apresentacao(self):
        return f"Quê? Conversar? Mas eu estava dormindo! Nome? {self.nome}"

    def boas_vindas(self):
        return "Diabo de conversa o quê, me deixa em paz."

    def despedida(self):
        return "Aleluia! Vou voltar a dormir."
