from Bots.Bot import Bot

class SistemaChatBot:
    def __init__(self,nomeEmpresa,lista_bots=[]):
        self.__empresa = nomeEmpresa
        ##verificar se a lista de bots contém apenas bots
        self.__lista_bots = list()
        for b in lista_bots:
            if isinstance(b,Bot):
                self.__lista_bots.append(b)
        self.__bot = None
        self.__running = True
    
    def boas_vindas(self):
        print(f"""Olá, esse é o sistema de chatbots da empresa {self.__empresa}
        \n Os chat bots disponíveis no momento são: """)

    def mostra_menu(self):
        for i,b in enumerate(self.__lista_bots):
            print(f"{i} - Bot: {b.nome} - Mensagem de apresentação: {b.apresentacao()}")
    
    def escolhe_bot(self):
        escolhe_bot = int(input('Digite o número do chat bot desejado: '))
        while not (escolhe_bot in range(len(self.__lista_bots))):
            print('Não há esse bot')
            escolhe_bot = int(input('Digite o número do chat bot desejado: '))
        self.__bot = self.__lista_bots[escolhe_bot]
        print(self.__bot.boas_vindas())
        ##faz a entrada de dados do usuário e atribui o objeto ao atributo __bot 

    def mostra_comandos_bot(self):
        print(self.__bot.mostra_comandos())

    ##mostra os comandos disponíveis no bot escolhido

    def le_envia_comando(self):
        comando = int(input('Digite o comando desejado (ou -1 para fechar o programa/sair): '))
        if comando == -1:
            print(self.__bot.despedida())
            self.__running = False
            return 
            
        while not (comando in list(range(len(self.__bot.comandos)))):
            print('Não há esse comando')
            comando = int(input('Digite o comando desejado (ou -1 para fechar o programa/sair): '))
        
        for i,k in enumerate(self.__bot.comandos.keys()):
            if i == comando:
                cmd = k
        print(self.__bot.executa_comando(cmd))
        ##faz a entrada de dados do usuário e executa o comando no bot ativo

    def inicio(self):
        self.boas_vindas()
        self.mostra_menu()
        self.escolhe_bot()
        while self.__running:
            self.mostra_comandos_bot()
            self.le_envia_comando()
        ## mostra mensagem de boas-vindas do sistema
        ## mostra o menu ao usuário
        ## escolha do bot      
        ## mostra mensagens de boas-vindas do bot escolhido
        ## entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
        ## ao sair mostrar a mensagem de despedida do bot
