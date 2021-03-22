'''
5) Utilizando a classe Televisão modificada no exercício anterior, crie
duas instâncias (objetos), especificando o valor de min e max por nome.
'''

from televisao import Televisao

tv1 = Televisao("dois", "dez")
tv2 = Televisao("cinco", "vinte")

print(f"Canal mínimo da primeira TV: {tv1.canal_min}\n"
      f"Canal máximo da primeira TV: {tv1.canal_max}\n")

print(f"Canal mínimo da segunda TV: {tv2.canal_min}\n"
      f"Canal máximo da segunda TV: {tv2.canal_max}")
