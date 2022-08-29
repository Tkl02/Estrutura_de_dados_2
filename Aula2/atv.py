from posixpath import split
import time

start = time.time()

with open("D:\desktopCODE\Estrutura_de_dados_2\Aula2\dados100.txt","r") as arquivo:
    lista = arquivo.read().replace(" ","")

x = lista.replace("[","").replace("]","").split(",")

y = list(map(int,x))

print ("resultado organizado")

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

with open ("senhas ordenadas.txt", "w") as arquivo:
    arquivo.write("{}".format(arr))

end = time.time()

print("tempo de execuçao:", time.strftime("%H : %M : %S", time.gmtime(end-start)),":{0:.0f}".format((end-start)*1000))

