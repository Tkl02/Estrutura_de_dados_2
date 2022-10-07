import time

start = time.time()

nome = "\n\n nome: leonardo faustino"
curso = "\n\n algoritomo: odernacao por heap sort"

with open(r'C:\Users\diasg\Documents\GitHub\Estrutura_de_dados_2\Aula2\dados5.txt', 'r') as arquivo:
    lista = arquivo.read().replace(" ","")

x = lista.replace("[","").replace("]","").split(",")

heap_rs = list(map(int,x))

def heapify(lista, n, i):
    largest = i  
    l = 2 * i + 1  
    r = 2 * i + 2 
 
    if l < n and lista[i] < lista[l]:
        largest = l
 
    if r < n and lista[largest] < lista[r]:
        largest = r
 
    if largest != i:
        (lista[i], lista[largest]) = (lista[largest], lista[i]) 
 
        heapify(lista, n, largest)
 
def heapSort(lista):
    n = len(lista)
 
    for i in range(n // 2 - 1, -1, -1):
        heapify(lista, n, i)
 
    for i in range(n - 1, 0, -1):
        (lista[i], lista[0]) = (lista[0], lista[i]) 
        heapify(lista, i, 0)
 
heapSort(heap_rs)

end = time.time()

tempo = ("tempo de execucao: "+ time.strftime("%H : %M : %S", time.gmtime(end-start))+":{0:.0f}".format((end-start)*1000))

with open (r"C:\Users\diasg\Documents\GitHub\Estrutura_de_dados_2\Aula5\heap ordenado.txt", "w") as arquivo:
    arquivo.write("{}\n\n{}{}{}".format(heap_rs,tempo,nome,curso).replace("(","").replace(")","").replace("'",""))