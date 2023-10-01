from lista import *
from random import randint

num_participantes = int(input())
num_vencedores = int(input())

assert num_participantes > 0
assert num_vencedores < num_participantes and num_vencedores>0


participantes = LinkedList()
for i in range(num_participantes):
    participante = input('Nome do participante: ')
    posicao = int(input('Posição a ser inserido: '))
    participantes.insert(participante,posicao)

print(f'Particpantes Iniciais: {participantes}')
start = randint(1,num_participantes)
rodada = 1
while len(participantes) != num_vencedores:   
        music = randint(4,15)
        print(f"Participantes: {participantes}")
        print(f"Rodada: {rodada}")
        print(f"Start: {participantes.element(start-1)} K={music}")
        eliminado = participantes.advance(start,music)
        posicaoEliminado = participantes.index(eliminado)+1
        prox= participantes.advance(posicaoEliminado,1)
        removido =participantes.remove(posicaoEliminado)
        print(f"Removido: {removido}")
        
        start = participantes.index(prox)+1
        
        print('---------------FIM DO ROUND---------------------')
        rodada+=1
print(f"O(s) participante(s) vencedor(es): {participantes}")

