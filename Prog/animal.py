class Animal:
    def __init__(self, nome, especie, raca, idade, dono):
        self.nome = nome
        self.especie = especie
        self.raca = raca
        self.idade = idade
        self.dono = dono

    def __str__(self):
        return f"Nome: {self.nome}, Espécie: {self.especie}, Raça: {self.raca}, Idade: {self.idade}, Dono: {self.dono}"
