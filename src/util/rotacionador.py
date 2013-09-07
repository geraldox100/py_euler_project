import copy

def girar(matriz_parametro, quantidade = 1):
    matriz = copy.deepcopy(matriz_parametro)
    if quantidade > 1:
        matriz = girar(matriz, quantidade - 1)
        
    tmp = 0
    N2 = len(matriz)/2
    N = len(matriz)
    
    for i in range(0,N2):
        for j in range(i,N-1-i):
            tmp= matriz[N-1-j][i];
            matriz[N-1-j][i]= matriz[N-1-i][N-1-j];
            matriz[N-1-i][N-1-j]= matriz[j][N-1-i];
            matriz[j][N-1-i]= matriz[i][j];
            matriz[i][j]= tmp;
            
    return matriz
    
if __name__ == "__main__":
    matriz = [
                [ 1, 2, 3, 13],
                [ 4, 5, 6, 14],
                [ 7, 8, 9, 15],
                [10,11,12, 16],
            ]
        
    matriz1 = [
                [ 10, 7, 4, 1],
                [ 11, 8, 5, 2],
                [ 12, 9, 6, 3],
                [16,15,14, 13],
            ]
    
    matriz2 = [
                [ 16, 12, 11, 10],
                [ 15,  9,  8,  7],
                [ 14,  6,  5,  4],
                [ 13,  3,  2,  1],
            ]
