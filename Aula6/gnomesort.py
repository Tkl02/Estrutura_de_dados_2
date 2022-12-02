comp="comp: 99999  "
move="move: 0  "
pcomp="comp:  4999851708  "
pmove="  move: 4999783757  "

import time
print("start")
start = time.time()

nome = "\n\n nome: leonardo faustino"
curso = "\n\n algoritomo: odernacao por gnome sort"
n=0
with open(r'C:\Users\diasg\Documents\GitHub\Estrutura_de_dados_2\Aula2\dados500_mil.txt', 'r') as arquivo:
    lista = arquivo.read().replace(" ","")

x = lista.replace("[","").replace("]","").split(",")

gnome = list(map(int,x))
# Função que faz a ordenação
def gnomeSort( lista, n):
    index = 0
    while index < n:
        if index == 0:
            index = index + 1
        if lista[index] >= lista[index - 1]:
            index = index + 1
        else:
            lista[index], lista[index-1] = lista[index-1], lista[index]
            index = index - 1
 
    return lista
 
lista = gnome
n = len(lista)
 
gnome = gnomeSort(gnome,n)

end = time.time()

tempo = ("tempo de execucao: "+ time.strftime("%H : %M : %S", time.gmtime(end-start))+":{0:.0f}".format((end-start)*1000))

with open (r"C:\Users\diasg\Documents\GitHub\Estrutura_de_dados_2\Aula6\gnome ordenado.txt", "w") as arquivo:
    arquivo.write("{}\n\n{}{}{}\n{}{}".format(gnome,tempo,nome,curso,comp,move).replace("(","").replace(")","").replace("'",""))

print("end")