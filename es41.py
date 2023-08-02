'''Programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER'''
from datetime import date
atual = date.today().year
ano = int(input("Digite seu ano de nascimento: "))
idade = atual - ano

if idade <= 9:
    print("O atleta tem {} anos e está na categoria Mirim".format(idade))
elif 9 < idade <= 14:
    print("O atleta tem {} e está na categoria Infantil".format(idade))
elif 14 < idade <= 19:
    print("O atleta tem {} e está na categoria Júnior".format(idade))
elif 19 < idade <= 25:
    print("O atleta tem {} e está na categoria Sênior".format(idade))
else:
    print("O atleta tem {} e está na categoria Master".format(idade))