# Calculografo 
# É a calculadora oficial do fotografo freelancer
# Desenvolvida por: Lucas Colossal - 2026. Técnico em informática desde 2013  
# Fotógrafo freelancer desde 2019
# Seja bem-vindo ao meu processo de aprendizado em Python,
# onde estou desenvolvendo esta calculadora para facilitar meus 
# cálculos diários relacionados à fotografia. Pode ajudar fotógrafos e contratantes

VALOR_HORA_BASE = 35.0
TETO_HORA = 80.0


def linhadobro():
    print("="*50)
    print("="*50)
def cabecalho():
    linhadobro()
    print("Bem-vindo ao Calculógrafo - a calculadora oficial do fotógrafo freelancer!")
    print(f"\nPreço da hora base é fixa em: R$ {VALOR_HORA_BASE:.2f} mas pode ser ajustada editando (com cuidado) o código-fonte")
    print("Para começar, por favor, me conte um pouco sobre a proposta:")
    linhadobro()

def calcular_orcamento():
      
    proposta = {}
    try:
        proposta["horas_captura"] = float(input("Horas de campo (captura): "))
        proposta["horas_edicao"] = float(input("Horas de ateliê (edição): "))
        proposta["nivel"] = int(input("Nível de inserção (valorização) no mercado local (0-10): "))
        proposta["distancia"] = input("Distância até o local (P/M/G): ").upper()
        proposta["urgencia"] = input("A captura / entrega é urgente? (S/N): ").upper()
        proposta["trabalho_chato"] = input("Trabalho chato? (S/N): ").upper()
    except ValueError:
        print("Entrada inválida.")
        return

    valor_hora = VALOR_HORA_BASE
    fator_nivel = 1 + ((proposta["nivel"] - 5) * 0.1)
    valor_hora *= fator_nivel

    if proposta["distancia"] == "M":
        valor_hora *= 1.15
    elif proposta["distancia"] == "G":
        valor_hora *= 1.30

    if proposta["urgencia"] == "S":
        valor_hora *= 1.25

    if proposta["trabalho_chato"] == "S":
        valor_hora *= 1.25

    valor_hora_captura = valor_hora * (1 + 2/3)

    total = (proposta["horas_captura"] * valor_hora_captura) + \
            (proposta["horas_edicao"] * valor_hora)

    horas_totais = proposta["horas_captura"] + proposta["horas_edicao"]
    teto = horas_totais * TETO_HORA
    total_final = min(total, teto)
    linhadobro()
    print(f"Valor sugerido pelo Calculógrafo: R$ {total_final:.2f}")
    if total_final < total:
        print(f"Valor elevado, o calculógrafo usou o teto {TETO_HORA} (para evitar supervalorização e perdas de contrato). O valor seria R$ {total:.2f}")
    linhadobro()
cabecalho()
calcular_orcamento()
input("\nPressione Enter para sair.")

