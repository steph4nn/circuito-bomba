from lista import LinkedList
class Jogo:
    def __init__(self, quantity:int, winners:int):
        self.__quantity = quantity
        self.__winners = winners
        self.__players = LinkedList()
    def players(self):
        for i in range(self.__quantity):
            player = input("Nome do jogador: ").title()
            self.__players.insert(player,1)
    def passarJogador(self,quantity):
        for i in range(quantity):
                print(self.__players.advance())
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
