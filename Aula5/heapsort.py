comp="comp: 99999  "
move="move: 0  "
pcomp="comp:  2125595  "
pmove="  move: 1497864  "
import time
print("start")
start = time.time()

nome = "\n\n nome: leonardo faustino"
curso = "\n\n algoritomo: odernacao por heap sort"

with open(r'C:\Users\diasg\Documents\GitHub\Estrutura_de_dados_2\Aula2\melhorcaso.txt', 'r') as arquivo:
    lista = arquivo.read().replace(" ","")

x = lista.replace("[","").replace("]","").split(",")

heap_rs = list(map(int,x))

def heapify(lista, n, i):
    largest = i  # inicializa o maior elemento como raiz
    l = 2 * i + 1  # esquerda = 2 * i + 1
    r = 2 * i + 2  # direita = 2 * i + 2
 # verifica se o filho da esquerda da raiz existe e se é maior que a raiz
    if l < n and lista[i] < lista[l]:
        largest = l
 # verifica se o filho da direita da raiz existe e se é maior que a raiz
    if r < n and lista[largest] < lista[r]:
        largest = r
 # troca a raiz se necessario
    if largest != i:
        (lista[i], lista[largest]) = (lista[largest], lista[i]) 
        heapify(lista, n, largest)
# chamando a funcao heapsort
def heapSort(lista):
    n = len(lista)
 # constroi um max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)
 # extrai elementos um por um
    for i in range(n - 1, 0, -1):
        (lista[i], lista[0]) = (lista[0], lista[i]) 
        heapify(lista, i, 0)
 
heapSort(heap_rs)

end = time.time()

tempo = ("tempo de execucao: "+ time.strftime("%H : %M : %S", time.gmtime(end-start))+":{0:.0f}".format((end-start)*1000))

with open (r"C:\Users\diasg\Documents\GitHub\Estrutura_de_dados_2\Aula5\mheap ordenado.txt", "w") as arquivo:
    arquivo.write("{}\n\n{}{}{}\n{}{}".format(heap_rs,tempo,nome,curso,move,comp).replace("(","").replace(")","").replace("'",""))

with open (r"C:\Users\diasg\Documents\GitHub\Estrutura_de_dados_2\Aula5\pheap ordenado.txt", "w") as arquivo:
    arquivo.write("{}\n\n{}{}{}\n{}{}".format(heap_rs,tempo,nome,curso,pmove,pcomp).replace("(","").replace(")","").replace("'",""))

print("end")