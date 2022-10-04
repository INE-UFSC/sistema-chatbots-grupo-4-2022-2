##implemente as seguintes classes

from abc import ABC, abstractmethod

class Bot(ABC):

    def __init__(self,nome: str,comandos: dict):
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
        return self.__comandos.copy()

    def mostra_comandos(self):
        comandos = ""
        for i,k in enumerate(self.comandos.keys()):
            comandos += f"{i} - {k}\n"
        return comandos

    def executa_comando(self,cmd):
        try:
            print(f"{self.nome} diz: Você disse: {cmd}")
            return f"Eu te respondo: " + self.__comandos[cmd]
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
