# Programação II
# Prof. Dr. Adilson Ferreira da Silva
# Roteiro de Atividades - 04
# Alunas: Amanda de Caires Ferreira
#         Clara Simone dos Santos
#         Francidalva de Sousa Moura
# APLICAÇÃO PERFUMARIA ABC - TECHO DO CÓDIGO PARA CADASTRO DOS DADOS 
# ---------------------------------------------------------------------------------------------------------------

# importando biblioteca...
import sqlite3

# conectando banco de dados...
conn = sqlite3.connect("Perfumaria_ABC.db")

# definindo um cursor...
cursor = conn.cursor()

# ---------------------------------------------------------------------------------------------------------------
# inicio do programa: cadastro de dados no banco de trabalho
print("------------------------------------------------------------------------------------")
print("                          Tela de cadastro dos Produtos                             ")
print("------------------------------------------------------------------------------------")

# início do while loop
rescadastro = "S" # resposta pergunta cadastro
while rescadastro.upper() == "S":
    print("")
    codprod = input ("Insira CÓDIGO do produto: ")
    dsprod = input ("Insira DESCRIÇÃO do produto: ")
    saldo = input ("Insira SALDO ATUAL do produto: ")
    sldmin = input ("Insira SALDO MÍNIMO do produto: ")
    prvenda = input ("Insira PREÇO DE VENDA do produto: ")
    prcusto = input ("Insira PREÇO DE CUSTO do produto: ")
    print("")
    
    # inserindo dados no banco
    cursor.execute("""
    insert into produto (codprod, dsprod, saldo, sldmin, prvenda, prcusto)
    values (?,?,?,?,?,?)
    """, (codprod, dsprod, saldo, sldmin, prvenda, prcusto))
    conn.commit()
    print("")
    print("Dados cadastrados com sucesso")
    print("")
    rescadastro = input("Deseja fazer nova consulta? (Digite 'S' para sim ou qualquer tecla para sair)") 
# ---------------------------------------------------------------------------------------------------------------
# fim do while loop

# encerrando conexão...
conn.close()
quit()
