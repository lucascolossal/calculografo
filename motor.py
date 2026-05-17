VALOR_HORA_BASE = 35.0
TETO_HORA = 80.0

class Motor:
    def calcular(self, proposta):
        valor_hora = VALOR_HORA_BASE
        fator_nivel = 1 + (((proposta.nivel)-5) *0.1)
        valor_hora *= fator_nivel

#____________________________________________________
#===============| BLOCO DE CONDIÇÕES |===============



#-------------------FATOR DISTÂNCIA---------------------------
        
        
        if proposta.distancia == "M":
            valor_hora *= 1.15
        elif proposta.distancia == "G":
            valor_hora *= 1.3


#--------------------FATOR URGÊNCIA----------------------------    
      
        if proposta.urgencia == "S":
            valor_hora *= 1.25

#--------------------FATOR DESGASTE---------------------------

        if proposta.trabalho_chato == "S":
            valor_hora *= 1.25       

#-------------------------------------------------------------
        valor_hora_captura = valor_hora * (1 + 2/3)

        total = (proposta.horas_captura * valor_hora_captura) + \
                (proposta.horas_edicao * valor_hora) 
#--------------------CÁLCULO FINAL----------------------------

        horas_totais = proposta.horas_captura + proposta.horas_edicao
        teto = horas_totais * TETO_HORA
        total_final = min(total, teto)

#--------------------RETORNO----------------------------------

        return total, total_final