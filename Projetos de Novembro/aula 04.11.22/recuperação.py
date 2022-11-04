# Escreva um programa para ler o nome da cidade
# o número total de eleitores de um município,
# o número de votos brancos, nulos e válidos.
# Exibir o nome da cidade, e calcular o percentual que cada
# um representa em relação ao total de eleitores.
# Ao final perguntar se deseja repetir e fazer de outra cidade.

print("Programa de Pesquisa de Eleições")

restart="sim"
while restart == "sim":
    print("ALGORITMO ELEITORES: ")
    nomeCidade = input("Digite o nome da cidade: ")
    n1 = int(input("Digite o número de votos válidos: "))
    n2 = int(input("Digite o número de votos nulos: "))
    n3 = int(input("Digite o número de votos brancos: "))

    totaleleitores = n1 + n2 + n3

    print("A cidade de", nomeCidade,"tem o numero total de votos de:",totaleleitores)
    print("O percentual de votos nulos foi de ",(n2/totaleleitores)*100,"%" )
    print("O percentual de votos brancos foi de ",(n3/totaleleitores)*100,"%" )
    print("O percentual de votos nulos foi de ",(n1/totaleleitores)*100,"%" )

    restart = input("Se deseja repetir e fazer de outra cidade digite sim: ")