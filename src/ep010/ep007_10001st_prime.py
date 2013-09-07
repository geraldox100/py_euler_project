'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, 
and 13, we can see that the 6th prime is 13.

What is the 10001st prime number?

resposta = 7927

'''

from util._primos import Primos
from time import time    

start_time = time()

primo = Primos.buscar_primo_numero(10001)
print "007", primo.numero(), "in", time() - start_time, "seconds"