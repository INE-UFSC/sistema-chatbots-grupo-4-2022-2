
from SistemaChatBot import SistemaChatBot as scb

#encoding: utf-8
from Bots.G4.BotFeliz import BotFeliz
from Bots.G4.BotTriste import BotTriste
from Bots.G4.BotZangado import BotZangado

# Bots Grupo 7
from Bots.G7.bg7feliz import BotFeliz as bg7feliz
from Bots.G7.bg7triste import BotTriste as bg7triste
from Bots.G7.bg7zangado import BotZangado as bg7zangado

# Bots Grupo 3
from Bots.G3.bg3feliz import BotFeliz as bg3feliz
from Bots.G3.bg3triste import BotTriste as bg3triste
from Bots.G3.bg3zangado import BotZangado as bg3zangado

# Bots Grupo 1
from Bots.G1.bg1zangado import BotZangado as bg1zangado
from Bots.G1.bg1inteligente import BotInteligente as bg1inteligente

###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("AHVG"), BotFeliz("Arnold Schwarzenegger"), BotTriste("Julius Caesar Tertius"),
              bg7feliz("G7Feliz"), bg7triste("G7Triste"), bg7zangado("G7Zangado"),
              bg3feliz("G3Feliz"), bg3triste("G3Triste"), bg3zangado("G3Zangado"),
              bg1zangado("G1Zangado"), bg1inteligente("G1Inteligente")]

sys = scb.SistemaChatBot("EMPRESA DO GRUPO 4",lista_bots)
sys.inicio()
