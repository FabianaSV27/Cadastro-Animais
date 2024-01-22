class Animais:
    def __init__(self, id, nome, idade, especie, raca):
        self.id = id 
        self.nome = nome
        self.idade = idade

class CadastroAnimais(Animais):
    def __init__(self, id, nome, idade, especie, raca):
        super().__init__( id, nome, idade)
        self.especie = especie
        self.raca = raca

class AnimaisDataBase:
    def __init__(self):
        self.animal = []

    
