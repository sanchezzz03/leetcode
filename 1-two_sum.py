target = 6
nums = [3,2,3]

def calcular(nums, target):
    # aqui salvamos o valor1 como o contador para que seja somado com todos os outros
    for i in range(len(nums)):
        valor1 = nums[i]
        # aqui começamos somamos com todos numeros que ainda não foram o valor1 (se for menor ou igual ele passa adiante)
        for c in range(len(nums)):
            if c <= i:
                continue
            else:
                # aqui dizemos que o valor 2 é o valor da lista com o indice c
                valor2 = nums[c]
                soma = valor1 + valor2
                if soma == target:
                    resp = [i, c]
                    return resp
                    break
                else:
                    # se a soma não for igual, ele zera o resultado e volta ao contador do valor 2 para tentar com o outro valor
                    soma = 0

result=calcular(nums, target)
print(f'{result}')