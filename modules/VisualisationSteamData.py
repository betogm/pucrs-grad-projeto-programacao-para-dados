from modules.ParseSteamData import ParseSteamData

class VisualisationSteamData:

    def __init__(self, csvPath="../data/excerto.csv"):
        print("Aguarde, carregando os dados...")

        self.steam = ParseSteamData(csvPath)

        print("Dados Carregados!")
        print()

    def showPercJogosGratuitos(self):
        """Mostra a porcentagem de jogos gratuítos"""
        print()
        print("Percentagem de jogos gratuítos disponíveis na plataforma Steam:", \
            f"{round(self.steam.getPercJogosGratuitos(), 2)}%")

    def showAnoMaisLancamentos(self):
        """Mostra o ano com o maior número de lançamentos de jogos"""
        anoMaisLanc = self.steam.getAnoMaisLancamentos()
        print()
        print("O ano com o maior número de lançamentos de jogos na plataforma Steam foi", \
            f"{anoMaisLanc[0]} com {str(anoMaisLanc[1])} jogos lançados.")

    def showPercJogosSo(self):
        """Retorna a porcentagem de jogos compatíveis com o SOs: Windows, Mac e Linux"""
        print()
        print("Compatibilidade dos jogos por sistema operacional:")
        print(f"Windows: {round(self.steam.getPercJogosWindows(), 2)}%")
        print(f"Mac: {round(self.steam.getPercJogosMac(), 2)}%")
        print(f"Linux: {round(self.steam.getPercJogosLinux(), 2)}%")
