names = ["Bruno", "Joao", "Bernardo", "Barbara", "Brian"]

print(*list(filter(lambda text: text[0].lower() == "b", names)), sep="\n")


