numH = int(input("Digite o valor para H. O valor deve ser inteiro, positivo e maior ou igual a 50: "))
 
while numH < 50 or numH < 0:
    numH = int(input("Erro! Digite o valor para H. O valor deve ser inteiro, positivo e maior ou igual a 50: "))
 
numS = int(input("Digite o valor para S. O valor deve ser inteiro, positivo e maior ou igual a 50: "))
 
while numS < 50 or numS < 0:
    numS = int(input("Erro! Digite o valor para S. O valor deve ser inteiro, positivo e maior ou igual a 50: "))

numP = int(input("Digite o valor para P. O valor deve ser inteiro, positivo e maior ou igual a 50: "))
 
while numP < 50 or numP < 0:
    numP = int(input("Erro! Digite o valor para P. O valor deve ser inteiro, positivo e maior ou igual a 50: "))

#   contas  #

def calcH(n):
    numH = 1
    h = 1
    positivo = True
    while numH < n:
        numH += 1
        if positivo:
            h += (numH * 2 - 1) / numH
            positivo = False
        else:
            h -= (numH * 2 - 1) / numH
            positivo = True
 
    return h
 
def calcS(n):
    numS = 1
    s = 1
    negativo = False
    while numS < n:
        numS += 1
        if negativo:
            s += numS / (numS * numS)
            negativo = False
        else:
            s -= numS / (numS * numS)
            negativo = True
 
    return s
 
def calcP(n):
    numP1 = 2
    numP2 = 1
    p = 0
    for x in range(n):
        p += numP1 / numP2 ** 3
        numP2 += 2
        conta = 1
        while True:
            if primo(numP1 + conta):
                numP1 += conta
                break 
            conta += 1 
            
    return p
 
 
def primo(num):
    eprimo = True
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                eprimo = False
                break
    if eprimo:
        return True
    else:
        return False

#   Resultado   #

totalH = calcH(numH)
 
print("H é igual a: ", + float(totalH))
 
totalS = calcS(numS)
 
print("S é igual a: ", + float(totalS))

totalP = calcP(numP)
 
print("P é igual a: ", + float(totalP))
