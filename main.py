import arquivos

estoque, avisos = arquivos.carregar("dados_ruim.csv")

print("Produtos carregados:", len(estoque.produtos))
for produto in estoque.listar_ordenado():
    print(" ", produto.codigo, produto.nome)

print("Avisos:")
for aviso in avisos:
    print(" ", aviso)

vazio, avisos_vazio = arquivos.carregar("nao_existe.csv")
print("Arquivo inexistente:", len(vazio.produtos), len(avisos_vazio))