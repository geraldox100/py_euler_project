'''
2520 is the smallest number that can be divided by 
each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly 
divisible by all of the numbers from 1 to 20?
'''
from time import time    

start_time = time()

i = 1
sequencia = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

eh_divisivel_pela_sequencia = True
while(True):
    for elemento in sequencia:
        eh_divisivel_pela_sequencia = True
        if i % elemento != 0:
            eh_divisivel_pela_sequencia = False
            break;
        
    if not eh_divisivel_pela_sequencia:
        i = i + 1
    else:
        break
        
print "005",i, "in", time() - start_time, "seconds"