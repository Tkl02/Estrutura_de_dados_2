import random
print("Lista de números aleatórios:")
listanum = []

for i in range(5):
    listanum.append(random.randint(1,9))

print(listanum)

def bubbleSort(listanum):

    for iteracao in range(1, len(listanum)):
        for indice in range(0, len(listanum) - iteracao):
            if listanum[indice] > listanum[indice + 1]:
                temp = listanum[indice]
                listanum[indice] = listanum[indice + 1]
                listanum[indice + 1] = temp


bubbleSort(listanum)

print("lista Ordenado:")
print(listanum)