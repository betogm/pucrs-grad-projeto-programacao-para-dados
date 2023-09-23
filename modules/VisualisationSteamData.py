from datetime import datetime

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

    def showPercJogosGratuitosPagos(self):
        """
            Mostra a porcentagem de jogos gratuítos
        
            >>> v.showPercJogosGratuitos()
            <BLANKLINE>
            Percentagem de jogos gratuítos disponíveis na plataforma Steam: 10.0%
        """
        print()
        print("Percentagem de jogos gratuítos e pagos disponíveis na plataforma Steam:")
        print(f"Gratuitos: {round(self.Steam.getPercJogosGratuitos(), 2)}%")
        print(f"Pagos: {round(100 - self.Steam.getPercJogosGratuitos(), 2)}%")

    def showMetacriticBetterAvaliated(self):
        """
            Mostra os dez jogos mais bem avaliados, de acordo com o Metacritic
        
            >>> v.showMetacriticBetterAvaliated()
            <BLANKLINE>
            Percentagem de jogos gratuítos disponíveis na plataforma Steam: 10.0%
        """
        print()
        print("Os dez jogos mais bem avaliados, de acordo com o Metacritic:")
        print()
        print("Score    Data Lançamento     Jogo")
        scores = self.Steam.getMetacriticScore()
        for jogo in scores :
            score = scores[jogo]["score"]
            dataLanc = datetime.strptime(scores[jogo]["releaseDate"], "%Y-%m-%d").strftime("%d/%m/%Y")
            game = scores[jogo]["jogo"]
            print(f"{score}         {dataLanc}      {game}")

    def showRpgData(self):
        """
            Jogos RPG: Mostra  número médio e máximo de: DLCs, avaliações positivas, avaliações negativas 
            e materiais de demonstração (número de capturas de tela e filmes, somados)
        
            >>> v.showRpgData()
            <BLANKLINE>
            Percentagem de jogos gratuítos disponíveis na plataforma Steam: 10.0%
        """
        rpgData = self.Steam.getRpgData()
        print()
        print("Jogos RPG: DLCs, avaliações e materiais de demonstração")
        print()
        print("DLCs")
        print(f"    Média por jogo: {round(rpgData['dlc']['sum'] / rpgData['numLines'], 2)}")
        print(f"    Máximo por jogo: {rpgData['dlc']['max']}")
        print()
        print("Avaliações")
        print(f"  Positivas:")
        print(f"    Média por jogo: {round(rpgData['avaliations']['positivas']['sum'] / rpgData['numLines'], 2)}")
        print(f"    Máximo por jogo: {rpgData['avaliations']['positivas']['max']}")
        print(f"  Negativas:")
        print(f"    Média por jogo: {round(rpgData['avaliations']['negativas']['sum'] / rpgData['numLines'], 2)}")
        print(f"    Máximo por jogo: {rpgData['avaliations']['negativas']['max']}")
        print()
        print("Materiais Demonstrativos")
        print(f"    Média por jogo: {round(rpgData['materiaisDemonstrativos']['sum'] / rpgData['numLines'], 2)}")
        print(f"    Máximo por jogo: {rpgData['materiaisDemonstrativos']['max']}")

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

    def showJogosLinux(self):
        """
            Mostra crescimento de jogos para linux 2018 -> 2022

            >>> v.showJogosLinux()
            <BLANKLINE>
            Compatibilidade dos jogos por sistema operacional:
            Windows: 100.0%
            Mac: 20.0%
            Linux: 15.0%
        """
        jogosLinuxPorAno = self.Steam.getJogosLinux()
        print()
        print("Crescimento da disponibilidade de jogos para Linux entre 2018 e 2022:")
        print(jogosLinuxPorAno)
        for ano in range(2018, 2023):
            print(f"Ano: {ano} - Lançamentos: {jogosLinuxPorAno[str(ano)]}")

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
    
    def showEmpresasMaisPublicam(self):
        """
            Mostra o ano com o maior número de lançamentos de jogos

            >>> v.showEmpresasMaisPublicam()
            <BLANKLINE>
            O ano com o maior número de lançamentos de jogos na plataforma Steam foi 2022 com 8 jogos lançados.
        """
        print()
        print("As cinco empresas que mais publicam jogos pagos na plataforma:")
        print()
        empresas = self.Steam.getEmpresasMaisPublicam()
        print(empresas)

# Testes
# Executar na raiz do projeto:
# > python modules/VisualisationSteamData.py -v
if __name__ == "__main__":
    import doctest
    from ParseSteamData import ParseSteamData
    doctest.testmod(extraglobs={'v': VisualisationSteamData("data/excerto.csv")})
else:
    from modules.ParseSteamData import ParseSteamData
