import random
import os
from menu import menu
from monstro import gerar_monstros
from itens import Mochila
from lista_itens import itens

mochila = Mochila()

def main():
    
      # Função principal para encapsular o jogo
    gerar_monstros(25)
    
    # Adicionar os 3 primeiros itens da lista à mochila
    for item in itens[:3]:
        
        mochila.adicionar_item(item)
    os.system('cls' if os.name == 'nt' else 'clear')
    menu(mochila)

if __name__ == "__main__":  # Ponto de entrada do script

    main()