
from datetime import datetime
import os
import json
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class Agendamento:
    def __init__(self, id, id_cliente, id_profissional, id_servico, data, hora):
        self.id = id
        self.id_cliente = id_cliente #se relaciona com a classe cliente
        self.id_profissional = id_profissional #id do profissional que vai atender 
        self.id_servico = id_servico #tipo de serviço q será feito
        self.data = data     # Exemplo: '2025-07-02'
        self.hora = hora     # Exemplo: '14:30'
#atributos do construtor

    def validar_horario(self):
        """Verifica se a data e a hora estão em formato válido."""
        try:
            datetime.strptime(self.data, '%Y-%m-%d') #tenta converter a data e a hora e se o formato tiver errado, n funciiona
            datetime.strptime(self.hora, '%H:%M')
            return True
        except ValueError:
            return False
        
    def cancelar(self):
        """Marca o agendamento como cancelado."""
        self.cancelado = True

    def to_dict(self):
        return {
            'id': self.id,
            'id_cliente': self.id_cliente,
            'id_profissional': self.id_profissional,
            'id_servico': self.id_servico,
            'data': self.data,
            'hora': self.hora,
            'cancelado': getattr(self, 'cancelado', False)  # se não tiver o atributo ainda, assume False
        }

    @classmethod
    def from_dict(cls, data):
        agendamento = cls(
            id=data['id'],
            id_cliente=data['id_cliente'],
            id_profissional=data['id_profissional'],
            id_servico=data['id_servico'],
            data=data['data'],
            hora=data['hora']
        )
        if data.get('cancelado'):
            agendamento.cancelado = True
        return agendamento

# vai controlar o armazenamento dos dados dos agendamentos 
class AgendamentoModel:
    FILE_PATH = os.path.join(DATA_DIR, 'agendamentos.json')#define o caminho do arquivo

    def __init__(self):
        self.agendamentos = self._load() #carrega todos os agendamentos salvos no arquivo.



    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Agendamento.from_dict(item) for item in data]

    def _save(self): #: salva os agendamentos 
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([a.to_dict() for a in self.agendamentos], f, indent=4, ensure_ascii=False)

    def get_all(self):
        return self.agendamentos

    def get_by_id(self, agendamento_id): #retorna um agendamento específico pelo ID 
        return next((a for a in self.agendamentos if a.id == agendamento_id), None)

    def add_agendamento(self, agendamento):
        self.agendamentos.append(agendamento)
        self._save()

    def update_agendamento(self, agendamento_atualizado):
        for i, ag in enumerate(self.agendamentos):
            if ag.id == agendamento_atualizado.id:
                self.agendamentos[i] = agendamento_atualizado
                self._save()
                break

    def delete_agendamento(self, agendamento_id):
        self.agendamentos = [a for a in self.agendamentos if a.id != agendamento_id]
        self._save()
