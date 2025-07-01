import os
import json

# Define o diretório para salvar os arquivos JSON (mesmo padrão que você usou para User)
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class Cliente:
    def __init__(self, id, nome, telefone, email, preferencias=None, historico_atendimentos=None):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.preferencias = preferencias if preferencias is not None else []
        self.historico_atendimentos = historico_atendimentos if historico_atendimentos is not None else []

    def adicionar_preferencia(self, preferencia):
        if preferencia not in self.preferencias:
            self.preferencias.append(preferencia)

    def ver_historico(self):
        return self.historico_atendimentos

    def to_dict(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'telefone': self.telefone,
            'email': self.email,
            'preferencias': self.preferencias,
            'historico_atendimentos': self.historico_atendimentos
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            nome=data['nome'],
            telefone=data['telefone'],
            email=data['email'],
            preferencias=data.get('preferencias', []),
            historico_atendimentos=data.get('historico_atendimentos', [])
        )


class ClienteModel:
    FILE_PATH = os.path.join(DATA_DIR, 'clientes.json')

    def __init__(self):
        self.clientes = self._load()

    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Cliente.from_dict(item) for item in data]

    def _save(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([cliente.to_dict() for cliente in self.clientes], f, indent=4, ensure_ascii=False)

    def get_all(self):
        return self.clientes

    def get_by_id(self, cliente_id):
        return next((c for c in self.clientes if c.id == cliente_id), None)

    def add_cliente(self, cliente):
        self.clientes.append(cliente)
        self._save()

    def update_cliente(self, cliente_atualizado):
        for i, c in enumerate(self.clientes):
            if c.id == cliente_atualizado.id:
                self.clientes[i] = cliente_atualizado
                self._save()
                break

    def delete_cliente(self, cliente_id):
        self.clientes = [c for c in self.clientes if c.id != cliente_id]
        self._save()
