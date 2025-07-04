from unittest.mock import patch, MagicMock
import bottle
from services.cliente_service import ClienteService

def teste_salvar_cliente():
    service = ClienteService()

    dados_form = {
        'nome': 'Maria',
        'telefone': '999999999',
        'email': 'maria@email.com'
    }

    # Criamos um mock para o objeto bottle.request
    mock_request = MagicMock()
    # Configuramos o atributo 'forms.get' para retornar os valores do dicionário dados_form
    mock_request.forms.get.side_effect = lambda key, default=None: dados_form.get(key, default)

    # Substituímos o bottle.request inteiro pelo nosso mock
    with patch('bottle.request', mock_request):
        service.salvar_cliente()

    clientes = service.listar_clientes()
    print("Clientes cadastrados:")
    for c in clientes:
        print(c.to_dict())

def teste_listar_clientes():
    service = ClienteService()
    clientes = service.listar_clientes()
    print(f"Clientes cadastrados: {len(clientes)}")
    for c in clientes:
        print(c.to_dict())

if __name__ == "__main__":
    teste_salvar_cliente()
    teste_listar_clientes()
