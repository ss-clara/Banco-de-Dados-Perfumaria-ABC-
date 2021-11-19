#Menu de opções
print("-*-" * 10)
print("PERFUMARIA ABC")
print("-*-" * 10)
#Menu 1
resp = int(input("""Selecione uma opção abaixo:")) 
[1] Alteração e exclusão de produtos;  
[2] Cadastro de produtos;
[3] Consulta de produtos;
[4] Outras opções de consulta de produtos;
[5] Sair.
Sua opção: """))

if resp == 1:
    # importando biblioteca...
    import sqlite3
    # conectando banco de dados...
    conn = sqlite3.connect("PerfumariaABC_(Amanda-Clara-Francidalva).db")
    # definindo um cursor...
    cursor = conn.cursor()
    # ---------------------------------------------------------------------------------------------------------------
    # inicio do programa: alteração de dados no banco de trabalho
    print("------------------------------------------------------------------------------------")
    print("                     Tela de alteração de dados dos Produtos                        ")
    print("------------------------------------------------------------------------------------")
    # início do while loop
    resalteracao = "S"
    while resalteracao.upper() == "S":
        print("")
        print("------------------------------------------------------------------------------------")
        codprod = input("Insira CÓDIGO do produto: ")
        print(codprod)  # MELHORAR ESSA PARTE DO CÓDIGO
        print("")
        print("------------------------------------------------------------------------------------")
        print("digite [1] Para mudar DESCRIÇÃO do produto")
        print("digite [2] Para mudar SALDO ATUAL do produto")
        print("digite [3] Para mudar SALDO MÍNIMO do produto")
        print("digite [4] Para mudar PREÇO DE VENDA do produto")
        print("digite [5] Para mudar PREÇO DE CUSTO do produto")
        print("digite [6] Para DELETAR produto")
        print("------------------------------------------------------------------------------------")
        escolhamalt = int(input("digite sua escolha: "))
        print("------------------------------------------------------------------------------------")
        print("")
        if escolhamalt == 1:
            n_dsprod = input("Insira nova DESCRIÇÃO do produto: ")
            cursor.execute("UPDATE produto SET dsprod = '" + n_dsprod + "' where codprod = " + codprod + ";")
            conn.commit()
        elif escolhamalt == 2:
            n_saldo = input("Insira novo SALDO ATUAL do produto: ")
            cursor.execute("UPDATE produto set saldo = '" + n_saldo + "' where codprod = " + codprod + ";")
            conn.commit()
        elif escolhamalt == 3:
            n_sldmin = input("Insira novo SALDO MÍNIMO do produto: ")
            cursor.execute("UPDATE produto set sldmin = '" + n_sldmin + "' where codprod = " + codprod + ";")
            conn.commit()
        elif escolhamalt == 4:
            n_prvenda = input("Insira novo PREÇO DE VENDA do produto: ")
            cursor.execute("UPDATE produto set prvenda = '" + n_prvenda + "' where codprod = " + codprod + ";")
            conn.commit()
        elif escolhamalt == 5:
            n_prcusto = input("Insira novo PREÇO DE CUSTO do produto: ")
            cursor.execute("UPDATE produto set prcusto = '" + n_prcusto + "' where codprod = " + codprod + ";")
            conn.commit()
        elif escolhamalt == 6:
            cursor.execute("DELETE from produto where codprod = " + codprod + ";")
            conn.commit()
            print("")
            print("Item deletado com sucesso!")
        else:
            print("opção inválida!")  # MELHORAR ESSA PARTE
        print("")
        print("Banco de dados atualizado com sucesso!")
        print("")
        resalteracao = input("Deseja fazer nova alteração? (Digite 'S' para sim ou qualquer tecla para sair)")
    # ---------------------------------------------------------------------------------------------------------------
    # fim do while loop
    # encerrando conexão...
    conn.close()
    quit()
if resp == 2:
    # importando biblioteca...
    import sqlite3
    # conectando banco de dados...
    conn = sqlite3.connect("PerfumariaABC_(Amanda-Clara-Francidalva).db")
    # definindo um cursor...
    cursor = conn.cursor()
    # ---------------------------------------------------------------------------------------------------------------
    # inicio do programa: cadastro de dados no banco de trabalho
    print("------------------------------------------------------------------------------------")
    print("                          Tela de cadastro dos Produtos                             ")
    print("------------------------------------------------------------------------------------")
    # início do while loop
    rescadastro = "S"  # resposta pergunta cadastro
    while rescadastro.upper() == "S":
        print("")
        codprod = input("Insira CÓDIGO do produto: ")
        dsprod = input("Insira DESCRIÇÃO do produto: ")
        saldo = input("Insira SALDO ATUAL do produto: ")
        sldmin = input("Insira SALDO MÍNIMO do produto: ")
        prvenda = input("Insira PREÇO DE VENDA do produto: ")
        prcusto = input("Insira PREÇO DE CUSTO do produto: ")
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
if resp == 3:
    # importando biblioteca...
    import sqlite3
    # conectando banco de dados...
    conn = sqlite3.connect("PerfumariaABC_(Amanda-Clara-Francidalva).db")
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
        codprod = input("Insira CÓDIGO do produto: ")
        print("------------------------------------------------------------------------------------")
        print("")
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
            print("Produto não cadastrado!")  # MELHORAR ESSA PARTE
        print("")
        resconsulta = input("Deseja fazer nova consulta? (Digite 'S' para sim ou qualquer tecla para sair)")
    # ---------------------------------------------------------------------------------------------------------------
    # fim do while loop
    # encerrando conexão...
    conn.close()
    quit()
if resp == 4:
    opcao = 0
    while opcao != 12:
        opcao = int(input("""Escolha uma das opções abaixo: 
        [1] A-Listar produtos em ordem alfabética;
        [2] B-Listar um produto identificado pelo código;
        [3] C-Listar produtos cujo saldo em estoque seja < saldo mínimo;
        [4] D-Listar produtos cujo saldo em estoque seja < saldo mínimo e preço de venda > 0;
        [5] E-Listar produtos cujo saldo em estoque seja < saldo mínimo e preço de custo > 0;
        [6] F-Listar produtos cujo saldo em estoque seja < saldo mínimo e preço de venda > 0 em ordem alfabética;
        [7] G-Listar produtos cujo preço de venda <= 0;
        [8] H-Listar a quantidade de produtos cadastrados;
        [9] I-Listar produtos com saldo em estoque zerado;
        [10] J-Listar produtos com saldo em estoque seja menor que o mínimo;
        [11] K-Listar rentabilidade dos produtos;
        [12] Sair.
        Sua opção desejada: """))
        if opcao == 1:
            import sqlite3
            # Conexão com SGDB
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

        elif opcao == 2:
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
            print("\033[1m--- RESULTADO OBTIDO ---\033[m")
            for linha in rs:
                print("\033[1;34mCódigo:\033[m ", linha[0])
                print("\033[1;33mNome:\033[m ", linha[1])
                print("\033[1;32mSaldo:\033[m ", linha[2])
                print("\033[1;31mSaldo mínimo:\033[m ", linha[3])
                print(" ")
            # Encerrar conexão
            conn.close
            quit()

        elif opcao == 3:
            import sqlite3
            # Conexão com SGDB
            conn = sqlite3.connect("PerfumariaABC_(Amanda-Clara-Francidalva).db")
            cursor = conn.cursor()
            # Preparar instrução SQL para enviar ao banco
            isql = "Select codprod, dsprod, saldo, sldmin from produto where saldo < sldmin"
            # Enviar instrução SQL para ser executada
            cursor.execute(isql)
            # Receber conjunto de dados retornado pelo Banco de dados
            rs = cursor.fetchall()
            print("\033[1m--- RESULTADOS OBTIDOS ---\033[m")
            for linha in rs:
                print("\033[1;34mCódigo:\033[m ", linha[0])
                print("\033[1;33mNome:\033[m ", linha[1])
                print("\033[1;32mSaldo:\033[m ", linha[2])
                print("\033[1;31mSaldo mínimo:\033[m ", linha[3])
                print(" ")
            # Encerrar conexão
            conn.close
            quit()

        elif opcao == 4:
            import sqlite3
            # Conexão com SGDB
            conn = sqlite3.connect("PerfumariaABC_(Amanda-Clara-Francidalva).db")
            cursor = conn.cursor()
            # Preparar instrução SQL para enviar ao banco
            isql = "Select codprod, dsprod, saldo, sldmin from produto where saldo < sldmin and prvenda > 0"
            # Enviar instrução SQL para ser executada
            cursor.execute(isql)
            # Receber conjunto de dados retornado pelo Banco de dados
            rs = cursor.fetchall()
            print("\033[1m--- RESULTADOS OBTIDOS ---\033[m")
            for linha in rs:
               print("\033[1;34mCódigo:\033[m ", linha[0])
               print("\033[1;33mNome:\033[m ", linha[1])
               print("\033[1;32mSaldo:\033[m ", linha[2])
               print("\033[1;31mSaldo mínimo:\033[m ", linha[3])
               print(" ")
            # Encerrar conexão
            conn.close
            quit()

        elif opcao == 5:
            import sqlite3
            # Conexão com SGDB
            conn = sqlite3.connect("PerfumariaABC_(Amanda-Clara-Francidalva).db")
            cursor = conn.cursor()
            # Preparar instrução SQL para enviar ao banco
            isql = "Select codprod, dsprod, saldo, sldmin from produto where saldo < sldmin and prcusto > 0"
            # Enviar instrução SQL para ser executada
            cursor.execute(isql)
            # Receber conjunto de dados retornado pelo Banco de dados
            rs = cursor.fetchall()
            print("\033[1m--- RESULTADOS OBTIDOS ---\033[m")
            for linha in rs:
                print("\033[1;34mCódigo:\033[m ", linha[0])
                print("\033[1;33mNome:\033[m ", linha[1])
                print("\033[1;32mSaldo em estoque:\033[m ", linha[2])
                print("\033[1;31mSaldo mínimo:\033[m ", linha[3])
                print(" ")
            # Encerrar conexão
            conn.close
            quit()

        elif opcao == 6:
            import sqlite3
            # Conexão com SGDB
            conn = sqlite3.connect("PerfumariaABC_(Amanda-Clara-Francidalva).db")
            cursor = conn.cursor()
            # Preparar instrução SQL para enviar ao banco
            isql = "Select codprod, dsprod, saldo, sldmin from produto where saldo < sldmin and prvenda > 0 order by dsprod"
            # Enviar instrução SQL para ser executada
            cursor.execute(isql)
            # Receber conjunto de dados retornado pelo Banco de dados
            rs = cursor.fetchall()
            print("\033[1m--- RESULTADOS OBTIDOS ---\033[m")
            for linha in rs:
                print("\033[1;34mCódigo:\033[m ", linha[0])
                print("\033[1;33mNome:\033[m ", linha[1])
                print("\033[1;32mSaldo em estoque:\033[m ", linha[2])
                print("\033[1;31mSaldo mínimo:\033[m ", linha[3])
                print(" ")
            # Encerrar conexão
            conn.close
            quit()

        elif opcao == 7:
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
            print("\033[1m--- RESULTADOS OBTIDOS ---\033[m")
            for linha in rs:
                print("\033[1;34mCódigo:\033[m ", linha[0])
                print("\033[1;33mNome:\033[m ", linha[1])
                print(" ")
            # Encerrar conexão
            conn.close
            quit()

        elif opcao == 8:
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
            print("\033[1m--- RESULTADOS OBTIDOS ---\033[m")
            for linha in rs:
                print("\033[1;34mTotal de produtos cadastrados:\033[m ", linha[0])
                print(" ")
            # Encerrar conexão
            conn.close
            quit()

        elif opcao == 9:
            import sqlite3
            # Conexão com SGDB
            conn = sqlite3.connect("PerfumariaABC_(Amanda-Clara-Francidalva).db")
            cursor = conn.cursor()
            # Preparar instrução SQL para enviar ao banco
            isql = "Select count(*) from produto where saldo = 0"
            # Enviar instrução SQL para ser executada
            cursor.execute(isql)
            # Receber conjunto de dados retornado pelo Banco de dados
            rs = cursor.fetchall()
            print("\033[1m--- RESULTADOS OBTIDOS ---\033[m")
            for linha in rs:
               print("\033[1;31mProdutos com estoque zerado:\033[m ", linha[0])
               print(" ")
            # Encerrar conexão
            conn.close
            quit()

        elif opcao == 10:
            import sqlite3
            # Conexão com SGDB
            conn = sqlite3.connect("PerfumariaABC_(Amanda-Clara-Francidalva).db")
            cursor = conn.cursor()
            # Preparar instrução SQL para enviar ao banco
            isql = "Select count(*) from produto where saldo < sldmin"
            # Enviar instrução SQL para ser executada
            cursor.execute(isql)
            # Receber conjunto de dados retornado pelo Banco de dados
            rs = cursor.fetchall()
            print("\033[1m--- RESULTADOS OBTIDOS ---\033[m")
            for linha in rs:
               print("\033[1;34mProdutos com saldo em estoque menor que o mínimo:\033[m ", linha[0])
               print(" ")
            # Encerrar conexão
            conn.close
            quit()

        elif opcao == 11:
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
            print("\033[1m--- RESULTADOS OBTIDOS ---\033[m")
            for linha in rs:
                print("\033[1;34mNome:\033[m ", linha[0])
                print("\033[1;33mSaldo:\033[m ", linha[1])
                print("\033[1;32mPreço de venda:\033[m ", linha[2])
                print("\033[1;35mRentabilidade:\033[m ", linha[3])
                print(" ")
            # Encerrar conexão
            conn.close
            quit()
        elif opcao == 12:
            print("Saindo do programa...")
            break
        else:
             print("Alternativa inválida. Tente novamente.")
             print(" ")
