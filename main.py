from produto import Produto
import arquivos

estoque = arquivos.carregar("dados.csv")
print("Produtos carregados:", len(estoque.produtos))

for produto in estoque.listar_ordenado():
    print(" ", produto.codigo, produto.nome, produto.preco, produto.quantidade)

print("Buscando código 50:", estoque.buscar_por_codigo(50).nome)

estoque.cadastrar(Produto(30, "Borracha", "Papelaria", 1.5, 200))
arquivos.salvar(estoque, "dados.csv")
print("Salvo com a borracha!")

outro = arquivos.carregar("arquivo_que_nao_existe.csv")
print("Estoque de arquivo inexistente:", len(outro.produtos))