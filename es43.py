"""Lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) 
e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso   93.450 A 1.65
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida"""

peso = float(input("Digite seu peso: (Kg) "))
al = float(input("Digite sua altura: (m) "))

imc = peso/(al ** 2)
print("\033[36mO IMC dessa pessoa é {:.1f}\033[m.".format(imc), end= " ")

if imc < 18.5:
    print("\033[33Status: Abaixo do Peso\033[m")
elif 18.5 <= imc < 25:
     print("\033[32mStatus: Peso Ideal\033[m")

elif 25 <= imc < 30:
    print("\033[34mStatus: Sobrepeso\033[m")

elif 30 <= imc < 40:
    print("\033[31mStatus: Obesidade\033[m")
else:
    print("\033[35mStatus: Obesidade Mórbida\033[m")


