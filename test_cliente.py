from models.cliente import Cliente, ClienteModel

def teste_cliente():
    c = Cliente(id=1, nome="Maria", telefone="99999-9999", email="maria@email.com")
    print("Cliente criado:", c.nome)

    c.adicionar_preferencia("massagem relaxante")
    print("Preferências:", c.preferencias)

    historico = c.ver_historico()
    print("Histórico de atendimentos:", historico)

    model = ClienteModel()
    model.add_cliente(c)
    print("Cliente salvo no model.")

if __name__ == "__main__":
    teste_cliente()
