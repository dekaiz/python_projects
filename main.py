# criar um mercado que pode:
# cadastrar produto
# remover produto
# listar produtos
# pesquisar produto
# calcular valor
# salvar dados

lista_produtos = []

# calcular valor dos produtos da lista
def calcular_valor_produtos():
    resultado = 0

    # para cada valor na lista dicionário some o valor resultado += resultado anterior
    for produto in lista_produtos:
        resultado += produto["valor"]

    print(resultado)

# cadastrar produtos
def cadastrar_produto(p, v):
    """Cadastra um usuário na lista_produtos"""
    encontrado = False

    for produto in lista_produtos:
        if produto["nome"] == p:
            print("Produto já cadastrado")
            encontrado = True
            break

    if not encontrado:
        cdt_produto = {
            "nome": p,
            "valor": v
        }
        lista_produtos.append(cdt_produto)
        print(f'o produto {cdt_produto["nome"]} foi cadastrado com sucesso!')

def remover_produto(p):
    """Remove produto da lista_produtos"""
    encontrado = False

    for rmv_produto in lista_produtos:
        if rmv_produto["nome"] == p:
            lista_produtos.remove(rmv_produto)
            print("Produto removido do banco de dados")
            encontrado = True
            break

    if not encontrado:
        print("O produto não está cadastrado no banco de dados")

def listar_produtos(lista):
    """Lista produtos da lista_produtos"""
    if not lista_produtos:
        print("Ainda não há produtos cadastrados")
    else:
        print("=== LISTA DE PRODUTOS ===")
        for produto in lista:
            print(f'{produto["nome"]} - {produto['valor']:.2f} R$')

def pesquisar_produto(p):
    """Pesquisa produtos na lista_produtos"""
    # quero que se o nome não estiver na lista então ele mostre que não foi possível encontrar no banco de dados
    encontrado = False # controle se foi encontrado ou não

    # loop para procurar produto
    for produto in lista_produtos:
        if produto["nome"] == p:
            print(f'{produto["nome"]} - {produto["valor"]:.2f} R$') # printa, já que encontrou resultado
            encontrado = True # encontrou produto e mudou a variavel de controle para verdadeiro
            break

    if not encontrado:
        print("Produto não encontrado no banco de dados")

while True:
    print('==== Mercado do João ====')
    print('1. Cadastrar produto')
    print('2. Remover produto')
    print('3. Listar produtos')
    print('4. Pesquisar produto')
    print('5. Calcular lista de produtos')
    print('0. Para sair do programa')

    print()
    funcao = input('Digite o número associado à função: ')


    if funcao == '1':
        nome = input('Digite o nome do produto: ')

        while True:
            try:
                valor = int(input('Digite o valor do produto: '))
                break
            except ValueError:
                print('Por favor digite apenas números!')

        cadastrar_produto(nome, valor)

    elif funcao == '2':
        nome = input('Digite o nome do produto: ')
        remover_produto(nome)

    elif funcao == '3':
        listar_produtos(lista_produtos)

    elif funcao == '4':
        nome = input('Digite o nome do produto: ')
        pesquisar_produto(nome)

    elif funcao == '5':
        calcular_valor_produtos()

    elif funcao == '0':
        break