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
        print("[5] Crescimento da disponibilidade de jogos para Linux entre 2018 e 2022")
        print("[6] Apresenta gráfico da disponibilidade de jogos por sistema operacional")
        print("[7] Apresenta número total de jogos single-player do gênero Indie e estratégia lançados por ano entre 2010 e 2020")
        print("[8] Apresenta o crescimento dos jogos tagueados como Aventura entre 2001 e 2022")
        print("[9] Quantos jogos foram lançados com preços iguais ou menores de $5.00?")
        print("[10] Mostra os 10 jogos que receberam mais recomendações")
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
    # Mostra crescimento de jogos para linux 2018 -> 2022
    elif opt == '5' :
        Steam.showJogosLinux()
        continue
    # Mostra gráfico da disponibilidade de jogos por sistema operacional
    elif opt == '6' :
        Steam.showPercJogosSo()
        continue
    # Número total de jogos single-player do gênero Indie e estratégia lançados por ano entre 2010 e 2020
    elif opt == '7' :
        Steam.showSinglePlayerIndieStretegy()
        continue
    # Lançamentos de jogos de aventura entre 2001 e 2022
    elif opt == '8' :
        Steam.showTagAdventureGamesEvolution()
        continue
    # Jogos com valores igual ou abaixo de $5.00
    elif opt == '9' :
        Steam.showGamesPriceLow()
        continue
    # Mostra os 10 jogos que receberam mais recomendações
    elif opt == '10' :
        Steam.show10HighRecommendations()
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
