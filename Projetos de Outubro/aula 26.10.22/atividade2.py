#Crie um programa que receba um numero digitedo pela usuario
#que sera comprarado se o numero digitado ´w maior que 10
# igual á 10 ou menor que 120

print ("programa adivinhe um numero inteiro")
num1 = int(input("Digite um numero inteiro: "))
if num1 > 10:
    print("O numero digitado é maior que o numero secreto", num1)
elif num1<10:
    print ("O numero digitado é menor que o numero secreto", num1)
else:
    print("Acertou o numero secreto!", num1)
