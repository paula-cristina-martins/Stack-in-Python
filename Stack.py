from datetime import datetime


class Stack:

    def __init__(self, altura=5):
        self.estoque_maquina = []
        self.altura = altura
        self.hora_inicio = datetime.now()
        self.hora_final = datetime.now()

    def push(self, container):
        if len(self.estoque_maquina) < self.altura:

            inicio = datetime.now()
            self.hora_inicio = inicio

            maquina_cartao = {
                'Serial Number': container,
                'Data / Hora de Entrada': inicio
            }

            self.estoque_maquina.append(maquina_cartao)
            return len(self.estoque_maquina)

        else:
            return None

    def pop(self):

        if self.estoque_maquina == []:
            return None

        else:
            final = datetime.now()
            self.hora_final = final
            maquina_cartao = self.estoque_maquina.pop()
            maquina_cartao['Data / Horário de Saída'] = final
            return maquina_cartao

