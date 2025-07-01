from bottle import request
from models.user import UsuarioModel, Usuario as User

class UserService:
    def __init__(self):
        self.user_model = UsuarioModel()

    def get_all(self):
        users = self.user_model.get_all()
        return users

    def save(self):
        last_id = max([u.id for u in self.user_model.get_all()], default=0)
        new_id = last_id + 1
        name = request.forms.get('name')
        email = request.forms.get('email')
        senha = request.forms.get('senha')
        tipo = request.forms.get('tipo', 'normal')  # se não for passado assume o tipo normal

        user = User(id=new_id, name=name, email=email, senha=senha, tipo=tipo)
        
        if user.validar():  # vai validar os dados antes de salvar 
            self.user_model.add_user(user)
        else:
            raise ValueError("Dados inválidos")

    def get_by_id(self, user_id):
        return self.user_model.get_by_id(user_id)

    def edit_user(self, user):
        name = request.forms.get('name')
        email = request.forms.get('email')
        senha = request.forms.get('senha')
        tipo = request.forms.get('tipo', 'normal')

        user.name = name
        user.email = email
        user._User__senha = senha  # Como senha está encapsulada, acessa assim para alterar
        user.tipo = tipo

        if user.validar():
            self.user_model.update_user(user)
        else:
            raise ValueError("Dados do usuário inválidos")

    def delete_user(self, user_id):
        self.user_model.delete_user(user_id)
    def autenticar_usuario(self, email, senha):
        """Verifica se há um usuário com esse email e senha"""
        for usuario in self.user_model.get_all():
            if usuario.autenticar(email, senha):
                return usuario
        return None  # nenhum usuário bateu

    def trocar_senha(self, user_id, senha_atual, nova_senha):
        """Tenta trocar a senha de um usuário com base no id"""
        usuario = self.user_model.get_by_id(user_id)
        if not usuario:
            return False  # usuário não existe
        if usuario.trocar_senha(senha_atual, nova_senha):
            self.user_model.update_user(usuario)
            return True
        return False  # senha atual errada
