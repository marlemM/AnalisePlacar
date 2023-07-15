import pandas as pd

# Carregar os dados dos jogos do Palmeiras
palmeiras_df = pd.read_csv('dados_jogos.csv')
palmeiras_df = palmeiras_df[(palmeiras_df['time_casa'] == 'Botafogo') | (palmeiras_df['time_visitante'] == 'Botafogo')]

# Carregar os dados dos jogos do Flamengo
flamengo_df = pd.read_csv('dados_jogos.csv')
flamengo_df = flamengo_df[(flamengo_df['time_casa'] == "Bragantino") | (flamengo_df['time_visitante'] == "Bragantino")]

# Estatísticas do Palmeiras
media_gols_palmeiras = palmeiras_df['gols_casa'].mean()
porcentagem_ambas_marcam_palmeiras = (palmeiras_df['ambas_marcam'] == 'Sim').mean() * 100
#media_posse_bola_palmeiras = palmeiras_df[['posse_bola_casa', 'posse_bola_visitante']].mean().mean()

# Estatísticas do Flamengo
media_gols_flamengo = flamengo_df['gols_casa'].mean()
porcentagem_ambas_marcam_flamengo = (flamengo_df['ambas_marcam'] == 'Sim').mean() * 100
#media_posse_bola_flamengo = flamengo_df[['posse_bola_casa', 'posse_bola_visitante']].mean().mean()

# Exibir os resultados
print('Estatísticas do time_casa')
print('Média de gols por jogo:', media_gols_palmeiras)
print('Porcentagem de jogos com ambas as equipes marcando:', porcentagem_ambas_marcam_palmeiras)
#print('Média de posse de bola:', media_posse_bola_palmeiras)
print()

print('Estatísticas do time_visitante')
print('Média de gols por jogo:', media_gols_flamengo)
print('Porcentagem de jogos com ambas as equipes marcando:', porcentagem_ambas_marcam_flamengo)
#print('Média de posse de bola:', media_posse_bola_flamengo)
