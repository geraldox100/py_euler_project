from math import sqrt

def eh_divisivel_por_dois(i):
    if i == 2:
        return False
    if i % 2 == 0:
        return True

def termina_em_cinco(i):
    if i == 5:
        return False
    if i % 5 == 0:
        return True
    
def eh_divisivel_por_tres(i):
    if i == 3:
        return False
          
    numeros_em_texto = list(str(i))

    soma = 0
    for numero in numeros_em_texto:
        soma += int(numero)
    
    if soma % 3 == 0:
        return True
    else:
        return False
    
def eh_divisivel_por_outro_primo(i,primos):
    raiz_do_numero = sqrt(i)
    for primo in primos:
        if(primo > raiz_do_numero):
            break
        if i % primo == 0:
            return True
    return False



def buscar_primos(quantidade):
    i =3
    primos = [2]
    while len(primos) < quantidade:
        if not eh_divisivel_por_dois(i):
            if not termina_em_cinco(i):
                if not eh_divisivel_por_tres(i):
                    if not eh_divisivel_por_outro_primo(i,primos):
                        primos.append(i)
        i+=2
    return primos

def busca_proximo(primo):
    novo_primo = primo
    while True:
        novo_primo += 1
        
        if not eh_divisivel_por_dois(novo_primo):
            if not termina_em_cinco(novo_primo):
                if not eh_divisivel_por_tres(novo_primo):
                    primos = buscar_primos(novo_primo)
                    if not eh_divisivel_por_outro_primo(novo_primo,primos):
                        return novo_primo
        
        
        


if __name__ == "__main__":
    import time

    inicio = time.time()
    
    #primos = buscar_primos(100000)
    #for primo in primos:
    #   print primo
    
    proximo = busca_proximo(53)
    print proximo
    proximo = busca_proximo(proximo)
    print proximo
    proximo = busca_proximo(proximo)
    print proximo
        
    fim = time.time()
    
    print fim-inicio