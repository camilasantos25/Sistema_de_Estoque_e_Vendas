def validar_preco(preco):
    if preco <= 0:
        raise ValueError("O preço deve ser maior que zero.")

def validar_quantidade(quantidade):
    if quantidade < 0:
        raise ValueError("A quantidade não pode ser negativa.")

class Produto:
    def __init__(self, codigo, nome, categoria, preco, quantidade):
        validar_preco(preco)
        validar_quantidade(quantidade)
        
        self.codigo = codigo
        self.nome = nome
        self.categoria = categoria
        self.preco = preco
        self.quantidade = quantidade