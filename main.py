print("main foi executado")
from livro import Livro
from revista import Revista
from usuario import Usuario
from emprestimo import Emprestimo
from prateleira import Prateleira

usuarios = []
itens = []
prateleiras = []
emprestimos = []

def mostrar_menu():
    print("\n================================")
    print("     BIBLIOTECA DOS NEGUINHOS ")
    print("================================")
    print("1  - Cadastrar usuário")
    print("2  - Cadastrar livro")
    print("3  - Cadastrar Revista")
    print("4  - Criar prateleira")
    print("5  - Adicionar item á prateleira")
    print("6  - Realizar empréstimo")
    print("7  - Finalizar empréstimo")
    print("8  - Listar usuários")
    print("9  - Listar itens")
    print("10 - Listar prateleiras")
    print("11 - Listar empréstimos")
    print("0  - Sair")
    print("================================")

while True:
    mostrar_menu()
        
    opcao = input("Escolha uma opção:")

    if opcao == "1":
        id_usuario = len(usuarios) + 1
        nome = input("Digite o  nome do usuário:")
        email = input("Digite o e-mail do usuário:")

        usuario = Usuario(id_usuario, nome, email)
        usuarios.append(usuario)

        print("Usuário Cadastrado!")

    if opcao == "2":
        codigo = len(itens) + 1
        titulo = input("Digite o título do livro:")
        autor = input("Digite o autor do livro: ")

        livro = Livro(codigo, titulo, autor)
        itens.append(livro)

        print("livro cadastrado!")

    if opcao == "3":
        codigo = len(itens) + 1
        titulo = input("Digite o título da revista: ")
        edicao = input("Digite o número da edição: ")

        revista = Revista(codigo, titulo, edicao)
        itens.append(revista)

        print("Revista cadastrada !")

    if opcao == "4":
        numero = len(prateleiras) + 1
        localizacao = input("Digite a localização da prateleira: ")

        prateleira = Prateleira(numero, localizacao)
        prateleiras.append(prateleira)

        print("Prateleira criada!")

    if opcao == "5":
        if not prateleiras:
            print("Nenhuma prateleira cadastrada!")
            continue
        if not itens:
            print("Nenhum item cadastrado")
            continue

        print("\nPrateleiras disponíveis:")

        for prateleira in prateleiras:
            print(f"{prateleira.numero} - {prateleira.localizacao}")

        numero_prateleira = int(input("Digite o número da prateleira:"))

        prateleira_escolhida = None

        for prateleira in prateleiras:
            if prateleira.numero == numero_prateleira:
                prateleira_escolhida = prateleira 
                break

        if prateleira_escolhida is None:
            print("Prateleira não encontrada")
            continue

        print("\nItens disponíveis:")

        for item in itens:
            print(f"{item.codigo} - {item.titulo}")

        codigo_item = int(input("Digite o código do item:"))

        item_escolhido = None

        for item in itens:
            if item.codigo == codigo_item:
                item_escolhido = item 
                break

        if item_escolhido is None:
            print("Item não encontrado.")
            continue

        prateleira_escolhida.adicionar_item(item_escolhido)

        print("Item adicionado á prateleira com sucesso!")


    if opcao == "6":
        if not usuarios:
            print("Nenhum usuário cadastrado.")
            continue 

        if not itens:
            print("Nenhum item cadastrado")
            continue

        print("\nUsuários cadastrados:")
        for usuario in usuarios:
            print(f"{usuario.id_usuario} - {usuario.nome}")

        id_usuario = int(input("Digite o ID do usuário:"))

        usuario_escolhido = None

        for usuario in usuarios:
            if usuario.id_usuario == id_usuario:
                usuario_escolhido = usuario
                break 

        if usuario_escolhido is None:
            print("Usuário não encontrado.")
            continue 

        print("\nitens disponíveis para empréstimos:")

        for item in itens:
            if item.disponivel:
                print(f"{item.codigo} - {item.titulo}")

        codigo_item = int(input("Digite o código do item:"))

        item_escolhido = None

        for item in itens:
            if item.codigo == codigo_item:
                item_escolhido = item
                break

        if item_escolhido is None:
            print("Item não encontrado.")
            continue

        if not item_escolhido.disponivel:
            print("Esse item já está emprestado.")
            continue

        data = input("Digite a data do empréstimo:")

        codigo_emprestimo = len(emprestimos) + 1 

        emprestimo = Emprestimo(codigo_emprestimo, data)

        emprestimo.adicionar_item(item_escolhido)

        item_escolhido.emprestar()

        usuario_escolhido.realizar_emprestimo(emprestimo)

        emprestimos.append(emprestimo)

        print("Empréstimo realizado com sucesso!")


    if opcao == "7":
        if not emprestimos:
            print("Nenhum empréstimo cadastrado")
            continue

        print("\nEmpréstimos cadastrados:")

        for emprestimo in emprestimos:
            print(
                f"{emprestimo.codigo} -"
                f"Data: {emprestimo.data_emprestimo}"
                )


        codigo_emprestimo = int(input("Digite o código do empréstimo:"))

        emprestimo_escolhido = None

        for emprestimo in emprestimos:
            if emprestimo.codigo == codigo_emprestimo:
                emprestimo_escolhido = emprestimo
                break

        if emprestimo_escolhido is None:
            print("Empréstimo não encontrado.")
            continue

        data_devolucao = input("Digite a data da devolução do item:")

        emprestimo_escolhido.finalizar(data_devolucao)

        print("Empréstimo finalizado! ")


    if opcao == "8":
        if not usuarios:
            print("Nenhum usuário cadastrado.")
            continue


        print("\n===== USUÁRIOS CADASTRADOS =====")

        for usuario in usuarios:
            print(f"ID: {usuario.id_usuario}")
            print(f"Nome: {usuario.nome}")
            print(f"E-mail: {usuario.email}")
            print(f"Empréstimos: {len(usuario.emprestimos)}")
            print("--------------------------------")

    if opcao == "9":
        if not itens:
            print("Nenhum item cadastrado.")
            continue

        print("\n===== ITENS DA BIBLIOTECA =====")

        for item in itens:
            print(item.exibir_informacoes())
            print(f"Disponível: {'Sim' if item.disponivel else 'Não'}")
            print("--------------------------------")

    if opcao == "10":
        if not prateleiras:
            print("nenhuma prateleira cadastrada.")
            continue 

        print ("\n===== PRATELEIRAS =====")

        for prateleira in prateleiras:
            print(prateleira.listar_itens())
            print("--------------------------------")

    if opcao == "11":
        if not emprestimos:
            print("Nenhum empréstimo cadastrado.")
            continue

        print("\n===== EMPRÉSTIMOS =====")

        for emprestimo in emprestimos:

            print(f"Código: {emprestimo.codigo}")
            print(
            f"Data do empréstimo: "
            f"{emprestimo.data_emprestimo}")

        if emprestimo.data_devolucao:
            print(
                f"Data da devolução: "
                f"{emprestimo.data_devolucao}"
            )
        else:
            print("Status: Em aberto")

        print("Itens:")

        for item_emprestado in emprestimo.itens:
            print(
                f"- {item_emprestado.exibir_item()}"
            )

        print("--------------------------------")

    elif opcao == "0":
        print("Encerrando o sistema...")
        break

    