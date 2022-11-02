#Crie um programa com uma função para multiplicar dois números
# e o algoritmo mostrar o resultado

print("Algoritmo para Multiplicação")

na = float(input("digite o primeiro números a ser multiplicados: "))
nb = float(input("digite o segundo número a ser miltiplicado: "))

def multiplica(n1,n2):
    resultado=n1*n2
    return print("O resultado da multiplicação é ",resultado)

multiplica(na,nb)