'''
The sequence of triangle numbers is generated by adding the natural numbers. 
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:


 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''
from util.primos import buscar_primos
primos = buscar_primos(1000)
divisores = []
quantidade = 500
numero = 0
i = 1
while len(divisores) <= quantidade:
    divisores = [1]
    fatores = []
    numero += i
    
    numero_temporario = numero
    
    
    # FATORES
    for primo in primos:
        while numero_temporario % primo == 0:
            
            fatores.append(primo)
            numero_temporario = numero_temporario / primo
            
    
    #DIVISORES
    for fator in fatores:
        tamanho_divisores = len(divisores)
        for d in range(0,tamanho_divisores):
            
            calculo = fator * divisores[d]
            
            
            if not calculo in divisores:
                divisores.append(calculo)
            
    i += 1
    if len(divisores) >= quantidade:
        print i, numero,fatores,divisores
