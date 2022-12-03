comp="comp: 0  "
move="move: 600000  "
pcomp="comp: 0  "
pmove="move: 600000  "
import time

start = time.time()

nome = "\n\n nome: leonardo faustino"
curso = "\n\n algoritomo: odernacao por radix sort"
n=0
with open(r'C:\Users\diasg\Documents\GitHub\Estrutura_de_dados_2\Aula2\melhorcaso.txt', 'r') as arquivo:
    lista = arquivo.read().replace(" ","")

x = lista.replace("[","").replace("]","").split(",")

radix = list(map(int,x))

# Função que faz a ordenação
def countingSort(lista, exp1):
    n = len(lista)
    output = [0] * (n)
    count = [0] * (10)
    for i in range(0, n):
        index = lista[i] // exp1
        count[index % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    i = n - 1
    while i >= 0:
        index = lista[i] // exp1
        output[count[index % 10] - 1] = lista[i]
        count[index % 10] -= 1
        i -= 1
    i = 0
    for i in range(0, len(lista)):
        lista[i] = output[i]
 
# Função principal que faz a ordenação
def radixSort(lista):
 
    max1 = max(lista)
    exp = 1
    while max1 / exp >= 1:
        countingSort(lista, exp)
        exp *= 10
 
lista = radix
 
radixSort(lista)
 
end = time.time()

tempo = ("tempo de execucao: "+ time.strftime("%H : %M : %S", time.gmtime(end-start))+":{0:.0f}".format((end-start)*1000))

with open (r"C:\Users\diasg\Documents\GitHub\Estrutura_de_dados_2\Aula6\radix ordenado.txt", "w") as arquivo:
    arquivo.write("{}\n\n{}{}{}\n{}{}".format(lista,tempo,nome,curso,comp,move).replace("(","").replace(")","").replace("'",""))

with open (r"C:\Users\diasg\Documents\GitHub\Estrutura_de_dados_2\Aula6\radix ordenado.txt", "w") as arquivo:
    arquivo.write("{}\n\n{}{}{}\n{}{}".format(lista,tempo,nome,curso,pcomp,pmove).replace("(","").replace(")","").replace("'",""))