# Crie um programa para calcular as notas obtidas pelo aluno do
# ensino médio, deverá mostrar mensagem para ser digitado a
# nota do 1º, 2º, 3º e 4º bimestre. Após deverá mostrar na tela se o aluno foi aprovado,
# se está em recuperação ou foi reprovado sem chance de recuperação

b1= float(input("Digite a nota do primeiro bimestre: "))
b2 = float(input("Digite a nota do segundo no bimestre: "))
b3 = (input("Digite a nota do terceiro no bimestre: "))
b4 = (input("Digite a nota do quarto no bimestre: "))

notaFinal = b1+b2+b3+b4
if (notaFinal >= 40 and notaFinal <= 100):
    print("Aluno de aprovado")
elif (notaFinal > 40 and notaFinal < 60):
    print("Aluno de recuperação")
elif (notaFinal < 40 and notaFinal >= 0):
    print("Aluno reprovado")
else:
    print ("Confira os valores digitados !!!")
