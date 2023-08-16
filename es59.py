'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa'''

from time import sleep
print("<=>" * 20)
n1 = float(input("Digite o 1ª número: "))
n2 = float(input("Digite o 2ªnúmero: "))
print("<=>" * 20)
at = 0
while at != 5:
    print("Opções:\n[ 1 ] somar \n[ 2 ] multiplicar \n[ 3 ] maior \n[ 4 ] novos números \n[ 5 ] sair do programa ")
    print("<=>" * 20)
    at = int(input("Escolha uma alternativa: "))
    if at == 1:
        a1 = n1 + n2
        print("Você escolheu somar os números o resultado é {}".format(a1))
    elif at == 2:
         a2 = n1 * n2
         print("Você escolheu multiplicar os números o resultado é {}".format(a2))
    elif at == 3:
        if n1 > n2:
            print("O número {} é maior que o número {}".format(n1, n2))
        else:
            print("O número {} é maior que o número {}".format(n2, n1))
    elif at == 4:
        n1 = float(input("Digite o novo número: ")) 
        n2 = float(input("Digite o novo número: "))                    
    sleep(2)
print("Fim")