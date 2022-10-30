import random
from pydantic import NumberNotGtError
maiorSeqCresc = int(1)
maiorSeqConsec = int(1)
maiorSeqCrescTotal = int(0)
maiorSeqConsecTotal = int(0)
ultimoNumero = int(0)
numero = int()


for x in range(150):

    numero = random.randrange(1, 500)
    print(f"seu {x + 1}º é "+ str(numero))
    
    if x != 0:

        if numero > ultimoNumero:
            maiorSeqCresc = maiorSeqCresc + 1

            if maiorSeqCresc > maiorSeqCrescTotal:
                maiorSeqCrescTotal = maiorSeqCresc

        elif numero == ultimoNumero:
            maiorSeqConsec = maiorSeqConsec + 1

            if maiorSeqConsec > maiorSeqConsecTotal:
                maiorSeqConsecTotal = maiorSeqConsec

    ultimoNumero = numero

print("a maior sequencia crescente: " + str(maiorSeqCrescTotal))
print("a maior sequencia de numeros constante: " + str(maiorSeqConsecTotal))