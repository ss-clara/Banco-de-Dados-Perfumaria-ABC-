# Programação II
# Prof. Dr. Adilson Ferreira da Silva
# Roteiro de Atividades - 04
# Alunas: Amanda de Caires Ferreira
#         Clara Simone dos Santos
#         Francidalva de Sousa Moura
# APLICAÇÃO PERFUMARIA ABC - TECHO DO CÓDIGO PARA CONCULTA DOS DADOS 
# ---------------------------------------------------------------------------------------------------------------

# importando biblioteca...
import sqlite3

# conectando banco de dados...
conn = sqlite3.connect("Perfumaria_ABC.db")

# definindo um cursor...
cursor = conn.cursor()

# ---------------------------------------------------------------------------------------------------------------
# inicio do programa: consulta aos dados no banco de trabalho
print("------------------------------------------------------------------------------------")
print("                     Tela de consulta aos dados dos Produtos                        ")
print("------------------------------------------------------------------------------------")

# início do while loop
resconsulta = "S"
while resconsulta.upper() == "S":
    print("")
    print("------------------------------------------------------------------------------------")
    codprod = input ("Insira CÓDIGO do produto: ")
    print("------------------------------------------------------------------------------------")
    print ("")
    # lendo dados do banco...
    cursor.execute("select * from produto where codprod = " + codprod)
    # mostrando dados na tela... 
    resultado_consulta = cursor.fetchone()
    if resultado_consulta[0] > 0:
        print("Código de produto cadastrado!")
        print("Descrição: ", resultado_consulta[1])
        print("Saldo Atual: ", resultado_consulta[2], " Unidades")
        print("Saldo Mínimo: ", resultado_consulta[3], " Unidades")
        print("Preço de Venda: R$ ", resultado_consulta[4])
        print("Preço de Custo: R$ ", resultado_consulta[5])
        print("")
    else:   
        print ("Produto não cadastrado!") #MELHORAR ESSA PARTE  
    print("")
    resconsulta = input("Deseja fazer nova consulta? (Digite 'S' para sim ou qualquer tecla para sair)")
# ---------------------------------------------------------------------------------------------------------------
# fim do while loop

# encerrando conexão...
conn.close()
quit()
