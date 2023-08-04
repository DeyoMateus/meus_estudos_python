'''Programa que diga se é possível formar um triângulo com as medidas inceridas e qual o seu tipo:
Para ser um triângulo a soma de dois lados deve ser menor que o lado restante.
EQUILÁTERO: todos os lados iguais
ISÓSCELES: dois lados iguais, um diferente
ESCALENO: todos os lados diferentes'''

l1 = float(input("Digite um número: "))
l2 = float(input("Digite o segundo numero: "))
l3 = float(input("Digite o terceiro número: "))

if  l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print("\033[32mOs números fornecidos formam um triângulo", end=" ")
    if l1 == l2 == l3:
        print("\033[32mEQUILÁTERO\033[m")
    elif l1 != l2 != l3 != l1:
        print("\033[32mESCALENO\033[m")
    else:
        print("\033[32mISÓSCELES\033[m")
else:
    print("\033[31mOs números não formam um triângulo\033[m")