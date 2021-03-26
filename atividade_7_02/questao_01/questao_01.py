'''
1) Adicione os atributos tamanho e marca à classe Televisão. Crie dois objetos
Televisão e atribua tamanhos e marcas diferentes. Depois, imprima o valor desses
atributos de forma a confirmar a independência dos valores de cada instância (objeto).
'''

from televisao import Televisao

tv1 = Televisao("Samsung", 50)
tv2 = Televisao("LG", 43)
tv1.tv_info()
tv2.tv_info()
