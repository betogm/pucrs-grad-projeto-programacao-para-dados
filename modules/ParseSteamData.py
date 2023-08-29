import csv

class ParseSteamData:

    def __init__(self, csvPath="../data/excerto.csv"):
        self.numLines = 0
        self.numGratuidos = 0
        self.dateDic = {}
        self.compatibilidade = {'Windows': 0, 'Mac': 0, 'Linux': 0}

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
                self._incrementaPorAnoLancamento(row['Release date'])

                # Compatibilidade com Sistemas Operacionais
                self._incrementaPorSistemaOperacional(row['Windows'], row['Mac'], row['Linux'])

    def _incrementaJogosGratuitos(self, price):
        """Incrementa um jogo gratuíto"""
        if float(price) == 0.0:
            self.numGratuidos += 1

    def _incrementaPorAnoLancamento(self, releaseDate):
        """Registra ano de lançamento concatenando um valor. 
        Faz um parser no campo 'Release date'"""
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

    def _incrementaPorSistemaOperacional(self, windows, mac, linux):
        """Incrementa a Compatibilidade com Sistemas Operacionais"""
        if windows == "True":
            self.compatibilidade['Windows'] += 1
        if mac == "True":
            self.compatibilidade['Mac'] += 1
        if linux == "True":
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

