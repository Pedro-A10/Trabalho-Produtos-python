from Produto_Exception import ProdutoInvalidoException

class Produto:
    lista_produtos = []

    def __init__(self, nome, id_produto, preco, quantidade):
        if not nome or not id_produto or float(preco) < 0 or int(quantidade) < 0:
            raise ProdutoInvalidoException("Dados do produto inválidos")
        self.nome = nome
        self.id_produto = id_produto
        self.preco = float(preco)
        self.quantidade = int(quantidade)
        self.preco_com_imposto = self.calcular_imposto(self.preco, self.quantidade)

    @staticmethod
    def calcular_imposto(preco, quantidade):
        imposto = 152
        return preco * quantidade + imposto

    @classmethod
    def cadastrar_produto(cls):
        nome = input("Digite o nome do produto: ")
        id_produto = input("Digite o ID do produto: ")
        preco = input("Digite o preço do produto: ")
        quantidade = input("Digite a quantidade do produto: ")

        produto = cls(nome, id_produto, preco, quantidade)
        cls.lista_produtos.append(produto)
        print("Produto cadastrado com sucesso!\n")

    @classmethod
    def listar_produtos(cls):
        if not cls.lista_produtos:
            print("Nenhum produto cadastrado.\n")
            return

        print("\nLista de Produtos:")
        for p in cls.lista_produtos:
            print(f"Nome: {p.nome}")
            print(f"ID: {p.id_produto}")
            print(f"Preço unitário: R${p.preco:.2f}")
            print(f"Quantidade: {p.quantidade}")
            print(f"Preço final com imposto: R${p.preco_com_imposto:.2f}")
            print("-" * 30)

while True:
    print("1 - Cadastrar Produto")
    print("2 - Listar Produtos")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        try:
            Produto.cadastrar_produto()
        except ProdutoInvalidoException as e:
            print(f"Erro ao cadastrar produto: {e}")
    elif opcao == "2":
        Produto.listar_produtos()
    elif opcao == "3":
        break
    else:
        print("Opção inválida.\n")
