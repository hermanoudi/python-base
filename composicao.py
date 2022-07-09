names = ["Hermano", "Luzia", "Jose", "Hugo", "Sebastião", "Manoelina", "Danilo", "Danilo"]

# TODO: Usar lambas

def isStartsWithH(nome):
    if nome.lower().startswith("d"):
        return True
    else:
        return False

print(*list(filter(isStartsWithH, names)))


