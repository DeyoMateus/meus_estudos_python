'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time Santos'''

clube = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fluminense', 'Grêmio', 'Bragantino', 'Atlhetico-PR', 'Fortaleza', 'Cuiabá', 'São Paulo',
         'Atlético-MG', 'Cruzeiro', 'Corinthians', 'Internacional', 'Goiás', 'Bahia', 'Santos', 'Vasco da Gama', 'Cotiriba', 'América-MG') 
print(">>>>"*10)
print(f"Os 5 primeiros segudo a colocação {clube[:5]}")
print(">>>>"*10)
print(f"Os últimos 4 times segundo a colocação {clube[-4:]}")
print(">>>>"*10)
print(f"Os times em ordem alfabética{sorted(clube)}")
print(">>>>"*10)
print(f"A posição que o time da Santos está é {clube.index('Santos')+1}ª")
print(">>>>"*10)