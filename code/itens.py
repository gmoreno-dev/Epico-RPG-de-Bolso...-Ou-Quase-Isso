import os
import time
from player import player

class Item:
    def __init__(self, nome, peso, descricao, quantidade):
        self.nome = nome
        self.peso = peso
        self.descricao = descricao
        self.quantidade = quantidade

class Mochila:
    def __init__(self, peso_maximo=100):
        self.peso_maximo = peso_maximo
        self.peso_atual = 0
        self.itens = []

    def adicionar_item(self, item):
        if self.peso_atual + item.peso <= self.peso_maximo:
            self.itens.append(item)
            self.peso_atual += item.peso
            print(f"Item '{item.nome}' adicionado à mochila.")
        else:
                print("Mochila cheia! Não é possível adicionar mais itens.")


    def remover_item(self, nome_item):
        for item in self.itens:
            if item.nome == nome_item:
                self.itens.remove(item)
                self.peso_atual -= item.peso
                print(f"Item '{item.nome}' removido da mochila.")
                return
        print(f"A quantidade de '{nome_item}' chegou a zero. 🚫")
        
    def exibir_itens(self):  # Agora dentro da classe Mochila
        if not self.itens:
            print("Mochila vazia.")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\n=== Inventário ===")
            for item in self.itens:
                print(f"- {item.nome} ({item.peso} kg): {item.descricao} (Quantidade: {item.quantidade})")
            print(f"\nPeso total: {self.peso_atual}/{self.peso_maximo} kg")

    def utilizar_itens(self):   
        global player
        print("\n=== Utilizar Itens ===")
        self.exibir_itens()
        if not self.itens:  # Verifica se a mochila está vazia
            print("Mochila vazia. Não há itens para utilizar.")
            return

        print("Digite o nome do item para utilizar (ou 'sair' para voltar): ")
        nome_item = input().lower()

        for item in self.itens:
            if item.nome.lower() == nome_item:
                os.system('cls' if os.name == 'nt' else 'clear')
                print(f"Utilizando '{item.nome}'...")
                time.sleep(1.5)

                match nome_item:
                    case 'poção de cura mixuruca':
                        player['hp'] += 25
                        print(f"Você foi curado! 💖 HP atual: {player['hp']}/{player['hp_max']}")
                    case 'sapo morto':
                        player['hp'] -= 5
                        print(f"Bolinhas surgiram em sua pele! -5 HP 🤢 HP atual: {player['hp']}/{player['hp_max']}")
                    case 'molho de chaves':
                        print('É um belo molho de chaves! +1 de Felicidade. 🗝️')
                    case _:
                        print("Você examina o item, mas não sabe como usá-lo.")

                item.quantidade -= 1
                if item.quantidade == 0:
                    time.sleep(1)  # Pequena pausa antes de remover o item
                    self.remover_item(nome_item)
                return  # Sai do loop após utilizar o item

        if nome_item != 'sair':
            print("Item não encontrado.")

    
