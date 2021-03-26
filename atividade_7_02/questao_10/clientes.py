class Cliente:
    def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone

    def dados(self):
        print(f"\nNome: {self.nome}")
        print(f"Telefone: {self.telefone}")