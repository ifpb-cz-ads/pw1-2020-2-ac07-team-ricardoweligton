"""
10) Altere a classe ContaEspecial de forma que seu extrato exiba o limite
e o total disponível para saque.
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
print()
print(c2.saque(500))
print()
print(c2.saque(300))

c2.extrato()
