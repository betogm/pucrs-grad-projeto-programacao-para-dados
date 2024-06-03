
teste = {
    205: {
        'releaseDate': '2022-08-21',
        'jogo': 'Ancient',
        'score': 205
    },
    2: {
        'releaseDate': '2023-02-21',
        'jogo': 'Zelda',
        'score': 2
    },
    15: {
        'releaseDate': '2021-02-21',
        'jogo': 'Modena',
        'score': 15
    }
}

for n in sorted(teste, reverse=True)[:2]:
    print(teste[n])