# Listar nome e preço de venda dos produtos em ordem alfabética pelo nome

import sqlite3
    #Conexão com SGDB
conn = sqlite3.connect("PerfumariaABC_(Amanda-Clara-Francidalva).db")
cursor = conn.cursor()
 
# Preparar instrução SQL para enviar ao banco
isql = "Select dsprod, prvenda from produto order by dsprod"

# Enviar instrução SQL para ser executada
cursor.execute(isql)
 
# Receber conjunto de dados retornado pelo Banco de dados
rs = cursor.fetchall()
for linha in rs:
       print("\033[1;34mNome:\033[m ", linha[0])
       print("\033[1;33mPreço de venda:\033[m ", linha[1])
       print(" ")
# Encerrar conexão
conn.close
quit()
