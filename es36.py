'''Ex 036 - Programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''


vc = float(input("Qual o valor da casa?R$ "))
sl = float(input("Qual o seu salário?R$ "))
tp = int(input("Em quantos anos vai pagar? "))

fina =  vc/(tp*12)
lim = sl * (30/100)

if fina > lim:
    print("\033[31mLamentamos informar que a parcela de R${:.2f}\n supera 30% do seu salário de R${:.2f}. Portanto está reprovado \003[m".format(fina, sl))
else:
    print("\033[32mParabéns, você está aprovado a parcela é de R${:.2f}!\033[m".format(fina))