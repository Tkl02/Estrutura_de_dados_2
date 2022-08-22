import random

class Pilha:
    def __init__(self):
        self.dados = []
        self.tamanho = 0

    def push(self, valor):
        self.dados.append(valor)
        self.tamanho += 1

    def pop(self):
        if self.tamanho == 0:
            return None
        else:
            self.tamanho -= 1
            return self.dados.pop()


if __name__ == "__main__":
    p = Pilha()

    for i in range(5):
        valor = random.randint(1, 10)
        p.push(valor)
        print("[{}]".format(valor))
    print("-" * 30)

    while p.tamanho > 0:
        print("[{}]".format(p.pop()))

    print("-" * 30)
    print("Pilha vazia")