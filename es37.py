'''Programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
 1 para binário, 2 para octal e 3 para hexadecimal.'''


num = int(input("Digite um número inteiro: "))
print('''Escolha uma opção para converter:
[1] Converter para Binário;
[2] Converter para Octal;
[3] Converter para Hexadecimal.''')
op = int(input("Qual conversão deseja? "))

if op == 1:
    print("O número escolhido {} convertido para número binário é {}".format(num, bin(num)[2:]))
    print("\033[32mObrigado por participar!\003[m")
elif op == 2:
    print("O número escolhido foi {} convertido para Octal é {}".format(num, oct(num)[2:]))
    print("\033[32mObrigado por participar!\003[m")
elif op == 3:
    print("O número escolhido é {} convertendo para hexadecimal é {}".format(num, hex(num)[2:]))
    print("\033[32mObrigado por participar!\003[m")
else:
    print("Resposta invalida")