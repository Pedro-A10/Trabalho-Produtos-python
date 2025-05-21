class Estoque:
    def __init__(self):
        self.produtos = {}

    def adicionar_produto(self, codigo, quantidade):
        if codigo in self.produtos:
            self.produtos[codigo] += quantidade  # Se produto existe, soma quantidade
        else:
            self.produtos[codigo] = quantidade  # Se não existe, cria nova entrada

    def remover_produto(self, codigo, quantidade):
        if codigo in self.produtos:
            if self.produtos[codigo] >= quantidade:
                self.produtos[codigo] -= quantidade
                if self.produtos[codigo] == 0:
                    del self.produtos[codigo]
                return True
            else:
                print("Quantidade insuficiente em estoque.")
                return False
        else:
            print("Produto não encontrado no estoque.")
            return False

    def consultar_estoque(self, codigo):
        return self.produtos.get(codigo, 0)

    def listar_estoque(self):
        if not self.produtos:
            print("Nenhum produto cadastrado no estoque.")
        else:
            for codigo, quantidade in self.produtos.items():
                print(f"Código: {codigo} - Quantidade: {quantidade}")