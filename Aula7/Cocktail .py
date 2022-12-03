comp="comp: 99999  "
move="move: 0  "
pcomp="comp: 5000000000  "
pmove="move: 4999783757  "
import time

print("-=- start -=-")

start = time.time()

nome = "\n\n nome: leonardo faustino"
curso = "\n\n algoritomo: odernacao por Cocktail sort"
n=0
with open(r'C:\Users\diasg\Documents\GitHub\Estrutura_de_dados_2\Aula2\melhorcaso.txt', 'r') as arquivo:
    lista = arquivo.read().replace(" ","")

x = lista.replace("[","").replace("]","").split(",")

listaF = list(map(int,x))
# Função que faz a ordenação
def cocktailSort(a):
	n = len(a)
	verificar = True
	inicio = 0
	fim = n-1
	while (verificar==True):

		verificar = False

		for i in range (inicio, fim):
			if (a[i] > a[i+1]) :
				a[i], a[i+1]= a[i+1], a[i]
				verificar=True

		if (verificar==False):
			break

		verificar = False

		fim = fim-1

		for i in range(fim-1, inicio-1,-1):
			if (a[i] > a[i+1]):
				a[i], a[i+1] = a[i+1], a[i]
				verificar = True

		inicio = inicio+1

a = listaF
cocktailSort(a)
 
end = time.time()

tempo = ("tempo de execucao: "+ time.strftime("%H : %M : %S", time.gmtime(end-start))+":{0:.0f}".format((end-start)*1000))

with open (r"C:\Users\diasg\Documents\GitHub\Estrutura_de_dados_2\Aula7\Cocktail ordenado.txt", "w") as arquivo:
    arquivo.write("{}\n\n{}{}{}\n{}{}".format(a,tempo,nome,curso,comp,move).replace("(","").replace(")","").replace("'",""))

with open (r"C:\Users\diasg\Documents\GitHub\Estrutura_de_dados_2\Aula7\Cocktail ordenado.txt", "w") as arquivo:
    arquivo.write("{}\n\n{}{}{}\n{}{}".format(a,tempo,nome,curso,pcomp,pmove).replace("(","").replace(")","").replace("'",""))
    
print("-=- end -=-")