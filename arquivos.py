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
    avisos = []

    try:
        with open(caminho, "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.reader(arquivo)
            next(leitor, None)
            numero_linha = 1
            for linha in leitor:
                numero_linha = numero_linha + 1

                try:
                    produto = Produto(
                        int(linha[0]),
                        linha[1],
                        linha[2],
                        float(linha[3]),
                        int(linha[4]),
                    )
                except (ValueError, IndexError) as erro:
                    avisos.append("Linha " + str(numero_linha) + " ignorada: " + str(erro))
                    continue
                if not estoque.cadastrar(produto):
                    avisos.append("Linha " + str(numero_linha) + " ignorada: código duplicado.")
    except FileNotFoundError:
        pass

    return estoque, avisos