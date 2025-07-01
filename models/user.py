import json
import os
from dataclasses import dataclass, asdict
from typing import List
print("Importando a classe User do models.user")

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

class Usuario:
    def __init__(self, id, name, email, senha, tipo='normal'):
        self.id = id
        self.name = name
        self.email = email
        self.__senha = senha
        self.tipo = tipo #normal ou do tipo adm
# o tipo ='normal' é pra que exista dois tipos de usuarios, se esse parametro normal  não for preenchido entao o codigo assumirá que o tipo de usuario é normal, nao adm


    def __repr__(self):
        return (f"User(id={self.id}, name='{self.name}', email='{self.email}', "
                f"tipo='{self.tipo}')")


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'senha': self.__senha,
            'tipo':self.tipo
        }

    def autenticar(self,email,senha):
        return self.email== email and self.__senha == senha
    #verifica se o email e a senha batem com os salvos no projeto
    
    def trocar_senha(self, senha_atual, nova_senha):
        if senha_atual == self.__senha: #verifica se a senha atual é  mesma que foi salva antes
            self.__senha = nova_senha
            return True
        else:
            return False
    #metodo q vai trocar  a senha do usuario caso pedido
    def validar(self):
                return(
                    isinstance(self.name, str) and len (self.name) > 0 and '@' in self.email and
                    isinstance(self.__senha,str) and len(self.__senha) >=4
                )
    # valida os dados do usuario, garante que o nome seja uma string que o email deve conter @ e que a senha deve ter pelo menos 4 caracteres

    
    @classmethod
    def from_dict(cls, data):
        return cls(
            id=data['id'],
            name=data['name'],
            email=data['email'],
            senha=data['senha'],
            tipo=data.get('tipo', 'normal')
        )

     
class UsuarioModel:
    FILE_PATH = os.path.join(DATA_DIR, 'users.json')

    def __init__(self):
        self.users = self._load()


    def _load(self):
        if not os.path.exists(self.FILE_PATH):
            return []
        with open(self.FILE_PATH, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return [Usuario.from_dict(item)for item in data]


    def _save(self):
        with open(self.FILE_PATH, 'w', encoding='utf-8') as f:
            json.dump([u.to_dict() for u in self.users], f, indent=4, ensure_ascii=False)


    def get_all(self):
        return self.users


    def get_by_id(self, user_id: int):
        return next((u for u in self.users if u.id == user_id), None)


    def add_usuario(self, user: Usuario):
        self.users.append(user)
        self._save()


    def update_user(self, updated_user: Usuario):
        for i, user in enumerate(self.users):
            if user.id == updated_user.id:
                self.users[i] = updated_user
                self._save()
                break


    def delete_usuario(self, user_id: int):
        self.users = [u for u in self.users if u.id != user_id]
        self._save()
