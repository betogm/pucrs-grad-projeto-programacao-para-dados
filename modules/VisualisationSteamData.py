
# Classe auxiliar que invoca a classe ParseSteamData
# e apresenta os dados parseados por esta
# em um formato para humanos
class VisualisationSteamData:

    def __init__(self, csvPath="data/excerto.csv"):
        print("Aguarde, carregando os dados...")

        self.Steam = ParseSteamData(csvPath)

        print("Dados Carregados!")
        print()

    def showPercJogosGratuitos(self):
        """
            Mostra a porcentagem de jogos gratuítos
        
            >>> v.showPercJogosGratuitos()
            <BLANKLINE>
            Percentagem de jogos gratuítos disponíveis na plataforma Steam: 10.0%
        """
        print()
        print("Percentagem de jogos gratuítos disponíveis na plataforma Steam:", \
            f"{round(self.Steam.getPercJogosGratuitos(), 2)}%")

    def showAnoMaisLancamentos(self):
        """
            Mostra o ano com o maior número de lançamentos de jogos

            >>> v.showAnoMaisLancamentos()
            <BLANKLINE>
            O ano com o maior número de lançamentos de jogos na plataforma Steam foi 2022 com 8 jogos lançados.
        """
        ano, lancamentos = self.Steam.getAnoMaisLancamentos()
        print()
        print("O ano com o maior número de lançamentos de jogos na plataforma Steam foi", \
            f"{ano} com {str(lancamentos)} jogos lançados.")

    def showPercJogosSo(self):
        """
            Mostra a porcentagem de jogos compatíveis com o SOs: Windows, Mac e Linux

            >>> v.showPercJogosSo()
            <BLANKLINE>
            Compatibilidade dos jogos por sistema operacional:
            Windows: 100.0%
            Mac: 20.0%
            Linux: 15.0%
        """
        print()
        print("Compatibilidade dos jogos por sistema operacional:")
        print(f"Windows: {round(self.Steam.getPercJogosWindows(), 2)}%")
        print(f"Mac: {round(self.Steam.getPercJogosMac(), 2)}%")
        print(f"Linux: {round(self.Steam.getPercJogosLinux(), 2)}%")

# Testes
# Executar na raiz do projeto:
# > python modules/VisualisationSteamData.py -v
if __name__ == "__main__":
    import doctest
    from ParseSteamData import ParseSteamData
    doctest.testmod(extraglobs={'v': VisualisationSteamData("data/excerto.csv")})
else:
    from modules.ParseSteamData import ParseSteamData
