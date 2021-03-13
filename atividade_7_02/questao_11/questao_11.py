"""
11) Observe o método saque das classes Conta e ContaEspecial. Modifique o
método saque da classe Conta de forma que a verificação da possibilidade
de saque seja feita por um novo método, substituindo a condição atual.
Esse novo método retornará verdadeiro se o saque puder ser efetuado, e
falso em caso contrário. Modifique a classe ContaEspecial de forma a
trabalhar com esse novo método. Verifique se você ainda precisa trocar o
método saque de ContaEspecial ou apenas o novo método criado para
verificar a possibilidade de saque.
"""

from contas import Conta, ContaEspecial
from clientes import Cliente
from bancos import Banco

banco = Banco("IF Bank")

jose = Cliente("José", "777-1234")
joao = Cliente("João", "555-4321")

c1 = Conta([jose], 150)
c2 = ContaEspecial([joao], 200, 0, 500)

banco.abre_conta(c1)
banco.abre_conta(c2)

c1.deposito(100)
c2.deposito(200)

banco.lista_contas()

print()
print(c1.saque(50))
print()
print(c1.saque(100))

c1.extrato()

print()
print(c2.saque(500))
print()
print(c2.saque(300))

c2.extrato()
