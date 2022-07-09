"""Exemplos de funções"""
"""
f(x) = 5 * (x / 2)
"""

# SOLID - Single Responsibility

def f(x): #assinatura
    result = 5 * (x /2)
    return result

def double(x):
    return x * 2

valor = double(f(10))

valor = f(10)

print(valor)
print(f(10) == 25)

###
# Procedimentos / Procedures
# Procedure with no explicit return
def print_in_upper(text):
    print(text.upper())

print_in_upper("Hermano")

"""Calcula a area de um triangulo"""
def heron(a, b, c):
    perimeter = a + b + c 
    s = perimeter / 2
    area = s * (s - a) * (s - b) * (s - c)
    return area ** 0.5 # math.sqrt(area)

"""Calcula a area de um triangulo"""
def heron2(params):
    a, b, c = params
    return heron(*params)

triangulos = [
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (12, 35, 37),
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (12, 35, 37)
]

print(list(map(heron2, triangulos)))

for t in triangulos:
    area = heron2(t)
    print(f"A area do triangulo é: {area}")

