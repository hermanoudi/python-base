#!/usr/bin/env python3
numeros = range(1, 10)
impares = []
pares = []

for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 != 0:
        impares.append(n)
    else:
        print("nem par e nem impar")
print("Pares: ")
print(pares)

print()

print("Impares: ")
print(impares)

    