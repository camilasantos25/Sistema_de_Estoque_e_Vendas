class Estoque:
    def __init__(self):
        self.produtos = []

    def cadastrar(self, produto):
        self.produtos.append(produto)