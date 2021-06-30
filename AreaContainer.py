from Stack import Stack


class AreaContainer:

    def __init__(self, numero_pilha, tamanho_altura):
        self.area_estoque_maquina = []
        self.numero_pilha = numero_pilha

        for n in range(numero_pilha):
            self.area_estoque_maquina.append(Stack(tamanho_altura))

    def add_maquininha(self, novo_estoque_maquina):
        pos = 0
        while True:
            posicao_pilha = self.area_estoque_maquina[pos].push(
                novo_estoque_maquina)
            if posicao_pilha is None:
                pos += 1
                if len(self.area_estoque_maquina) == pos:
                    print(
                        f"\nArmazenamento indisponível. Não há espaço para armazenamento do modelo escolhido de máquinas de cartão.\n")
                    exit()

            else:
                print(
                    f"-> Máquina de Cartão {novo_estoque_maquina} armazenada na posição {pos} na altura {posicao_pilha}.\n")
                break

    def del_maquininha(self):
        pos = -1
        while True:
            estoque_maquina = self.area_estoque_maquina[pos].pop()
            if estoque_maquina is None:
                pos -= 1
                if pos == ((len(self.area_estoque_maquina)+1) * -1):
                    print(
                        f"Todas as pilhas estão vazias. Não há máquinas de cartão em estoque!")
                    break
            else:
                print(f"\n-> Envio de Máquina de Cartão...:")
                print(
                    f"-> Número de Série..................: {estoque_maquina['Serial Number']} retirada!")
                print(
                    f"-> Horário de Entrada...............: {estoque_maquina['Data / Hora de Entrada']}")
                print(
                    f"-> Horário de Saída.................: {estoque_maquina['Data / Horário de Saída']}")
                print(
                    f"-> Tempo aguardado para envio.......: {estoque_maquina['Data / Horário de Saída']-estoque_maquina['Data / Hora de Entrada']}")
                break

