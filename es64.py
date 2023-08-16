'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário 
digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi
 a soma entre eles (desconsiderando o flag).'''

soma = num = c = 0
num = int(input("Digite um número [999 Para parar]: "))
while num != 999:
    soma += num
    c += 1
    num = int(input("Digite um número [999 Para parar]: "))
print("Foram digitados {} números e a soma entre eles é {}".format(c, soma))
