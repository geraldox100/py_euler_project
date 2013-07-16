def coordenadas_diagonais_matriz_quadrada(ordem):
    coordenadas = []
    coordenadas_de_cima_para_baixo = []
    for x in range(0,ordem):
        linha = []
        for y in range(0,x+1):
            linha.append([x-y,y])
            
        coordenadas_de_cima_para_baixo.append(linha)

    coordenadas_de_baixo_para_cima = []
    for x in range(ordem-1,0,-1):
        linha = []
        contador = 0
        for y in range(ordem-1, x-1 ,-1):
                linha.append([x+contador,y])
                contador += 1
        coordenadas_de_baixo_para_cima.append(linha)
        
    coordenadas.extend(coordenadas_de_cima_para_baixo)
    coordenadas.extend(coordenadas_de_baixo_para_cima[::-1])
    return coordenadas
    
    
def buscar_diagonais(matriz):
    coordenadas = coordenadas_diagonais_matriz_quadrada(ordem=len(matriz))
    diagonais = []
    for linha in coordenadas:
        diagonal = []
        for coordenada in linha:
            diagonal.append(matriz[coordenada[0]][coordenada[1]])

        diagonais.append(diagonal)
        
    return diagonais


if __name__ == "__main__":
    matriz = [
                [ 1, 2, 3, 13],
                [ 4, 5, 6, 14],
                [ 7, 8, 9, 15],
                [10,11,12, 16],
            ]
            
    diagonais = buscar_diagonais(matriz)
    for diagonal in diagonais:
        print diagonal