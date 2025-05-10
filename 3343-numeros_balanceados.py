import itertools as it
class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        count = 0
        for i in set(it.permutations(num)):
            lista_par = []
            lista_impar = []
            soma_par = 0
            soma_impar = 0
            num_atual = "".join(i)
            for x in range(len(num_atual)):
                numero = int(num_atual[x])
                if x % 2 == 0:
                    lista_par.append(numero)
                else: 
                    lista_impar.append(numero)
        
            for z in lista_par: 
                soma_par = (soma_par + z)
                
            for y in lista_impar: 
                soma_impar = (soma_impar + y)
                
            if soma_par == soma_impar:
                count+=1

        return count % (10**9 + 7)
