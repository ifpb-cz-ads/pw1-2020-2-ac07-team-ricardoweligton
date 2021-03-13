class Estado:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla
        self.cidades = []

    def abrange_cidade(self, cidade):
        self.cidades.append(cidade)

    def detalhes(self):
        print(f"\nNome: {self.nome}")
        print(f"Sigla: {self.sigla}")
        populacao = 0
        for cidade in self.cidades:
            populacao += cidade.populacao
        print(f"População: {populacao} habitantes")

    def cidades_abrangidas(self):
        print(f"\nCidades - {self.nome}")
        for cidade in self.cidades:
            cidade.detalhes()
