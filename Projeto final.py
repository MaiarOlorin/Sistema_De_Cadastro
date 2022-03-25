import ast
import os
from re import A 
import time
from modulos import *
def resgistro(): 
        resgistro_produtos["nome"] = str(input("Nome do produto: "))
        quantidade_estoque = str(input("Quantidade em estoque: "))
        while not quantidade_estoque.isdigit():
            quantidade_estoque = str(input("Quantidade em estoque: "))
        qe1 = int(quantidade_estoque)
        resgistro_produtos["Qnt.estoque"] = qe1
        custo_produto = str(input("Preço de custo: "))
        while not custo_produto.isdigit():
            custo_produto = str(input("Preço de custo: "))
        cp1 = int(custo_produto)   
        resgistro_produtos["custo"] = cp1
        preço_venda = str(input("Preço de venda: "))
        while not preço_venda.isdigit():
            preço_venda = str(input("Preço de venda: "))
        ve1 = int(preço_venda)
        resgistro_produtos["venda"] = ve1
        produtos_reg.append(resgistro_produtos.copy())
        return produtos_reg[0]  
produtos_reg = list()
resgistro_produtos = dict()
tot_valor_custo = 0
tot_valor_venda = 0
pro = ""
while True:
    op = menu()
    while not op.isdigit():
        op=menu()
    opc = int(op)
    if opc == 0:
        for t in range(3, 0, -1):
            print("\033[1;95m")
            print(f"Saindo do programa até a proxima... {t}")
            time.sleep(1)
        os.system('cls')
        print("\033[1;97m")
        break
    if opc == 1:
        print("\033[1;95m","                  Acessando opção de cadastro...")
        time.sleep(1)
        os.system('cls')
        while True:
            cad = selecao()
            while cad == 1:
                os.system('cls')
                teste = resgistro()
                arquivo = open("cadastro.txt", "a")
                arquivo.write(f'{teste}\n')
                produtos_reg.clear()
                arquivo.close()
                cad = selecao()
            if cad == 2:
                os.system('cls')
                break
    if opc == 2:
        print("\033[1;95m","                  Acessando opção de alteração...")
        time.sleep(1)
        os.system('cls')
        alr = selecao()
        while True:
            while alr  == 1:
                os.system('cls')
                print("=========================== PRODUTOS CADASTRADOS ===========================")
                arquivo = open('cadastro.txt')
                conteudo = arquivo.readlines()
                cont = 0
                for linha in conteudo:
                    linha = linha.replace("{","")
                    linha = linha.replace("}","")
                    print(f"[{cont}] {linha}")
                    cont += 1
                arquivo.close()   
                print("=============================================================================")  
                num_produto = int(input("Numero do produto: "))
                prod_selec = conteudo[num_produto].strip()
                print(f"Você selecionou: {prod_selec}")
                reg_produto = resgistro()
                troca_produto = str(reg_produto)
                arquivo = open("cadastro.txt", "r")
                substituir = ""
                for linha in arquivo:
                    linha = linha.strip()
                    alteração = linha.replace(prod_selec, troca_produto)
                    substituir = substituir + alteração + "\n"
                produtos_reg.clear()
                arquivo.close()
                arquivo = open("cadastro.txt", "w")
                arquivo.write(substituir)
                arquivo.close()
                print("Alteração concluida...")
                alr = selecao()
            if alr == 2:
                os.system('cls')
                break
    if opc == 3:
        os.system('cls')
        print("\033[1;95m","                  Acessando opção de exclusão...")
        time.sleep(1)
        exc =  selecao()
        if exc == 1:
            os.system('cls')
            print("=========================== PRODUTOS CADASTRADOS ===========================")
            arquivo = open('cadastro.txt')
            conteudo0 = arquivo.readlines()
            cont = 0
            for linha in conteudo0:
                linha = linha.replace("{","")
                linha = linha.replace("}","")
                print(f"[{cont}] {linha}")
                cont += 1
            arquivo.close()   
            print("=============================================================================")
            numero_excluir = int(input("Selecione o numero do produto que deseja excluir do sistema: "))
            excluir_selecionado = conteudo0[numero_excluir].strip()
            arquivo = open("cadastro.txt", "r")
            substituir = ""
            for linha in arquivo:
                linha = linha.strip()
                if linha != excluir_selecionado:
                    substituir = substituir + linha + "\n"
                aux = substituir.strip()
            arquivo.close()
            for t in range(3,-1,-1):
                print:tempo(f"Exclusão concluida em...{t}")
            arquivo = open("cadastro.txt", "w")
            arquivo.write(aux)
            arquivo.close()
            os.system('cls')            
    if opc == 4:
        print("\033[1;95m","                  Acessando opção de venda...")
        time.sleep(1)
        os.system('cls')
        ven = selecao()
        if ven == 1:
            os.system('cls')
            print("=========================== PRODUTOS CADASTRADOS ===========================")
            arquivo = open('cadastro.txt')
            conteudo2 = arquivo.readlines()
            cont = 0
            for linha in conteudo2:
                linha = linha.replace("{","")
                linha = linha.replace("}","")
                print(f"[{cont}] {linha}")
                cont += 1
            arquivo.close()   
            print("=============================================================================")
            numero_produto = int(input("Selecione o produto vendido: "))
            qnt_vendido = int(input("Quantidade vendida: ")) 
            produto_nome = conteudo2[numero_produto].strip()
            produto_alterado1 = produto_nome
            dicionario_produto = ast.literal_eval(str(produto_alterado1))
            if dicionario_produto["Qnt.estoque"] <= 0:
                print("Por favor selecione outro produto o atual se esgotou!")
                time.sleep(3)
                break 
            dicionario_produto["Qnt.estoque"] -= qnt_vendido
            volta_str = str(dicionario_produto)
            del dicionario_produto["nome"]
            del dicionario_produto["Qnt.estoque"]
            del dicionario_produto["custo"]
            del dicionario_produto["venda"]
            print(dicionario_produto)
            arquivo = open("cadastro.txt", "r")
            substituir = ""
            for linha in arquivo:
                linha = linha.strip()
                alteração = linha.replace(produto_nome, volta_str)
                substituir = substituir + alteração + "\n"
            arquivo.close()
            arquivo = open("cadastro.txt", "w")
            arquivo.write(substituir)
            arquivo.close()
            print("Operação concluida...")
            os.system('cls')
    if opc == 5:
        print("\033[1;95m","                  Acessando opção de compra...")
        time.sleep(1)
        os.system('cls')
        com = selecao()
        if com == 1:
            os.system('cls')
            print("=========================== PRODUTOS CADASTRADOS ===========================")
            arquivo = open('cadastro.txt')
            conteudo3 = arquivo.readlines()
            cont = 0
            for linha in conteudo3:
                linha = linha.replace("{","")
                linha = linha.replace("}","")
                print(f"[{cont}] {linha}")
                cont += 1
            arquivo.close()   
            print("=============================================================================")
            numero_produto2 = int(input("Selecione o produto comprado: "))
            qnt_comprada = int(input("Quantidade comprada: ")) 
            produto_nome2 = conteudo3[numero_produto2].strip()
            produto_alterado1 = produto_nome2
            dicionario_produto2 = ast.literal_eval(str(produto_alterado1))
            dicionario_produto2["Qnt.estoque"] += qnt_comprada
            volta_str2 = str(dicionario_produto2)
            del dicionario_produto2["nome"]
            del dicionario_produto2["Qnt.estoque"]
            del dicionario_produto2["custo"]
            del dicionario_produto2["venda"]
            arquivo = open("cadastro.txt", "r")
            substituir = ""
            for linha in arquivo:
                linha = linha.strip()
                alteração = linha.replace(produto_nome2, volta_str2)
                substituir = substituir + alteração + "\n"
            arquivo.close()
            arquivo = open("cadastro.txt", "w")
            arquivo.write(substituir)
            arquivo.close()                 
            print("Operação concluida...")
            os.system('cls')
    if opc == 6:
        print("\033[1;95m","                  Acessando opção de estoque...")
        time.sleep(1)
        os.system('cls') 
        es = selecao()
        if es == 1:
            estq = int(es)
            arquivo = open("cadastro.txt")
            conteudo4 = arquivo.readlines()
            lista_estoque = ""
            lista_estoque = list()
            for linha in conteudo4:
                lista_estoque.append(linha.strip())  
            lista_aux = list()   
            arquivo.close()     
            for k, v in enumerate(lista_estoque):
                mult = 0
                valor = 0
                lista_aux.append(lista_estoque[k])
                estoque_aux = lista_aux[0]
                lista_aux.pop(0)
                estoque_aux2 = str(estoque_aux)
                dicionario_estoque = ast.literal_eval(str(estoque_aux2))
                mult = dicionario_estoque["Qnt.estoque"]
                valor = dicionario_estoque["custo"]
                tot_valor_custo += mult * valor
                del dicionario_estoque
            print(f"Valor total de preço de custo dos produtos em estoque: R$ {tot_valor_custo}")
            for k, v in enumerate(lista_estoque):
                mult = 0
                valor = 0
                lista_aux.append(lista_estoque[k])
                estoque_aux = lista_aux[0]
                lista_aux.pop(0)
                estoque_aux2 = str(estoque_aux)
                dicionario_estoque = ast.literal_eval(str(estoque_aux2))
                mult = dicionario_estoque["Qnt.estoque"]
                valor = dicionario_estoque["venda"]
                tot_valor_venda += mult * valor
                del dicionario_estoque
            print(f"Valor total de preço de venda dos produtos em estoque: R$ {tot_valor_venda}")
            consul_especifica = input("Deseja colsultar um produto especifico? [S/N] ")
            os.system('cls')
            if consul_especifica in "Ss":
                mult1 = 0
                custo1 = 0
                venda1 = 0
                arquivo = open("cadastro.txt")
                conteudo5 = arquivo.readlines()
                lista_estoque = ""
                lista_estoque = list()
                cont = 0
                for linha in conteudo5:
                    linha = linha.replace("{","")
                    linha = linha.replace("}","")
                    print(f"[{cont}] {linha}")
                    cont += 1
                lista_aux = list()   
                arquivo.close()
                numero_produto4 = int(input("Selecione o numero produto que deseja consultar: ")) 
                produto_nome4 = conteudo5[numero_produto4].strip()
                estoque_alterado = produto_nome4
                dicionario_estoque3 = ast.literal_eval(str(estoque_alterado))
                mult1 = dicionario_estoque3["Qnt.estoque"]
                custo1 = dicionario_estoque3["custo"]
                venda1 = dicionario_estoque3["venda"]
                tot_valor_venda_especifica = mult1 * venda1
                tot_valor_custo_especifica = mult1 * custo1
                print(f'O valor de custo total do produto "{dicionario_estoque3["nome"]}" em estoque é: R$ {tot_valor_custo_especifica}')
                print(f'O valor de venda total do produto "{dicionario_estoque3["nome"]}" em estoque é: R$ {tot_valor_venda_especifica}')