class Cidade:
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao

    def detalhes(self):
        print(f"\nNome: {self.nome}")
        print(f"População: {self.populacao}")