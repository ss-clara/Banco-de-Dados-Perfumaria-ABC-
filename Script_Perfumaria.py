# Programação II
# Prof. Dr. Adilson Ferreira da Silva
# Roteiro de Atividades - 04
# Alunas: Amanda de Caires Ferreira
#         Clara Simone dos Santos
#         Francidalva de Sousa Moura
# APLICAÇÃO PERFUMARIA ABC - TECHO DO CÓDIGO PARA CADASTRO, CONCULTA, ALTERAÇÃO E EXCLUSÃO DOS DADOS 
# ---------------------------------------------------------------------------------------------------------------

# importando biblioteca...
import sqlite3

# conectando banco de dados...
conn = sqlite3.connect("PerfumariaABC_(Amanda-Clara-Francidalva).db")

# definindo um cursor...
cursor = conn.cursor()

# ---------------------------------------------------------------------------------------------------------------
# definição da função CADASTRO DE PRODUTOS
def cadastroprod():
    print("------------------------------------------------------------------------------------")
    print("                         \033[1;36mTela de cadastro dos Produtos\033[m              ")
    print("------------------------------------------------------------------------------------")

    # início do while loop
    resp_cadastro = "S" # resposta pergunta cadastro
    while resp_cadastro.upper() == "S":
        print("")
        codprod = input ("Insira CÓDIGO do produto: ")
        # validando dados: o código do produto deve ser único e não pode ser nulo
        while codprod == None: # ESSA PARTE AINDA ESTÁ ERRADA
            codprod = input ("Informe um CÓDIGO válido para produto: ")
        else:
            cursor.execute("select codprod from produto")
            rescon_codprod = cursor.fetchone()
            if rescon_codprod == codprod:
                print ("\033[1;31mCódigo já cadastrado\033[m")

        print("")
        dsprod = input("Insira DESCRIÇÃO do produto: ")
        # validando dados: nome do produto não pode estar vazio ou em branco...
        while (dsprod) == None:
            print("A descrição do produto não pode estar vazia ou em branco")
            dsprod = input ("Informe DESCRIÇÃO válida para o produto: ")

        print("")
        saldo = int(input("Insira SALDO ATUAL do produto: "))
        # validando dados: não pode ser cadastrado produto com saldo negativo...
        while (saldo) < 0:
            print("Não é possível cadastrar um produto com saldo atual negativo")
            saldo = int(input ("Informe SALDO ATUAL válido para produto: "))

        print("")   
        sldmin = int(input("Insira SALDO MÍNIMO do produto: "))
        # validando dados: não pode ser cadastrado produto com saldo negativo...
        while (sldmin) < 0:
            print("Não é possível cadastrar um produto com saldo mínimo negativo")
            sldmin = int(input ("Informe SALDO MÍNIMO válido para produto: "))

        print("")
        prvenda = float(input("Insira PREÇO DE VENDA do produto: "))
        # validando dados: não pode ser cadastrado produto com preço negativo...
        while (prvenda) < 0:
            print("Não é possível cadastrar um produto com preço de venda negativo")
            prvenda = float(input("Informe PREÇO DE VENDA válido para produto: "))

        print("")
        prcusto = float(input("Insira PREÇO DE CUSTO do produto: "))
        # validando dados: não pode ser cadastrado produto com preço negativo...
        while (prcusto) < 0:
            print("Não é possível cadastrar um produto com preço de custo negativo")
            prcusto = float(input("Informe PREÇO DE CUSTO válido para produto: "))
    
        # inserindo dados no banco
        cursor.execute("""
        insert into produto (codprod, dsprod, saldo, sldmin, prvenda, prcusto)
        values (?,?,?,?,?,?)
        """, (codprod, dsprod, saldo, sldmin, prvenda, prcusto))
        conn.commit()
        print("")
        print("Dados cadastrados com sucesso")
        print("")
        # pergunta continuação
        resp_cadastro = input("Deseja cadastrar novo produto? (Digite 'S' para sim ou qualquer tecla para voltar)")
# ---------------------------------------------------------------------------------------------------------------
# fim da definição

# ---------------------------------------------------------------------------------------------------------------
# definição da função CONSULTA DE PRODUTOS
def consultaprod():
    print("------------------------------------------------------------------------------------")
    print("                    \033[1;36mTela de consulta aos dados dos Produtos\033[m         ")
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
        if resultado_consulta != None:
            print("Código de produto cadastrado!")
            print("Descrição: ", resultado_consulta[1])
            print("Saldo Atual: ", resultado_consulta[2], " Unidades")
            print("Saldo Mínimo: ", resultado_consulta[3], " Unidades")
            print("Preço de Venda: R$ ", resultado_consulta[4])
            print("Preço de Custo: R$ ", resultado_consulta[5])
            print("")
        else:   
            print ("\033[1;31mProduto não cadastrado!\033[m")
        print("")
        resconsulta = input("Deseja fazer nova consulta? (Digite 'S' para sim ou qualquer tecla para voltar)")
# ---------------------------------------------------------------------------------------------------------------
# fim da definição

# ---------------------------------------------------------------------------------------------------------------
# definição da função ALTERAÇÃO DE PRODUTOS
def alteracaoprod():
    print("------------------------------------------------------------------------------------")
    print("                    \033[1;36mTela de alteração de dados dos Produtos\033[m         ")
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
            print("\033[1;31mopção inválida!\033[m") # MELHORAR ESSA PARTE
        print("")
        print("Banco de dados atualizado com sucesso!")
        print("")
        resalteracao = input("Deseja fazer nova alteração? (Digite 'S' para sim ou qualquer tecla para sair)")
# ---------------------------------------------------------------------------------------------------------------
# fim da definição

# definição da função OUTRAS FORMAS DE CONSULTA DE PRODUTOS
def outrasopcoes():
    print("------------------------------------------------------------------------------------")
    print("                    \033[1;36mTela de consulta aos dados dos Produtos\033[m         ")
    print("------------------------------------------------------------------------------------")
    resconsulta = "S"
    while resconsulta.upper() == "S":
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
        elif opcao == 5:
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

        elif opcao == 6:
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

        elif opcao == 7:
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

        elif opcao == 8:
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


        elif opcao == 9:
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

        elif opcao == 10:
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

        elif opcao == 11:
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

        elif opcao == 12:
            print("Saindo do programa...")
            break
        else:
            print("Alternativa inválida. Tente novamente.")
            print(" ")
        resconsulta = input("Deseja fazer nova consulta? (Digite 'S' para sim ou qualquer tecla para voltar)")

# ---------------------------------------------------------------------------------------------------------------
#                                        INÍCIO MENU INICIAL
respencerrar = "N"
while respencerrar.upper() == "N":
    print("------------------------------------------------------------------------------------")
    print("                              BEM-VINDO:  TELA INICIAL                              ")
    print("------------------------------------------------------------------------------------")
    print("")
    print("------------------------------------------------------------------------------------")
    print("digite [1] Para CADASTRAMENTO de produtos")
    print("digite [2] Para CONSULTA de produtos")
    print("digite [3] Para ALTERAÇÃO de produtos")
    print("digite [4] Para OUTRAS opções de consulta")
    print("------------------------------------------------------------------------------------")
    escolhamprincipal = int(input("Digite sua escolha: "))
    print("------------------------------------------------------------------------------------")
    print("")
    
    # chamada das funções
    if escolhamprincipal == 1:
        cadastroprod()
    elif escolhamprincipal == 2:
        consultaprod()
    elif escolhamprincipal == 3:
        alteracaoprod()
    elif escolhamprincipal == 4:
        outrasopcoes()
    else:
        print("opção inválida!") # MELHORAR ESSA PARTE
    #pergunta continuar
    print("")
    respencerrar = input("Deseja encerrar essa aplicação? (Digite 'N' para não ou qualquer tecla para sair)")
# ---------------------------------------------------------------------------------------------------------------
# fim MENU INICIAL 

# encerrando conexão...
conn.close()
quit()
