from math import sqrt
import itertools

class Primos:
    __lista = []
    
    @staticmethod
    def __buscar_numero_na_lista(numero):
        return Primos.__lista[numero]
    
    @staticmethod
    def __inicializar_lista(numeros):
        Primos.__lista = numeros
        
    @staticmethod
    def __adicionar_primo_na_lista(primo):
        Primos.__lista.append(primo)
        
    @staticmethod
    def __montar_objeto_primo(posicao):
        return Primo(
                     numero=Primos.__buscar_numero_na_lista(posicao-1),
                     posicao=posicao,
                     proximo=Primos.__buscar_numero_na_lista(posicao),
                     anterior=Primos.__buscar_numero_na_lista(posicao-2)
                     )
    
    @staticmethod
    def __eh_divisivel_por_dois(i):
        if i == 2:
            return False
        if i % 2 == 0:
            return True
        
    @staticmethod
    def __termina_em_cinco(i):
        if i == 5:
            return False
        if i % 5 == 0:
            return True
    
    @staticmethod    
    def __eh_divisivel_por_tres(i):
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
    
    @staticmethod    
    def __eh_divisivel_por_outro_primo(i):
        raiz_do_numero = sqrt(i)
        for primo in Primos.__lista:
            if(primo > raiz_do_numero):
                break
            if i % primo == 0:
                return True
        return False
    
    @staticmethod
    def quantidade_de_primos():
        return len(Primos.__lista)
    
    @staticmethod
    def buscar_primo_numero(posicao):
        if Primos.quantidade_de_primos() <= posicao:
            Primos.carregar_primos_ate_a_posicao(posicao+10)
        return Primos.__montar_objeto_primo(posicao)
    
    @staticmethod
    def carregar_primos_ate_o_numero(numero):
        if Primos.quantidade_de_primos() == 0:
            Primos.carregar_primos_ate_a_posicao(100)
            
        while not any(primo >= numero for primo in Primos.__lista):
            Primos.carregar_primos_ate_a_posicao(len(Primos.__lista)+100)
    
    @staticmethod
    def carregar_primos_ate_a_posicao(posicao):
        
        if Primos.quantidade_de_primos() > 0:
            i = Primos.__buscar_numero_na_lista(-1)
        else:
            i = 3
            Primos.__inicializar_lista([2])
            
            
        while Primos.quantidade_de_primos() < posicao:
            if Primos.eh_primo(i):
                if not i in Primos.__lista:
                    Primos.__adicionar_primo_na_lista(i)
            i+=2
    
    @staticmethod        
    def buscar_primos_ate(numero):
        
        Primos.carregar_primos_ate_o_numero(numero)
        
        retorno = [ list(x[1]) for x in itertools.groupby(Primos.__lista, lambda x: x > numero) if not x[0] ]
        if retorno:
            return retorno[0]
        return []
         
            
    @staticmethod
    def eh_primo(numero):
        if not Primos.__eh_divisivel_por_dois(numero):
            if not Primos.__termina_em_cinco(numero):
                if not Primos.__eh_divisivel_por_tres(numero):
                    if not Primos.__eh_divisivel_por_outro_primo(numero):
                        return True
        return False


class Primo:

    def __init__(self,numero,proximo,anterior,posicao):
        self.__numero = numero
        self.__proximo = proximo
        if self.__numero == 2:
            self.__anterior = 0
        else:
            self.__anterior = anterior
        self.__posicao = posicao
        
    def numero(self):
        return self.__numero
     
    def proximo(self):
        return Primos.buscar_primo_numero(self.__posicao+1)
     
    def anterior(self):
        return Primos.buscar_primo_numero(self.__posicao-1)
     
    def posicao(self):
        return self.__posicao
    
    def __str__(self):
        return str(self.__numero)   
    
    def __repr__(self):
        return self.__str__()
    


def imprime_primo(primo):
    print "numero",primo.numero()
    print "proximo",primo.proximo()
    print "anterior",primo.anterior()
    print "posicao",primo.posicao()
    
if __name__ == '__main__':
    from time import time
    quantidade = 1000
    
    start_time = time()
    primo = Primos.buscar_primo_numero(quantidade)
    imprime_primo(primo)
    print time() - start_time, "seconds"
    
    print
    
    
    start_time = time()             
    primo = Primos.buscar_primo_numero(quantidade*2)
    imprime_primo(primo)
    print time() - start_time, "seconds"
    
    print
    
    start_time = time()             
    primo = Primos.buscar_primo_numero(quantidade*3)
    imprime_primo(primo)
    print time() - start_time, "seconds"
    
    print
    primos = Primos.buscar_primo_ate(11);
    print primos