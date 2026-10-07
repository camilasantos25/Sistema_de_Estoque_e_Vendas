import csv
from estoque import Estoque
from produto import Produto

def salvar(estoque, caminho):
    with open(caminho, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow(["codigo", "nome", "categoria", "preco", "quantidade"])
        for produto in estoque.produtos_ordenados:
            escritor.writerow([
                produto.codigo,
                produto.nome,
                produto.categoria,
                produto.preco,
                produto.quantidade,
            ])

def carregar(caminho):
    estoque = Estoque()

    try:
        with open(caminho, "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor, None)
            for linha in leitor:
                produto = Produto(
                    int(linha[0]),
                    linha[1],
                    linha[2],
                    float(linha[3]),
                    int(linha[4]),
                )
                estoque.cadastrar(produto)
    except FileNotFoundError:
        pass

    return estoque