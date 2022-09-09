from posixpath import split
import time

start1 = time.time()

# aquivo a ser lido

with open("C:\Users\diasg\Documents\GitHub\Estrutura_de_dados_2\Aula2\dados5.txt","r") as arquivo:
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
    print("movimentos",y)
arr = y
insertionSort(arr) 

# representaçao de arquivos organizados

with open ("insert ordenado.txt", "w") as arquivo:
    arquivo.write("{}".format(arr))

end1 = time.time()

print("tempo de execuçao:", time.strftime("%H : %M : %S", time.gmtime(end1-start1)),":{0:.0f}".format((end1-start1)*1000))
print ("insertion sort organizado")

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

with open ("select ordenado.txt", "w") as arquivo:
    arquivo.write("{}".format(arr2))

end2 = time.time()

print("tempo de execuçao:", time.strftime("%H : %M : %S", time.gmtime(end2-start2)),":{0:.0f}".format((end2-start2)*1000))
print ("insertion sort organizado")