import sqlite3
#fazendo conexão com SGDB
conn = sqlite3.connect("PerfumariaABC_(Amanda-Clara-Francidalva).db")
cursor = conn.cursor()

#identificação do menu
print ("----------------------------------------------------------------")
print ("               Tela de cadastro de novos produtos               ")
print ("----------------------------------------------------------------")
    
while True:
    #Entrada de dados para serem cadastrados
    print ("")
    print ("----------------------------------------------------------------")
    codprod = input ("Insira CÓDIGO do produto: (digite 000 para encerrar)")

    if codprod == "000":
        break

    isql = "Select count(*), dsprod, saldo, sldmin, prvenda, prcusto from produto where codprod = " + codprod
    cursor.execute(isql)
    rs = cursor.fetchone()
    if rs[0] > 0:
        print ("")
        print ("Código de produto já cadastrado!")
        print ("")
        print ("DESCRIÇÃO: ", rs[1])
        print ("SALDO ATUAL: ", rs[2])
        print ("SALDO MÍNIMO: ", rs[3])
        print ("PREÇO DE CUSTO: ", rs[4])
        print ("PREÇO DE VENDA: ", rs[5])
        continue

    dsprod = input ("Insira DESCRIÇÃO do produto: ")
    saldo = input ("Insira SALDO ATUAL do produto: ")
    sldmin = input ("Insira SALDO MÍNIMO do produto: ")
    prcusto = input ("Insira PREÇO DE CUSTO do produto: ")
    prvenda = input ("Insira PREÇO DE VENDA do produto: ")

#contrução de instrução SQL para cadastramento dos dados do produto
#(método: concatenação de string)
    isql = ""
    isql = isql + " insert into produto (codprod, dsprod, saldo, sldmin, prvenda, prcusto)"
    isql = isql + " values ("
    isql = isql + codprod + ","
    isql = isql + "'" + dsprod + "'" + ","
    isql = isql + saldo + ","
    isql = isql + sldmin + ","
    isql = isql + prcusto + ","
    isql = isql + prvenda + ");"
    print(isql)

## Envia a instrução SQL para ser executada pelo SGDB e efetivar a transação
    cursor.execute(isql)
    conn.commit()
    
## Fechar conexão
conn.close
quit()
