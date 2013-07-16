'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
from primos import buscar_primos
from math import sqrt    
    
valor = 600851475143
#valor = 1456001
#valor = 13195
primo_querido = 0
primos = buscar_primos(sqrt(valor))
i = 0

while( i < len(primos)):
    primo = primos[i]

    if valor % primo == 0:
        valor = valor / primo
        primo_querido = primo
        if valor <= 1:
            break
    else:
        i = i + 1


print "003",primo_querido
