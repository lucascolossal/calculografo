#_____________________________________________________
#==================| PROPOSTA |=======================

class Proposta:
    def __init__(self, horas_captura, horas_edicao,
                 nivel, distancia, urgencia, trabalho_chato):

#--------------------| ATRIBUTOS |--------------------

        self.horas_captura  = horas_captura
        self.horas_edicao   = horas_edicao
        self.nivel          = nivel
        self.distancia      = distancia
        self.urgencia       = urgencia
        self.trabalho_chato = trabalho_chato