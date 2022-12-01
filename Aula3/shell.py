move = '   '
comp = '   '
import string
import time

print("-=- start -=-")

nome = "\n\n nome: leonardo faustino"
curso = "\n\n algoritomo: odernacao por bogo sort"

start=time.time()


with open(r'C:\Users\diasg\Documents\GitHub\Estrutura_de_dados_2\Aula2\dados500_mil.txt', 'r') as arquivo:
    lista = arquivo.read().replace(" ","")

x = lista.replace("[","").replace("]","").split(",")

shell_rs = list(map(int,x))

def shellSort(arr):

	# inicio do gap
	n = len(arr)
	gap = n/2

# Faça uma classificação por inserção de intervalo para este tamanho de intervalo.

# ordem continue adicionando mais um elemento até todo o array
	# sort gap
	while gap > 0:

		for i in range(gap,n):

			# add a[i] to the elements that have been gap sorted
			# save a[i] in temp and make a hole at position i
			temp = arr[i]

			# shift earlier gap-sorted elements up until the correct
			# location for a[i] is found
			j = i
			while j >= gap and arr[j-gap] >temp:
				arr[j] = arr[j-gap]
				j -= gap

			# put temp (the original a[i]) in its correct location
			arr[j] = temp
		gap /= 2


arr = shell_rs

n = len(arr)
shellSort(n,arr)

end = time.time()

tempo = ("tempo de execucao: "+ time.strftime("%H : %M : %S", time.gmtime(end-start))+":{0:.0f}".format((end-start)*1000))

with open (r"C:\Users\diasg\Documents\GitHub\Estrutura_de_dados_2\Aula3\shell ordenado.txt", "w") as arquivo:
    arquivo.write("{}\n\n{}{}{}\n{}{}".format(arr,tempo,nome,curso,move,comp).replace("(","").replace(")","").replace("'",""))

print("-=- end -=-")

