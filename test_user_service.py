from services.user_service import UserService

service = UserService()

# Teste de login
print("🔒 Teste de login com email e senha:")
usuario = service.autenticar_usuario("rayca@example.com", "1234")
if usuario:
    print("✅ Login bem-sucedido:", usuario.name)
else:
    print("❌ Falha no login")

# Teste de troca de senha
print("\n🔁 Teste de troca de senha:")
resultado = service.trocar_senha(1, "1234", "nova123")
print("Senha trocada?", "✅ Sim" if resultado else "❌ Não")
