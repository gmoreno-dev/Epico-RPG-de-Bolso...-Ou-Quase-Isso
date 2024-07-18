import random
from inimigos import lista_nomes
from player import player
lista_monstros = []

def criar_monstro(level):
    vida_max = int(random.randint(50, 100))
    novo_monstro = {
        'nome': random.choice(lista_nomes),
        'level': level,
        'ataque': level * 10,
        'defesa': level * 10,
        'vida': vida_max * level,
        'vida_max': vida_max * level,
        'exp': level * random.randint(50, 100) / 10
    }

    return(novo_monstro)

def gerar_monstros(n_monstros):
    nivel_monstro = [player['level'], player['level'] + 1, player['level'] + 2]
    for x in range(n_monstros):
        novo_monstro = criar_monstro(random.choice(nivel_monstro))
        lista_monstros.append(novo_monstro)

def exibir_monstros():

    for monstro in lista_monstros:
        print(f"Nome: {monstro['nome']}, Level: {monstro['level']}, Ataque: {monstro['ataque']}, Defesa: {monstro['defesa']}, Vida: {monstro['vida']}\n")
