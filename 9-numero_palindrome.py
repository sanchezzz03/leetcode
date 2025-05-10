def isPalindrome(x: int) -> bool:
    if x < 0:
        return False  # negativos não são palíndromos

    y = str(x)
    contrario_y = y[::-1]

    if y == contrario_y:
        return(True)
    else:
        return(False)


result = isPalindrome(12231)
print(result)