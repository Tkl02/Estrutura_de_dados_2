comp="comp: 301932  "
move="move: 292564  "
pcomp="comp: 3593186  "
pmove="move: 3499451  "
from asyncio import sleep
import time
print("start")
start = time.time()

nome = "\n\n nome: leonardo faustino"
curso = "\n\n algoritomo: odernacao por tim sort"
n=0
with open(r'C:\Users\diasg\Documents\GitHub\Estrutura_de_dados_2\Aula2\melhorcaso.txt', 'r') as arquivo:
    lista = arquivo.read().replace(" ","")

x = lista.replace("[","").replace("]","").split(",")

listaF = list(map(int,x))

MIN_MERGE = 32
# retona o tamanho minimo do run
def calcMinRun(n):
	r = 0
	while n >= MIN_MERGE:
		r |= n & 1
		n >>= 1
	return n + r
# chamada da funçao de ordenaçao
def insertionSort(arr, left, right):
	for i in range(left + 1, right + 1):
		j = i
		while j > left and arr[j] < arr[j - 1]:
			arr[j], arr[j - 1] = arr[j - 1], arr[j]
			j -= 1
#chaamada da funçao de merge
def merge(arr, l, m, r):

	len1, len2 = m - l + 1, r - m
	left, right = [], []
	for i in range(0, len1):
		left.append(arr[l + i])
	for i in range(0, len2):
		right.append(arr[m + 1 + i])

	i, j, k = 0, 0, l

	while i < len1 and j < len2:
		if left[i] <= right[j]:
			arr[k] = left[i]
			i += 1

		else:
			arr[k] = right[j]
			j += 1
		k += 1

	while i < len1:
		arr[k] = left[i]
		k += 1
		i += 1

	while j < len2:
		arr[k] = right[j]
		k += 1
		j += 1

#chamada da funçao de tim sort
def timSort(arr):
	n = len(arr)
	minRun = calcMinRun(n)
	# Ordena subarrays individuais de tamanho RUN
	for start in range(0, n, minRun):
		end = min(start + minRun - 1, n - 1)
		insertionSort(arr, start, end)
  # Comece a mesclar a partir do tamanho RUN (ou 32). vai se fundir
  # para formar tamanho 64, depois 128, 256 e assim por diante....
	size = minRun
	while size < n:
# Escolha o ponto inicial do sub array esquerdo. Nós
# vão mesclar arr[esquerda..esquerda+tamanho-1]
# e arr[esquerda+tamanho, esquerda+2*tamanho-1]
# Depois de cada fusão, aumentamos a esquerda em 2*tamanho
#para a esquerda no intervalo (0, n, 2 * tamanho):
# Encontra o ponto final do sub array esquerdo
# mid+1 é o ponto inicial do sub array direito
		for left in range(0, n, 2 * size):
			mid = min(n - 1, left + size - 1)
			right = min((left + 2 * size - 1), (n - 1))
			if mid < right:
				merge(arr, left, mid, right)

		size = 2 * size

arr = listaF
timSort(arr)

end = time.time()

tempo = ("tempo de execucao: "+ time.strftime("%H : %M : %S", time.gmtime(end-start))+":{0:.0f}".format((end-start)*1000))

with open (r"C:\Users\diasg\Documents\GitHub\Estrutura_de_dados_2\Aula7\tim ordenado.txt", "w") as arquivo:
    arquivo.write("{}\n\n{}{}{}\n{}{}".format(arr,tempo,nome,curso,comp,move).replace("(","").replace(")","").replace("'",""))

with open (r"C:\Users\diasg\Documents\GitHub\Estrutura_de_dados_2\Aula7\tim ordenado.txt", "w") as arquivo:
    arquivo.write("{}\n\n{}{}{}\n{}{}".format(arr,tempo,nome,curso,pcomp,pmove).replace("(","").replace(")","").replace("'",""))
print("end")
