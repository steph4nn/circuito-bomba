from node import Node

class ListaException(Exception):
    """Classe de exceção lançada quando uma violação de ordem genérica da lista é identificada.
    """

    def __init__(self,msg):
        """ Construtor padrão da classe, que recebe uma mensagem que se deseja
            embutir na exceção
        """
        super().__init__(msg)




'''
Esta classe implementa uma estrutura Lista Simplesmente Encadeada
'''
class Lista:
    # constructor initializes an empty linkd list
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__tamanho = 0

    def estaVazia(self):
        return self.__tamanho == 0 

    def __len__(self):
        return self.__tamanho

    def elemento(self, posicao:int)->any:
        try:
            assert not self.estaVazia(), 'Lista vazia'
            assert posicao > 0 and posicao <= len(self), f'Posicao invalida. Lista contém {self.__tamanho} elementos'

            cursor = self.__head
            contador = 1
            while( cursor != None  and contador < posicao):
                cursor = cursor.next
                contador += 1

            return cursor.data

        except AssertionError as ae:
            raise ListaException(ae)

    def index(self, elem):
        '''
        retorna o index do elemento
        '''
        try:
            assert not self.estaVazia(), 'Lista vazia'
            
            cursor = self.__head
            for i in range(len(self)):
                if cursor.data == elem:
                    return i
                else:
                    cursor =cursor.next


        except AssertionError as ae:
            raise ListaException(ae)

    def modificar(self, posicao:int, carga: any):

        try:
            assert posicao > 0, f'A posicao não pode ser 0 (zero) ou um número negativo'
            assert posicao <= len(self), f'Posicao invalida. Lista contém {self.__tamanho} elementos'
            assert not self.estaVazia(), 'Lista vazia'

            cursor = self.__head
            contador = 1
            while( cursor != None and contador < posicao ):
                cursor = cursor.next
                contador += 1

            cursor.data = carga
        except TypeError:
            raise ListaException(f'A posição deve ser um número do tipo inteiro')            
        except AssertionError as ae:
            raise ListaException(ae.__str__())
    
    def busca(self, chave:any)->int:
        if (self.estaVazia()):
            raise ListaException(f'Lista vazia')

        cursor = self.__head
        contador = 1

        for i in range(1,len(self)+1):
            if( cursor.data == chave):
                return contador
            cursor = cursor.next
            contador += 1
            
        raise ListaException(f'O valor {valor} não está armazenado na lista')

    def inserir(self, posicao:int, carga:any ):
        try:
            assert posicao > 0 and posicao <= len(self)+1, f'Posicao invalida. Lista contém {self.__tamanho} elementos' 

            # CONDICAO 1: insercao se a lista estiver vazia
            if (self.estaVazia()):
                self.__head = Node(carga)
                self.__tail = Node(carga)
                self.__head.next = self.__head
                self.__tamanho += 1
                return
            
            # CONDICAO 2: insercao na primeira posicao em uma lista nao vazia
            if ( posicao == 1):
                cursor = self.__head
                novo = Node(carga)
                self.__tail.next = novo
                novo.next = self.__head
                self.__head = novo
                self.__tamanho += 1
                return

            # CONDICAO 3: insercao na ultima posicao em uma lista circular
            if (posicao == len(self)+1):
                cursor = self.__head
                contador = 1
                while ( contador < posicao-1):
                    cursor = cursor.next
                    contador += 1
                novo = Node(carga)
                novo.next = cursor.next
                cursor.next = novo
                self.__tail = novo
                self.__tamanho += 1
                return

            # CONDICAO 4: insercao apos a primeira posicao em lista nao vazia
            cursor = self.__head
            contador = 1
            while ( contador < posicao-1):
                cursor = cursor.next
                contador += 1

            novo = Node(carga)
            novo.next = cursor.next
            cursor.next = novo
            self.__tamanho += 1

        except TypeError:
            raise ListaException(f'A posição deve ser um número inteiro')            
        except AssertionError:
            raise ListaException(f'A posicao não pode ser um número negativo ou 0 (zero)')



    def remover(self, posicao:int)->any:
        try:
            if( self.estaVazia() ):
                raise ListaException(f'Não é possível remover de uma lista vazia')
            
            assert posicao > 0 and posicao <= len(self), f'Posicao invalida. Lista contém {self.__tamanho} elementos'

            cursor = self.__head
            contador = 1

            if (posicao ==len(self)):
                while( contador <= len(self)-1):
                    anterior = cursor
                    cursor = cursor.next
                    contador+=1
                anterior.next = cursor.next
                data = cursor.data
                self.__tamanho -=1
                return data

            if (posicao != len(self)):
                while( contador <= posicao-1 ) :
                    anterior = cursor
                    cursor = cursor.next
                    contador+=1

                data = cursor.data

                if( posicao == 1):
                    self.__head = cursor.next
                else:
                    anterior.next = cursor.next
                self.__tamanho -= 1

                return data
        
        except TypeError:
            raise ListaException(f'A posição deve ser um número inteiro')            
        except AssertionError:
            raise ListaException(f'A posicao não pode ser um número negativo')
        
    def __str__(self):

        str = 'Lista: [ '
        if self.estaVazia():
            str+= ']'
            return str

        cursor = self.__head

        for i in range(1,len(self)+1):
            str += f'{cursor.data}, '
            cursor = cursor.next

        str = str[:-2] + " ]"
        return str


