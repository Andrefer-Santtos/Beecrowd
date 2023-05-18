# Source code example - atividade de listas com py

import random
lista1 = [0]*10
i = 0

while i < len(lista1):
    lista1[i] = random.randint(0, 563)
    i = i + 1

i = 0
conta = 0
while i < len(lista1):
    if lista1[i] % 2 == 0:
        conta = conta+1
    i = i+1
print(i)
print(conta)
print("Quantidade de números pares %d " % conta)
