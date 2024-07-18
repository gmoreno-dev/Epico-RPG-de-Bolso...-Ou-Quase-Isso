import time
import random
import os
from player import player, exibir_player
from monstro import lista_monstros
from itens import Mochila
from lista_itens import itens

def iniciar_batalha(monstro, mochila):
    global monstro_selecionado
    monstro_selecionado = monstro
    exibir_info_batalha(monstro)
    menu_batalha(mochila)

def menu_batalha(mochila):
   while player['hp'] > 0 and monstro_selecionado['vida'] > 0:
        
        escolha = str(input("\n1 - Atacar\n2 - Defender\n3 - Mochila\n4 - Fugir\nEscolha: "))
        
        if escolha == '1':

            atacar_monstro(monstro_selecionado)
            print(f'\n{monstro_selecionado['nome']} está preparando o ataque...')

            if monstro_selecionado['vida'] == 0:

                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"\n{monstro_selecionado['nome']} morreu!")
                print(f'Você ganhou {monstro_selecionado['exp']} EXP!')
                player['exp'] += monstro_selecionado['exp']
                dropar_pocao(mochila)
                exibir_player()
                lista_monstros.remove(monstro_selecionado)
                break

            elif player['hp'] == 0:
                
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"\n{player['nome']} morreu! :(")
                time.sleep(2)
                exit()

            else:
                    
                time.sleep(3)
                atacar_player(monstro_selecionado)

        elif escolha == '2':

            defesa_player()

        elif escolha == '3':
           
           mochila.utilizar_itens()

        elif escolha == '4':

            print(f"{player['nome']} Fugiu da batalha. 💨")
            break     

        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Opção inválida. Tente novamente.")
            continue


def defesa_player():
    tentativa_defesa = [1, 2]
    tentativa_defesa = random.choice(tentativa_defesa)
    global defesa
    match tentativa_defesa:
        case 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            defesa = True
            print(f"{player['nome']} defendeu-se. 🛡")
            time.sleep(2)
        case 2:
            os.system('cls' if os.name == 'nt' else 'clear')
            defesa = False
            print(f"{player['nome']} falhou na defesa. ❌")
            time.sleep(2)
            atacar_player(monstro_selecionado)
        case _:
            print("Opção inválida.")    
    

def atacar_player(monstro):
    os.system('cls' if os.name == 'nt' else 'clear')
    dano_causado_monstro = (monstro['ataque'] - random.randint(1, 10)) 
    player['hp'] -=  dano_causado_monstro
    print(f"\n{monstro_selecionado['nome']} atacou {player['nome']}. 💥")
    print(f"\n{player['nome']} recebeu {dano_causado_monstro} de dano!")

    if player['hp'] == 0:
                
                print(f"\n{player['nome']} morreu! :(")
                time.sleep(2)
                exit()

    exibir_info_batalha(monstro_selecionado)
    
def atacar_monstro(monstro):

    chance_crit = [1,2,3,4,5,6,7,8,9,10]
    critou = random.choice(chance_crit)
    
    if critou == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nAtaque mal executado!")
        monstro['vida'] -= player['ataque'] - 5
        print(f"\n{player['nome']} atacou {monstro_selecionado['nome']}. 💥")
        exibir_info_batalha(monstro_selecionado)

    elif critou == 10:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nAtaque crítico!")
        monstro['vida'] -= player['ataque'] * 2
        print(f"\n{player['nome']} atacou {monstro_selecionado['nome']}. 💥")
        exibir_info_batalha(monstro_selecionado)

    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        monstro['vida'] -= player['ataque']
        print(f"\n{player['nome']} atacou {monstro_selecionado['nome']}. 💥")
        exibir_info_batalha(monstro_selecionado)    

def exibir_info_batalha(monstro):

    if player['hp'] < 0:
        player['hp'] = 0
    elif monstro['vida'] < 0:
        monstro['vida'] = 0

    print("\n=== Batalha ===\n")
    print(f"{player['nome']} HP: {player['hp']}/{player['hp_max']} 🤺")
    print('👹🤺')
    print(f"{monstro['nome']}, Vida: {monstro['vida']}/{monstro['vida_max']}, Level: {monstro['level']}")    

def dropar_pocao(mochila):
    chance_drop = random.randint(1, 100)  # Chance de 13% 
    if chance_drop <= 13:
        for item in itens:
            if item.nome.lower() == "poção de cura mixuruca":
                mochila.adicionar_item(item)
                print(f"\nVocê recebeu duas {item.nome}!\n")
                break  # Sai do loop após encontrar e adicionar a poção