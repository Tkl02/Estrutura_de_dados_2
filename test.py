import re

n = input("?")
n = re.sub('[^0-9]', '', n)

def imprime(n):
    if n == 0:
        return
    print("recursividade")
    imprime(n-1)
    
if __name__ == "__main__":
    imprime(int(n))