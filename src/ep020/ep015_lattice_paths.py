'''
Starting in the top left corner of a 2x2 grid, 
and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20x20 grid?

'''
from time import time

start_time = time()

tamanho_maximo = 20

contador = 0

def quantidade_de_tabs(x):
    retorno = ""
    for x in range(0,x-1):
        retorno += "\t"
        
    return retorno

def andar(x,y):
    
    if x < tamanho_maximo:
        print quantidade_de_tabs(x+1),"->"
        andar(x+1,y)
        print quantidade_de_tabs(x+1),"<-"
        
    if y < tamanho_maximo:
        print quantidade_de_tabs(x),"v"
        andar(x,y+1)
        print quantidade_de_tabs(x),"^"
    
    if x >= tamanho_maximo and y >= tamanho_maximo:
        global contador
        print "contei"
#         if contador % 10000000 ==0:
#             print contador
        contador = contador + 1

    
# andar(0,0)

matriz = []
for x in range(0,tamanho_maximo+1):
    linha = []
    for y in range(0,tamanho_maximo+1):
        linha.append(0)
        
    matriz.append(linha)

for x in range(0,tamanho_maximo+1):
    for y in range(0,tamanho_maximo+1):
        if x == 0 or y == 0:
            matriz[x][y] = 1
        else:
            matriz[x][y] = matriz[x-1][y] + matriz[x][y-1]
        
# for linha in matriz:
#     print linha
    
print "015",matriz[tamanho_maximo][tamanho_maximo],"in",time() - start_time,"seconds"