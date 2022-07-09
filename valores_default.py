import time

def imprime_nome(nome, sobrenome="Sabugosa"):
    print(f"Seu nome é {nome} {sobrenome}")

imprime_nome("Hermano", "Flavio")
imprime_nome("Linus")
    
def conecta(host, timeout=7):
    print("conectando com {host}")
    for i in range(0, timeout + 1):
        time.sleep(1)
        print("." * i)
    print("erro ao conectar..")

conecta("localhost", 5)
conecta("localhost")