#Listar código e nome de todos os produtos que estão com preço de venda menor ou igual a zero.

import sqlite3

# Conexão com SGDB
conn = sqlite3.connect("PerfumariaABC_(Amanda-Clara-Francidalva).db")
cursor = conn.cursor()

# Preparar instrução SQL para enviar ao banco
isql = "Select codprod, dsprod from produto where prvenda <= 0"

# Enviar instrução SQL para ser executada
cursor.execute(isql)

# Receber conjunto de dados retornado pelo Banco de dados
rs = cursor.fetchall()
print("\033[1m--- RESULTADOS OBTIDOS ---\033[m" )
for linha in rs:
    print("\033[1;34mCódigo:\033[m ", linha[0])
    print("\033[1;33mNome:\033[m ", linha[1])
    print(" ")
# Encerrar conexão
conn.close
quit()