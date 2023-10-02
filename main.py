from lista import *
from random import randint

num_participantes = int(input())
num_vencedores = int(input())

assert num_participantes > 0
assert num_vencedores < num_participantes and num_vencedores>0

posicao =1 
participantes = LinkedList()
for i in range(num_participantes):
    participante = input('Nome do participante: ')
    # posicao = int(input('Posição a ser inserido: '))
    participantes.insert(participante,posicao)

print(f'Particpantes Iniciais: {participantes}')
start = randint(1,num_participantes)
print(start)
rodada = 1
for i in range(start-1):
        participantes.advance()
while len(participantes) != num_vencedores:   
        music = randint(4,15)
        print(f"Participantes: {participantes}")
        print(f"Rodada: {rodada}")
        print(f"Start: {participantes.element(start-1)} K={music}")
        for i in range(music):
            print(f"----->{participantes.advance()}<------")
        eliminado = participantes.goTo(start,music)
        posicaoEliminado = participantes.index(eliminado)+1
        prox= participantes.goTo(posicaoEliminado,1)
        removido =participantes.remove(posicaoEliminado)
        print(f"Removido: {removido}")
        start = participantes.index(prox)+1  
        print('---------------FIM DO ROUND---------------------')
        rodada+=1
print(f"O(s) participante(s) vencedor(es): {participantes}")

