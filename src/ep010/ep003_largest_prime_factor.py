'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''
from util._primos import Primos
from math import sqrt
from time import time    

start_time = time()
    
valor = 600851475143

primo_querido = 0

primos = Primos.buscar_primos_ate(sqrt(valor))

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


print "003",primo_querido, "in", time() - start_time, "seconds"
