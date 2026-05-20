# criar um mercado que pode:
# cadastrar produto
# remover produto
# listar produtos
# pesquisar produto
# calcular valor
# salvar dados

lista_produtos = []

def cadastrar_produto(nome, valor):
    # se o produto já existe em lista_produtos então retorne "produto já cadastrado"
    for produto in lista_produtos:
        if produto["nome"] == nome:
            print("Produto já cadastrado")

    cdt_produto = {
        "nome": nome,
        "valor": valor
    }
    lista_produtos.append(cdt_produto)
    print(f"Produto: {cdt_produto} cadastrado com sucesso!")

def remover_produto(nome):
    for rmv_produto in lista_produtos:
        if rmv_produto["nome"] == nome:
            lista_produtos.remove(rmv_produto)

def listar_produtos(lista):
    print("=== LISTA DE PRODUTOS ===")
    for produto in lista:
        print(f"{produto["nome"]} - {produto["valor"]:.2f} R$")

def pesquisar_produto(nome):
    # quero que se o nome não estiver na lista então ele mostre que não foi possível encontrar no banco de dados
    encontrado = False # controle se foi encontrado ou não

    # loop para procurar produto
    for produto in lista_produtos:
        if produto["nome"] == nome:
            encontrado = True # encontrou produto e mudou a variavel de controle para verdadeiro
            print(f"{produto["nome"]} - {produto["valor"]:.2f} R$") # printa, já que encontrou resultado
            break

    if not encontrado:
        print("Produto não encontrado no banco de dados")


cadastrar_produto('Notebook', 1500)
cadastrar_produto('Teclado', 200)
cadastrar_produto('Mouse', 100)
remover_produto('Notebook')
listar_produtos(lista_produtos)
print()
pesquisar_produto("Mouse")
pesquisar_produto("Caneta")



