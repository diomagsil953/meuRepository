# Faça um Programa que leia dois vetores com 10 posições
# cada e receba números inteiros. Gere um terceiro vetor
# de 20 elementos, cujos valores deverão ser compostos
# pelos elementos intercalados dos dois outros vetores.
# Mostre ao final os três vetores.

vetor1 = [0]*5
vetor1[0] = 4
vetor1[1] = -9
vetor1[2] = 78
vetor1[3] = 0
vetor1[4] = 25
print(vetor1)

vetor2 = [0]*5
vetor2[0] = 8
vetor2[1]= 2
vetor2[2] = 34
vetor2[3] = 90
vetor2[4]= 200
print(vetor2)

v3 = [0] * 5

def zipar(v1,v2):
    zipar = []
    for x,y in zip(v1, v2):
        zipar.append(x)
        zipar.append(y)
    return zipar



ListaZipada = zipar(vetor1, vetor2)

for i in ListaZipada:

    print(i ,end=" " )