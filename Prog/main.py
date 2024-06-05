from petshop import PetShop
import os
import time

def main():
    petshop = PetShop()

    def exibir_menu():
        print("Selecione a opção desejada: ")
        print("[1] - Adicionar animal")
        print("[2] - Excluir animal")
        print("[3] - Pesquisar animal")
        print("[4] - Exibir animais")
        print("[5] - Quantidade de raças e espécies")
        print("[6] - Pesquisar donos dos animais")
        print("[0] - Finalizar programa")

    while True:
        exibir_menu()
        opcao = input("Selecione a opção desejada a ser processada: ")
        match opcao:
            case "1":
                os.system('cls')
                print("Adição de animal \n")  
                nome = input("Insira o nome do animal: ")
                especie = input("Insira a especie do animal: ")
                raca = input("Insira a raca do animal: ")
                idade = input("Insira a idade do animal: ")
                dono = input("Insira o nome do dono: ")
                os.system('cls')                
                petshop.adicionar_animais(nome, especie, raca, idade, dono)
                time.sleep(1)
                os.system('cls')

            case "2":
                os.system('cls')
                print("Exlusão de animal \n")
                nome = input("Insira o animal a ser excluído: ")
                animal = petshop.excluir_animais(nome)
                if animal:
                    os.system('cls')
                    print("Erro na exclusão.")
                    time.sleep(1)
                    os.system('cls')
                else:
                    os.system('cls')
                    print("Animal excluído.")
                    time.sleep(1)
                    os.system('cls')      
            case "3":
                os.system('cls')
                print("Pesquisa de animal \n")
                nome = input("Insira o animal a ser pesquisado: ")
                animal = petshop.pesq_animais(nome)
                if animal:
                    os.system('cls')
                    print(animal)
                    time.sleep(3)
                    os.system('cls')
                else:
                    os.system('cls')
                    print("Animal não encontrado.")
                    time.sleep(1.5)
                    os.system('cls')   
            case "4":   
                 print("Lista de animais \n")
                # animais = petshop.exibir_animais()
                # for animal in animais:
                #     print(animal)                
            case "5":
                print("Quantidade de Racas/Espécies")  
            case "6":
                print("Pesquisa de dono \n")
            case "0":
                print("Func. Finalizar")

if __name__ == "__main__":
   main()
        
