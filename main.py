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

        for animal in self.animais:
            if animal.id_animal == id_animal:
                return animal
        print(f"Animal com ID {id_animal} não encontrado!")


    def atualizar_animal(self, id_animal):
        for animal in self.animais:
            if animal.id_animal == id_animal:
                nome_novo = input("Novo nome:")
                idade_nova = int(input("Nova idade: "))
                especie_nova = input("Nova especie: ")
                raca_nova = input("Nova raça: ")

                animal.nome = nome_novo
                animal.idade = idade_nova
                animal.especie = especie_nova
                animal.raca = raca_nova
                print(f"Animal {nome_novo} atualizado!")
                return
        print(f"Animal com ID {id_animal} não encontrado!")    


    def remover_animal(self, id_animal):
        for animal in self.animais:
            if animal.id_animal == id_animal:
                excluir_animal = Animal(id_animal, nome, idade, especie, raca)
                self.animais.remove(excluir_animal)
                print(f"Animal {nome} excluido com sucesso!")
                return
        print(f"Animal com ID {id_animal} não encontrado!")


banco_de_dados = AnimaisDataBase()

banco_de_dados.criar.animal()