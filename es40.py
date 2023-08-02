'''Programa que leia duas notas de um aluno e calcule sua média,
 mostrando uma mensagem no final, de acordo com a média atingida:'''

nota1 = float(input("Digite a Primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
m = (nota1 + nota2) / 2
print("\033[32mTirando {} e {} tem a média de {}\033[m".format(nota1, nota2, m))
if m >= 7:
    print("\033[32mEstá Aprovado sua média foi de {}\033[m".format(m))
elif 6.9 > m >= 5 :
    print("\033[33mEstá de recuperação sua média foi de {}\033[m".format(m))

else:
    print("\033[31mEstá reprovado sua média é de {:.2f} e está abaixo de 5.0\033[m".format(m))