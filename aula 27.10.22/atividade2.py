# Crie um programa para realizar as operações de uma tabuada de multiplicação
# Onde será solicitado ao usuário digitar qual numero será a tabuada e
# qual intervalo do inicio e fim da tabuada, e exibir na tela o resultado conforme intervalo.
print("Programa para calcular tabuada de Miltiplicação")
numero = int(input("Digite o numero que voce deseja saber a multiplicação: "))
inicio = int(input("Digite o inicio do intervalor que voçe deseja começar: "))
fim = int(input("Digite o fim do intervalo: "))

print("Tabuada de", numero, "de", inicio, "ate", fim)
for i in range(inicio, fim + 1):
 print(numero, '*', i, "*", (numero*(i)))

