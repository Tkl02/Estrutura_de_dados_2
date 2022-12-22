
def ler_arquivo():
    with open('C:\\Users\\diasg\\Documents\\GitHub\\Estrutura_de_dados_2\\dados\\dados5.txt','r') as file:
        dados = file.read()
    arr = dados.replace("[","").replace("]","").split(",")
    return arr

def salver_arquivo(arr):
    with open('C:\\Users\\diasg\\Documents\\GitHub\\Estrutura_de_dados_2\\dados\\dados5.txt','w') as file:
        file.write(str(arr))