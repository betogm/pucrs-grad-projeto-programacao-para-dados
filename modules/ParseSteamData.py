import csv
from datetime import datetime
import pandas as pd

class ParseSteamData:

    def __init__(self, csvPath="data/excerto.csv"):
        self.df = pd.read_csv(csvPath)

        self.df = self.df.astype({
            'Price':'float',
            'Positive':'int',
            'Negative':'int'
        })

        self.numLines = 0
        self.isRpg = False
        self.numGratuidos = 0
        self.dateDic = {}
        self.rpg = {
            'numLines': 0,
            'dlc': {'sum': 0, 'max': 0},
            'avaliations': {'positivas': {'sum': 0, 'max': 0}, 'negativas': {'sum': 0, 'max': 0}},
            'materiaisDemonstrativos': {'sum': 0, 'max': 0}
        }
        self.compatibilidade = {'Windows': 0, 'Mac': 0, 'Linux': 0}
        self.linuxPorAno = {'2018': 0, '2019': 0, '2020': 0, '2021': 0, '2022': 0}
        self.metacriticScoreData = {}
        self.metacriticScore = {}
        self.metacriticScore10 = {}

        # Carrega o arquivo de dados
        with open(csvPath) as csvfile:
            reader = csv.DictReader(csvfile)
            
            # Itera sobre todas as linhas do arquivo,
            # consumindo de uma vez as informações necessárias
            # evitando mais de um loop
            for row in reader:
                # Soma uma nova linha em cada iteração
                self.numLines += 1

                # Soma jogos gratuítos
                self._incrementaJogosGratuitos(row['Price'])

                # Registra ano de lançamento concatenando um valor
                self._incrementaPorAnoLancamento(row['Release date'], row['Linux'])

                # Compatibilidade com Sistemas Operacionais
                self._incrementaPorSistemaOperacional(row['Windows'], row['Mac'], row['Linux'])

                # Verifica se é um jogo RPG
                self._isRpg(row['Genres'])

                # DLC
                self._incrementaDlc(int(row['DLC count']))

                # Avaliações positivas e negativas
                self._incrementaAvaliacoes(int(row['Positive']), int(row['Negative']))

                # Materiais Demonstrativos - imagens e videos
                self._incrementaMatDemo(row['Screenshots'], row['Movies'])

                # Registra Metacritc Score
                self._incrementaMetacriticScore(row['Name'], row['Release date'], row['Metacritic score'])

    def _incrementaJogosGratuitos(self, price):
        """
            Incrementa um jogo gratuíto

            >>> p._incrementaJogosGratuitos(1.5)
            2

            >>> p._incrementaJogosGratuitos(0.0)
            3
        """
        if float(price) == 0.0:
            self.numGratuidos += 1

        return self.numGratuidos

    def _incrementaPorAnoLancamento(self, releaseDate, linux):
        """
            Registra ano de lançamento concatenando um valor.
            Faz um parser no campo 'Release date'

            >>> p._incrementaPorAnoLancamento('Sep 13, 2022')
            {'2022': 9, '2012': 1, '2016': 3, '2019': 1, '2023': 2, '2021': 1, '2015': 1, '2018': 1, '2017': 2}

            >>> p._incrementaPorAnoLancamento('Aug 10, 2008')
            {'2022': 9, '2012': 1, '2016': 3, '2019': 1, '2023': 2, '2021': 1, '2015': 1, '2018': 1, '2017': 2, '2008': 1}
        """
        if "," in releaseDate :
            parseDate = releaseDate.split(',')
        elif " " in releaseDate :
            parseDate = releaseDate.split(' ')

        if len(parseDate) == 2 :
            year = parseDate[1].strip()
        else: 
            year = "undefined"
            self.dateDic['error'] = releaseDate

        if year not in self.dateDic:
            self.dateDic[year] = 1
        else:
            self.dateDic[year] += 1

        # Computa lançamentos em Linux
        if linux == "True" and year != 'undefined' and int(year) <= 2022 and int(year) > 2017:
            self.linuxPorAno[year] += 1
        
        return self.dateDic

    def _incrementaPorSistemaOperacional(self, windows, mac, linux):
        """
            Incrementa a Compatibilidade com Sistemas Operacionais

            >>> p._incrementaPorSistemaOperacional("False", "False", "False")
            {'Windows': 20, 'Mac': 4, 'Linux': 3}
            
            >>> p._incrementaPorSistemaOperacional("True", "True", "True")
            {'Windows': 21, 'Mac': 5, 'Linux': 4}
        """
        if windows == "True":
            self.compatibilidade['Windows'] += 1
        if mac == "True":
            self.compatibilidade['Mac'] += 1
        if linux == "True":
            self.compatibilidade['Linux'] += 1
        
        return self.compatibilidade

    def _isRpg(self, genres):
        if "RPG" in genres:
            self.rpg['numLines'] += 1
            self.isRpg = True
            return True
        self.isRpg = False
        return False
    
    def _incrementaDlc(self, unit):
        """
            Calcula a porcentagem de um valor em relação ao total de registros

            >>> p._incrementaDlc(1)
            {}
        """
        if self.isRpg:
            self.rpg['dlc']['sum'] += unit
            if unit > self.rpg['dlc']['max'] :
                self.rpg['dlc']['max'] = unit
            return self.rpg['dlc']
        return {}

    def _incrementaAvaliacoes(self, positivas, negativas):
        """
            Calcula a porcentagem de um valor em relação ao total de registros

            >>> p._incrementaAvaliacoes(1, 2)
            {}
        """
        if self.isRpg:
            self.rpg['avaliations']['positivas']['sum'] += int(positivas)
            if positivas > self.rpg['avaliations']['positivas']['max']:
                self.rpg['avaliations']['positivas']['max'] = positivas
            self.rpg['avaliations']['negativas']['sum'] += int(negativas)
            if negativas > self.rpg['avaliations']['negativas']['max']:
                self.rpg['avaliations']['negativas']['max'] = negativas
            return self.rpg['avaliations']
        return {}

    def _incrementaMatDemo(self, screenshots, movies):
        """
            Calcula a porcentagem de um valor em relação ao total de registros

            >>> p._incrementaMatDemo("asdf,fdsa", "qwer,rewq,zxcv")
            30
        """
        if self.isRpg:
            materiaisDemonstrativos = 0
            materiaisDemonstrativos += len(screenshots.split(","))
            materiaisDemonstrativos += len(movies.split(","))
            self.rpg['materiaisDemonstrativos']['sum'] += materiaisDemonstrativos
            if materiaisDemonstrativos > self.rpg['materiaisDemonstrativos']['max'] :
                self.rpg['materiaisDemonstrativos']['max'] = materiaisDemonstrativos
            return self.rpg['materiaisDemonstrativos']
        return {}

    def _incrementaMetacriticScore(self, jogo, dataLancamento, metacriticScore):
        """
            Calcula a porcentagem de um valor em relação ao total de registros

            >>> p._incrementaMetacriticScore("Zelda", "Sep 25, 2022", "50")
            {}

            >>> p._incrementaMetacriticScore("Zelda", "Sep 2022", "50")
            {}

            >>> p._incrementaMetacriticScore("Zelda", "Sep", "50")
            Sep
            False
        """
        try:
            numWords = len(dataLancamento.split())
            if(numWords == 3):
                dataFormatada = datetime.strptime(dataLancamento, "%b %d, %Y").strftime("%Y-%m-%d")
            else:
                dataFormatada = datetime.strptime(dataLancamento, "%b %Y").strftime("%Y-%m-01")
        
            dados = {
                'releaseDate': dataFormatada,
                'jogo': jogo,
                'score': metacriticScore
            }
            if metacriticScore not in self.metacriticScoreData :
                self.metacriticScoreData[metacriticScore] = {dataFormatada: dados}
            else :
                self.metacriticScoreData[metacriticScore][dataFormatada] = dados
            return dados
        except ValueError:
            print(dataLancamento)
            return False


    def _computaMetacriticScore(self):
        """
            Calcula a porcentagem de um valor em relação ao total de registros

            >>> p._computaMetacriticScore()
            {}
        """
        self.metacriticScore = {}
        for n in sorted(self.metacriticScoreData, reverse=True)[:10] :
            for i in sorted(self.metacriticScoreData[n]) :
                self.metacriticScore[n + "_" + i] = self.metacriticScoreData[n][i]
        i = 0
        for n in self.metacriticScore:
            self.metacriticScore10[n] = self.metacriticScore[n]
            if(i >= 10) :
                break
            i = i +1
        return self.metacriticScore10

    def getMetacriticScore(self):
        """
            Mostra os dez jogos mais bem avaliados, de acordo com o Metacritic

            >>> p.getMetacriticScore()
            {}
        """
        if self.metacriticScore10 == {} :
            return self._computaMetacriticScore()
        else :
            return self.metacriticScore10

    def getRpgData(self):
        """
            Mostra os dez jogos mais bem avaliados, de acordo com o Metacritic

            >>> p.getRpgData()
            {}
        """
        return self.rpg

    def getEmpresasMaisPublicam(self):
        """
            Mostra os dez jogos mais bem avaliados, de acordo com o Metacritic

            >>> p.getEmpresasMaisPublicam()
            {}
        """
        filtrada = self.df.loc[:, ["Publishers", "Price"]]
        filtrada = filtrada[self.df["Price"] > 0.0]
        filtrada = filtrada.value_counts()

        return filtrada.head()

    def _getPercentagemSobreTotal(self, valor, numLines = 0):
        """
            Calcula a porcentagem de um valor em relação ao total de registros

            >>> p._getPercentagemSobreTotal(100.0)
            500.0

            >>> p._getPercentagemSobreTotal(50.0)
            250.0
        """
        if numLines == 0:
            numLines = self.numLines
        return (100 * valor) / numLines;

    def getDlc(self):
        pass

    def getPercJogosGratuitos(self):
        """
            Retorna a porcentagem de jogos gratuítos

            >>> p.getPercJogosGratuitos()
            15.0
        """
        return self._getPercentagemSobreTotal(self.numGratuidos)

    def getPercJogosWindows(self):
        """
            Retorna a porcentagem de jogos compatíveis com o SO Windows

            >>> p.getPercJogosWindows()
            105.0
        """
        return self._getPercentagemSobreTotal(self.compatibilidade['Windows'])

    def getPercJogosMac(self):
        """
            Retorna a porcentagem de jogos compatíveis com o SO Windows

            >>> p.getPercJogosMac()
            25.0
        """
        return self._getPercentagemSobreTotal(self.compatibilidade['Mac'])

    def getJogosLinux(self):
        """
            Retorna a porcentagem de jogos compatíveis com o SO Windows

            >>> p.getJogosLinux()
            25.0
        """
        return self.linuxPorAno

    def getPercJogosLinux(self):
        """
            Retorna a porcentagem de jogos compatíveis com o SO Windows
        
            >>> p.getPercJogosLinux()
            20.0
        """
        return self._getPercentagemSobreTotal(self.compatibilidade['Linux'])

    def getAnoMaisLancamentos(self):
        """
            Retorna uma lista com o ano com o maior número de lançamentos de jogos.
            Item [0] contém o ano e Item [1] o número de jogos lançados.
        
            >>> p.getAnoMaisLancamentos()
            ('2022', 9)
        
        """
        Ano = 0
        Lancamentos = 0
        for ano, num in self.dateDic.items():
            if Lancamentos < num :
                Ano = ano
                Lancamentos = num

        return Ano, Lancamentos

# Testes
# Executar na raiz do projeto:
# > python modules/ParseSteamData.py -v
if __name__ == "__main__":
    import doctest
    doctest.testmod(extraglobs={'p': ParseSteamData("data/excerto.csv")})