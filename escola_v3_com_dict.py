#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.

Imprimir a lista de crianças agrupadas por sala 
que frequenta cada uma das atividades.
"""
__version__ = "0.1.1"

dados = {
    "sala1" : ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Joana"],
    "sala2" : ["João", "Antonio", "Carlos", "Maria", "Isolda"],
}

atividades = {
    "aula_ingles"  : ["Erik", "Maia", "Joana", "Carlos", "Antonio"],
    "aula_musica" : ["Erik", "Carlos", "Maria"],
    "aula_danca" : ["Gustavo", "Sofia", "Joana", "Antonio"],

}

# Listar alunos em cada atividade por sala
for nome_atividade, aluno in atividades.items():
    print(f"Alunos da atividade {nome_atividade}\n")
    print("#" * 40)
    # sala1 que tem interseção com a atividade
    atividade_sala1 = set(dados["sala1"]) & set(aluno)
    atividade_sala2 = set(dados["sala2"]).intersection(set(aluno))

    print("sala1 ", atividade_sala1)
    print("sala2 ", atividade_sala2)
    print()
    print("#" * 40)
 
