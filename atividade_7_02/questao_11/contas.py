class Conta:
    def __init__(self, clientes, número, saldo=0):
        self.saldo = 0
        self.clientes = clientes
        self.número = número
        self.operações = []
        self.deposito(saldo)

    def resumo(self):
        print("\nCC N°%s Saldo: %10.2f" %
              (self.número, self.saldo))

        for cliente in self.clientes:
            cliente.dados()

    def verifica_saque(self, saldo, valor):
        if valor <= saldo:
            return True
        return False

    def saque(self, valor):
        if self.verifica_saque(self.saldo, valor):
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])
            return True
        print("Saldo insuficiente!")
        return False

    def deposito(self, valor):
        self.saldo += valor
        self.operações.append(["DEPÓSITO", valor])

    def extrato(self):
        print("Extrato CC N° %s\n" % self.número)

        for o in self.operações:
            print("%10s %10.2f" % (o[0], o[1]))

        print("\n       Saldo: %10.2f\n" % self.saldo)


class ContaEspecial(Conta):
    def __init__(self, clientes, número, saldo=0, limite=0):
        Conta.__init__(self, clientes, número, saldo)
        self.limite = limite

    def saque(self, valor):
        if self.verifica_saque(self.saldo + self.limite, valor):
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])
            return True
        return False

    def extrato(self):
        print("Extrato CC N° %s\n" % self.número)

        for o in self.operações:
            print("%10s %10.2f" % (o[0], o[1]))

        print("\n       Limite: %10.2f" % self.limite)
        print("       Saldo: %11.2f" % self.saldo)
        print("       Disponível: %0.2f" % (self.saldo + self.limite))
