#encoding: utf-8
from Bots.BotFeliz import BotFeliz
from Bots.BotTriste import BotTriste
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado

###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("AHVG"), BotFeliz("Arnold Schwarzenegger"), BotTriste("Julius Caesar Tertius")]

sys = scb.SistemaChatBot("EMPRESA DO GURPO 4",lista_bots)
sys.inicio()
