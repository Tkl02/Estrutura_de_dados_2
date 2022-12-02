comp="comp: 9999900000  "
move="move: 0  "
pcomp=" comp:  9999900000  "
pmove="  move: 4999783757  "


import string
import time

print("-=- start -=-")

nome = "\n\n nome: leonardo faustino"
curso = "\n\n algoritomo: odernacao por bogo sort"

start=time.time()


with open(r'C:\Users\diasg\Documents\GitHub\Estrutura_de_dados_2\Aula2\dados500_mil.txt', 'r') as arquivo:
    lista = arquivo.read().replace(" ","")

x = lista.replace("[","").replace("]","").split(",")

bubble_rs = list(map(int,x))

def bubbleSort(arr):
	n = len(arr)
    # otimiza o código, então se o array já estiver ordenado, não precisa
    # para passar por todo o processo
	swapped = False
	# Percorre todos os elementos do array
	for i in range(n-1):
		# range(n) também funciona, mas o loop externo funcionará
        # repita uma vez mais do que o necessário.
        # Os últimos i elementos já estão no lugar
		for j in range(0, n-i-1):

            # percorre o array de 0 a n-i-1
            # Troca se o elemento encontrado for maior
            # do que o próximo elemento
			if arr[j] > arr[j + 1]:
				swapped = True
				arr[j], arr[j + 1] = arr[j + 1], arr[j]
		
		if not swapped:
			# se não precisamos fazer uma única troca, nós
            # pode simplesmente sair do loop principal.
			return

arr = bubble_rs

bubbleSort(arr)
 
end = time.time()

tempo = ("tempo de execucao: "+ time.strftime("%H : %M : %S", time.gmtime(end-start))+":{0:.0f}".format((end-start)*1000))

with open (r"C:\Users\diasg\Documents\GitHub\Estrutura_de_dados_2\Aula3\bubble ordenado.txt", "w") as arquivo:
    arquivo.write("{}\n\n{}{}{}\n{}{}".format(arr,tempo,nome,curso,move,comp).replace("(","").replace(")","").replace("'",""))

print("-=- end -=-")
