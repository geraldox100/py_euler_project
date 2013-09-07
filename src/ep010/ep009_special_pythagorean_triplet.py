'''
A Pythagorean triplet is a set of three natural numbers, a  b  c, 
for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for 
which a + b + c = 1000.
Find the product abc.

'''
from time import time    

start_time = time()
a = 0
b = 0
c = 0
m = 2
n = 1
breakk = False
for n in range (1,100):
    for m in range(1,100):
        
        a = (m**2) - (n**2)
        b = 2*m*n
        c = (m**2) + (n**2)

        if a+b+c == 1000:
            if ((a**2)+(b**2)==c**2):
                print "009",a*b*c, "in", time() - start_time, "seconds"
                breakk = True
                break
    if breakk:
        break



