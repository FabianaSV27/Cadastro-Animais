class CadastroAnimais:
    def __init__(self, id_cadastro, nome, idade, especie, raca):
        self.id_cadastro = id_cadastro 
        self.nome = nome
        self.idade = idade

class Animal(CadastroAnimais):
    def __init__(self, id_animal, nome, idade, especie, raca):
        super().__init__( id_animal, nome, idade)
        self.especie = especie
        self.raca = raca

class AnimaisDataBase:
    def __init__(self):
        self.animais = []

     
    def registro_animais(self):

        id_animal = int(input("Digite o ID do animal: "))
        nome = input("Nome do Animal: ")
        idade = int(input("Idade do Animal: "))
        especie = input("Especie do Animal: ")
        raca = input("Raça do animal:")

        novo_animal = Animal(id_animal, nome, idade, especie, raca)
        self.animais.append(novo_animal)
        print(f"Animal {nome} registrado com sucesso!")

    def ler_animal(self, id_animal):

        for animal in self.animal:
            if animal.id_animal == id_animal:
                return animal
