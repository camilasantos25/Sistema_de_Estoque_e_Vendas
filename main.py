from produto import Produto
from estoque import Estoque

def mostrar(produtos):
    if len(produtos) == 0:
        print("  (nenhum produto)")
    for produto in produtos:
        print(" ", produto.codigo, produto.nome, "- qtd:", produto.quantidade)

estoque = Estoque()

estoque.cadastrar(Produto(50, "Caneta Vermelha", "Papelaria", 2.5, 100))
estoque.cadastrar(Produto(12, "Caderno", "Papelaria", 15.9, 40))
estoque.cadastrar(Produto(99, "Mochila", "Acessorios", 120.0, 8))
estoque.cadastrar(Produto(7, "Caneta Preta", "Papelaria", 3.0, 60))
estoque.cadastrar(Produto(30, "Borracha", "Papelaria", 1.5, 5))

print("Por código:")
mostrar(estoque.listar_ordenado())

print("Categoria papelaria:")
mostrar(estoque.listar_por_categoria("papelaria"))

print("Categoria livros:")
mostrar(estoque.listar_por_categoria("livros"))

print("Estoque baixo (limite 10):")
mostrar(estoque.estoque_baixo())

estoque.definir_limite(50)
print("Estoque baixo (limite 50):")
mostrar(estoque.estoque_baixo())

estoque.definir_limite(0)
print("Estoque baixo (limite 0):")
mostrar(estoque.estoque_baixo())