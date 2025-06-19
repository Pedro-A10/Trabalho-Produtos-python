class ClienteJaExisteException(Exception):
    pass

class ClienteInvalidoException(Exception):
    pass

class ClienteNaoEncontradoException(Exception):
    pass

class ProdutoNaoEncontradoNoEstoqueException(Exception):
    pass

class EstoqueInsuficienteException(Exception):
    pass

class QuantidadeInvalidaException(Exception):
    pass

class ProdutoJaExisteException(Exception):
    pass

class ProdutoInvalidoException(Exception):
    pass

class ProdutoNaoEncontradoException(Exception):
    pass

class Cliente:
    lista_clientes = []

    def __init__(self, nome, email):
        try:
            if not nome or not email:
                raise ClienteInvalidoException("Nome e email são obrigatórios.")
            self.nome = nome
            self.email = email
        except ClienteInvalidoException as e:
            print(f"Erro ao criar cliente: {e}")

    def __str__(self):
        try:
            return f"Cliente: {self.nome}, Email: {self.email}"
        except Exception as e:
            print(f"Erro ao converter cliente para string: {e}")

    @classmethod
    def cadastrar_cliente(cls):
        try:
            nome = input("Digite o nome do cliente: ")
            email = input("Digite o email do cliente: ")

            for cliente in cls.lista_clientes:
                if cliente.email == email:
                    print("Cliente já cadastrado com esse email!\n")
                    return

            cliente = cls(nome, email)
            cls.lista_clientes.append(cliente)
            print("Cliente cadastrado com sucesso!\n")
        except Exception as e:
            print(f"Erro ao cadastrar cliente: {e}")

    @classmethod
    def listar_clientes(cls):
        try:
            if not cls.lista_clientes:
                print("Nenhum cliente cadastrado.\n")
                return

            print("\nLista de Clientes:")
            for c in cls.lista_clientes:
                print(f"Nome: {c.nome}")
                print(f"Email: {c.email}")
                print("-" * 30)
        except Exception as e:
            print(f"Erro ao listar clientes: {e}")

class Estoque:
    def __init__(self):
        try:
            self.produtos = {}
        except Exception as e:
            print(f"Erro ao inicializar estoque: {e}")

    def adicionar_produto(self, codigo, quantidade):
        try:
            if quantidade <= 0:
                raise QuantidadeInvalidaException("Quantidade deve ser maior que zero")
            if codigo in self.produtos:
                self.produtos[codigo] += quantidade
            else:
                self.produtos[codigo] = quantidade
        except (QuantidadeInvalidaException, Exception) as e:
            print(f"Erro ao adicionar produto: {e}")

    def remover_produto(self, codigo, quantidade):
        try:
            if codigo not in self.produtos:
                raise ProdutoNaoEncontradoNoEstoqueException("Produto não encontrado no estoque.")
            if quantidade <= 0:
                raise QuantidadeInvalidaException("Quantidade deve ser maior que zero")
            if self.produtos[codigo] < quantidade:
                raise EstoqueInsuficienteException("Quantidade insuficiente em estoque.")
            self.produtos[codigo] -= quantidade
            if self.produtos[codigo] == 0:
                del self.produtos[codigo]
        except (ProdutoNaoEncontradoNoEstoqueException, QuantidadeInvalidaException, EstoqueInsuficienteException, Exception) as e:
            print(f"Erro ao remover produto: {e}")

    def consultar_estoque(self, codigo):
        try:
            return self.produtos.get(codigo, 0)
        except Exception as e:
            print(f"Erro ao consultar estoque: {e}")

    def listar_estoque(self):
        try:
            if not self.produtos:
                print("Nenhum produto cadastrado no estoque.")
            else:
                for codigo, quantidade in self.produtos.items():
                    print(f"Código: {codigo} - Quantidade: {quantidade}")
        except Exception as e:
            print(f"Erro ao listar estoque: {e}")

class Produto:
    lista_produtos = []

    def __init__(self, nome, id_produto, preco, quantidade):
        try:
            if not nome or not id_produto or float(preco) < 0 or int(quantidade) < 0:
                raise ProdutoInvalidoException("Dados do produto inválidos")
            self.nome = nome
            self.id_produto = id_produto
            self.preco = float(preco)
            self.quantidade = int(quantidade)
            self.preco_com_imposto = self.calcular_imposto(self.preco, self.quantidade)
        except ProdutoInvalidoException as e:
            print(f"Erro ao criar produto: {e}")
        except Exception as e:
            print(f"Erro inesperado ao criar produto: {e}")

    @staticmethod
    def calcular_imposto(preco, quantidade):
        try:
            imposto = 152
            return preco * quantidade + imposto
        except Exception as e:
            print(f"Erro ao calcular imposto: {e}")
            return 0

    @classmethod
    def cadastrar_produto(cls):
        try:
            nome = input("Digite o nome do produto: ")
            id_produto = input("Digite o ID do produto: ")
            preco = input("Digite o preço do produto: ")
            quantidade = input("Digite a quantidade do produto: ")

            produto = cls(nome, id_produto, preco, quantidade)
            cls.lista_produtos.append(produto)
            print("Produto cadastrado com sucesso!\n")
        except ProdutoInvalidoException as e:
            print(f"Erro ao cadastrar produto: {e}")
        except Exception as e:
            print(f"Erro inesperado ao cadastrar produto: {e}")

    @classmethod
    def listar_produtos(cls):
        try:
            if not cls.lista_produtos:
                print("Nenhum produto cadastrado.\n")
                return

            print("\nLista de Produtos:")
            for p in cls.lista_produtos:
                try:
                    print(f"Nome: {p.nome}")
                    print(f"ID: {p.id_produto}")
                    print(f"Preço unitário: R${p.preco:.2f}")
                    print(f"Quantidade: {p.quantidade}")
                    print(f"Preço final com imposto: R${p.preco_com_imposto:.2f}")
                    print("-" * 30)
                except Exception as e:
                    print(f"Erro ao exibir produto: {e}")
        except Exception as e:
            print(f"Erro ao listar produtos: {e}")

if __name__ == "__main__":
    while True:
        try:
            print("1 - Cadastrar Produto")
            print("2 - Listar Produtos")
            print("3 - Cadastrar Cliente")
            print("4 - Listar Clientes")
            print("5 - Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                try:
                    Produto.cadastrar_produto()
                except ProdutoInvalidoException as e:
                    print(f"Erro ao cadastrar produto: {e}")
            elif opcao == "2":
                Produto.listar_produtos()
            elif opcao == "3":
                Cliente.cadastrar_cliente()
            elif opcao == "4":
                Cliente.listar_clientes()
            elif opcao == "5":
                break
            else:
                print("Opção inválida.\n")
        except Exception as e:
            print(f"Erro no menu principal: {e}")
