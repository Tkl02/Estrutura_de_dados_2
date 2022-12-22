from algoritimos import *

def ler_arquivo():
    with open('C:\\Users\\diasg\\Documents\\GitHub\\Estrutura_de_dados_2\\dados\\dados5.txt','r') as file:
        dados = file.read()
    arr = dados.replace("[","").replace("]","").split(",")
    return arr

def salvar_arquivo(arr):
    nome = "Leonardo Faustino"
    nomeAlgoritimo = "xxxxxxx"
    with open('C:\\Users\\diasg\\Documents\\GitHub\\Estrutura_de_dados_2\\dados\\dados5.txt','w') as file:
        file.write("{}\n{}{}\n{}{}"format(dados,nome,nomeAlgoritimo,numeroTrocas,numeroComp))
        
