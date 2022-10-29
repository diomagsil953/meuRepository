# Crie um programa para calcular as notas obtidas pelo aluno do
# ensino médio, deverá mostrar mensagem para ser digitado a
# nota do 1º, 2º, 3º e 4º bimestre. Após deverá mostrar na tela se o aluno foi aprovado,
# se está em recuperação ou foi reprovado sem chance de recuperação

primeiroBimestre = float(input("Digite a nota do primeiro bimestre: "))

segundoBimestre = float(input("Digite a nota do segundo no bimestre: "))

terceiroBimestre = (input("Digite a nota do terceiro no bimestre: "))

quartoBimestre = (input("Digite a nota do quarto no bimestre: "))

notaFinal = float(primeiroBimestre , segundoBimestre , terceiroBimestre, quartoBimestre)
if (notaFinal >= 40 and notaFinal < 60):
    print("Aluno de recuperação")
elif notaFinal >= 60:
    print("Aluno aprovado")
else:
    print("Aluno reprovado")
