def menu():
    print("\033[1;34m","=-"*10,"Escolha a opção desejada", "-="*10)
    print("\033[0;32m","""
                      Cadastro de Produtos.[1]
                      Alterar Produtos.....[2] 
                      Excluir Produtos.....[3] 
                      Venda de Produtos....[4]
                      Compra de Produtos...[5] 
                      Colsultar estoque....[6]                       
                      Sair do programa.....[0]
""")
    print("\033[1;34m","=-"*9, "Por favor digite um numero", "-="*10)
    a = (input("Digite um dos numeros para acessar as funcionalidades do programa: "))
    return(a)
def print2():
    print("")
    print("")
    print("")
    print("")
    print("")
    print("")
def cadastro():
    import os 
    os.system('cls')
    print("""                        Escolha sua opção 
                   ===========================""")
    print2()
    print("\033[1;36m","                  Continuar..[1]")
    print("\033[1;31m" ,"                  Voltar.....[2]")
    print("\033[1;34m")
    a = input("                   Digite a opção desejada: ")
    print("\033[0;32m")
    return(a)
def selecao():
    ca = cadastro()
    while not ca.isdigit():
        ca = cadastro()
    cad = int(ca)
    return (cad)

def tempo(x):
    import time
    time.sleep(1)
    print(x)