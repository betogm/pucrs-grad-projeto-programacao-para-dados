# PUCRS - Curso Superior de Tecnologia em Gestão da Tecnologia da Informação: Soluções Baseadas em Nuvem
# Trimestre: 03
# Disciplina: Programação para Dados
# Professores:  Marco Aurélio Souza Mangan
# Projeto - Fase 1
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
        print("=========== Jogos Eletrônicos - Fase 1 ===========")
        print("Escolha a opção digitando o número ou letra para escolher o tipo de Informação desejada:")
        print("[1] Pergunta 1: Qual o percentual de jogos gratuitos e pagos na plataforma?")
        print("[2] Pergunta 2: Qual o ano com o maior número de novos jogos?")
        print("[3] Pergunta 3: Quais os percentuais de compatibilidade com cada Sistema Operacional?")
        print("[m] para mostrar o menu novamente")
        print("[s] para sair do programa")
        mostrarMenu = False

    print()
    opt = input("Qual a sua opção? ('m' para mostrar o menu) ")

    # Trata entrada do usuário, se o valor digitado
    # não for nenhuma das opções, reinicia o loop

    # Mostra o percentual de jogos gratuítos
    if opt == '1' :
        Steam.showPercJogosGratuitos()
        continue
    # Mostra o ano com mais lançamentos de jogos
    elif opt == '2' :
        Steam.showAnoMaisLancamentos()
        continue
    # Mostra a compatibilidade com os Sistemas Operacionais
    elif opt == '3' :
        Steam.showPercJogosSo()
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
