from animal import Animal

class PetShop:
    def __init__(self):
        self.animais = []

    def adicionar_animais(self,nome,especie,raca,idade,dono):
        animal = Animal(nome, especie, raca, idade, dono)
        self.animais.append(animal)
        print(f"Animal '{animal.nome}' adicionado com sucesso!")

    def excluir_animais(self,nome):
        for animal in self.animais:
            if animal.nome == nome:
                self.animais.remove(animal)
    
    def pesq_animais(self, nome):
        for animal in self.animais:
            if animal.nome == nome:
                return animal
        return None

    # def exibir_animais(self):
    #     return self.animais
