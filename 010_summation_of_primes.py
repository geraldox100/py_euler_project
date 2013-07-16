'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
from primos import buscar_primos


primos = buscar_primos(2000000)

somatorio = 0

for primo in primos:
    if primo >= 2000000:
        break
    somatorio += primo
  
print "010",somatorio  
