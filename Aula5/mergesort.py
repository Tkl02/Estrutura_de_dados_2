import time

start = time.time()

nome = "\n\n nome: leonardo faustino"
curso = "\n\n algoritomo: odernacao por merge sort"

with open(r'C:\Users\diasg\Documents\GitHub\Estrutura_de_dados_2\Aula2\dados5.txt', 'r') as arquivo:
    lista = arquivo.read().replace(" ","")

x = lista.replace("[","").replace("]","").split(",")

merge_rs = list(map(int,x))
# Função que faz a ordenação
def mergesort(lista, inicio=0, fim=None):
    # Se fim não for especificado, considere a lista toda
    if fim is None:
        fim = len(lista)
    if(fim - inicio > 1):
        meio = (fim + inicio)//2
        mergesort(lista, inicio, meio)
        mergesort(lista, meio, fim)
        merge(lista, inicio, meio, fim)
# Função que faz a junção das listas
def merge(lista, inicio, meio, fim):
    left = lista[inicio:meio]
    right = lista[meio:fim]
    top_left, top_right = 0, 0
    for k in range(inicio, fim):
        if top_left >= len(left):
            lista[k] = right[top_right]
            top_right = top_right + 1
        elif top_right >= len(right):
            lista[k] = left[top_left]
            top_left = top_left + 1
        elif left[top_left] < right[top_right]:
            lista[k] = left[top_left]
            top_left = top_left + 1
        else:
            lista[k] = right[top_right]
            top_right = top_right + 1

mergesort(merge_rs)

end = time.time()

tempo = ("tempo de execucao: "+ time.strftime("%H : %M : %S", time.gmtime(end-start))+":{0:.0f}".format((end-start)*1000))

with open (r"C:\Users\diasg\Documents\GitHub\Estrutura_de_dados_2\Aula5\Merge ordenado.txt", "w") as arquivo:
    arquivo.write("{}\n\n{}{}{}".format(merge_rs,tempo,nome,curso).replace("(","").replace(")","").replace("'",""))