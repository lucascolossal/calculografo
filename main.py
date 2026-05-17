from motor import Motor
from proposta import Proposta

#_____________________________________________________
#=================| BLOCO DE COLETA |=================

def coletar_dados():
    try:
        horas_captura = float(input("Horas de campo (captura): "))
        horas_edicao  = float(input("Horas de ateliê (edição): "))
        nivel         = int(input("Nível de inserção no mercado local (0-10): "))
        distancia     = input("Distância até o local (P/M/G): ").upper()
        urgencia      = input("A captura / entrega é urgente? (S/N): ").upper()
        trabalho_chato = input("Trabalho chato? (S/N): ").upper()

#--------------| INSTANCIAMENTO DA PROPOSTA |---------

        proposta = Proposta(horas_captura, horas_edicao, nivel,
                            distancia, urgencia, trabalho_chato)
        return proposta

#--------------------| EXCEÇÃO |-----------------------

    except ValueError:
        print("Entrada inválida.")
        return

#_____________________________________________________
#================| INICIALIZADOR |====================

def inicializar():
    proposta = coletar_dados()
    motor = Motor()
    total, total_final = motor.calcular(proposta)

#--------------------| RESULTADO |--------------------

    if total > total_final:
        print(f"Valor calculado excede o teto.")
        print(f"Valor final sugerido : R$ {total_final:.2f}")
        print(f"Valor sem teto       : R$ {total:.2f}")
    else:
        print(f"Valor final sugerido : R$ {total:.2f}")

#_____________________________________________________
#==================| ENTRADA |========================

inicio = int(input("Inicializar cálculo? 1-Sim, 2-Não: "))

if inicio == 1:
    inicializar()
elif inicio == 2:
    exit()
else:
    print("Entrada inválida.")