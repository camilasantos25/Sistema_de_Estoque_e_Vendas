from produto import Produto
from estoque import Estoque

estoque = Estoque()

estoque.cadastrar(Produto(50, "Caneta Vermelha", "Papelaria", 2.5, 100))
estoque.cadastrar(Produto(12, "Caderno", "Papelaria", 15.9, 40))
estoque.cadastrar(Produto(99, "Mochila", "Acessorios", 120.0, 8))

print(len(estoque.produtos))
print(estoque.produtos[0].nome)
print(estoque.produtos[2].nome)