# SOLID - Single Responsibility
def funcao(*args, timeout=10, **kwargs):
    for item in args:
        print(item)
    print(kwargs)
    print(f"timeout {timeout}")

funcao("HERMANO", 1, True, [], 99, timeout=90, nome="JOAO", cidade="Uberlandia", data="hoje", teclado=True, banana=5, panela=2)