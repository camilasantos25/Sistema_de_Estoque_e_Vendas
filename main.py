from produto import Produto
from estoque import Estoque

estoque = Estoque()

estoque.cadastrar(Produto(50, "Caneta Vermelha", "Papelaria", 2.5, 100))
estoque.cadastrar(Produto(12, "Caderno", "Papelaria", 15.9, 40))
estoque.cadastrar(Produto(99, "Mochila", "Acessorios", 120.0, 8))

print("Vender 10 canetas:", estoque.vender(50, 10))
print("Estoque da caneta:", estoque.buscar_por_codigo(50).quantidade)

print("Vender 500 canetas:", estoque.vender(50, 500))
print("Vender produto 1234:", estoque.vender(1234, 1))

print("Editar caderno:", estoque.editar(12, "Caderno Grande", "Papelaria", 20.0, 35))
print("Novo nome:", estoque.buscar_por_codigo(12).nome)
print("Editar produto 1234:", estoque.editar(1234, "X", "Y", 1.0, 1))

print("Remover mochila:", estoque.remover(99))
print("Buscar mochila:", estoque.buscar_por_codigo(99))
print("Remover de novo:", estoque.remover(99))
print("Total nas listas:", len(estoque.produtos), len(estoque.produtos_ordenados))