class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self._preco = preco

    def get_preco(self):
        return self._preco
    
    
    def exibir_detalhe(self):
        print(f"Produto: {self.nome} | Preço: R$ {self._preco}")