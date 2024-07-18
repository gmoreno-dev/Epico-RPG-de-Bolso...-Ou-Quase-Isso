import os
import time

player = {
    'nome': 'player',
    'level': 1,
    'exp': 0,
    'exp_max': 30,
    'ataque': 45,
    'defesa': 30,
    'hp': 100,
    'hp_max': 100,
    'moedas': 0,
    'armas': [] 
}

def exibir_player():

    print(f"Nome: {player['nome']}, Level: {player['level']}, Ataque: {player['ataque']}, Defesa: {player['defesa']}, Vida: {player['hp']}/{player['hp_max']}, EXP: {player['exp']}/{player['exp_max']}\n")

def level_up(level):

    if player['exp'] >= player['exp_max']:

        player['level'] += 1
        player['exp'] = 0
        player['exp_max'] = player['exp_max'] * 2
        player['ataque'] += 15
        player['defesa'] += 15
        player['hp_max'] += 100
        player['hp'] = player['hp_max']

        time.sleep(1.5)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\nLevel up! Você agora está no level {player['level']}")
        exibir_player()
