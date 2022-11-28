import time

start = time.time()

nome = "\n\n nome: leonardo faustino"
curso = "\n\n algoritomo: odernacao por quick sort"

with open(r'C:\Users\diasg\Documents\GitHub\Estrutura_de_dados_2\Aula2\dados5.txt', 'r') as arquivo:
    lista = arquivo.read().replace(" ","")

x = lista.replace("[","").replace("]","").split(",")

quick_rs = list(map(int,x))

def quicksort(lista, inicio=0, fim=None):
    # Se fim não for especificado, considere a lista toda
    if fim is None:
        fim = len(lista)-1
    # Se a lista tiver mais de um elemento
    if inicio < fim:
        p = partition(lista, inicio, fim)
        quicksort(lista, inicio, p-1)
        quicksort(lista, p+1, fim)
        
    # Retorna a lista ordenada
def partition(lista, inicio, fim):
    # Escolha o elemento mais à direita como pivô
    pivot = lista[fim]
    i = inicio
    for j in range(inicio, fim):
        if lista[j] <= pivot:
            lista[j], lista[i] = lista[i], lista[j]
            i = i + 1
    lista[i], lista[fim] = lista[fim], lista[i]
    return i

quicksort(quick_rs)

end = time.time()

tempo = ("tempo de execucao: "+ time.strftime("%H : %M : %S", time.gmtime(end-start))+":{0:.0f}".format((end-start)*1000))

with open (r"C:\Users\diasg\Documents\GitHub\Estrutura_de_dados_2\Aula4\Quick ordenado.txt", "w") as arquivo:
    arquivo.write("{}\n\n{}{}{}".format(quick_rs,tempo,nome,curso).replace("(","").replace(")","").replace("'",""))