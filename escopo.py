# aqui começa o escopo global

nome = "Global"

# print(globals())

def funcao():
    # aqui começa o escopo local
    nome = "Local"

    def funcao_interna(): # inner function    # closure
        # aqui começa o escopo local da funcao interna
        nome = "interna"
        # print("Escopo local da funcao interna: ", locals())
        # print("-" * 30)
        print(nome)
        return nome
        #aqui termina o escopo local da funcao interna

    # print("Escopo local da funcao: ", locals())
    funcao_interna()
    # print(locals()["nome"])
    print(nome)
    return nome
    # aqui termina o escopo local

# print("Escopo global do programa", globals())
# print("-" * 30)
funcao()
print(nome)

