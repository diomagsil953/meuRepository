# Numa fazenda em um local reservado para criação
# coloca-se um casal de coelhos. Supondo que em
# cada mês, a partir do segundo mês de vida, cada
# casal dá origem a um novo casal de coelhos, ao
# fim de um ano, quantos casais de coelhos estão
# no pátio? Escreva um programa para calcular a
# quantidade de coelhos em um ano.

def rec_fib(n):
    if n > 1:
        return rec_fib(n-1) + rec_fib(n-2)
    return n
for i in range(10):
    print(rec_fib(i))