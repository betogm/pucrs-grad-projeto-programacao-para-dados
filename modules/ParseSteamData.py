import csv

class ParseSteamData:

    def __init__(self, csvPath="data/excerto.csv"):
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

    def _incrementaPorAnoLancamento(self, releaseDate):
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


    def _getPercentagemSobreTotal(self, valor):
        """
            Calcula a porcentagem de um valor em relação ao total de registros

            >>> p._getPercentagemSobreTotal(100.0)
            500.0

            >>> p._getPercentagemSobreTotal(50.0)
            250.0
        """
        return (100 * valor) / self.numLines;

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