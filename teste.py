
conta = {"numero" : 123, "titular": "Jr", "saldo": 55.0, "limite": 1000.0}
conta2 = {"numero" : 321, "titular": "José", "saldo": 100.0, "limite": 2500.0}

print(conta2["saldo"])
print(conta)

def cria_conta(numero, titular, saldo, limite):
    conta = {"numero": numero, "titular": titular, "saldo": saldo, "limite": limite}
    return conta

from teste import cria_conta

conta = cria_conta(123, 'jr', 100, 5000)

print(conta)
