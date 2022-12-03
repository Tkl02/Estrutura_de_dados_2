comp="comp: 39890  "
move="move: 100000  "
pcomp="comp: 39890  "
pmove="move: 100000  "
import time

print("-=- start -=-")

start = time.time()

nome = "\n\n nome: leonardo faustino"
curso = "\n\n algoritomo: odernacao por buckt sort"
n=0
with open(r'C:\Users\diasg\Documents\GitHub\Estrutura_de_dados_2\Aula2\melhorcaso.txt', 'r') as arquivo:
    lista = arquivo.read().replace(" ","")

x = lista.replace("[","").replace("]","").split(",")

listaF = list(map(int,x))

def bucketSort(array):
    bucket = []
# criaçao dos baldes
    for i in range(len(array)):
        bucket.append([])
# inserçao dos elementos nos baldes
    for j in array:
        index_b = int(10 / j)
        bucket[index_b].append(j)
# Ordene os elementos de cada balde
    for i in range(len(array)):
        bucket[i] = sorted(bucket[i])
    k = 0
# # Pega os elementos ordenados
    for i in range(len(array)):
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array

x=listaF
bucketSort(x)

end = time.time()

tempo = ("tempo de execucao: "+ time.strftime("%H : %M : %S", time.gmtime(end-start))+":{0:.0f}".format((end-start)*1000))

with open (r"C:\Users\diasg\Documents\GitHub\Estrutura_de_dados_2\Aula7\buck ordenado.txt", "w") as arquivo:
    arquivo.write("{}\n\n{}{}{}\n{}{}".format(x,tempo,nome,curso,move,comp).replace("(","").replace(")","").replace("'",""))

with open (r"C:\Users\diasg\Documents\GitHub\Estrutura_de_dados_2\Aula7\buck ordenado.txt", "w") as arquivo:
    arquivo.write("{}\n\n{}{}{}\n{}{}".format(x,tempo,nome,curso,pmove,pcomp).replace("(","").replace(")","").replace("'",""))
    
print("-=- end -=-")