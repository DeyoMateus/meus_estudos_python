'''Elabore um programa que calcule o valor a ser pago por um produto, 
considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal 
– 3x ou mais no cartão: 20% de juros'''

from functools import total_ordering


valor = float(input("Digite o valor da compra:R$ "))

print("{:=^40}".format(" Lojas "))
print(''' Formas de pagamento:
      [1] À vista dinheiro/cheque: 10% de desconto.
      [2] À vista no cartão: 5% de desconto.
      [3] Em até 2x no cartão: preço formal.
      [4] 3x ou mais no cartão: 20% de juros''')

op = int(input("Escolha a forma de pagamento: "))

if op == 1:
    total = valor - (valor * 10 / 100)
elif op == 2:
    total = valor - (valor * 5 / 100)
elif op == 3:
    total = valor
    pc = total / 2
    print("Pagando em 2x você ira pagar 2 parcelas de R${:.2f}".format(pc))
elif op == 4:
    pc = int(input("Vai dividir em quantas vezes?"))
    total = valor + (valor * 20 / 100)
    totalpac = total / pc
    print("Sua compra será dividida em {}x de R${:.2f}".format(pc, totalpac))
print("Sua compra de R${:.2f} no final sairá por R${:.2f}".format(valor, total))
