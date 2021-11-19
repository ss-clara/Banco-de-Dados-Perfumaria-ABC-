# Listar código, nome, saldo em estoque e saldo mínimo de
# um produto identificado pelo seu código.

import sqlite3

# Conexão com SGDB
conn = sqlite3.connect("PerfumariaABC_(Amanda-Clara-Francidalva).db")
cursor = conn.cursor()

# Preparar instrução SQL para enviar ao banco
isql = "Select codprod, dsprod, saldo, sldmin from produto where codprod = 502"

# Enviar instrução SQL para ser executada
cursor.execute(isql)

# Receber conjunto de dados retornado pelo Banco de dados
rs = cursor.fetchall()
print("\033[1m--- RESULTADO OBTIDO ---\033[m" )
for linha in rs:
    print("\033[1;34mCódigo:\033[m ", linha[0])
    print("\033[1;33mNome:\033[m ", linha[1])
    print("\033[1;32mSaldo:\033[m ", linha[2])
    print("\033[1;31mSaldo mínimo:\033[m ", linha[3])
    print(" ")
# Encerrar conexão
conn.close
quit()
