
from dataclasses import replace


insfos =['nome:','leonardo dias', 'algoritimo:', 'slect/insert sort']

arr = insfos
with open ("insert ordenado.txt", "w") as arquivo:
    arquivo.write("{}".format(arr+insfos))
