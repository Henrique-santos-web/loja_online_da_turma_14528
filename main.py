from Roupa import Roupa
from Eletronico import Eletronico
from Carrinho import CarrinhoDeCompras
import os
import time

TEMPO = 3

def exibir_menu():
    print("\n" + "="*45)
    print("🏪 MENU DA LOJA 🏪".center(45))
    print("="*45)
    print("[ 1 ] 👕 Adicionar Roupa")
    print("[ 2 ] 🔌 Adicionar Eletrônico")
    print("[ 3 ] 🛒 Ver Resumo do Carrinho")
    print("[ 0 ] 🚪 Sair do Sistema")
    print("="*45)

def main():

    carrinho = CarrinhoDeCompras()
    
    print("\n Bem-vindo ao Sistema de Gestão da Loja!")

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        os.system('cls' if os.name == 'nt' else 'clear')

        if opcao == "1":
            print("\n --- Cadastrando Roupa ---")
            nome = input("Nome da Roupa: ")

            try:
                preco = float(input("Preço: R$ "))
                tamanho = input("Tamanho: P|M|G: ").upper()
                nova_roupa = Roupa(nome, preco, tamanho)
                carrinho.adicionar_produto(nova_roupa)
                time.sleep(TEMPO)
                os.system('cls' if os.name == 'nt' else 'clear')
            except ValueError:
                print("⚠️ Erro: Por favor, digite um valor numérico válido para o preço.")
                time.sleep(TEMPO)
                os.system('cls' if os.name == 'nt' else 'clear')
        elif opcao == "2":
            print("\n ---   Cadastrando Eletrônico ---")
            nome = input("Nome do eletrônico: ")
            try:
                preco = float(input("Preço: R$ "))
                voltagem = input("Voltagem (ex: 110V/220V)")
                novo_eletronico = Eletronico(nome, preco, voltagem)
                carrinho.adicionar_produto(novo_eletronico)
                time.sleep(TEMPO)
                os.system('cls' if os.name == 'nt' else 'clear')
            except ValueError:
                print("⚠️ Erro: Por favor, digite um valor numérico válido para o preço.")
                time.sleep(TEMPO)
                os.system('cls' if os.name == 'nt' else 'clear')
            
        elif opcao == "3":
            carrinho.exibir_resumo()
            time.sleep(TEMPO)
            os.system('cls' if os.name == 'nt' else 'clear')

        elif opcao == "0":
            print("\n 👋 Encerrando o sistema. Até logo!\n")
            time.sleep(TEMPO)
            break
        else:
            print("\n⚠️ Erro: Opção inválida! Por favor, escolha um número de 0 a 3")
            time.sleep(TEMPO)
            os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()