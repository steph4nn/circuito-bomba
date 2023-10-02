from lista import LinkedList

lista = LinkedList()
lista.insert(80,1)
lista.insert(60,1)
lista.insert(40,1)
lista.insert(20,1)


print(lista)
n = 3
c = 1
while c <= 3: 
    print(lista.advance(3))
    c+=1