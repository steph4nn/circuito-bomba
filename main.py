from lista import *
from random import randint
from jogo import Jogo

num_participantes = int(input("Quantas pessoas participarão da brincadeira? "))
num_vencedores = int(input("Quantas pessoas vão vencer o jogo? "))

assert num_participantes > 0
assert num_vencedores < num_participantes and num_vencedores>0

jogo = Jogo(num_participantes,num_vencedores)
jogo.players()
start = randint(1,num_participantes)
print(f"valor do start {start}")
jogo.definirPrimeiro(start-1)

rodada = 1
music = randint(4,15)
print()
while num_vencedores < len(jogo):
    print("--------------------COMEÇO DO ROUND------------------")
    print(f"participantes: {jogo}")
    print(f"Rodada: {rodada}")
    print(f"Start: {jogo.mostrarJogador(start-1)} K={music}")
    jogo.passarJogador(music)
    eliminado =jogo.selecionarJogador(start,music)
    start = eliminado
    print(f"Jogador eliminado: {jogo.eliminarJogador(eliminado)}")
    print("--------------------FIM DO ROUND------------------")
    print()
print()
print(f"Vencedor: {jogo}")

