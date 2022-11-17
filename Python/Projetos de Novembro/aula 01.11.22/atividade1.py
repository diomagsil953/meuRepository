#• Faça um Programa que pergunte quanto você ganha por hora
# e o número de horas trabalhadas no mês. Calcule e mostre
# o total do seu salário no referido mês, sabendo-se que são descontados
# 11% para o Imposto de Renda, 8% para o INSS e 5% para
# o sindicato, mostre todos os descontos,
# mostre o salário bruto e o líquido.

print ("Programa de seu perguntar Salario")

salariototal = float(input("Digite o número de horas trabalhadas no mês: ")) * float(input("Digite o valor da hora trabalhada: "))
print("Salario total: ",salariototal)

IR = (salariototal*0.11)
INSS = (salariototal*0.08)
sindicato = (salariototal*0.05)

print("desconto IR: -",IR)
print("desconto INSS: -",INSS)
print("desconto sindicato: -",sindicato)
salarioliquido=(salariototal-IR-INSS-sindicato)

print("Salario liquido: ",salarioliquido)
