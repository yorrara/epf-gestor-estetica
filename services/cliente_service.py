from bottle import request
from models.cliente import ClienteModel, Cliente

class ClienteService:
    def __init__(self):
        self.cliente_model = ClienteModel()

    def salvar_cliente(self):
        last_id = max([c.id for c in self.cliente_model.get_all()], default=0)
        new_id = last_id + 1

        nome = request.forms.get('nome')
        telefone = request.forms.get('telefone')
        email = request.forms.get('email')
        preferencias = []  # Pode ser extendido depois

        cliente = Cliente(
            id=new_id,
            nome=nome,
            telefone=telefone,
            email=email,
            preferencias=preferencias
        )

        self.cliente_model.add_cliente(cliente)

    def listar_clientes(self):
        return self.cliente_model.get_all()

    def buscar_por_id(self, cliente_id):
        return self.cliente_model.get_by_id(cliente_id)

    def excluir_cliente(self, cliente_id):
        self.cliente_model.delete_cliente(cliente_id)
