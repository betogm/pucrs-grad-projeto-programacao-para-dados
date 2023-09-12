# PUCRS - Curso Superior de Tecnologia em Gestão da Tecnologia da Informação: Soluções Baseadas em Nuvem
# Trimestre: 03
# Disciplina: Programação para Dados
# Professores:  Marco Aurélio Souza Mangan
# Projeto - Fase 2
# Título: Jogos Eletrônicos - Fun Corp
# Aluno: Huberto Gastal Mayer

from modules.VisualisationSteamData import VisualisationSteamData

# Instancia um objeto da classe VisualisationSteamData
Steam = VisualisationSteamData('data/steam_games.csv')

# Início do loop para interação com o usuário
mostrarMenu = True
while True :

    if mostrarMenu :
        # Menu de opções:
        print()
        print("=========== Jogos Eletrônicos - Fase 2 ===========")
        print("Escolha a opção digitando o número ou letra para escolher o tipo de Informação desejada:")
        print("[1] Mostra o percentual de jogos gratuitos e pagos na plataforma?")
        print("[2] Mostra os dez jogos mais bem avaliados, de acordo com o Metacritic")
        print("[3] Jogos RPG: DLCs, avaliações e materiais de demonstração")
        print("[4] Empresas que mais publicaram jogos")
        print("[m] para mostrar o menu novamente")
        print("[s] para sair do programa")
        mostrarMenu = False

    print()
    opt = input("Qual a sua opção? ('m' para mostrar o menu) ")

    # Trata entrada do usuário, se o valor digitado
    # não for nenhuma das opções, reinicia o loop

    # Mostra o percentual de jogos gratuitos e pagos
    if opt == '1' :
        Steam.showPercJogosGratuitosPagos()
        continue
    # Mostra os dez jogos mais bem avaliados, de acordo com o Metacritic
    elif opt == '2' :
        Steam.showMetacriticBetterAvaliated()
        continue
    # Mostra dados de Jogos RPG
    elif opt == '3' :
        Steam.showRpgData()
        continue
    # Mostra Empresas que mais publicaram jogos
    elif opt == '4' :
        Steam.showEmpresasMaisPublicam()
        continue
    # Mostra o menu de opções novamente
    elif opt == 'm' :
        mostrarMenu = True
        continue
    # Sai do loop eterno (e do programa)
    elif opt == 's' :
        break
    else :
        print("Opção inválida, tente novamente.")
        continue

print("Obrigado por utilizar o programa, saindo...")