from Conta import *

contaGui = ContaCorrente(15)
contaGui.depositar(500)

contaDani = ContaCorrente(47685)
contaDani.depositar(1000)

contas = [contaGui, contaDani]
for conta in contas:
    print(f'{conta}\n')