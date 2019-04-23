from decimal_to_hexadecimal import convert

def main():
    number = input("Ingrese un numero entero :")
    print(esnumero(number))

def esnumero(number):
    try:
        x = int(number)
        return convert(x)
    except:
        return "Debe ingresar un numero entero"
main()