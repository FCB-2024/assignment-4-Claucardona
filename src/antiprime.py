## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
import sys

def es_antiprimo(x):
## YOUR CODE SHOULD START HERE AT THE SAME
## INDENTATION AS THIS COMMENT
    r = 1
    d = 1
    k = 1
    i = 0
    n = 0
    while r <= x:
        if x % r == 0:
            n = n + 1
        r = r + 1
    while d < x:
        k = 1
        i = 0
        while k <= d:
            if d % k == 0:
                i = i + 1
            k = k + 1
        if i >= n:
            return "not anti-prime"
        d = d + 1
    return "anti-prime"

def main():
    # Verificar si hay un argumento proporcionado en la línea de comandos
    if len(sys.argv) != 2:
        print("Uso: python programa.py <numero>")
        return

    try:
        x = int(sys.argv[1])
        if x <= 0:
            print("Por favor, ingrese un número entero positivo.")
            return
    except ValueError:
        print("Por favor, ingrese un número entero válido.")
        return
## THE LAST LINES OF YOUR CODE SHOULD EITHER
    ## PRINT THE SENTENCE "friends" or "not friends"
    ## REPLACE THE FOLLOWING LINE BY WHATEVER LINES
    ## OF CODE END UP WRITING "friends" or "not friends"
    ##print("not friends")
## DO NOT REMOVE THESE LINES
    resultado = es_antiprimo(x)
    print(resultado)

if __name__ == "__main__":
    main()
