from collections import Counter
import re

def contar_palavras(texto):
    # Limpar o texto: converter para minúsculas e remover caracteres especiais
    texto_limpo = re.sub(r'[^a-zA-Z0-9\s]', '', texto.lower())
    
    # Dividir o texto em palavras
    palavras = texto_limpo.split()
    
    # Contar a frequência de cada palavra
    contagem = Counter(palavras)
    
    return contagem

def mostrar_palavras_frequentes(contagem, n):
    # Obter as n palavras mais frequentes
    palavras_frequentes = contagem.most_common(n)
    
    # Mostrar as palavras e suas frequências
    for palavra, frequencia in palavras_frequentes:
        print(f"{palavra}: {frequencia}")

# Obter o texto do usuário
texto = input("Digite um texto: ")

# Contar as palavras no texto
contagem = contar_palavras(texto)

# Mostrar as 10 palavras mais frequentes
print("As 10 palavras mais frequentes:")
mostrar_palavras_frequentes(contagem, 10)
