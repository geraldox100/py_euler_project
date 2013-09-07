'''
2 ** 15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2 ** 1000?
'''

from time import time

start_time = time()

numero_em_texto = str( (2 ** 1000) )
soma = 0

for numero in numero_em_texto:
    soma += int(numero)
    
    
print "015", soma, "in", time() - start_time,"seconds"