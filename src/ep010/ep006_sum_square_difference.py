'''
The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

range_ = 101

squares = 0
for i in range(1,range_):
    squares += i ** 2
    
sums = 0
for i in range(1,range_):
    sums += i
sums = sums ** 2
    
print "006", sums - squares