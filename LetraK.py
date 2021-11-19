# Informar o nome do produto, saldo em estoque,
# preço de venda e a previsão de rentabilidade com a venda de cada produto.
# Rentabilidade: Saldo em estoque*preço de venda

import sqlite3

# Conexão com SGDB
conn = sqlite3.connect("PerfumariaABC_(Amanda-Clara-Francidalva).db")
cursor = conn.cursor()

# Preparar instrução SQL para enviar ao banco
isql = "Select dsprod, saldo,prvenda, (saldo * prvenda) as Rentabilidade from produto"

# Enviar instrução SQL para ser executada
cursor.execute(isql)

# Receber conjunto de dados retornado pelo Banco de dados
rs = cursor.fetchall()
print("\033[1m--- RESULTADOS OBTIDOS ---\033[m" )
for linha in rs:
    print("\033[1;34mNome:\033[m ", linha[0])
    print("\033[1;33mSaldo:\033[m ", linha[1])
    print("\033[1;32mPreço de venda:\033[m ", linha[2])
    print("\033[1;35mRentabilidade:\033[m ", linha[3])
    print(" ")
# Encerrar conexão
conn.close
quit()