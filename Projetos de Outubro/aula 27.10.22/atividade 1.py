# Faça um algoritmo que pergunte em que turno você estuda.

# Peça para digitar M-matutino ou V-Vespertino ou N-Noturno.

# Mostre a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"

# ou "Valor Inválido!", conforme o caso.

print ("Programa para identificar seu turno")
turno = input("Escreva a letra correspondente ao seu turno digitar M-matutino ou V-Vespertino ou N-Noturno: ")

match turno:
    case "M":
        print("Bom Dia!")
    case "V":
        print("Boa Tarde!")
    case "N":
        print("Boa Noite")
    case _:
        print("Valor Invalido")
