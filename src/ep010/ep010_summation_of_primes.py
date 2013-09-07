'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
from util.primos import buscar_primos
from util._primos import Primos
from time import time    

start_time = time()
primos = buscar_primos(2000000)
print "in", time() - start_time, "seconds"

start_time = time()
primos = Primos.buscar_primos_ate(2000000)
print "in", time() - start_time, "seconds"

somatorio = 0

for primo in primos:
    if primo >= 2000000:
        break
    somatorio += primo
  
print "010",somatorio, "in", time() - start_time, "seconds"