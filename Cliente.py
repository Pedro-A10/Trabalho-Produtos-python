from Cliente_Exception import ClienteInvalidoException

class Cliente:
    def __init__(self, nome, email):
         if not nome or not email:
            raise ClienteInvalidoException("Nome e email são obrigatórios.")
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"Cliente: {self.nome}, Email: {self.email}"
