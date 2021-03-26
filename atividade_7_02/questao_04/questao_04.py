'''
4) Utilizando o que aprendemos com funções, modifique o construtor da classe Televisão
de forma que min e max sejam parâmetros opcionais, onde min vale 2 e max vale 14, caso
outro valor não seja passado.
'''

from televisao import Televisao

tv = Televisao()

print(f"{tv.canal_min}, {tv.canal_max}")
