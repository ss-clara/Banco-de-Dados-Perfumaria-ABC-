# Programação II
# Prof. Dr. Adilson Ferreira da Silva
# Roteiro de Atividades - 04
# Alunas: Amanda de Caires Ferreira
#         Clara Simone dos Santos
#         Francidalva de Sousa Moura
# APLICAÇÃO PERFUMARIA ABC - APLICATIVO COMPLETO 
# ---------------------------------------------------------------------------------------------------------------

# importando bibliotecas...
import sqlite3
import os # biblioteca que permite recurso de limpar tela

# conectando banco de dados...
conn = sqlite3.connect("PerfumariaABC_(Amanda-Clara-Francidalva).db")

# definindo um cursor...
cursor = conn.cursor()

# ---------------------------------------------------------------------------------------------------------------
# DEFININDO FUNÇÃO: LIMPANDO TELA
def limpar_tela():
    os.system('cls')

# ---------------------------------------------------------------------------------------------------------------
# DEFININDO FUNÇÃO: ENCERRANDO CONEXÃO
def encerrar():
    print("")
    print("\033[1;32m------------------------------------------------------------------------------------")
    print(" >>>>>  >>>>>  >>>>>     E  N  C  E  R  R  A  N  D  O . . .     <<<<<  <<<<<  <<<<< ")
    print("------------------------------------------------------------------------------------\033[m")
    print("")
    conn.close()
    quit()

# ---------------------------------------------------------------------------------------------------------------
# DEFININDO FUNÇÃO: CADASTRO DE PRODUTOS
def cadastroprod():
    limpar_tela()
    print("\033[1;32m------------------------------------------------------------------------------------")
    print(">>>>> >>>>> >>>>>     C A D A S T R O  D E  P R O D U T O S  :     <<<<< <<<<< <<<<<")
    print("------------------------------------------------------------------------------------\033[m")

    # início do while loop
    resp_cadastro = "S" # resposta pergunta cadastro
    while resp_cadastro.upper() == "S":
        print("")
        codprod = int(input("Insira CÓDIGO do produto: "))
        # validando dados: o código do produto deve ser único e não pode ser nulo
        while codprod == None:
            codprod = int(input("Informe um CÓDIGO válido para produto: "))

        while (codprod) <= 0:
            codprod = int(input("Informe um CÓDIGO válido para produto: "))
        cursor.execute("select codprod from produto where codprod = " + str(codprod) + " ;")
        rescon_codprod = cursor.fetchone()
        # verificando se código já está cadastrado
        while rescon_codprod != None:
            print ("\033[31mcódigo já cadastrado!\033[m")
            break

        # prosseguindo para castro e validação das outras informações 
        else:
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

            print("")
            prcusto = float(input("Insira PREÇO DE CUSTO do produto: "))
    
            # inserindo dados no banco
            cursor.execute("""
            insert into produto (codprod, dsprod, saldo, sldmin, prvenda, prcusto)
            values (?,?,?,?,?,?)
            """, (codprod, dsprod, saldo, sldmin, prvenda, prcusto))
            conn.commit()
            print("------------------------------------------------------------------------------------")
            print("Dados cadastrados com sucesso!")
            print("")
        # pergunta continuação
        print("------------------------------------------------------------------------------------")
        print("DESEJA CADASTRAR NOVO PRODUTO?")
        resp_cadastro = input("Digite 'S' para sim ou qualquer tecla para voltar: ")

# ---------------------------------------------------------------------------------------------------------------
# DEFININDO FUNÇÃO: CONSULTA DE PRODUTOS
def consultaprod():
    limpar_tela()
    print("\033[1;32m------------------------------------------------------------------------------------")
    print(">>>>> >>>>> >>>>>     C O N S U L T A  D E  P R O D U T O S  :     <<<<< <<<<< <<<<<")
    print("------------------------------------------------------------------------------------\033[m")

    # início do while loop
    resconsulta = "S"
    while resconsulta.upper() == "S":
        print("")
        print("------------------------------------------------------------------------------------")
        codprod = input ("Insira CÓDIGO do produto: ")
        print("------------------------------------------------------------------------------------")
        print("")
        # lendo dados do banco...
        cursor.execute("select * from produto where codprod = " + codprod)
        # mostrando dados na tela... 
        resultado_consulta = cursor.fetchone()
        if resultado_consulta != None:
            print("Código de produto cadastrado!")
            print("Descrição: ", resultado_consulta[1])
            print("Saldo Atual: ", resultado_consulta[2], " unidades")
            print("Saldo Mínimo: ", resultado_consulta[3], " unidades")
            print("Preço de Venda: R$ ", resultado_consulta[4])
            print("Preço de Custo: R$ ", resultado_consulta[5])
            print("")
        else:
            print("------------------------------------------------------------------------------------")
            print("\033[31mProduto não cadastrado!\033[m")
            print("")
        # pergunta continuação
        print("------------------------------------------------------------------------------------")
        print("DESEJA FAZER NOVA CONSULTA?")
        resconsulta = input("Digite 'S' para SIM ou qualquer tecla para VOLTAR: ")

# ---------------------------------------------------------------------------------------------------------------
# DEFININDO FUNÇÃO: ALTERAÇÃO DE PRODUTOS
def alteracaoprod():
    limpar_tela() # CHAMANDO FUNÇÃO
    print("\033[1;32m------------------------------------------------------------------------------------")
    print(">>>>>     A L T E R A Ç Ã O   D E   D A D O S   D O S   P R O D U T O S  :     <<<<<")
    print("------------------------------------------------------------------------------------\033[m")

    # início do while loop
    resalteracao = "S"
    while resalteracao.upper() == "S":
        print("")
        print("------------------------------------------------------------------------------------")
        codprod = input("Insira CÓDIGO do produto: ")
        print("------------------------------------------------------------------------------------")
        # lendo dados do banco...
        cursor.execute("select * from produto where codprod = " + codprod)
        # mostrando dados na tela... 
        resultado_consulta = cursor.fetchone()
        if resultado_consulta != None:
            print("")
            print("VEJA O QUE ESTÁ CADASTRADO PARA ESSE PRODUTO")
            print("Descrição: ", resultado_consulta[1])
            print("Saldo Atual: ", resultado_consulta[2], " unidades")
            print("Saldo Mínimo: ", resultado_consulta[3], " unidades")
            print("Preço de Venda: R$ ", resultado_consulta[4])
            print("Preço de Custo: R$ ", resultado_consulta[5])
            print("")
            # início do loop menu
            while True:
                print("------------------------------------------------------------------------------------")
                print("[1] Para mudar DESCRIÇÃO do produto")
                print("[2] Para mudar SALDO ATUAL do produto")
                print("[3] Para mudar SALDO MÍNIMO do produto")
                print("[4] Para mudar PREÇO DE VENDA do produto")
                print("[5] Para mudar PREÇO DE CUSTO do produto")
                print("[6] Para DELETAR produto")
                print("[S] Para SAIR do produto")
                print("------------------------------------------------------------------------------------")
                escolhamalt = input("digite sua escolha: ")
                print("------------------------------------------------------------------------------------")
                print("")
                if escolhamalt == "1":
                    # Enviando instrução para ser executada
                    n_dsprod = input("Insira nova DESCRIÇÃO do produto: ")
                    cursor.execute("UPDATE produto SET dsprod = '" + n_dsprod + "' where codprod = " + codprod + ";")
                    conn.commit()
                elif escolhamalt == "2":
                    # Enviando instrução para ser executada
                    n_saldo = input("Insira novo SALDO ATUAL do produto: ")
                    cursor.execute("UPDATE produto set saldo = '" + n_saldo + "' where codprod = " + codprod + ";")
                    conn.commit()
                elif escolhamalt == "3":
                    # Enviando instrução para ser executada
                    n_sldmin = input("Insira novo SALDO MÍNIMO do produto: ")
                    cursor.execute("UPDATE produto set sldmin = '" + n_sldmin + "' where codprod = " + codprod + ";")
                    conn.commit()
                elif escolhamalt == "4":
                    # Enviando instrução para ser executada
                    n_prvenda = input("Insira novo PREÇO DE VENDA do produto: ")
                    cursor.execute("UPDATE produto set prvenda = '" + n_prvenda + "' where codprod = " + codprod + ";")
                    conn.commit()
                elif escolhamalt == "5":
                    # Enviando instrução para ser executada
                    n_prcusto = input("Insira novo PREÇO DE CUSTO do produto: ")
                    cursor.execute("UPDATE produto set prcusto = '" + n_prcusto + "' where codprod = " + codprod + ";")
                    conn.commit()
                elif escolhamalt == "6":
                    # Confirmando exclusão
                    print("Para confirmar exclusão do produto, digite [DELETE] confome aparece entre chaves:")
                    conf_exclusão = input(" ")
                    while conf_exclusão != "DELETE":
                        conf_exclusão = input("Digite [DELETE] para confirmar exclusão do produto:")
                    else:
                        # Enviando instrução para ser executada
                        cursor.execute("DELETE from produto where codprod = " + codprod + ";")
                        conn.commit()
                        print("")
                        print("Item deletado com sucesso!")
                        break 
                elif escolhamalt.upper() == "S":
                    break # interrompendo loop
                else:
                    print("\033[31mOPÇÃO INVÁLIDA!\033[m")
            print("------------------------------------------------------------------------------------")
            print("Banco de dados atualizado com sucesso!")
            print("")
        else:
            print("------------------------------------------------------------------------------------")
            print("\033[1;31mProduto não cadastrado!\033[m")
            print("")
        # pergunta continuação
        print("------------------------------------------------------------------------------------")
        print("DESEJA ALTERAR OUTRO PRODUTO?")
        resalteracao = input("Digite 'S' para SIM ou qualquer tecla para VOLTAR: ")
        
# ---------------------------------------------------------------------------------------------------------------        
# DEFININDO FUNÇÃO: LETRA A
def letra_a():
    # Preparar instrução SQL para enviar ao banco
    isql = "Select dsprod, prvenda from produto order by dsprod"
    # Enviar instrução SQL para ser executada
    cursor.execute(isql)
    # Receber conjunto de dados retornado pelo Banco de dados
    rs = cursor.fetchall()
    print("\033[1;32m-------------------------------------------------------------------------------------------------------")
    print(">>>>>>   >>>>>>   >>>>>>     R E S U L T A D O S   D A   C O N S U L T A :     <<<<<<   <<<<<<   <<<<<<")
    print("-------------------------------------------------------------------------------------------------------\033[m")
    print(" ")
    print("       \033[1;33m[A] LISTA DE PRODUTOS EM ORDEM ALFABÉTICA\033[m")
    print(" ")
    for linha in rs:
        print("-------------------------------------------------------------------------------------------------------")
        print(" ")
        print("\033[1;34mNome:\033[m ", linha[0])
        print("\033[1;33mPreço de venda:\033[m ", linha[1])
        print(" ")
    print("-------------------------------------------------------------------------------------------------------")
    pausa = input("DIGITE QUALQUER TECLA PARA VOLTAR") # pausa para execução em cmd windows
    
# ---------------------------------------------------------------------------------------------------------------        
# DEFININDO FUNÇÃO: LETRA B 
def letra_b():
    print("\033[1;32m-------------------------------------------------------------------------------------------------------")
    print(">>>>>>   >>>>>>   >>>>>>     R E S U L T A D O S   D A   C O N S U L T A :     <<<<<<   <<<<<<   <<<<<<")
    print("-------------------------------------------------------------------------------------------------------\033[m")
    print(" ")
    codprod = input("       \033[33m[B] LISTAR UM PRODUTO IDENTIFICADO PELO CÓDIGO:\033[m ")
    print(" ")
    
    # Preparar instrução SQL para enviar ao banco
    isql = "Select codprod, dsprod, saldo, sldmin from produto where codprod = " + str(codprod) + ";"
    # Enviar instrução SQL para ser executada
    cursor.execute(isql)
    # Receber conjunto de dados retornado pelo Banco de dados
    rs = cursor.fetchall()
    if rs == None:
        print("-------------------------------------------------------------------------------------------------------")
        print("NENHUM RESULTADO FOI ENCONTRADO")
        print(" ")
    else:
        for linha in rs:
            print("-------------------------------------------------------------------------------------------------------")
            print(" ")
            print("\033[1;34mCódigo:\033[m ", linha[0])
            print("\033[1;33mNome:\033[m ", linha[1])
            print("\033[1;32mSaldo:\033[m ", linha[2])
            print("\033[1;31mSaldo mínimo:\033[m ", linha[3])
            print(" ")
    print("-------------------------------------------------------------------------------------------------------")
    pausa = input("DIGITE QUALQUER TECLA PARA VOLTAR") # pausa para execução em cmd windows
    
# ---------------------------------------------------------------------------------------------------------------        
# DEFININDO FUNÇÃO: LETRA C
def letra_c():
    # Preparar instrução SQL para enviar ao banco
    isql = "Select codprod, dsprod, saldo, sldmin from produto where saldo < sldmin"
    # Enviar instrução SQL para ser executada
    cursor.execute(isql)
    # Receber conjunto de dados retornado pelo Banco de dados
    rs = cursor.fetchall()
    print("\033[1;32m-------------------------------------------------------------------------------------------------------")
    print(">>>>>>   >>>>>>   >>>>>>     R E S U L T A D O S   D A   C O N S U L T A :     <<<<<<   <<<<<<   <<<<<<")
    print("-------------------------------------------------------------------------------------------------------\033[m")
    print(" ")
    print("       \033[33m[C] LISTA DE PRODUTOS CUJO SALDO EM ESTOQUE SEJA < SALDO MÍNIMO\033[m")
    print(" ")
    if rs == None:
        print("-------------------------------------------------------------------------------------------------------")
        print("NENHUM RESULTADO FOI ENCONTRADO")
        print(" ")
    else:
        for linha in rs:
            print("-------------------------------------------------------------------------------------------------------")
            print(" ")
            print("\033[1;34mCódigo:\033[m ", linha[0])
            print("\033[1;33mNome:\033[m ", linha[1])
            print("\033[1;32mSaldo:\033[m ", linha[2])
            print("\033[1;31mSaldo mínimo:\033[m ", linha[3])
            print(" ")
    print("-------------------------------------------------------------------------------------------------------")
    pausa = input("DIGITE QUALQUER TECLA PARA VOLTAR") # pausa para execução em cmd windows
    
# ---------------------------------------------------------------------------------------------------------------        
# DEFININDO FUNÇÃO: LETRA D
def letra_d():
    # Preparar instrução SQL para enviar ao banco
    isql = "Select codprod, dsprod, saldo, sldmin from produto where saldo < sldmin and prvenda > 0"
    # Enviar instrução SQL para ser executada
    cursor.execute(isql)
    # Receber conjunto de dados retornado pelo Banco de dados
    rs = cursor.fetchall()
    print("\033[1;32m-------------------------------------------------------------------------------------------------------")
    print(">>>>>>   >>>>>>   >>>>>>     R E S U L T A D O S   D A   C O N S U L T A :     <<<<<<   <<<<<<   <<<<<<")
    print("-------------------------------------------------------------------------------------------------------\033[m")
    print(" ")
    print("       \033[33m[D] LISTA DE PRODUTOS CUJO SALDO EM ESTOQUE SEJA < SALDO MÍNIMO E PREÇO DE VENDA > 0\033[m")
    print(" ")
    if rs == None:
        print("-------------------------------------------------------------------------------------------------------")
        print("NENHUM RESULTADO FOI ENCONTRADO")
        print(" ")
    else:
        for linha in rs:
            print("-------------------------------------------------------------------------------------------------------")
            print(" ")
            print("\033[1;34mCódigo:\033[m ", linha[0])
            print("\033[1;33mNome:\033[m ", linha[1])
            print("\033[1;32mSaldo:\033[m ", linha[2])
            print("\033[1;31mSaldo mínimo:\033[m ", linha[3])
            print(" ")
    print("-------------------------------------------------------------------------------------------------------")
    pausa = input("DIGITE QUALQUER TECLA PARA VOLTAR") # pausa para execução em cmd windows
    
# ---------------------------------------------------------------------------------------------------------------        
# DEFININDO FUNÇÃO: LETRA E
def letra_e():
    # Preparar instrução SQL para enviar ao banco
    isql = "Select codprod, dsprod, saldo, sldmin from produto where saldo < sldmin and prcusto > 0"
    # Enviar instrução SQL para ser executada
    cursor.execute(isql)
    # Receber conjunto de dados retornado pelo Banco de dados
    rs = cursor.fetchall()
    print("\033[1;32m-------------------------------------------------------------------------------------------------------")
    print(">>>>>>   >>>>>>   >>>>>>     R E S U L T A D O S   D A   C O N S U L T A :     <<<<<<   <<<<<<   <<<<<<")
    print("-------------------------------------------------------------------------------------------------------\033[m")
    print(" ")
    print("       \033[33m[E] LISTA DE PRODUTOS CUJO SALDO EM ESTOQUE SEJA < SALDO MÍNIMO E PREÇO DE CUSTO > 0\033[m")
    print(" ")
    if rs == None:
        print("-------------------------------------------------------------------------------------------------------")
        print("NENHUM RESULTADO FOI ENCONTRADO")
        print(" ")
    else:
        for linha in rs:
            print("-------------------------------------------------------------------------------------------------------")
            print(" ")
            print("\033[1;34mCódigo:\033[m ", linha[0])
            print("\033[1;33mNome:\033[m ", linha[1])
            print("\033[1;32mSaldo em estoque:\033[m ", linha[2])
            print("\033[1;31mSaldo mínimo:\033[m ", linha[3])
            print(" ")
    print("-------------------------------------------------------------------------------------------------------")
    pausa = input("DIGITE QUALQUER TECLA PARA VOLTAR") # pausa para execução em cmd windows
    
# ---------------------------------------------------------------------------------------------------------------        
# DEFININDO FUNÇÃO: LETRA F
def letra_f():
    # Preparar instrução SQL para enviar ao banco
    isql = "Select codprod, dsprod, saldo, sldmin from produto where saldo < sldmin and prvenda > 0 order by dsprod"
    # Enviar instrução SQL para ser executada
    cursor.execute(isql)
    # Receber conjunto de dados retornado pelo Banco de dados
    rs = cursor.fetchall()
    print("\033[1;32m-------------------------------------------------------------------------------------------------------")
    print(">>>>>>   >>>>>>   >>>>>>     R E S U L T A D O S   D A   C O N S U L T A :     <<<<<<   <<<<<<   <<<<<<")
    print("-------------------------------------------------------------------------------------------------------\033[m")
    print(" ")
    print("       \033[33m[F] LISTA DE PRODUTOS CUJO SALDO EM ESTOQUE SEJA < SALDO MÍNIMO E PREÇO DE VENDA > 0")
    print("           EM ORDEM ALFABÉTICA\033[m")
    print(" ")
    if rs == None:
        print("-------------------------------------------------------------------------------------------------------")
        print("NENHUM RESULTADO FOI ENCONTRADO")
        print(" ")
    else:
        for linha in rs:
            print("-------------------------------------------------------------------------------------------------------")
            print(" ")
            print("\033[1;34mCódigo:\033[m ", linha[0])
            print("\033[1;33mNome:\033[m ", linha[1])
            print("\033[1;32mSaldo em estoque:\033[m ", linha[2])
            print("\033[1;31mSaldo mínimo:\033[m ", linha[3])
            print(" ")
    print("-------------------------------------------------------------------------------------------------------")
    pausa = input("DIGITE QUALQUER TECLA PARA VOLTAR") # pausa para execução em cmd windows
    
# ---------------------------------------------------------------------------------------------------------------        
# DEFININDO FUNÇÃO: LETRA G
def letra_g():
    # Preparar instrução SQL para enviar ao banco
    isql = "Select codprod, dsprod from produto where prvenda <= 0"
    # Enviar instrução SQL para ser executada
    cursor.execute(isql)
    # Receber conjunto de dados retornado pelo Banco de dados
    rs = cursor.fetchall()
    print("\033[1;32m-------------------------------------------------------------------------------------------------------")
    print(">>>>>>   >>>>>>   >>>>>>     R E S U L T A D O S   D A   C O N S U L T A :     <<<<<<   <<<<<<   <<<<<<")
    print("-------------------------------------------------------------------------------------------------------\033[m")
    print(" ")
    print("       \033[m[G] LISTA DE PRODUTOS CUJO PREÇO DE VENDA <= 0\033[m")
    print(" ")
    if rs == None:
        print("-------------------------------------------------------------------------------------------------------")
        print("NENHUM RESULTADO FOI ENCONTRADO")
        print(" ")
    else:
        for linha in rs:
            print("-------------------------------------------------------------------------------------------------------")
            print(" ")
            print("\033[1;34mCódigo:\033[m ", linha[0])
            print("\033[1;33mNome:\033[m ", linha[1])
            print(" ")
    print("-------------------------------------------------------------------------------------------------------")
    pausa = input("DIGITE QUALQUER TECLA PARA VOLTAR") # pausa para execução em cmd windows
    
# ---------------------------------------------------------------------------------------------------------------        
# DEFININDO FUNÇÃO: LETRA H
def letra_h():
    # Preparar instrução SQL para enviar ao banco
    isql = "Select count(*) from produto"
    # Enviar instrução SQL para ser executada
    cursor.execute(isql)
    # Receber conjunto de dados retornado pelo Banco de dados
    rs = cursor.fetchall()
    print("\033[1;32m-------------------------------------------------------------------------------------------------------")
    print(">>>>>>   >>>>>>   >>>>>>     R E S U L T A D O S   D A   C O N S U L T A :     <<<<<<   <<<<<<   <<<<<<")
    print("-------------------------------------------------------------------------------------------------------\033[m")
    for linha in rs:
        print(" ")
        print("   \033[33m[H] TOTAL DE PRODUTOS CADASTRADOS:\033[m    ", linha[0])
        print(" ")
    print("-------------------------------------------------------------------------------------------------------")
    pausa = input("DIGITE QUALQUER TECLA PARA VOLTAR") # pausa para execução em cmd windows
    
# ---------------------------------------------------------------------------------------------------------------        
# DEFININDO FUNÇÃO: LETRA I
def letra_i():
    # Preparar instrução SQL para enviar ao banco
    isql = "Select count(*) from produto where saldo = 0"
    # Enviar instrução SQL para ser executada
    cursor.execute(isql)
    # Receber conjunto de dados retornado pelo Banco de dados
    rs = cursor.fetchall()
    print("\033[1;32m-------------------------------------------------------------------------------------------------------")
    print(">>>>>>   >>>>>>   >>>>>>     R E S U L T A D O S   D A   C O N S U L T A :     <<<<<<   <<<<<<   <<<<<<")
    print("-------------------------------------------------------------------------------------------------------\033[m")
    if rs == None:
        print(" ")
        print("NENHUM RESULTADO FOI ENCONTRADO")
        print(" ")
    else:
        for linha in rs:
            print(" ")
            print("   \033[33m[I] TOTAL DE PRODUTOS COM SALDO EM ESTOQUE ZERADO:\033[m    ", linha[0])
            print(" ")
    print("-------------------------------------------------------------------------------------------------------")
    pausa = input("DIGITE QUALQUER TECLA PARA VOLTAR") # pausa para execução em cmd windows
    
# ---------------------------------------------------------------------------------------------------------------        
# DEFININDO FUNÇÃO: LETRA J
def letra_j():
    # Preparar instrução SQL para enviar ao banco
    isql = "Select count(*) from produto where saldo < sldmin"
    # Enviar instrução SQL para ser executada
    cursor.execute(isql)
    # Receber conjunto de dados retornado pelo Banco de dados
    rs = cursor.fetchall()
    print("\033[1;32m-------------------------------------------------------------------------------------------------------")
    print(">>>>>>   >>>>>>   >>>>>>     R E S U L T A D O S   D A   C O N S U L T A :     <<<<<<   <<<<<<   <<<<<<")
    print("-------------------------------------------------------------------------------------------------------\033[m")
    if rs == None:
        print(" ")
        print("NENHUM RESULTADO FOI ENCONTRADO")
        print(" ")
    else:
        for linha in rs:
            print(" ")
            print("   \033[33m[J] PRODUTOS COM SALDO EM ESTOQUE MENOR QUE O MÍNIMO:\033[m   ", linha[0])
            print(" ")
    print("-------------------------------------------------------------------------------------------------------")
    pausa = input("DIGITE QUALQUER TECLA PARA VOLTAR") # pausa para execução em cmd windows
    
# ---------------------------------------------------------------------------------------------------------------        
# DEFININDO FUNÇÃO: LETRA K
def letra_k():
    # Preparar instrução SQL para enviar ao banco
    isql = "Select dsprod, saldo,prvenda, (saldo * prvenda) as Rentabilidade from produto"
    # Enviar instrução SQL para ser executada
    cursor.execute(isql)
    # Receber conjunto de dados retornado pelo Banco de dados
    rs = cursor.fetchall()
    print("\033[1;32m-------------------------------------------------------------------------------------------------------")
    print(">>>>>>   >>>>>>   >>>>>>     R E S U L T A D O S   D A   C O N S U L T A :     <<<<<<   <<<<<<   <<<<<<")
    print("-------------------------------------------------------------------------------------------------------\033[m")
    print(" ")
    print("       \033[33m[K] LISTA DE RENTABILIDADE DOS PRODUTOS\033[m   ")
    print(" ")
    for linha in rs:
        print("-------------------------------------------------------------------------------------------------------")
        print(" ")
        print("\033[1;34mNome:\033[m ", linha[0])
        print("\033[1;33mSaldo:\033[m ", linha[1])
        print("\033[1;32mPreço de venda:\033[m ", linha[2])
        print("\033[1;35mRentabilidade:\033[m ", linha[3])
        print(" ")
    print("-------------------------------------------------------------------------------------------------------")
    pausa = input("DIGITE QUALQUER TECLA PARA VOLTAR") # pausa para execução em cmd windows
    
# ---------------------------------------------------------------------------------------------------------------        
# DEFININDO FUNÇÃO: OUTRAS FORMAS DE CONSULTA DE PRODUTOS
def outrasopcoes():
    while True:
        limpar_tela() # CHAMANDO FUNÇÃO
        print("")
        print("\033[1;32m-------------------------------------------------------------------------------------------------------")
        print(">>>>>   >>>>>   >>>>>     O U T R A S   O P Ç Õ E S   D E   C O N S U L T A :     <<<<<   <<<<<   <<<<<")
        print("-------------------------------------------------------------------------------------------------------\033[m")
        print("")
        print("[A] Listar produtos em ordem alfabética;")
        print("[B] Listar um produto identificado pelo código;")
        print("[C] Listar produtos cujo saldo em estoque seja < saldo mínimo;")
        print("[D] Listar produtos cujo saldo em estoque seja < saldo mínimo e preço de venda > 0;")
        print("[E] Listar produtos cujo saldo em estoque seja < saldo mínimo e preço de custo > 0;")
        print("[F] Listar produtos cujo saldo em estoque seja < saldo mínimo e preço de venda > 0 em ordem alfabética;")
        print("[G] Listar produtos cujo preço de venda <= 0;")
        print("[H] Listar a quantidade de produtos cadastrados;")
        print("[I] Listar produtos com saldo em estoque zerado;")
        print("[J] Listar produtos com saldo em estoque seja menor que o mínimo;")
        print("[K] Listar rentabilidade dos produtos;")
        print("")
        print("[V] PARA VOLTAR")
        print("")
        print("-------------------------------------------------------------------------------------------------------")
        escolhamopcoes = input("Digite sua escolha: ")
        print("-------------------------------------------------------------------------------------------------------")
        print("")

        # chamada das funções
        if escolhamopcoes.upper() == "A":
            letra_a()
        elif escolhamopcoes.upper() == "B":
            letra_b()
        elif escolhamopcoes.upper() == "C":
            letra_c()
        elif escolhamopcoes.upper() == "D":
            letra_d()
        elif escolhamopcoes.upper() == "E":
            letra_e()
        elif escolhamopcoes.upper() == "F":
            letra_f()
        elif escolhamopcoes.upper() == "G":
            letra_g()
        elif escolhamopcoes.upper() == "H":
            letra_h()
        elif escolhamopcoes.upper() == "I":
            letra_i()
        elif escolhamopcoes.upper() == "J":
            letra_j()
        elif escolhamopcoes.upper() == "K":
            letra_k()
        elif escolhamopcoes.upper() == "V":
            area_trabalho()
        else:
            print("OPÇÃO INVÁLIDA. TENTE DE NOVO.")

# ---------------------------------------------------------------------------------------------------------------
# DEFINIÇÃO FUNÇÃO: ÁREA DE TRABALHO FUNCIONÁRIO
def area_trabalho():
    while True:
        limpar_tela() # CHAMANDO FUNÇÃO
        print("")
        print("\033[1;32m------------------------------------------------------------------------------------")
        print(">>>>>   >>>>>   >>>>>     Á R E A  D E  T R A B A L H O  :     <<<<<   <<<<<   <<<<<")
        print("------------------------------------------------------------------------------------\033[m")
        print("")
        print("       [1] PARA CADASTRAMENTO DE PRODUTOS")
        print("       [2] PARA CONSULTA DE PRODUTOS")
        print("       [3] PARA ALTERAÇÃO E EXCLUSÃO DE PRODUTOS")
        print("       [4] PARA OUTRAS OPÇÕES DE CONSULTA")
        print("       [V] PARA PARA VOLTAR")
        print("       [E] PARA ENCERRAR APLICAÇÃO")
        print("")
        print("------------------------------------------------------------------------------------")
        escolhamprincipal = input("Digite sua escolha: ")
        print("------------------------------------------------------------------------------------")
        print("")
    
        # chamada das funções
        if escolhamprincipal == "1":
            cadastroprod() 
        elif escolhamprincipal == "2":
            consultaprod() 
        elif escolhamprincipal == "3":
            alteracaoprod() 
        elif escolhamprincipal == "4":
            outrasopcoes() 
        elif escolhamprincipal.upper() == "V":
            tela_inicial() 
        elif escolhamprincipal.upper() == "E":
            encerrar() 
        else:
            print("OPÇÃO INVÁLIDA. TENTE DE NOVO.")
        
# ---------------------------------------------------------------------------------------------------------------
# DEFINIÇÃO FUNÇÃO: LOGIN FUNCIONÁRIO
def login_funcionario():
    limpar_tela() # CHAMANDO FUNÇÃO
    print("\033[1;32m-------------------------------------------------")
    print(">>>>>     >>>>>     L O G I N     <<<<<     <<<<<")
    print("-------------------------------------------------\033[m")
    print("")
    login = input(" ")
    # buscando usuário cadastrado no sistema
    cursor.execute("select login from funcionario where login = '" + login + "';")
    resp_cons_login = cursor.fetchone()
    # comparando usuário cadastrado com usuário informado
    while resp_cons_login == None:
        print ("USUÁRIO NÃO CADASTRADO.")
        login = input("USUÁRIO: ")
        cursor.execute("select login from funcionario where login = '" + login + "';")
        resp_cons_login = cursor.fetchone()
    else:
        print("\033[1;32m-------------------------------------------------")
        print(">>>>>     >>>>>     S E N H A     <<<<<     <<<<<")
        print("-------------------------------------------------\033[m")
        print("")
        senha = input(" ")
        # buscando usuário e senha cadastrados no sistema
        cursor.execute("select senha from funcionario where login = '" + login + "' and senha = '" + senha + "';")
        resp_cons_senha = cursor.fetchone()
        # comparando usuário e senha cadastrados com usuário e senha informados
        while resp_cons_senha == None:
            print("SENHA INVÁLIDA.")
            senha = input("SENHA: ")
            cursor.execute("select senha from funcionario where login = '" + login + "' and senha = '" + senha + "';")
            resp_cons_senha = cursor.fetchone()
        else:
            print("")
            print("\033[1;32m------------------------------------------------------------------------------------")
            print(">>>>>    >>>>>    >>>>>     B  E  M  -  V  I  N  D  O  !     <<<<<    <<<<<    <<<<<")
            print("------------------------------------------------------------------------------------\033[m")
            area_trabalho() # CHAMANDO FUNÇÃO
            
# ---------------------------------------------------------------------------------------------------------------
# DEFININDO FUNÇÃO: ALTERAÇÃO DE PRODUTOS
def bloqueiofun():
    limpar_tela() # CHAMANDO FUNÇÃO
    print("\033[1;32m------------------------------------------------------------------------------------")
    print(">>>>>   >>>>>     B L O Q U E I O   D E   F U N C I O N Á R I O  :     <<<<<   <<<<<")
    print("------------------------------------------------------------------------------------\033[m")
    print("")
    # lendo dados do banco...
    cursor.execute("select CPF, nomefun from funcionario where administrador = 0;")
    # mostrando dados na tela... 
    resultado_consulta_fun = cursor.fetchall()
    print("LISTA DOS FUNCIONÁRIOS CADASTRADOS:")
    print("------------------------------------------------------------------------------------")
    for linha in resultado_consulta_fun:
        print("")
        print("CPF: ", linha[0])
        print("NOME COMPLETO: ", linha[1])
        print("")
        print("------------------------------------------------------------------------------------")
    resbloqueio = "S"
    while resbloqueio.upper() == "S":
        CPF = input("Informe CPF do funcionário que deseja bloquear:")
        print("------------------------------------------------------------------------------------")
        # buscando usuário cadastrado no sistema
        cursor.execute("select CPF from funcionario where CPF = '" + CPF + "';")
        resp_cons_CPF = cursor.fetchone()
        # comparando usuário cadastrado com usuário informado
        while resp_cons_CPF == None:
            print ("CPF NÃO CADASTRADO.")
            CPF = input("Informe um número de CPF cadastrado: ")
            cursor.execute("select CPF from funcionario where CPF = '" + CPF + "';")
            resp_cons_CPF = cursor.fetchone()
        else:
            print("")
            print("Para confirmar bloqueio do funcionário, digite [BLOCK] confome aparece entre chaves: ")
            print("")
            conf_exclusão = input(" ")
            while conf_exclusão != "BLOCK":
                print("")
                conf_exclusão = input("Digite [BLOCK] para confirmar exclusão do produto: ")
            else:
                # Enviando instrução para ser executada
                cursor.execute("DELETE from funcionario where CPF = " + CPF + ";")
                conn.commit()
                print("")
                print("Funcionário bloqueado com sucesso!")
                break # interrompendo loop
        # pergunta continuação
        print("------------------------------------------------------------------------------------")
        print("DESEJA BLOQUEAR OUTRO FUNCIONÁRIO?")
        resbloqueio = input("Digite 'S' para sim ou qualquer tecla para voltar: ")

# ---------------------------------------------------------------------------------------------------------------
# DEFINIÇÃO FUNÇÃO: CADASTRO FUNCIONÁRIO
def cadastrofun():
    limpar_tela() # CHAMANDO FUNÇÃO
    print("")
    print("\033[1,32m------------------------------------------------------------------------------------")
    print(">>>>>  >>>>>     C A D A S T R O   D E   F U N C I O N Á R I O S  :     <<<<<  <<<<<")
    print("------------------------------------------------------------------------------------\033[m")

    # início do while loop
    resp_cadastro_fun = "S" # resposta pergunta cadastro
    while resp_cadastro_fun.upper() == "S":
        print("")
        CPF = int(input("Insira CPF do funcionário: "))
        # validando dados: o cpf do funcionário deve ser único e não pode ser nulo
        while CPF == None:
            CPF = int(input("Informe um número de CPF válido: "))

        while (CPF) <= 0:
            codprod = int(input("Informe um número de CPF válido: "))
            
        cursor.execute("select CPF from funcionario where CPF = " + str(CPF) + " ;")
        rescon_CPF = cursor.fetchone()

        while rescon_CPF != None:
            print ("\033[1;31mFuncionário já cadastrado!\033[m")
            break

        else:
            print("")
            nomefun = input("Insira NOME COMPLETO do funcionário: ")
            # validando dados: nome do funcionário não pode estar vazio ou em branco...
            while (nomefun) == None:
                print("O nome do funcionário não pode estar vazio ou em branco")
                nomefun = input ("Informe NOME COMPLETO válido para funcionário: ")

            print("")
            login = input("Insira LOGIN do funcionário para acesso ao sistema: ")
            # validando dados: o campo login do funcionário não pode estar vazio ou em branco...
            while (login) == None:
                print("O campo login não pode estar vazio ou em branco")
                login = input ("Insira LOGIN válidO para acesso ao sistema: ")

            print("")   
            senha = input("Insira SENHA do funcionário para controle de acesso ao sistema: ")
            # validando dados: o campo senha do funcionário não pode estar vazio ou em branco...
            while (senha) == None:
                print("O campo senha não pode estar vazio ou em branco")
                senha = input ("Insira SENHA válida para controle de acesso ao sistema: ")

            # validando dados: apenas o administrador terá privilégios no sistema
            # então, para os demais funcionários, a variável administrador será sempre igual a 0
            administrador = 0
    
            # inserindo dados no banco
            cursor.execute("""
            insert into funcionario (CPF, nomefun, login, senha, administrador)
            values (?,?,?,?,?)
            """, (CPF, nomefun, login, senha, administrador))
            conn.commit()
            print("------------------------------------------------------------------------------------")
            print("Funcionário cadastrado com sucesso!")
            print("")
        # pergunta continuação
        print("------------------------------------------------------------------------------------")
        print("DESEJA CADASTRAR NOVO FUNCIONÁRIO?")
        resp_cadastro_fun = input("Digite 'S' para SIM ou qualquer tecla para VOLTAR: ")
            
# ---------------------------------------------------------------------------------------------------------------
# DEFINIÇÃO FUNÇÃO: LOGIN FUNCIONÁRIO
def area_adm():
    while True:
        limpar_tela() # CHAMANDO FUNÇÃO
        print("")
        print("\033[1;32m------------------------------------------------------------------------------------")
        print(">>>>> >>>>> >>>>>     A  D  M  I  N  I  S  T  R  A  T  I  V  O     <<<<< <<<<< <<<<<")
        print("------------------------------------------------------------------------------------\033[m")
        print("")
        print("       [1] CADASTRAR NOVOS FUNCIONÁRIOS")
        print("       [2] BLOQUEAR ACESSO")
        print("       [V] PARA VOLTAR")
        print("")
        print("------------------------------------------------------------------------------------")
        print("")
        escolha_adm = input("SUA ESCOLHA: ")

        # chamada das funções
        if escolha_adm == "1":
            cadastrofun()
        elif escolha_adm.upper() == "2":
            bloqueiofun()
        elif escolha_adm.upper() == "V":
            limpar_tela() 
            tela_inicial() 
        else:
            print("\033[1;31mOPÇÃO INVÁLIDA. TENTE DE NOVO.\033[m")

# ---------------------------------------------------------------------------------------------------------------
# DEFINIÇÃO FUNÇÃO: LOGIN FUNCIONÁRIO
def login_adm():
    limpar_tela() # CHAMANDO FUNÇÃO
    print("\033[1;32m-------------------------------------------------")
    print(">>>>>     >>>>>     L O G I N     <<<<<     <<<<<")
    print("-------------------------------------------------\033[m")
    print("")
    login = input(" ")
    # buscando usuário cadastrado no sistema como administrador
    cursor.execute("select login from funcionario where login = '" + login + "' and administrador = 1;")
    resp_cons_login = cursor.fetchone()
    # comparando usuário cadastrado com usuário informado como administrador
    while resp_cons_login == None:
        print ("USUÁRIO NÃO CADASTRADO.")
        login = input("USUÁRIO: ")
        cursor.execute("select login from funcionario where login = '" + login + "'and administrador = 1;")
        resp_cons_login = cursor.fetchone()
    else:
        print("\033[1;32m-------------------------------------------------")
        print(">>>>>     >>>>>     S E N H A     <<<<<     <<<<<")
        print("-------------------------------------------------\033[m")
        print("")
        senha = input(" ")
        # buscando usuário e senha cadastrados no sistema como administrador
        cursor.execute("select senha from funcionario where login = '" + login + "' and senha = '" + senha + "'and administrador = 1;")
        resp_cons_senha = cursor.fetchone()
        # comparando usuário e senha cadastrados com usuário e senha informados como administrador
        while resp_cons_senha == None:
            print("SENHA INVÁLIDA.")
            senha = input("SENHA: ")
            cursor.execute("select senha from funcionario where login = '" + login + "' and senha = '" + senha + "'and administrador = 1;")
            resp_cons_senha = cursor.fetchone()
        else:
            print("")
            print("\033[1;32m------------------------------------------------------------------------------------")
            print(">>>>>    >>>>>    >>>>>     B  E  M  -  V  I  N  D  O  !     <<<<<    <<<<<    <<<<<")
            print("------------------------------------------------------------------------------------\033[m")
            area_adm() # CHAMANDO FUNÇÃO

# ---------------------------------------------------------------------------------------------------------------
# DEFINIÇÃO FUNÇÃO: MENU INICIAL
def menu_inicial():
    print("")
    print("\033[1;32m------------------------------------------------------------------------------------")
    print(">>>>>  P E R F U M A R I A   A B C  :   C O N T R O L E   D E   E S T O Q U E  <<<<<")
    print("------------------------------------------------------------------------------------\033[m")
    print("")
    print("       [1] PARA ÁREA DE TRABALHO FUNCIONÁRIO")
    print("       [2] PARA CONTROLE ADMINISTRAÇÃO")
    print("       [E] PARA ENCERRAR APLICAÇÃO")
    print("")
    print("------------------------------------------------------------------------------------")

# ---------------------------------------------------------------------------------------------------------------
# DEFINIÇÃO FUNÇÃO: TELA INICIAL
def tela_inicial():
    while True:
        menu_inicial() # CHAMANDO FUNÇÃO
        escolha_controle = input("SUA ESCOLHA: ")
        if escolha_controle == "1":
            login_funcionario() # CHAMANDO FUNÇÃO
        elif escolha_controle == "2":
            login_adm() # CHAMANDO FUNÇÃO
        elif escolha_controle.upper() == "E":
            encerrar() # CHAMANDO FUNÇÃO
        else:
            print("\033[1;31mOPÇÃO INVÁLIDA. TENTE DE NOVO.\033[m")
            
# ---------------------------------------------------------------------------------------------------------------   
# ---------------------------------------------------------------------------------------------------------------
# PROGRAMA PRINCIPAL: TELA INICIAL
# ---------------------------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------------------------
print("\033[1;32m------------------------------------------------------------------------------------")
print(">>>>>    >>>>>    >>>>>     B  E  M  -  V  I  N  D  O  !     <<<<<    <<<<<    <<<<<")
print("------------------------------------------------------------------------------------\033[m")
tela_inicial() # CHAMANDO FUNÇÃO

# ---------------------------------------------------------------------------------------------------------------
