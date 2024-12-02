import time
import armazenamento


# Função para cadastrar um novo produto
def cadastrar_produto(id, nome, preco, quantidade, funcionario):
    armazenamento.produtos[id] = {
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade,
        "data": time.strftime("%d/%m/%Y"),
        "funcionario": funcionario
    }


# Função para listar os produtos cadastrados
def listar_produtos():
    return armazenamento.produtos


# Função para atualizar os dados de um produto
def atualizar_produto(id, campo, valor):
    if id in armazenamento.produtos:
        armazenamento.produtos[id][campo] = valor
    else:
        print(f"Produto com ID {id} não encontrado.")


# Função para deletar um produto
def deletar_produto(id):
    if id in armazenamento.produtos:
        del armazenamento.produtos[id]
    else:
        print(f"Produto com ID {id} não encontrado.")


# Função para registrar uma venda
def registrar_venda(venda):
    armazenamento.registro_vendas.append(venda)


# Função para listar todas as vendas registradas
def listar_vendas():
    return armazenamento.registro_vendas


# Função para abastecer o estoque de um produto
def abastecer_estoque(id_produto, quantidade_adicional):
    if id_produto in armazenamento.produtos:
        armazenamento.produtos[id_produto]["quantidade"] += quantidade_adicional
    else:
        print(f"Produto com ID {id_produto} não encontrado.")
