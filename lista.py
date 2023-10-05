class Node:
    '''
    Classe de objetos para um nó dinâmico na memória
    '''
    def __init__(self,data):
        self.__data = data
        self.__next = None
    
    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, newData):
        self.__data = newData

    @property
    def next(self):
        return self.__next
    
    @next.setter
    def next(self, newNext):
        self.__next = newNext

    def hasNext(self):
        return self.__next != None
    
    def __str__(self):
        return str(self.__data)

class ListException(Exception):
    def __init__(self,msg):
        super().__init__(msg)


class LinkedList:
    def __init__(self) -> None:
        self.__head = None
        self.__tail = None
        self.__size = 0
        self.__pointer = self.__head

    def isEmpty(self):
        return self.__size == 0
    
    def __len__(self):
        return self.__size
    
    def insert(self, value, position):
        try:
            assert position > 0 and position <= len(self)+1, f'Posicao invalida. Lista contém {self.__size} elementos' 
            if self.isEmpty():
                if ( position != 1):
                    raise ListException(f'A lista esta vazia. A posicao correta para insercao é 1.')
                new = Node(value)
                self.__head = new
                self.__tail = new
                self.__tail.next = self.__head
                self.__size+=1
                self.__pointer = self.__head
            elif position == 1:
                new = Node(value)
                new.next = self.__head
                self.__head = new
                self.__tail.next = self.__head
                self.__size +=1
                self.__pointer = self.__head
            elif position == len(self)+1:
                new = Node(value)
                self.__tail.next = new
                self.__tail = new
                self.__tail.next = self.__head
                self.__size+=1
            else:
                new = Node(value)
                pointer = self.__head
                count = 1
                while (count < (position-1)):
                    pointer = pointer.next
                    count+=1
                new.next = pointer.next
                pointer.next = new
                self.__size+=1
        except TypeError:
            raise ListException(f'A posição deve ser um número inteiro')            
        except AssertionError as ae:
            raise ListException(ae)

    def advance(self):
        self.__pointer = self.__pointer.next
        return self.__pointer.data

    def goTo(self,start ,quantity):
        pointer = self.__head
        count = 1
        while (count<start):
            pointer = pointer.next
            count+=1
        for i in range(quantity):
            pointer = pointer.next
        return pointer.data
    
    def remove(self,position):
        try:
            if( self.isEmpty() ):
                raise ListException(f'Não é possível remover de uma lista vazia')            
            assert position > 0 and position <= len(self), f'Posicao invalida. Lista contém {self.__tamanho} elementos'
            
            if position == 1:
                data = self.__head.data
                pointer = self.__head
                self.__tail.next = pointer.next
                self.__head = pointer.next
                self.__size-=1
                self.__pointer = self.__head
                if data == self.__pointer.data:
                    self.__pointer = self.__pointer.next
                return data
            elif position == len(self):
                data = self.__tail.data
                count = 1
                pointer = self.__head
                while count <position-1:
                    pointer = pointer.next
                    count+=1
                pointer.next = self.__head
                self.__tail = pointer
                self.__size-=1
                if data == self.__pointer.data:
                    self.__pointer = self.__pointer.next
                return data
            else:
                pointer = self.__head
                ant =  self.__head
                count = 1
                while (count < position):
                    ant = pointer
                    pointer = pointer.next
                    count+=1
                ant.next = pointer.next
                data = pointer.data
                if data == self.__pointer.data:
                    self.__pointer = self.__pointer.next
                self.__size-=1
                return data
        except TypeError:
            raise ListException(f'A posição deve ser um número inteiro')            
        except AssertionError as ae:
            raise ListException(ae)

    def index(self, elem):
        if (self.isEmpty()):
            raise ListException(f'Lista vazia')
        pointer = self.__head
        count = 1
        while True:
            if pointer.data == elem:
                return count
            pointer = pointer.next
            if pointer == self.__head:
                break
        raise ListException(f'O elemento {elem} não está armazenado na lista')

    def element(self, index):
        try:
            assert not self.isEmpty(), 'Lista vazia'
            assert index >= 0 and index <= len(self), f'Posicao invalida. Lista contém {self.__size} elementos'

            pointer = self.__head
            count = 1
            while(count <= index):
                pointer = pointer.next 
                count+=1
            return pointer.data
        except TypeError:
            raise ListException(f'A posição deve ser um número inteiro')            
        except AssertionError as ae:
            raise ListException(ae)
    def verifyElement(self,element):
        try:
            pointer= self.__head
            for i in range(len(self)):
                assert pointer.data != element, f'O elemento [{element}] já está na lista e não pode ser adicionado de novo.'
                pointer = pointer.next
        except AssertionError as ae:
            raise ListException(ae)
    def __str__(self) -> str:
        str = '[ '
        if self.isEmpty():
            str+= ']'
            return str
        pointer = self.__head
        for i in range(1,len(self)+1):
            str += f'{pointer.data}, '
            pointer = pointer.next
        str = str[:-2] + " ]"
        return str
