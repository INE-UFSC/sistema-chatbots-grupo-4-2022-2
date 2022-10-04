from Bots.Bot import Bot

class BotFeliz(Bot):
    def __init__(self, nome):
        super().__init__(nome=nome,
                         comandos={"Bom dia": f"--> {nome} diz: Você disse 'Bom dia'\n--> Eu te respondo: 'Bom dia? Dia MA-RA-VI-LHO-SO!'",
                                   "Qual é o seu nome?": f"--> {nome} diz: Você disse 'Qual o seu nome?'\n--> Eu te respondo: 'Que bom que perguntou! Meu nome é {nome}!!!!'",
                                   "Conselho": f"--> {nome} diz: Você disse 'Quero um conselho'\n--> Eu te respondo: 'Se você quer encontrar a felicidade, encontre a gratidão!'",
                                   "Adeus": f"--> {nome} diz: Você disse 'Adeus'\n--> Eu te respondo: 'Até a proxima!'"})

    def apresentacao(self):
        return f"É um prazer conhece-lo! meu nome é {self.nome}"
    
    def executa_comando(self,cmd):
        return self.comandos.get(cmd, "Comando não encontrado")

    def boas_vindas(self):
        return f"--> {self.nome} diz: 'Esse é definitivamente o dia mais feliz da minha vida!!! :D'"

    def despedida(self):
        return f"--> {self.nome} diz: 'Adorei você! Sentirei saudades! :)'"