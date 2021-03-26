"""
6) Altere o programa de forma que a mensagem saldo insuficiente seja
exibida caso haja tentativa de sacar mais dinheiro que o saldo disponível
(classe Conta).
"""

from contas import Conta
from clientes import Cliente
from bancos import Banco

banco = Banco("IF Bank")

jose = Cliente("José", "777-1234")
joao = Cliente("João", "555-4321")

c1 = Conta([jose], 150)
c2 = Conta([joao], 200)

banco.abre_conta(c1)
banco.abre_conta(c2)

c1.deposito(100)
c1.saque(150)
