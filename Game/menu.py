import random
import os
from player import player, exibir_player, level_up
from monstro import lista_monstros, gerar_monstros
from batalha import iniciar_batalha

def menu(mochila):
    global escolha
    escolha = 0
    nome_player = str(input('Insira seu nome de aventureiro: '))
    while (escolha != 2):  # Loop principal do menu
        player['nome'] = nome_player
        print("\n=== Menu ===")
        print("1. Iniciar Batalha")
        print("2. Sair")
        escolha = input('Opção Escolhida: ')

        if escolha == '1' and player['hp'] != 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            global monstro_selecionado
            monstro_selecionado = random.choice(lista_monstros)  # Escolhe um monstro aleatório
            iniciar_batalha(monstro_selecionado, mochila)
            level_up(player['level'])  # Verifica se há level up após a batalha
        elif escolha == '2':
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Saindo do jogo...")
            exit() 
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Opção inválida. Tente novamente.")