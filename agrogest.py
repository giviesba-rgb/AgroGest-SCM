# AgroGest - Gerenciamento de Operacoes Agricolas

def criar_operacao(cultura, atividade, data_prevista,
                   status="Planejada"):
    """Cria um registro de operacao agricola."""

    if not cultura.strip() or not atividade.strip():
        raise ValueError("Cultura e atividade sao obrigatorias.")

    return {
        "cultura": cultura,
        "atividade": atividade,
        "data_prevista": data_prevista,
        "status": status
    }


def listar_operacoes(operacoes):
    """Exibe as operacoes agricolas cadastradas."""

    print("\n=== AGROGEST ===")
    print("Acompanhamento das operacoes agricolas\n")

    for numero, operacao in enumerate(operacoes, start=1):
        print(f"Operacao {numero}")
        print(f"Cultura: {operacao['cultura']}")
        print(f"Atividade: {operacao['atividade']}")
        print(f"Data prevista: {operacao['data_prevista']}")
        print(f"Status: {operacao['status']}")
        print("-" * 35)


def main():
    operacoes = [
        criar_operacao("Milho", "Plantio", "10/11/2026"),
        criar_operacao(
            "Soja", "Adubacao", "15/11/2026", "Em execucao"
        )
    ]

    listar_operacoes(operacoes)


if __name__ == "__main__":
    main()
