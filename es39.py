'''Programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar
ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''

from datetime import date
atual = date.today().year
ano = int(input("Digite o seu ano de nascimento: "))
idade = atual - ano
print("Você nasceu no ano {}, completa {} no ano de {}".format(ano, idade, atual))
if idade > 18:
    id = (atual - ano) - 18
    dt = atual - id
    print("Passou do tempo de se alistar em {} anos".format(id))
    print("Seu alistamento foi em {}".format(dt))
elif idade < 18:
    id1 = 18 - (atual - ano)
    dtt = atual + id1
    print("Falta {} anos para você se alistar".format(id1))
    print("Seu alistamento será em {}".format(dtt))
else:
    print("Você deve se alistar imediatamente")