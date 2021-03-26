'''
3) Modifique a classe Televisão de forma que, se pedirmos para mudar o canal para baixo,
além do mínimo, ela vá para o canal máximo. Se mudarmos para cima, além do canal máximo,
que volte ao canal mínimo. Exemplo:

> > > tv=Televisão(2,10)
> > > tv.muda_canal_para_baixo()
> > > tv.canal
10
> > > tv.muda_canal_para_cima()
> > > tv.canal
2
'''

from televisao import Televisao

tv = Televisao(2, 10)

tv.muda_canal_para_baixo()
print(f"\nA TV esta sintonizada no canal {tv.canal}")
tv.muda_canal_para_cima()
print(f"\nA TV agora esta sintonizada no canal {tv.canal}")
