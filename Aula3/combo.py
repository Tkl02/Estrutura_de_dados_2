import string
import time

print("-=- start -=-")

nome = "\n\n nome: leonardo faustino"
curso = "\n\n algoritomo: odernacao por bogo sort"

start=time.time()


with open(r'C:\Users\diasg\Documents\GitHub\Estrutura_de_dados_2\Aula2\dados500_mil.txt', 'r') as arquivo:
    lista = arquivo.read().replace(" ","")

x = lista.replace("[","").replace("]","").split(",")

combo_rs = list(map(int,x))

# To find next gap from current
def getNextGap(gap):

	# Shrink gap by Shrink factor
	gap = (gap * 10)//13
	if gap < 1:
		return 1
	return gap

# Function to sort arr[] using Comb Sort
def combSort(arr):
	n = len(arr)

	# inicio gap
	gap = n

	# loops
	swapped = True

	# interaçao gap swap
	while gap !=1 or swapped == 1:

		# poximo gap
		gap = getNextGap(gap)

		# inicializa o swap
		# swap verdadeiro se for necessário
		swapped = False

		# comparar todos os elementos com o gap
		for i in range(0, n-gap):
			if arr[i] > arr[i + gap]:
				arr[i], arr[i + gap]=arr[i + gap], arr[i]
				swapped = True


arr = combo_rs
combSort(arr)
 
end = time.time()

tempo = ("tempo de execucao: "+ time.strftime("%H : %M : %S", time.gmtime(end-start))+":{0:.0f}".format((end-start)*1000))

with open (r"C:\Users\diasg\Documents\GitHub\Estrutura_de_dados_2\Aula3\combo ordenado.txt", "w") as arquivo:
    arquivo.write("{}\n\n{}{}{}\n{}{}".format(arr,tempo,nome,curso,move,comp).replace("(","").replace(")","").replace("'",""))

print("-=- end -=-")
