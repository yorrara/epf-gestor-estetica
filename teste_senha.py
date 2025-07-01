class User:
    def __init__(self, id, name, email, senha, tipo='normal'):
        self.id = id
        self.name = name
        self.email = email
        self.__senha = senha
        self.tipo = tipo

    def trocar_senha(self, senha_atual, nova_senha):
        if senha_atual == self.__senha:
            self.__senha = nova_senha
            return True
        else:
            return False

def teste_trocar_senha():
    user = User(id=1, name="Rayca", email="rayca@example.com", senha="1234")

    print("Senha original:", user._User__senha)

    resultado = user.trocar_senha("1234", "abcd")
    print("Troca com senha correta:", resultado)
    print("Nova senha:", user._User__senha)

    resultado = user.trocar_senha("wrongpass", "efgh")
    print("Troca com senha incorreta:", resultado)
    print("Senha após tentativa incorreta:", user._User__senha)

if __name__ == "__main__":
    teste_trocar_senha()
