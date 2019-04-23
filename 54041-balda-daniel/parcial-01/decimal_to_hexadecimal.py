def convert(number):
    hexadecimal = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    aux = 0
    hexasave = []
    result = ""
    if number == 0:
        result = "0"
    else:
        while number > 0:
            hexasave.append(number%16)
            number = number//16
            aux = aux + 1
        for invert in hexasave[::-1]:
            result = result + hexadecimal[invert]
    return result