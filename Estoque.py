from Estoque_Exception import ProdutoNaoEncontradoNoEstoqueException, EstoqueInsuficienteException, QuantidadeInvalidaException

class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, codigo, quantidade):
        if quantidade <= 0:
            raise QuantidadeInvalidaException("Quantidade deve ser maior que zero")
        if codigo in self.produtos:
            self.produtos[codigo] += quantidade  # Se produto existe, soma quantidade
        else:
            self.produtos[codigo] = quantidade  # Se não existe, cria nova entrada

    def remover_produto(self, codigo, quantidade):
        if codigo not in self.produtos:
            raise ProdutoNaoEncontradoNoEstoqueException("Produto não encontrado no estoque.")
        if quantidade <= 0:
            raise QuantidadeInvalidaException("Quantidade deve ser maior que zero")
        if self.produtos[codigo] < quantidade:
            raise EstoqueInsuficienteException("Quantidade insuficiente em estoque.")
        self.produtos[codigo] -= quantidade
        if self.produtos[codigo] == 0:
            del self.produtos[codigo]

    def consultar_estoque(self, codigo):
        return self.produtos.get(codigo, 0)

    def listar_estoque(self):
        if not self.produtos:
            print("Nenhum produto cadastrado no estoque.")
        else:
            for codigo, quantidade in self.produtos.items():
                print(f"Código: {codigo} - Quantidade: {quantidade}")
    def listar_estoque(self):
        if not self.produtos:
            print("Nenhum produto cadastrado no estoque.")
        else:
            for codigo, quantidade in self.produtos.items():
                print(f"Código: {codigo} - Quantidade: {quantidade}")
