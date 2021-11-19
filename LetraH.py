#Informar quantos produtos estão cadastrados.
import sqlite3

# Conexão com SGDB
conn = sqlite3.connect("PerfumariaABC_(Amanda-Clara-Francidalva).db")
cursor = conn.cursor()

# Preparar instrução SQL para enviar ao banco
isql = "Select count(*) from produto"

# Enviar instrução SQL para ser executada
cursor.execute(isql)

# Receber conjunto de dados retornado pelo Banco de dados
rs = cursor.fetchall()
print("\033[1m--- RESULTADOS OBTIDOS ---\033[m" )
for linha in rs:
    print("\033[1;34mTotal de produtos cadastrados:\033[m ", linha[0])
    print(" ")
# Encerrar conexão
conn.close
quit()