from lista import *
from random import randint
from jogo import Jogo
from datetime import *

num_participantes = int(input("Quantas pessoas participarão da brincadeira? "))
num_vencedores = int(input("Quantas pessoas vão vencer o jogo? "))

assert num_participantes > 0
assert num_vencedores < num_participantes and num_vencedores>0

jogo = Jogo(num_participantes,num_vencedores)
jogo.players()
start = randint(1,num_participantes)
print(f"valor do start {start}")
jogo.definirPrimeiro(start-1)
jogo.iniciarJogo(start)
data = datetime.now()
dataformatada = (f'{data.day}-{data.month}-{data.hour}-{data.minute}')
arq = open(f'./vencedores/vencedores{dataformatada}.txt', 'a')
for i in range(len(jogo)):
    jogador = jogo.mostrarJogador(i)
    arq.write(jogador)
