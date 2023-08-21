'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
 Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

cont = ("Zero", "Um", "Dois", "Três", "Quatro", "Cinco", "Seis", " Sete", "Oito", "Nove", "Dez", "Onze",
        "Doze", "Treze", "Quatorze", "Quinze", "Dezesseis", "Dezessete", "Dezoito", "Dezenove", "Vinte")
while True:
    num = int(input("Digite qualquer número de 0 a 20: "))
    if 0 <= num <= 20:
        print(f"O número digitado foi {num} e por extenso é {cont[num]}")
    if num > 20:
       break
    dj = str(input("Deseja continuar [S/N]? ")).strip().upper()[0]
    if dj == "N":
      break
print("Obrigado por participar")



