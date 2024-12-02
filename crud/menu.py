import time
import os
import funcionalidades
import armazenamento


def limpar_tela():
    time.sleep(2)
    os.system("cls")


id_produto = 0

while True:
    opcao = int(input("[1]- Cadastrar\n[2]- Listar\n[3]- Atualizar\n[4]- Deletar\n[5]- Registrar venda\n[6]- Listar registro de vendas\n[7]- Abastecer estoque\n[8]- Sair\n"))

    if opcao == 1:  # Cadastrar
        nome = input("Produto: ")
        preco = float(input("Preço: "))
        quantidade = int(input("Quantidade: "))
        funcionario = input("Funcionário que fez o cadastro: ")
        funcionalidades.cadastrar_produto(id_produto, nome, preco, quantidade, funcionario)
        id_produto += 1
        print("Produto cadastrado com sucesso!")
        limpar_tela()

    elif opcao == 2:  # Listar
        produtos = funcionalidades.listar_produtos()
        if not produtos:
            print("Não há produtos cadastrados!")
        else:
            for id, produto in produtos.items():
                print(f"ID: {id} | Produto: {produto['nome']} | Preço: R${produto['preco']:.2f} | Quantidade: {produto['quantidade']} | Data: {produto['data']} | Funcionário: {produto['funcionario']}")
        print("\n")

    elif opcao == 3:  # Atualizar
        id_att = int(input("Informe o ID do produto que deseja atualizar: "))
        if id_att in armazenamento.produtos:
            print("Escolha o campo que deseja atualizar:")
            print("[1]- Nome\n[2]- Preço\n[3]- Quantidade\n")

            escolha = input("Digite o número correspondente: ")

            if escolha == "1":
                campo = "nome"
                valor = input("Novo nome: ")
            elif escolha == "2":
                campo = "preco"
                valor = float(input("Novo preço: "))
            elif escolha == "3":
                campo = "quantidade"
                valor = int(input("Nova quantidade: "))
            else:
                print("Opção inválida!")
                continue

            funcionalidades.atualizar_produto(id_att, campo, valor)
            print("Produto atualizado com sucesso!")
        else:
            print("Erro: Produto não encontrado!")
        limpar_tela()

    elif opcao == 4:  # Deletar
        id_delet = int(input("Informe o ID do produto que deseja deletar: "))
        if id_delet in armazenamento.produtos:
            funcionalidades.deletar_produto(id_delet)
            print("Produto deletado com sucesso!")
        else:
            print("Erro: Produto não encontrado!")
        limpar_tela()

    elif opcao == 5:  # Registrar venda
        vendedor = input("Digite o nome do vendedor responsável pela venda: ")
        while True:
            id_produto_venda = int(input("Informe o ID do produto vendido: "))
            if id_produto_venda in armazenamento.produtos:
                quantidade_vendida = int(input("Informe a quantidade vendida: "))
                produto = armazenamento.produtos[id_produto_venda]

                if produto["quantidade"] >= quantidade_vendida:
                    armazenamento.itens_vendidos.append({
                        "id_produto": id_produto_venda,
                        "nome_produto": produto["nome"],
                        "quantidade": quantidade_vendida,
                        "valor": quantidade_vendida * produto["preco"]
                    })

                    produto["quantidade"] -= quantidade_vendida

                    continuar = input("Deseja adicionar mais itens? (s/n): ").lower()
                    if continuar == "n":
                        break
                else:
                    print(f"Quantidade insuficiente de {produto['nome']} no estoque!")
            else:
                print("Erro: Produto não encontrado!")

        total_venda = 0
        for item in armazenamento.itens_vendidos:
            total_venda += item["valor"]

        venda = {
            "vendedor": vendedor,
            "data": time.strftime("%d/%m/%Y"),
            "itens": armazenamento.itens_vendidos,
            "total": total_venda
        }

        funcionalidades.registrar_venda(venda)
        print("Venda registrada com sucesso!")
        limpar_tela()


    elif opcao == 6:  # Listar vendas
        vendas = funcionalidades.listar_vendas()
        if not vendas:
            print("Não há vendas registradas!")
        else:
            for venda in vendas:
                print(f"Data: {venda['data']} | Vendedor: {venda['vendedor']}")
                for item in venda["itens"]:
                    print(f"Produto: {item['nome_produto']}, Quantidade: {item['quantidade']}, "
                          f"Valor: R${item['valor']:.2f}")
                print(f"Total da venda: R${venda['total']:.2f}\n")

    elif opcao == 7:  # Abastecer estoque
        id_produto = int(input("Informe o ID do produto a ser abastecido: "))
        if id_produto in armazenamento.produtos:
            quantidade_adicional = int(input("Quantidade a ser adicionada ao estoque: "))
            funcionalidades.abastecer_estoque(id_produto, quantidade_adicional)
            print("Estoque atualizado com sucesso!")
        else:
            print("Erro: Produto não encontrado!")
        limpar_tela()

    elif opcao == 8:  # Sair
        print("Volte sempre!")
        limpar_tela()
        break

    else:
        print("Opção inválida! Tente novamente.")
        limpar_tela()
