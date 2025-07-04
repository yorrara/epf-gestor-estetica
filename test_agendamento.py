from models.agendamento import Agendamento

def teste_agendamento():
    print("🗓️ Testando criação e métodos do agendamento:")

    # Criando agendamento de exemplo
    ag = Agendamento(
        id=1,
        id_cliente=10,
        id_profissional=5,
        id_servico=3,
        data="2025-07-05",
        hora="14:00"
    )

    print(f"📄 Dados do agendamento:\n{ag.to_dict()}")

    # Testando validação de horário
    valido = ag.validar_horario()
    print("✅ Horário válido?" if valido else "❌ Horário inválido!")

    # Testando cancelamento
    print("🛑 Cancelando agendamento...")
    ag.cancelar()
    print("⏳ Após cancelamento:")
    print(f"Data: {ag.data}, Hora: {ag.hora}")


if __name__ == "__main__":
    teste_agendamento()
