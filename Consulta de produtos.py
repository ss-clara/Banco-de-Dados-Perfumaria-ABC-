import sqlite3
#fazendo conexão com SGDB
conn = sqlite3.connect("PerfumariaABC_(Amanda-Clara-Francidalva).db")
cursor = conn.cursor()

print ("----------------------------------------------------------------")
print ("                  Tela de consulta de produtos                  ")
print ("----------------------------------------------------------------")
print ("")
resposta = "S"
#LOOP
while resposta.upper() == "S":
    print ("")
    print ("----------------------------------------------------------------")
    codprod = input ("Insira CÓDIGO do produto: ")
    isql = "Select count(*), dsprod, saldo, sldmin, prvenda, prcusto from produto where codprod = " + codprod
    cursor.execute(isql)
    rs = cursor.fetchone()
    if rs[0] > 0:
        print ("Código de produto cadastrado!")
        print ("DESCRIÇÃO: ", rs[1])
        print ("SALDO ATUAL: ", rs[2])
        print ("SALDO MÍNIMO: ", rs[3])
        print ("PREÇO DE CUSTO: ", rs[4])
        print ("PREÇO DE VENDA: ", rs[5])
        print ("")
    resposta = input ("Deseja fazer nova consulta? (Digite 'S' para sim ou qualquer tecla para sair)")

## Envia a instrução SQL para ser executada pelo SGDB e efetivar a transação
cursor.execute(isql)
conn.commit()
## Fechar conexão
conn.close
quit()
