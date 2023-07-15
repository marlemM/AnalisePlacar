import pandas as pd

# Dados dos jogos
jogos = [
    {'id': 1, 'time_casa': 'Atlético PR', 'time_visitante': 'Palmeiras', 'gols_casa': 2, 'gols_visitante': 2, 'posse_bola_casa': 53, 'posse_bola_visitante': 47},
    {'id': 2, 'time_casa': 'Flamengo', 'time_visitante': 'Fortaleza', 'gols_casa': 2, 'gols_visitante': 0, 'posse_bola_casa': 50, 'posse_bola_visitante': 50},
    {'id': 3, 'time_casa': 'Palmeiras', 'time_visitante': 'Botafogo', 'gols_casa': 0, 'gols_visitante': 1, 'posse_bola_casa': 56, 'posse_bola_visitante': 44},
    {'id': 4, 'time_casa': 'Santos', 'time_visitante': 'Flamengo', 'gols_casa': 2, 'gols_visitante': 3, 'posse_bola_casa': 38, 'posse_bola_visitante': 62}
]

# Criar DataFrame com os dados
df = pd.DataFrame(jogos)

# Salvar DataFrame em um arquivo CSV
df.to_csv('dados_jogos.csv', index=False)
