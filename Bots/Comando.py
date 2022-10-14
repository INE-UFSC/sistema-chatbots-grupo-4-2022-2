
from random import Random


class Comando:

    def __init__(self, id: int, mensagem: str, respostas: list[str]) -> None:
        self.__id = id
        self.__mensagem = mensagem
        self.__respostas = respostas

    @property 
    def id(self) -> int:
        return self.__id
    
    @id.setter
    def id(self, id: int) -> None:
        self.__id = id

    @property
    def mensagem(self) -> str:
        return self.__mensagem
    
    @mensagem.setter
    def mensagem(self, mensagem: str) -> None:
        self.__mensagem = mensagem
    
    @property
    def respostas(self) -> list[str]:
        return self.__respostas
    
    @respostas.setter
    def respostas(self, respostas) -> None:
        self.__respostas = respostas

    def get_resposta_random(self) -> str:
        
        r = Random.randint(0, len(self.respostas))
        return self.respostas[r];
