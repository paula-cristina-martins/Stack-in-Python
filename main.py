from AreaContainer import AreaContainer

# ------------------------------------------------------------------------------------------------------------ #

mccc = AreaContainer(1, 3)
mccw = AreaContainer(5, 8)
mccr = AreaContainer(5, 7)
maqm = AreaContainer(5, 6)

# ------------------------------------------------------------------------------------------------------------ #

print("\nBoas Vindas ao nosso Sistema de Estoque!\n" +
      "Opções a serem armazenadas no sistema:\n" +
      "1 - MCCC - Máquina de cartão / Conexão CHIP.\n" +
      "2 - MCCW - Máquina de cartão / Conexão Wireless.\n" +
      "3 - MCCR - Máquina de cartão / Conexão Cabo de Rede.\n" +
      "4 - MAQM - Máquina de cartão Mobile.\n"
      )

opcao_modelo_add = int(input("Informe modelo deseja guardar? "))

# mccc - limite 45
if (opcao_modelo_add == 1):
    quantidade_maquininha = int(
        input("\nInsira a quantidade que deseja cadastrar / armazenar? "))
    if quantidade_maquininha > 45:
        print("\nQuantidade superior ao limite disponível!")
        exit()

    for i in range(quantidade_maquininha):
        serial_number = input(
            "Insira o cód. de série do equipamento: ")
        mccc.add_maquininha(serial_number)

# mccw - limite 40
elif (opcao_modelo_add == 2):
    quantidade_maquininha = int(
        input("\nInsira a quantidade que deseja cadastrar / armazenar? "))
    if quantidade_maquininha > 40:
        print("\nQuantidade superior ao limite disponível!")
        exit()

    for i in range(quantidade_maquininha):
        serial_number = input(
            "Insira o cód. de série do equipamento: ")
        mccw.add_maquininha(serial_number)

# mccr - limite 35
elif (opcao_modelo_add == 3):
    quantidade_maquininha = int(
        input("\nInsira a quantidade que deseja cadastrar / armazenar? "))
    if quantidade_maquininha > 35:
        print("\nQuantidade superior ao limite disponível!")
        exit()

    for i in range(quantidade_maquininha):
        serial_number = input(
            "Insira o cód. de série do equipamento: ")
        mccr.add_maquininha(serial_number)

# maqm - limite 30
elif (opcao_modelo_add == 4):
    quantidade_maquininha = int(
        input("\nInsira a quantidade que deseja cadastrar / armazenar? "))
    if quantidade_maquininha > 30:
        print("\nQuantidade superior ao limite disponível!")
        exit()

    for i in range(quantidade_maquininha):
        serial_number = input(
            "Insira o cód. de série do equipamento: ")
        maqm.add_maquininha(serial_number)

else:
    print("\nOpção Inválida! Por favor, tente novamente!\n")

# ------------------------------------------------------------------------------------------------------------ #

info = int(input("Deseja enviar máquinas de cartão? "
                 "\n1 - SIM"
                 "\n2 - NAO\n\nEscolha uma opção: "
                 ))
if (info == 1):
    print("\nOpções a serem enviadas as máquinas de cartão no sistema:\n" +
          "1 - MCCC - Máquina de cartão / Conexão CHIP.\n" +
          "2 - MCCW - Máquina de cartão / Conexão Wireless.\n" +
          "3 - MCCR - Máquina de cartão / Conexão Cabo de Rede.\n" +
          "4 - MAQM - Máquina de cartão Mobile.\n"
          )

    opcao_modelo_remove = int(input("Informe modelo deseja enviar? "))

    if opcao_modelo_remove == 1:
        mccc.del_maquininha()

    elif opcao_modelo_remove == 2:
        mccw.del_maquininha()

    elif opcao_modelo_remove == 3:
        mccr.del_maquininha()

    elif opcao_modelo_remove == 4:
        maqm.del_maquininha()

    else:
        print('Opção Inválida!')

print("\nnAgradecemos por utilizar nossos serviços!\n\n")

# ------------------------------------------------------------------------------------------------------------ #

