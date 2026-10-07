from produto import Produto
from estoque import Estoque

estoque = Estoque()

estoque.cadastrar(Produto(50, "Caneta Vermelha", "Papelaria", 2.5, 100))
estoque.cadastrar(Produto(12, "Caderno", "Papelaria", 15.9, 40))
estoque.cadastrar(Produto(99, "Mochila", "Acessorios", 120.0, 8))
estoque.cadastrar(Produto(7, "Caneta Preta", "Papelaria", 3.0, 60))
estoque.cadastrar(Produto(30, "Borracha", "Papelaria", 1.5, 200))

achado = estoque.buscar_por_codigo(50)
print(achado.codigo, achado.nome)

achado = estoque.buscar_por_codigo(7)
print(achado.codigo, achado.nome)

achado = estoque.buscar_por_codigo(99)
print(achado.codigo, achado.nome)

print(estoque.buscar_por_codigo(40))

duplicado = Produto(12, "Caderno Repetido", "Papelaria", 10.0, 5)
print("Cadastrou o duplicado?", estoque.cadastrar(duplicado))
print("Total:", len(estoque.produtos), len(estoque.produtos_ordenados))