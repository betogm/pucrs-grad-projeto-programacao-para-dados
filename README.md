# PUCRS GRADUAÇÃO TI - Projeto para disciplina de Programação para Dados - 3º Trimestre

## Projeto de Análise de Jogos Eletrônicos - Fun Corp

### Instruções Fase 1

1. Para executar o programa, entre no diretório raiz do programa e na shell execute o arquivo fase-1.py com o comando:
```bash
python fase-1.py
```
2. Ao ser executado, o programa apresenta um menu interativo autoexplicativo em que convida o usuário a digitar a opção da pergunta desejada.
```bash
=========== Jogos Eletrônicos - Fase 1 ===========
Escolha a opção digitando o número ou letra para escolher o tipo de Informação desejada:
[1] Pergunta 1: Qual o percentual de jogos gratuitos e pagos na plataforma?
[2] Pergunta 2: Qual o ano com o maior número de novos jogos?
[3] Pergunta 3: Quais os percentuais de compatibilidade com cada Sistema Operacional?
[m] para mostrar o menu novamente
[s] para sair do programa

Qual a sua opção? ('m' para mostrar o menu) 
```
3. Digite o número da pergunta desejada para obter a resposta. Digite "m" mara mostrar o menu novamente ou "s" para sair do programa.

### Instruções Fase 2

1. Para executar o programa, entre no diretório raiz do programa e na shell execute o arquivo fase-2.py com o comando:
```bash
python fase-2.py
```
2. Ao ser executado, o programa apresenta um menu interativo autoexplicativo em que convida o usuário a digitar a opção da pergunta desejada.
```bash
=========== Jogos Eletrônicos - Fase 2 ===========
Escolha a opção digitando o número ou letra para escolher o tipo de Informação desejada:
[1] Mostra o percentual de jogos gratuitos e pagos na plataforma?
[2] Mostra os dez jogos mais bem avaliados, de acordo com o Metacritic
[3] Jogos RPG: DLCs, avaliações e materiais de demonstração
[4] Empresas que mais publicaram jogos
[m] para mostrar o menu novamente
[s] para sair do programa

Qual a sua opção? ('m' para mostrar o menu) 
```
3. Digite o número da pergunta desejada para obter a resposta. Digite "m" mara mostrar o menu novamente ou "s" para sair do programa.

### Testes

Os testes foram feitos utilizando Doctest, e consomem dados dos 20 registros do arquivo data/excerto.csv.
Para executar os testes nos dois módulos, execute os comandos:

1. Testar todos os métodos da classe *ParseSteamData*:
```bash
python modules/ParseSteamData.py -v
```

2. Testar todos os métodos da classe *VisualisationSteamData*:
```bash
python modules/VisualisationSteamData.py -v
```
