'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''



valor = (int(input("Digite um número: ")),
         int(input("Digite um número: ")),
         int(input("Digite um número: ")),
         int(input("Digite um número: ")))

    
print(f"O número 9 apareceu {valor.count(9)} vezes")
if 3 in valor:
    print(f"O número 3 foi digitado pela primeira vez na posição {valor.index(3)+1}ª")
else:
    print("O número 3 não foi digitado")
print("Os valores pares digitados foram", end= " ")    
for n in valor:
    if n % 2 == 0: 
        print(n, end= " ")