filmes = []
clientes = []
alugueis = []

#****************************************************************************************************************

#cliente
def cadastrar_cliente():
    print("\n - Cadastro de cliente - ")

    nome = input("Digite seu nome: ").upper()

    cpf = input("Digite seu CPF (somente números): ")
    cpf_formatado = cpf[:3] + "." + cpf[3:6] + "." + cpf[6:9] + "-" + cpf[9:]

    telefone = input("Digite seu número de telefone (somente números): ")

    if len(telefone) == 11:
        telefone_formatado = f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
    else:
        telefone_formatado = telefone 

    endereco = input("Digite seu endereço: ")

    novo_cliente = {
        "nome": nome,
        "cpf": cpf_formatado,
        "telefone": telefone_formatado,
        "endereco": endereco
    }

    clientes.append(novo_cliente)
    print(f"Cliente '{nome}' cadastrado com sucesso!\n")

def listar_clientes():
    print("\n - Lista de Clientes Cadastrados - ")
    encontrados = False
    for cliente in clientes:
        print(f'Nome: {cliente["nome"].upper()} | CPF: {cliente["cpf"]} | Telefone: {cliente["telefone"]} | Endereço: {cliente["endereco"].upper()}')
        encontrados = True
    if not encontrados:
        print("Nenhum cliente cadastrado no momento.\n")

def alterar_clientes():
    print("\n - Alterar Dados do Cliente  - ")
    cpf = input("Digite o CPF do cliente que deseja alterar: ")

    for cliente in clientes:
        if cliente["cpf"] == cpf:
            print(f"Cliente encontrado: {cliente['nome']}")
            novo_nome = input("Novo nome (deixe vazio para manter o atual): ")
            novo_telefone = input("Novo telefone (deixe vazio para manter o atual): ")
            novo_endereco = input("Novo endereço (deixe vazio para manter o atual): ")

            if novo_nome:
                cliente["nome"] = novo_nome
            if novo_telefone:
                cliente["telefone"] = novo_telefone
            if novo_endereco:
                cliente["endereco"] = novo_endereco

            print("Dados do cliente atualizados com sucesso!\n")
            return

    print("Cliente não encontrado com esse CPF.\n")

def excluir_clientes():
    print("\n=== Excluir Cliente ===")
    cpf = input("Digite o CPF do cliente que deseja excluir: ")

    for cliente in clientes:
        if cliente["cpf"] == cpf:
            confirmacao = input(f"Tem certeza que deseja excluir o cliente '{cliente['nome']}'? (s/n): ").lower()
            if confirmacao == 's':
                clientes.remove(cliente)
                print("Cliente removido com sucesso!\n")
            else:
                print("Operação cancelada.\n")
            return

    print("Cliente não encontrado com esse CPF.\n")

#****************************************************************************************************************

#filme
def cadastrar_filme():
    print("\n=== Cadastro de Filme ===")
    codigo = input("Código do Filme: ")
    titulo = input("Título do Filme: ").upper()
    genero = input("Gênero: ").upper()
    ano = input("Ano de Lançamento: ")

    novo_filme = {
        "codigo": codigo,
        "titulo": titulo,
        "genero": genero,
        "ano": ano,
        "disponivel": True
    }

    filmes.append(novo_filme)
    print("Filme adicionado à coleção com sucesso!\n")

def listar_filmes():
    print("\n - Lista de Filmes Disponíveis - ")
    encontrados = False
    for filme in filmes:
        if filme["disponivel"]:
            print(f'Código: {filme["codigo"]} | Título: {filme["titulo"]} | Gênero: {filme["genero"]} | Ano: {filme["ano"]}')
            encontrados = True
    if not encontrados:
        print("Nenhum filme disponível no momento.\n")

def alterar_filme():
    print("\n=== Alterar Dados do Filme ===")
    codigo = input("Digite o código do filme que deseja alterar: ")

    for filme in filmes:
        if filme["codigo"] == codigo:
            print(f"Filme encontrado: {filme['titulo']}")
            novo_titulo = input("Novo título (deixe vazio para manter o atual): ").upper()
            novo_genero = input("Novo gênero (deixe vazio para manter o atual): ").upper()
            novo_ano = input("Novo ano (deixe vazio para manter o atual): ")

            if novo_titulo:
                filme["titulo"] = novo_titulo
            if novo_genero:
                filme["genero"] = novo_genero
            if novo_ano:
                filme["ano"] = novo_ano

            print("Dados do filme atualizados com sucesso!\n")
            return

    print("Filme não encontrado.\n")

def excluir_filme():
    print("\n=== Excluir Filme ===")
    codigo = input("Digite o código do filme que deseja excluir: ")

    for filme in filmes:
        if filme["codigo"] == codigo:
            confirmacao = input(f"Tem certeza que deseja excluir '{filme['titulo']}'? (s/n): ").lower()
            if confirmacao == 's':
                filmes.remove(filme)
                print("Filme removido com sucesso!\n")
            else:
                print("Operação cancelada.\n")
            return

    print("Filme não encontrado.\n")


#****************************************************************************************************************

#aluguel

from datetime import date

def registrar_aluguel():
    print("\n - Registrar Aluguel - ")
    cpf = input("CPF do cliente: ")
    codigo = input("Código do filme: ")


    cliente_encontrado = any(c["cpf"] == cpf for c in clientes)
    if not cliente_encontrado:
        print("Cliente não encontrado.\n")
        return

   
    for filme in filmes:
        if filme["codigo"] == codigo and filme["disponivel"]:
            aluguel = {
                "cpf_cliente": cpf,
                "codigo_filme": codigo,
                "data_retirada": date.today().strftime("%d/%m/%Y"),
                "data_devolucao": None
            }
            alugueis.append(aluguel)
            filme["disponivel"] = False  # marca como alugado
            print("Aluguel registrado com sucesso!\n")
            return

    print("Filme não disponível ou não encontrado.\n")

def listar_aluguel():
    print("\n - Lista de Aluguéis - ")
    if alugueis:
        for aluguel in alugueis:
            print(f"Cliente: {aluguel['cpf_cliente']} | Filme: {aluguel['codigo_filme']} | Data Retirada: {aluguel['data_retirada']}")
    else:
        print("Nenhum aluguel registrado.\n")

def devolver_filme():
    print("\n - Devolver Filme - ")
    cpf = input("CPF do cliente: ")
    codigo = input("Código do filme: ")

    for aluguel in alugueis:
        if aluguel["cpf_cliente"] == cpf and aluguel["codigo_filme"] == codigo and aluguel["data_devolucao"] is None:
            aluguel["data_devolucao"] = date.today().strftime("%d/%m/%Y")
            for filme in filmes:
                if filme["codigo"] == codigo:
                    filme["disponivel"] = True  # marca o filme como disponível novamente
            print(f"Filme devolvido com sucesso!\n")
            return

    print("Aluguel não encontrado ou já devolvido.\n")



#****************************************************************************************************************


def menu():
    while True:
        print("*" * 60)
        print(" MENU - Locadora CineFácil".center(60))
        print("*" * 60)
        print('''
0. Sair
1. Cadastrar um novo filme
2. Lista de filmes disponíveis
3. Alterar dados do filme
4. Excluir filme cadastrado
5. Cadastrar um novo cliente
6. Lista de clientes
7. Alterar dados do cliente
8. Excluir cliente cadastrado
9. Registrar aluguel
10. Listar aluguéis
11. Devolução
''')
        
#****************************************************************************************************************

        nmr_menu = input("Digite o número da função desejada: ").strip()

        if nmr_menu== "0":
            print("Encerrando... Obrigado por usar a Locadora CineFácil!")
            break

        #filme
        elif nmr_menu == "1":
            cadastrar_filme()
        elif nmr_menu == "2":
            listar_filmes()
        elif nmr_menu == "3":
            alterar_filme()
        elif nmr_menu == "4":
            excluir_filme()
            

        #cliente
        elif nmr_menu == "5":
            cadastrar_cliente()
        elif nmr_menu == "6":
            listar_clientes()
        elif nmr_menu == "7":
            alterar_clientes()
        elif nmr_menu == "8":
            excluir_clientes()

        #aluguel
        elif nmr_menu == "9":
            registrar_aluguel()
        elif nmr_menu == "10":
            listar_aluguel()
        elif nmr_menu == "11":
            devolver_filme()
        else:

            print("Opção inválida.\n")

menu()
