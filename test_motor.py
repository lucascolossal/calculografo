from proposta import Proposta
from motor import Motor

def test_calculo_basico():
    p = Proposta(2, 1, 5, "M", "N", "S")
    motor = Motor()
    total, total_final = motor.calcular(p)
    assert round(total_final, 2) == 218.02
def test_calculo_basico2():
    p = Proposta(3, 2, 5, "M", "S", "S")
    motor = Motor()
    total, total_final = motor.calcular(p)
    assert round(total_final, 2) == 400.0
print(test_calculo_basico2())