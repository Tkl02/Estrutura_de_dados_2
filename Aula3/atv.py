from random import randint,shuffle
import string
import time

nome = "\n\n nome: leonardo faustino"
curso = "\n\n algoritomo: odernacao por bogo sort"

with open(r'C:\Users\diasg\Documents\GitHub\Estrutura_de_dados_2\Aula2\dados5.txt', 'r') as arquivo:
    lista = arquivo.read().replace(" ","")

x = lista.replace("[","").replace("]","").split(",")

a = list(map(int,x))

start = time.time()

def bogo_sort(a):
	def is_sorted(a):
		for i in range(1,len(a)):
			if a[i]<a[i-1]: return False
		return True
    
	ct=0
	while not is_sorted(a):
		shuffle(a)
		ct+=1
	return ct,a 

s=bogo_sort(a)

end = time.time()

tempo = ("tempo de execucao: "+ time.strftime("%H : %M : %S", time.gmtime(end-start))+":{0:.0f}".format((end-start)*1000))

with open (r"C:\Users\diasg\Documents\GitHub\Estrutura_de_dados_2\Aula3\bogo ordenado.txt", "w") as arquivo:
    arquivo.write("{}\n\n{}{}{}".format(s,tempo,nome,curso).replace("(","").replace(")","").replace("'",""))

