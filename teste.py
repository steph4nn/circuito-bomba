from lista import LinkedList

lista = LinkedList()
lista.insert(80,1)
lista.insert(60,1)
lista.insert(40,1)
lista.insert(20,1)


print(lista)
n = 3
c = 1
# print(f"Sem interar: {lista.advance(3)}")
print("Interando:")
for i in range(3):
    print(lista.advance())
    