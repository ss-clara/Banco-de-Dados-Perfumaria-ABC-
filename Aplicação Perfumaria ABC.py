# Programação II
# Prof. Dr. Adilson Ferreira da Silva
# Roteiro de Atividades - 04
# Alunas: Amanda de Caires Ferreira
#         Clara Simone dos Santos
#         Francidalva de Sousa Moura
# APLICAÇÃO PERFUMARIA ABC

import sqlite3
# Conexão com SGDB
conn = sqlite3.connect("PerfumariaABC_(Amanda-Clara-Francidalva).db")
cursor = conn.cursor()

# Preparar instrução SQL para enviar ao banco
isql = "Select codprod, dsprod from produto;"

# Enviar instrução SQL para ser executada
cursor.execute(isql)

# Receber conjunto de dados retornado pelo Banco de dados
rs = cursor.fetchall()
for linha in rs:
    print("Código:",linha[0])
    print("Nome: ",linha[1])
# Encerrar conexão
conn.close
quit()
