from posixpath import split
import time
print("start: \n ")
start1 = time.time()

nome = "\n\n nome: leonardo faustino"
curso = "\n algoritomo: odernacao por select/insert sort"


# aquivo a ser lido

with open(r'C:\Users\diasg\Documents\GitHub\Estrutura_de_dados_2\Aula2\melhorcaso.txt', 'r') as arquivo:
    lista = arquivo.read().replace(" ","")

x = lista.replace("[","").replace("]","").split(",")

y = list(map(int,x))


#funçao insertion sort

def insertionSort(arr): 
    y=0
    for i in range(1, len(arr)):  
        key = arr[i] 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key
        y=y+1

arr = y

insertionSort(arr) 

# representaçao de arquivos organizados

end1 = time.time()

temp=("tempo de execucao:"+ time.strftime("%H : %M : %S", time.gmtime(end1-start1))+":{0:.0f}".format((end1-start1)*1000))

with open (r"C:\Users\diasg\Documents\GitHub\Estrutura_de_dados_2\Aula2\insert ordenado.txt", "w") as arquivo:
    arquivo.write("{}{}{}\n{}\n{}{}".format(arr,nome,curso,temp).replace("(","").replace(")","").replace("'",""))


#funçao selection sort

start2 = time.time()


def selectionSort(arr2): 
  
    for i in range(len(arr2)): 
  
        min_idx = i 
        for j in range(i+1, len(arr2)): 
            if arr2[min_idx] > arr2[j]: 
                min_idx = j 
                  
        arr2[i], arr2[min_idx] = arr2[min_idx], arr2[i] 
  
arr2 = y

selectionSort(arr2)
end2 = time.time()

temp2=("tempo de execucao: "+ time.strftime("%H : %M : %S", time.gmtime(end2-start2))+":{0:.0f}".format((end2-start2)*1000))

with open (r"C:\Users\diasg\Documents\GitHub\Estrutura_de_dados_2\Aula2\select ordenado.txt", "w") as arquivo:
    arquivo.write("{}{}{}\n{}\n{}{}".format(arr2,nome,curso,temp2).replace("(","").replace(")","").replace("'",""))

print("fim -=-=-=-")
