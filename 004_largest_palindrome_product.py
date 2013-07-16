'''
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit 
numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit 
numbers.
'''
def eh_palindromo(n):
    numero_normal = str(n)
    numero_invertido = str(n)[::-1]
    return numero_normal == numero_invertido
        

palindromos = []    
tamanho = 1000
n = 0
eh_pra_para_loop = False
for i in reversed(range(tamanho)):
    for j in reversed(range(tamanho)):
        n = i * j
        if eh_palindromo(n):
            palindromos.append([i,j,n])
print "004",max(palindromos, key=lambda x: x[2])[2]
