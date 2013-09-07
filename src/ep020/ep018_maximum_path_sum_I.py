'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, 
the maximum total from top to bottom is 23.

   3
  7 4
 2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

                 75
               95 64
              17 47 82
             18 35 87 10
            20 04 82 47 65
           19 01 23 75 03 34
          88 02 77 73 07 63 67
        99 65 04 28 06 16 70 92
       41 41 26 56 83 40 80 70 33
     41 48 72 33 47 32 37 16 94 29
    53 71 44 65 25 43 91 52 97 51 14
   70 11 33 28 77 73 17 78 39 68 17 57
  91 71 52 38 17 14 91 43 58 50 27 29 48
 63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. 
However, Problem 67, is the same challenge with a triangle containing one-hundred rows; 
it cannot be solved by brute force, and requires a clever method! ;o)
'''
from time import time

start_time = time()

piramide = []

# piramide.append([3])
# piramide.append([7,4])
# piramide.append([2,4,6])
# piramide.append([8,5,9,3])

piramide.append([75])
piramide.append([95,64])
piramide.append([17, 47, 82])
piramide.append([18, 35, 87, 10])
piramide.append([20, 04, 82, 47, 65])
piramide.append([19, 01, 23, 75, 03, 34])
piramide.append([88, 02, 77, 73, 07, 63, 67])
piramide.append([99, 65, 04, 28, 06, 16, 70, 92])
piramide.append([41, 41, 26, 56, 83, 40, 80, 70, 33])
piramide.append([41, 48, 72, 33, 47, 32, 37, 16, 94, 29])
piramide.append([53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14])
piramide.append([70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57])
piramide.append([91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48])
piramide.append([63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31])
piramide.append([04, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 04, 23])

soma = 0

posicao = 0
for i in range(len(piramide)):
    linha = piramide[i]
    if posicao == len(linha)-1:
        soma += linha[posicao]
        print i,linha[posicao]
    if posicao < len(linha)-1:

        if linha[posicao] > linha[posicao+1]:
            soma += linha[posicao]
            print i,linha[posicao]
        elif linha[posicao+1] > linha[posicao]:
            soma += linha[posicao+1]
            print i,linha[posicao+1]
            posicao = posicao + 1
    
print "018",soma,"in",time()-start_time,"seconds"