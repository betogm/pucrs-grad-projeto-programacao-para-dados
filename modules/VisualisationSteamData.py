from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

# Classe auxiliar que invoca a classe ParseSteamData
# e apresenta os dados parseados por esta
# em um formato para humanos
class VisualisationSteamData:

    def __init__(self, csvPath="data/excerto.csv"):
        # Estilos padronizados dos gráficos
        self.plotFontTitle = {'family':'sans-serif','color':'blue','size':16}
        self.plotFontLabel = {'family':'sans-serif','color':'gray','size':14}

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
            Mostra a porcentagem de jogos gratuítos e Pagos
        
            >>> v.showPercJogosGratuitosPagos()
            <BLANKLINE>
            Percentagem de jogos gratuítos e pagos disponíveis na plataforma Steam:
            Gratuitos: 10.0%
            Pagos: 90.0%
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
            Os dez jogos mais bem avaliados, de acordo com o Metacritic:
            <BLANKLINE>
            Score    Data Lançamento     Jogo
            69         31/01/2017      Gladiator: Sword of Vengeance
            0         11/10/2012      Democracy 2
            0         20/08/2015      City Quest
            0         03/06/2016      Slash or Die
            0         15/07/2016      MechRunner
            0         03/11/2016      City Car Driving
            0         18/04/2017      Aesthetic Melody
            0         07/03/2018      The Final Days: Blood Dawn
            0         17/12/2019      TERMINAL VR
            0         04/11/2021      Challenge Dream Cat
            0         22/02/2022      Tank Mechanic Simulator VR Playtest
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
            Crescimento da disponibilidade de jogos para Linux entre 2018 e 2022:
            Ano: 2018 - Lançamentos: 0
            Ano: 2019 - Lançamentos: 0
            Ano: 2020 - Lançamentos: 0
            Ano: 2021 - Lançamentos: 0
            Ano: 2022 - Lançamentos: 0
        """
        jogosLinuxPorAno = self.Steam.getJogosLinux()
        print()
        print("Crescimento da disponibilidade de jogos para Linux entre 2018 e 2022:")
        for ano in range(2018, 2023):
            print(f"Ano: {ano} - Lançamentos: {jogosLinuxPorAno[str(ano)]}")

    def showPercJogosSo(self):
        """
            Mostra a porcentagem de jogos compatíveis com o SOs: Windows, Mac e Linux
        """
        print()
        print("Compatibilidade dos jogos por sistema operacional:")
        print(f"Windows: {round(self.Steam.getPercJogosWindows(), 2)}%")
        print(f"Mac: {round(self.Steam.getPercJogosMac(), 2)}%")
        print(f"Linux: {round(self.Steam.getPercJogosLinux(), 2)}%")

        distribuicao_por_so = {
            'sistemas_operacionais': ['Windows', 'Mac', 'Linux'],
            'disponibilidade': [
                round(self.Steam.getPercJogosWindows(), 2), 
                round(self.Steam.getPercJogosMac(), 2), 
                round(self.Steam.getPercJogosLinux(), 2)
            ],
            'color': ['#0066ff', '#ff8080', '#9fff80']
        }

        bubble_chart = BubbleChart(area=distribuicao_por_so['disponibilidade'],
                                bubble_spacing=0.1)

        bubble_chart.collapse()

        fig, ax = plt.subplots(subplot_kw=dict(aspect="equal"))
        bubble_chart.plot(
            ax, distribuicao_por_so['sistemas_operacionais'], distribuicao_por_so['disponibilidade'], distribuicao_por_so['color'])
        ax.axis("off")
        ax.relim()
        ax.autoscale_view()
        ax.set_title('Disponibilidade de jogos por sistema operacional', fontdict=self.plotFontTitle)

        plt.show()

    def showSinglePlayerIndieStretegy(self):
        """
            Mostra o Número total de jogos single-player do gênero Indie e estratégia lançados por ano entre 2010 e 2020
        """
        indie, strategy = self.Steam.getSinglePlayerIndieStretegy()
        anos = np.arange(2010, 2020)

        fig, ax = plt.subplots()

        ax.bar(anos, indie, label='Indie')
        ax.bar(anos, strategy, label='Strategy')

        ax.set_ylabel('Lançamentos', fontdict=self.plotFontLabel)
        ax.set_xlabel('Ano', fontdict=self.plotFontLabel)
        ax.legend(title='Gêneros', ncols=2)
        plt.title("Lançamentos de jogos Single-player Indie e Strategy", fontdict=self.plotFontTitle)
        plt.show()

    def showTagAdventureGamesEvolution(self):
        """
            Mostra os Lançamentos de jogos de aventura entre 2001 e 2022
        """
        pol = self.Steam.getTagAdventureByYear()
        valores = []
        anos = range(2001, 2023)
        for ano in anos:
            if ano not in pol:
                valor = 0
            else:
                valor = pol[ano]
            valores.append(valor)

        fig, ax = plt.subplots()

        ax.bar(anos, valores, label='Adventure')

        ax.set_ylabel('Lançamentos', fontdict=self.plotFontLabel)
        ax.set_xlabel('Ano', fontdict=self.plotFontLabel)
        # ax.legend(title='Gêneros', ncols=2)
        plt.title("Lançamentos de jogos de Aventura", fontdict=self.plotFontTitle)
        plt.show()


    def showGamesPriceLow(self):
        """
            Mostra os Jogos com valores igual ou abaixo de $5.00

            >>> v.showGamesPriceLow()
            <BLANKLINE>
            Foram lançados 9 jogos pagos com valores iguais ou menores de 5 dólares.
            <BLANKLINE>
        """
        priceLow = self.Steam.getGamesPriceLow()
        # print(priceLow)
        print()
        print(f"Foram lançados {priceLow['Price']} jogos pagos com valores iguais ou menores de 5 dólares.")
        print()
        # empresas = self.Steam.getEmpresasMaisPublicam()
        # print(empresas)

    def showEmpresasMaisPublicam(self):
        """
            Mostra Empresas que mais publicaram jogos

            >>> v.showEmpresasMaisPublicam()
            <BLANKLINE>
            As cinco empresas que mais publicam jogos pagos na plataforma:
            <BLANKLINE>
            Publishers            Price
            Adam DeLease          2.99     1
            ClickGames            1.99     1
            eTIRUe                0.79     1
            Zankey Studio         2.99     1
            WASABI entertainment  15.99    1
            Name: count, dtype: int64
        """
        print()
        print("As cinco empresas que mais publicam jogos pagos na plataforma:")
        print()
        empresas = self.Steam.getEmpresasMaisPublicam()
        print(empresas)

    def show10HighRecommendations(self):
        """
            Mostra os 10 jogos que receberam mais recomendações

            >>> v.show10HighRecommendations()
            <BLANKLINE>
            Os 10 jogos mais recomendados na plataforma:
            <BLANKLINE>
                                                        Name  Recommendations
            9                               City Car Driving            15683
            18                                       Just Go              302
            15                                  Slash or Die              141
            0                                   Six Braves 🕌                0
            1                                     Caterpilla                0
            2                                   F*ckable Kim                0
            3            Tank Mechanic Simulator VR Playtest                0
            4                                    Democracy 2                0
            5                                         Medusa                0
            6                                   SmileXCorp 3                0
            7                                     MechRunner                0
            8                                    TERMINAL VR                0
            10                                 Hide and Seek                0
            11                           Challenge Dream Cat                0
            12                                    City Quest                0
            13                                     Birb Race                0
            14                    The Final Days: Blood Dawn                0
            16                 Gladiator: Sword of Vengeance                0
            17                              Aesthetic Melody                0
            19  Paze Knight Ellen and the Dungeon town Sodom                0
        """
        print()
        print("Os 10 jogos mais recomendados na plataforma:")
        print()
        top_10_recommendations = self.Steam.get10HighRecommendations()
        print(top_10_recommendations)

# Testes
# Executar na raiz do projeto:
# > python modules/VisualisationSteamData.py -v
if __name__ == "__main__":
    import doctest
    from ParseSteamData import ParseSteamData
    doctest.testmod(extraglobs={'v': VisualisationSteamData("data/excerto.csv")})
else:
    from modules.ParseSteamData import ParseSteamData
    from modules.BubbleChart import BubbleChart
