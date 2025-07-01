from models.user import Usuario as User

print(User.__init__)
print(User.__module__)

def teste_trocar_senha():
    # Criando um usuário de exemplo
    user = User(id=1, name="Rayca", email="rayca@example.com", senha="1234")

    print("Senha original:", user._Usuario__senha)  # acessando senha privada para verificar

    # Teste 1: tentar trocar com senha atual correta
    resultado = user.trocar_senha("1234", "abcd")
    print("Troca com senha correta:", resultado)  # espera True
    print("Nova senha:", user._Usuario__senha)

    # Teste 2: tentar trocar com senha atual incorreta
    resultado = user.trocar_senha("wrongpass", "efgh")
    print("Troca com senha incorreta:", resultado)  # espera False
    print("Senha após tentativa incorreta:", user._Usuario__senha)

if __name__ == "__main__":
    teste_trocar_senha()
