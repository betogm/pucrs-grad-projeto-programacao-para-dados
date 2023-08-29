import csv

class ParseSteamData:

    def __init__(self, csvPath="../data/excerto.csv"):
        self.numLines = 0
        self.numGratuidos = 0
        self.dateDic = {}
        self.compatibilidade = {'Windows': 0, 'Mac': 0, 'Linux': 0}

        with open(csvPath) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Soma uma nova linha em cada iteração
                self.numLines += 1

                # Soma jogos gratuítos
                if float(row['Price']) == 0.0:
                    self.numGratuidos += 1

                # Registra ano de lançamento concatenando um valor
                if "," in row['Release date'] :
                    parseDate = row['Release date'].split(',')
                elif " " in row['Release date'] :
                    parseDate = row['Release date'].split(' ')

                if len(parseDate) == 2 :
                    releaseDate = parseDate[1].strip()
                else: 
                    releaseDate = "undefined"
                    self.dateDic['error'] = row['Release date']

                if releaseDate not in self.dateDic:
                    self.dateDic[releaseDate] = 1
                else:
                    self.dateDic[releaseDate] += 1

                # Compatibilidade com Sistemas Operacionais
                if row['Windows'] == "True":
                    self.compatibilidade['Windows'] += 1
                if row['Mac'] == "True":
                    self.compatibilidade['Mac'] += 1
                if row['Linux'] == "True":
                    self.compatibilidade['Linux'] += 1

    def _getPercentagemSobreTotal(self, valor):
        """Calcula a porcentagem de um valor em relação ao total de registros"""
        return (100 * valor) / self.numLines;

    def getPercJogosGratuitos(self):
        """Retorna a porcentagem de jogos gratuítos"""
        return self._getPercentagemSobreTotal(self.numGratuidos)

    def getPercJogosWindows(self):
        """Retorna a porcentagem de jogos compatíveis com o SO Windows"""
        return self._getPercentagemSobreTotal(self.compatibilidade['Windows'])

    def getPercJogosMac(self):
        """Retorna a porcentagem de jogos compatíveis com o SO Windows"""
        return self._getPercentagemSobreTotal(self.compatibilidade['Mac'])

    def getPercJogosLinux(self):
        """Retorna a porcentagem de jogos compatíveis com o SO Windows"""
        return self._getPercentagemSobreTotal(self.compatibilidade['Linux'])

    def getAnoMaisLancamentos(self):
        """Retorna uma lista com o ano com o maior número de lançamentos de jogos.
        Item [0] contém o ano e Item [1] o número de jogos lançados."""
        anoMaisLanc = ["0", 0]
        for ano, num in self.dateDic.items():
            if anoMaisLanc[1] < num:
                anoMaisLanc[0] = ano
                anoMaisLanc[1] = num
        return anoMaisLanc

