
Saldo = 0
import os
# O comando def é utilizado para definir uma função
def LimparConsole():
    os.system('cls')

def Instrucoes():
    print("Seja bem vindo ao sistema de conta bancaria em Python!")
    print("Digite 1 para consultar seu saldo.")
    print("Digite 2 para depositar em sua conta.")
    print("Digite 3 para sacar dinheiro")
    print("Digite 0 para sair do sistema")
    print("") # Espaço em branco para pular linha 

def Laco_Repeticao():
    global Saldo
    while True:
        Digito = input()
        Instrucoes()
        if Digito == '1':
            LimparConsole()
            print("O seu saldo é R$"+str(Saldo)+"")
            print("") # Espaço em branco para pular linha 
            Instrucoes()
        elif Digito == '2':
            LimparConsole()
            print("Digite o valor a ser depositado:")
            ValorDepositado = float(input())
            Saldo = Saldo + ValorDepositado
            LimparConsole()
            print("Voce depositou R$"+str(ValorDepositado)+" com sucesso")
            print("") # Espaço em branco para pular linha 
            Instrucoes()
        elif Digito == '3':
            LimparConsole()
            print("Digite o valor a ser sacado")
            print("") # Espaço em branco para pular linha 
            ValorSacado = float(input())
            if ValorSacado <= Saldo:
                LimparConsole()
                Saldo = Saldo - ValorSacado
                LimparConsole()
                print("Voce sacou R$"+str(ValorSacado)+" com sucesso!")
                print("") # Espaço em branco para pular linha 
                Instrucoes()
            elif ValorSacado > Saldo:
                LimparConsole()
                print("O valor a sacar é maior que o seu saldo. A operacao nao foi concluida.")
                print("") # Espaço em branco para pular linha 
                Instrucoes()
        elif Digito == '0':
            LimparConsole()
            print("Obrigado por utilizar nossos serviços!")
            break
        else:
            LimparConsole()
            print("Digito invalido.")
            print("") # Espaço em branco para pular linha 
            Instrucoes()

Instrucoes()
Laco_Repeticao()