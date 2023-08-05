'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
No final do programa, mostre: a média de idade do grupo, qual é o nome do 
homem mais velho e quantas mulheres têm menos de 20 anos.'''

totm20 = 0
maioridadeh = 0
médiaidade = 0
somaidade = 0
nomevelho = ""
for p in range(1, 5):
    print("-------{}ª Pessoa--------".format(p))
    nome = str(input("Digite o nome:")).strip()
    idade = int(input("Digite a idade: "))
    sexo = str(input("Qual seu sexo [M/F]? ")).strip()
    somaidade += idade
    if  p == 1 and sexo in "Mm":
        maioridadeh = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maioridadeh:
        maioridadeh = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        totm20 += 1 

médiaidade = somaidade / 4

print("A média das idades é {:.2f}".format(médiaidade))
print("O nome do homem mais velho é {} e sua idade é {} anos".format(nomevelho, maioridadeh))
print("Tem {} mulheres com menos de 20 anos de idade". format(totm20))