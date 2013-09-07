'''
If the numbers 1 to 5 are written out in words: 
one, two, three, four, five, 
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive 
were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.

'''
from time import time

start_time = time()

quantidade = 0
numeros = ['','one','two','three','four','five','six','seven','eight','nine','ten']
numeros_entre_10_e_20 = ['','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
dezenas = [ 'ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
unidades = ['hundred','thousand']
conjuncoes = ['and']

todos_os_numeros_por_extenso = ''
def buscar_dois_digitos(texto):
    
    if texto != '00':
        if 10 < int(texto) < 20:
            n = int(texto) % 10
            return numeros_entre_10_e_20[n]
        if int(texto) < 10:
            return numeros[int(texto)]
        return dezenas[int(texto[0])-1] + ' ' + numeros[int(texto[1])]
    return ''
contador = 1
for i in range(1,1001):
    texto = str(i)
    tamanho_texto = len(texto)
    if tamanho_texto == 1:
        todos_os_numeros_por_extenso += numeros[int(texto)]
        print contador,numeros[int(texto)]
    if tamanho_texto == 2:
        todos_os_numeros_por_extenso += buscar_dois_digitos(texto)
        print contador,buscar_dois_digitos(texto)
    if tamanho_texto == 3:
        if int(texto) % 100 == 0:
            todos_os_numeros_por_extenso += numeros[int(texto[0])] + ' ' + unidades[0]
            print contador,numeros[int(texto[0])] + ' ' + unidades[0]
        else:
            todos_os_numeros_por_extenso += numeros[int(texto[0])] + ' ' + unidades[0] + ' ' + conjuncoes[0] + ' ' + buscar_dois_digitos(texto[1]+texto[2])
            print contador,numeros[int(texto[0])] + ' ' + unidades[0] + ' ' + conjuncoes[0] + ' ' + buscar_dois_digitos(texto[1]+texto[2])
    if tamanho_texto == 4:
        todos_os_numeros_por_extenso += numeros[int(texto[0])] + ' ' + unidades[1]
        print contador,numeros[int(texto[0])] + ' ' + unidades[1]
        
    contador +=1

todos_os_numeros_por_extenso = todos_os_numeros_por_extenso.replace(' ', '')
print "017",len(todos_os_numeros_por_extenso),"in",time()-start_time,"seconds"