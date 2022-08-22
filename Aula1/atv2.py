def posfixa(prefixa):
    prefixa = prefixa.split()
    operandos = []
    operadores = []

    for i in prefixa:
        if i == '+' or i == '-' or i == '*' or i == '/':
            operadores.append(i)
        else:
            operandos.append(i)

    posfixa = ''
    for i in range(len(prefixa)):
        if prefixa[i] == '+' or prefixa[i] == '-' or prefixa[i] == '*' or prefixa[i] == '/':
            posfixa += operandos.pop() + ' ' + operandos.pop() + ' ' + operadores.pop() + ' '
        else:
            posfixa += prefixa[i] + ' '

    posfixa = posfixa.split()
    posfixa.reverse()
    posfixa = ' '.join(posfixa)
    return posfixa

def prefixa(posfixa):
    posfixa = posfixa.split()
    operandos = []
    operadores = []

    for i in posfixa:
        if i == '+' or i == '-' or i == '*' or i == '/':
            operadores.append(i)
        else:
            operandos.append(i)

    prefixa = ''
    for i in range(len(posfixa)):
        if posfixa[i] == '+' or posfixa[i] == '-' or posfixa[i] == '*' or posfixa[i] == '/':
            prefixa += operadores.pop() + ' ' + operandos.pop() + ' ' + operandos.pop() + ' '
        else:
            prefixa = posfixa[i] + ' ' + prefixa

    prefixa = prefixa.split()
    prefixa = ' '.join(prefixa)
    return prefixa

prefixa = input("Digite a equação na forma prefixa: ")
posfixa = input("Digite a equação na forma posfixa: ")

prefixa = posfixa(prefixa)
posfixa = prefixa(posfixa)

print("Equação na forma prefixa:", prefixa)
print("Equação na forma posfixa:", posfixa)