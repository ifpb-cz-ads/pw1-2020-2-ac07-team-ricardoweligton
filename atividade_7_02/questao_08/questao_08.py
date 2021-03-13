"""
8) Crie classes para representar estados e cidades. Cada estado tem um
nome, sigla e cidades. Cada cidade tem nome e população. Escreva um
programa de testes que crie três estados com algumas cidades em cada um.
Exiba a população de cada estado como a soma da população de suas cidades.
"""

from cidades import Cidade
from estados import Estado

cidade1 = Cidade("Cajazeiras", 62000)
cidade2 = Cidade("Sousa", 65000)
cidade3 = Cidade("São José de Piranhas", 20000)

estado = Estado("Paraíba", "PB")

estado.abrange_cidade(cidade1)
estado.abrange_cidade(cidade2)
estado.abrange_cidade(cidade3)

estado.detalhes()
estado.cidades_abrangidas()
