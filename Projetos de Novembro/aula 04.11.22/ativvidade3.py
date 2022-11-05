# Faça um programa que calcule o fatorial
# de um número,é obrigatório o uso de função
# recursiva para o calculo fatorial.

print("Algoritmo de Multiplicação")

aa1 = int(input("digite um numero: "))
aa2 = int(input("digite outro número para a conta: "))

def multiplica(b1,b2):
    resultado=b1*b2
    return print("O resultado da multiplicação é ",resultado)

multiplica(aa1,aa2)