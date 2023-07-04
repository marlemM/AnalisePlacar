# Dicionário para armazenar as informações do Campeonato Brasileiro
campeonato = {}

# Loop para inserir as rodadas, placares e ano
while True:
    rodada = input("Insira a rodada (ou 'nada' para parar): ")
    if rodada.lower() == 'nada':
        break

    ano = input("Insira o ano do Campeonato Brasileiro: ")

    if ano not in campeonato:
        campeonato[ano] = {}

    placares = []
    while True:
        placar = input(f"Insira um placar para a rodada {rodada} do ano {ano} (ou 'nada' para parar): ")
        if placar.lower() == 'nada':
            break
        placares.append(placar)

    campeonato[ano][rodada] = placares

# Verifica se existem rodadas e placares inseridos
if len(campeonato) > 0:
    placares_geral = []

    # Exibe o placar mais comum por rodada e ano
    with open("placares.txt", "w") as file:
        for ano, rodadas in campeonato.items():
            for rodada, placares in rodadas.items():
                placares_rodada = {}

                # Conta a ocorrência de cada placar na rodada
                for placar in placares:
                    placares_rodada[placar] = placares_rodada.get(placar, 0) + 1

                # Ordena os placares pelo número de ocorrências em ordem decrescente
                placares_ordenados = sorted(placares_rodada.items(), key=lambda x: x[1], reverse=True)
                placar_mais_comum_rodada = placares_ordenados[0][0]

                # Exibe o placar mais comum da rodada e ano
                print(f"Placar mais comum na rodada {rodada} do ano {ano}: {placar_mais_comum_rodada}")

                # Grava a informação no arquivo
                file.write(f"Rodada {rodada} do ano {ano}: Placar mais comum: {placar_mais_comum_rodada}\n")

                # Adiciona o placar mais comum da rodada aos placares gerais
                placares_geral.extend(placares)

        # Conta a ocorrência de cada placar no geral
        placares_geral_contagem = {}
        for placar in placares_geral:
            placares_geral_contagem[placar] = placares_geral_contagem.get(placar, 0) + 1

        # Ordena os placares gerais pelo número de ocorrências em ordem decrescente
        placares_geral_ordenados = sorted(placares_geral_contagem.items(), key=lambda x: x[1], reverse=True)
        placar_mais_comum_geral = placares_geral_ordenados[0][0]

        # Exibe o placar mais comum no geral
        print(f"\nPlacar mais comum no geral: {placar_mais_comum_geral}")

        # Grava a informação no arquivo
        file.write(f"Placar mais comum no geral: {placar_mais_comum_geral}\n")

else:
    print("Nenhuma rodada foi inserida.")
