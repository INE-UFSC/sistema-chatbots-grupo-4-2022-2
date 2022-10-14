##implemente as seguintes classes

from abc import ABC, abstractmethod
from Comando import Comando

class Bot(ABC):

    def __init__(self,nome: str, comandos: list[Comando]):
        self.__nome = nome
        self.__comandos = comandos

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,nome):
        self.__nome = nome

    @property
    def comandos(self):
        return self.__comandos

    def mostra_comandos(self):
        comandos = ""
        for i, c in enumerate(self.comandos):
            comandos += f"{i} - {c.mensagem}"
        
        return comandos


    def executa_comando(self, cmd):
        try:
            print(f"{self.nome} diz: Você disse: {cmd}")
            return f"Eu te respondo: " + self.comandos.get_resposta_random()
        except ValueError as e:
            print(e)

    @abstractmethod
    def apresentacao(self):
        pass

    @abstractmethod
    def boas_vindas(self):
        pass
    
    @abstractmethod
    def despedida(self):
        pass
