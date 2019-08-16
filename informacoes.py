print('Bem-vindo(a) ao GROGER BANK, para continuar cadatre as seguintes informações:''\n')
nome = input('Digite seu nome completo: ''\n')
idade = int( input('Digite sua idade: ''\n'))
saldo = float(input('Digite seu saldo: ''\n'))

def atm(nome, idade, saldo):
    janela = input("""
        Digite (1) para saque\n
        Digite (2) para deposito\n
        Digite (3) para emprestimo\n
        Digite (4) para ver as opções novamente
    """)
    if janela == 1:
        saque1(saldo)
        

    elif janela == 2:
        deposito(saldo)

    elif janela == 4:
        atm(nome, idade, saldo)

    else:
        print('erro')

def saque1 (saldo) :
    valor = float(input('Digite valor do saque: '))
    if valor <= 1000:
        print('saque permitido')
        saldo = saldo-valor
        return atm(nome, idade, saldo)


def deposito(saldo):
    valor = float(input('Digite o valor do deposito: '))
    if valor<5000:
        saldo= saldo+valor
        print('Deposito valido')
        return atm(nome, idade, saldo)

print(atm(nome, idade, saldo))