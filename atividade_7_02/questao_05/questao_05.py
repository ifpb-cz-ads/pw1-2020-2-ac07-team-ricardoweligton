'''
5) Utilizando a classe Televisão modificada no exercício anterior, crie
duas instâncias (objetos), especificando o valor de min e max por nome.
'''

from televisao import Televisao

tv1 = Televisao(min=2, max=10)
tv2 = Televisao(min=5, max=20)

print(f"Canal minimo da primeira TV: {tv1.min}\n"
      f"Canal maximo da primeira TV: {tv1.max}\n")

print(f"Canal minimo da segunda TV: {tv2.min}\n"
      f"Canal maximo da segunda TV: {tv2.max}")
