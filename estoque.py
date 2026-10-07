class Estoque:
    def __init__(self):
        self.produtos = []
        self.produtos_ordenados = []

    def posicao_para_inserir(self, codigo):
        for i in range(len(self.produtos_ordenados)):
            if self.produtos_ordenados[i].codigo > codigo:
                return i
        return len(self.produtos_ordenados)

    def buscar_por_codigo(self, codigo):
        baixo = 0
        alto = len(self.produtos_ordenados) -1

        while baixo <= alto:
            meio = (baixo + alto) // 2
            produto = self.produtos_ordenados[meio]

            if produto.codigo == codigo:
                return produto
            elif produto.codigo < codigo:
                baixo = meio + 1
            else:
                alto = meio - 1
        return None

    def cadastrar(self, produto):
        if self.buscar_por_codigo(produto.codigo) is not None:
            return False
        
        self.produtos.append(produto)
        posicao = self.posicao_para_inserir(produto.codigo)
        self.produtos_ordenados.insert(posicao, produto)
        return True

    def buscar_por_nome(self, nome):
        encontrados = []
        for produto in self.produtos:
            if nome.lower() in produto.nome.lower():
                encontrados.append(produto)
        return encontrados

    def editar(self, codigo, nome, categoria, preco, quantidade):
        produto = self.buscar_por_codigo(codigo)
        if produto is None:
            return False

        produto.nome = nome
        produto.categoria = categoria
        produto.preco = preco
        produto.quantidade = quantidade
        return True

    def remover(self, codigo):
        produto = self.buscar_por_codigo(codigo)
        if produto is None:
            return False

        self.produtos.remove(produto)
        self.produtos_ordenados.remove(produto)
        return True

    def vender(self, codigo, quantidade):
        produto = self.buscar_por_codigo(codigo)
        if produto is None:
            return "Inexistente"
        if quantidade > produto.quantidade:
            return "Insuficiente"

        produto.quantidade = produto.quantidade - quantidade
        return "Ok"
