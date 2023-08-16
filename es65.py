'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, 
mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

res = "s"
num = qtd = soma = maior = menor = 0
while res in "Ss":
    num = int(input("Digite um número: "))
    soma += num
    qtd +=1
    if qtd == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < maior:
            menor = num
    res = str(input("Deseja continuar? [S/N] ")).upper().strip()[0]
med = soma / qtd
print("A quantidades de números digitados foi {} e a média entre os números foi {}.".format(qtd, med))
print("O menor número digitado foi {} e o maior número digitado foi {}.".format(menor, maior))
