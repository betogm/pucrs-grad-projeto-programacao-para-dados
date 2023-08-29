from modules.ParseSteamData import ParseSteamData

# Classe auxiliar que invoca a classe ParseSteamData
# e apresenta os dados parseados por esta
# em um formato para humanos
class VisualisationSteamData:

    def __init__(self, csvPath="../data/excerto.csv"):
        print("Aguarde, carregando os dados...")

        self.Steam = ParseSteamData(csvPath)

        print("Dados Carregados!")
        print()

    def showPercJogosGratuitos(self):
        """Mostra a porcentagem de jogos gratuítos"""
        print()
        print("Percentagem de jogos gratuítos disponíveis na plataforma Steam:", \
            f"{round(self.Steam.getPercJogosGratuitos(), 2)}%")

    def showAnoMaisLancamentos(self):
        """Mostra o ano com o maior número de lançamentos de jogos"""
        anoMaisLanc = self.Steam.getAnoMaisLancamentos()
        print()
        print("O ano com o maior número de lançamentos de jogos na plataforma Steam foi", \
            f"{anoMaisLanc[0]} com {str(anoMaisLanc[1])} jogos lançados.")

    def showPercJogosSo(self):
        """Mostra a porcentagem de jogos compatíveis com o SOs: Windows, Mac e Linux"""
        print()
        print("Compatibilidade dos jogos por sistema operacional:")
        print(f"Windows: {round(self.Steam.getPercJogosWindows(), 2)}%")
        print(f"Mac: {round(self.Steam.getPercJogosMac(), 2)}%")
        print(f"Linux: {round(self.Steam.getPercJogosLinux(), 2)}%")
