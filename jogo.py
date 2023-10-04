from lista import LinkedList
from random import randint
from time import sleep
class Jogo:
    def __init__(self, quantity:int, winners:int):
        self.__quantity = quantity
        self.__winners = winners
        self.__players = LinkedList()
    def playersAut(self, arq):
        arqOpen =open(arq, 'r')
        string_jogadores = arqOpen.readlines()
        string_jogadores = string_jogadores[0]
        print(string_jogadores)
        arr_jogadores = string_jogadores.split(', ')
        for i in range(self.__quantity):
            player = arr_jogadores[i].title()
            self.__players.insert(player,1)
    def playersManual(self):
        for i in range(self.__quantity):
            player = input("Nome do jogador: ").title()
            self.__players.insert(player,1)
    def passarJogador(self,quantity):
        for i in range(quantity):
                print(self.__players.advance())
                sleep(1)
    def definirPrimeiro(self, quantity):
        if quantity==1:
            return
        for i in range(quantity):
                self.__players.advance()
    def selecionarJogador(self,start,quantity):
        eliminado = self.__players.goTo(start, quantity)
        posicaoEliminado = self.__players.index(eliminado)+1
        return posicaoEliminado
    def eliminarJogador(self, position):
        removido =self.__players.remove(position)
        return removido
    def mostrarJogador(self, quantity):
        jogador = self.__players.element(quantity)
        return jogador
    def posicaoJogador(self, elemen):
        posicao = self.__players.index(elemen)+1
        return posicao
    def __str__(self) -> str:
        str = '[ '
        for i in range(len(self.__players)):
            str += f'{self.__players.element(i)}, '
        str = str[:-2] + " ]"
        return str
    def __len__(self):
        return len(self.__players)
    def iniciarJogo(self,start:int):
        round = 1
        while self.__winners < len(self):
            music = randint(4,15)
            print("--------------------COMEÇO DO ROUND------------------")
            print(f"participantes: {self}")
            print(f"Rodada: {round}")
            print(f"Start: {self.mostrarJogador(start-1)} K={music}")
            self.passarJogador(music)
            eliminado =self.selecionarJogador(start,music)
            start = eliminado
            print(f"Jogador eliminado: {self.eliminarJogador(eliminado)}")
            print("--------------------FIM DO ROUND------------------")
            print()
            round +=1
            sleep(2)
        print()
        print(f"O(s) participante(s) vencedor(es): {self}")
        