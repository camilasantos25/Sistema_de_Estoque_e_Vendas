import arquivos
from estoque import Estoque
from produto import validar_preco, validar_quantidade

ARQUIVO = "dados.csv"

def ler_valor(pergunta, converter, validar=None):
    while True:
        texto = input(pergunta)
        try:
            valor = converter(texto)
            if validar is not None:
                validar(valor)
            return valor
        except ValueError as erro:
            print("Entrada inválida:", erro)

def ler_decimal(texto):
    return float(texto.replace(",", "."))

def ler_texto(pergunta):
    while True:
        texto = input(pergunta).strip()
        if texto != "":
            return texto
        print("Este campo não pode ficar vazio.")

def validar_quantidade_venda(quantidade):
    if quantidade <= 0:
        raise ValueError("A quantidade da venda deve ser maior que zero.")

def validar_limite(limite):
    if limite < 0:
        raise ValueError("O limite não pode ser negativo.")

def mostrar_produto(produto):
    print(
        " ", produto.codigo, "|", produto.nome, "|", produto.categoria,
        "| R$", produto.preco, "| qtd:", produto.quantidade,
    )

def mostrar_lista(produtos):
    if len(produtos) == 0:
        print("  (nenhum produto)")
    for produto in produtos:
        mostrar_produto(produto)

def mostrar_menu():
    print()
    print("===== Sistema de Estoque e Vendas =====")
    print("1 - Listar produtos (por código)")
    print("2 - Buscar produto por código")
    print("3 - Buscar produtos por nome")
    print("4 - Listar produtos por categoria")
    print("5 - Cadastrar produto")
    print("6 - Editar produto")
    print("7 - Remover produto")
    print("8 - Registrar venda")
    print("9 - Relatório de estoque baixo")
    print("10 - Configurar limite de estoque baixo")
    print("0 - Salvar e sair")

def listar_produtos(estoque):
    mostrar_lista(estoque.listar_ordenado())

def buscar_por_codigo(estoque):
    codigo = ler_valor("Código: ", int)
    produto = estoque.buscar_por_codigo(codigo)
    if produto is None:
        print("Produto não encontrado.")
    else:
        mostrar_produto(produto)

def buscar_por_nome(estoque):
    nome = ler_texto("Nome (ou parte dele): ")
    mostrar_lista(estoque.buscar_por_nome(nome))

def listar_por_categoria(estoque):
    categoria = ler_texto("Categoria: ")
    mostrar_lista(estoque.listar_por_categoria(categoria))

def cadastrar_produto(estoque):
    codigo = ler_valor("Código: ", int)
    if estoque.buscar_por_codigo(codigo) is not None:
        print("Já existe um produto com esse código.")
        return

    nome = ler_texto("Nome: ")
    categoria = ler_texto("Categoria: ")
    preco = ler_valor("Preço: ", ler_decimal, validar_preco)
    quantidade = ler_valor("Quantidade: ", int, validar_quantidade)

    produto = Produto(codigo, nome, categoria, preco, quantidade)
    estoque.cadastrar(produto)
    print("Produto cadastrado!")

def editar_produto(estoque):
    codigo = ler_valor("Código do produto a editar: ", int)
    if estoque.buscar_por_codigo(codigo) is None:
        print("Produto não encontrado.")
        return

    nome = ler_texto("Novo nome: ")
    categoria = ler_texto("Nova categoria: ")
    preco = ler_valor("Novo preço: ", ler_decimal, validar_preco)
    quantidade = ler_valor("Nova quantidade: ", int, validar_quantidade)

    estoque.editar(codigo, nome, categoria, preco, quantidade)
    print("Produto editado!")

def remover_produto(estoque):
    codigo = ler_valor("Código do produto a remover: ", int)
    if estoque.remover(codigo):
        print("Produto removido!")
    else:
        print("Produto não encontrado.")

def registrar_venda(estoque):
    codigo = ler_valor("Código do produto: ", int)
    quantidade = ler_valor("Quantidade: ", int, validar_quantidade_venda)

    resultado = estoque.vender(codigo, quantidade)
    if resultado == "ok":
        print("Venda registrada!")
    elif resultado == "insuficiente":
        print("Estoque insuficiente.")
    else:
        print("Produto não encontrado.")

def relatorio_estoque_baixo(estoque):
    print("Limite atual:", estoque.limite_estoque_baixo)
    mostrar_lista(estoque.estoque_baixo())

def configurar_limite(estoque):
    print("Limite atual:", estoque.limite_estoque_baixo)
    limite = ler_valor("Novo limite: ", int, validar_limite)
    estoque.definir_limite(limite)
    print("Limite atualizado!")

def main():
    estoque, avisos = arquivos.carregar(ARQUIVO)
    for aviso in avisos:
        print("Aviso:", aviso)

    while True:
        mostrar_menu()
        opcao = input("Escolha: ").strip()

        if opcao == "1":
            listar_produtos(estoque)
        elif opcao == "2":
            buscar_por_codigo(estoque)
        elif opcao == "3":
            buscar_por_nome(estoque)
        elif opcao == "4":
            listar_por_categoria(estoque)
        elif opcao == "5":
            cadastrar_produto(estoque)
        elif opcao == "6":
            editar_produto(estoque)
        elif opcao == "7":
            remover_produto(estoque)
        elif opcao == "8":
            registrar_venda(estoque)
        elif opcao == "9":
            relatorio_estoque_baixo(estoque)
        elif opcao == "10":
            configurar_limite(estoque)
        elif opcao == "0":
            arquivos.salvar(estoque, ARQUIVO)
            print("Dados salvos. Até logo!")
            break
        else:
            print("Opção inválida.")

main()