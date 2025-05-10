def reverse(x: int) -> int:
    if x < 0:
        res = -int(str(-x)[::-1])
    else:
        res = int(str(x)[::-1])

    # verificação do tamanho do número
    if res < -2**31 or res > 2**31 - 1:
        return 0
    return res

result = reverse(123)
print(result)