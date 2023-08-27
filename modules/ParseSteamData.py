import csv

class ParseSteamData:
    def __init__(self, csvPath="../data/excerto.csv"):
        self.numLines = 0
        self.numGratuidos = 0
        self.dateDic = {}
        self.compatibilidade = {'Windows': 0, 'Mac': 0, 'Linux': 0}

        print("Aguarde, carregando os dados...")
        with open(csvPath) as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Soma uma nova linha em cada iteração
                self.numLines += 1

                # Busca jogos gratuítos
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
                if(row['Windows'] == "True"):
                    self.compatibilidade['Windows'] += 1
                if(row['Mac'] == "True"):
                    self.compatibilidade['Mac'] += 1
                if(row['Linux'] == "True"):
                    self.compatibilidade['Linux'] += 1

    def getPercJogosGratuitos(self):
        return (100 * self.numGratuidos) / self.numLines;

    def __str__(self) :
        return "numLines: " + str(self.numLines) + "\n" + \
            "numGratuidos: " + str(self.numGratuidos)# + "\n" + \
            # "dateDic: " + str(self.dateDic) + "\n" + \
            # "compatibilidade: ", str(self.compatibilidade)