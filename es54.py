''' Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não 
atingiram a maioridade e quantas já são maiores.'''

from datetime import date
ma = 0
me = 0
ano = date.today().year
c = 0
for nas in range(1, 8):
    nas = int(input("Em que ano a {}ª pessoa nasceu: ".format(nas)))
    c += 1
    idd = ano - nas
    if idd >= 21:
        ma += 1
    else:
        me += 1
print("De {} pessoas, {} pessoas são maior de idade e {} são menores de idade".format(c, ma, me))