# Programação II
# Prof. Dr. Adilson Ferreira da Silva
# Roteiro de Atividades - 04
# Alunas: Amanda de Caires Ferreira
#         Clara Simone dos Santos
#         Francidalva de Sousa Moura
# APLICAÇÃO PERFUMARIA ABC - TECHO DO CÓDIGO PARA ALTERAÇÃO DOS DADOS 
# ---------------------------------------------------------------------------------------------------------------

# importando biblioteca...
import sqlite3

# conectando banco de dados...
conn = sqlite3.connect("Perfumaria_ABC.db")

# definindo um cursor...
cursor = conn.cursor()

# ---------------------------------------------------------------------------------------------------------------
# inicio do programa: alteração de dados no banco de trabalho
print("------------------------------------------------------------------------------------")
print("                     Tela de alteração de dados dos Produtos                        ")
print("------------------------------------------------------------------------------------")

# início do while loop
resalteracao = "S"
while resalteracao.upper() == "S":
    print("")
    print("------------------------------------------------------------------------------------")
    codprod = input("Insira CÓDIGO do produto: ")
    print(codprod)  # MELHORAR ESSA PARTE DO CÓDIGO
    print("")
    print("------------------------------------------------------------------------------------")
    print("digite [1] Para mudar DESCRIÇÃO do produto")
    print("digite [2] Para mudar SALDO ATUAL do produto")
    print("digite [3] Para mudar SALDO MÍNIMO do produto")
    print("digite [4] Para mudar PREÇO DE VENDA do produto")
    print("digite [5] Para mudar PREÇO DE CUSTO do produto")
    print("digite [6] Para DELETAR produto")
    print("------------------------------------------------------------------------------------")
    escolhamalt = int(input("digite sua escolha: "))
    print("------------------------------------------------------------------------------------")
    print("")
    if escolhamalt == 1:
        n_dsprod = input("Insira nova DESCRIÇÃO do produto: ")
        cursor.execute("UPDATE produto SET dsprod = '" + n_dsprod + "' where codprod = " + codprod + ";")
        conn.commit()
    elif escolhamalt == 2:
        n_saldo = input("Insira novo SALDO ATUAL do produto: ")
        cursor.execute("UPDATE produto set saldo = '" + n_saldo + "' where codprod = " + codprod + ";")
        conn.commit()
    elif escolhamalt == 3:
        n_sldmin = input("Insira novo SALDO MÍNIMO do produto: ")
        cursor.execute("UPDATE produto set sldmin = '" + n_sldmin + "' where codprod = " + codprod + ";")
        conn.commit()
    elif escolhamalt == 4:
        n_prvenda = input("Insira novo PREÇO DE VENDA do produto: ")
        cursor.execute("UPDATE produto set prvenda = '" + n_prvenda + "' where codprod = " + codprod + ";")
        conn.commit()
    elif escolhamalt == 5:
        n_prcusto = input("Insira novo PREÇO DE CUSTO do produto: ")
        cursor.execute("UPDATE produto set prcusto = '" + n_prcusto + "' where codprod = " + codprod + ";")
        conn.commit()
    elif escolhamalt == 6:
        cursor.execute("DELETE from produto where codprod = " + codprod + ";")
        conn.commit()
        print("")
        print("Item deletado com sucesso!")
    else:
        print("opção inválida!") # MELHORAR ESSA PARTE
    print("")
    print("Banco de dados atualizado com sucesso!")
    print("")
    resalteracao = input("Deseja fazer nova alteração? (Digite 'S' para sim ou qualquer tecla para sair)")
# ---------------------------------------------------------------------------------------------------------------
# fim do while loop

# encerrando conexão...
conn.close()
quit()
