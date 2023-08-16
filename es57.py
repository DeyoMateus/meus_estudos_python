'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores
M ou F. Caso esteja errado, peça a digitação novamente até ter um valor correto.
'''
sexo = str(input("Digite seu sexo: ")).strip().upper()[0]
print(sexo)
while sexo not in "FfMm":
    sexo = str(input("\033[31mSexo invalido, informe seu sexo novamente: \033[m"))
print("\033[32mSexo {} validado com sucesso!\033[m".format(sexo))