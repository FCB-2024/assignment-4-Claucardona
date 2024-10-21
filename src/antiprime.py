## ADD WHATEVER ARGUMENTS ARE NECESSARY TO THE MAIN FUNCTION
## IN THE SAME ORDER AS THE ARGUMENTS ARE TAKEN FROM THE
## COMMAND LINE SPECIFIED BELOW
def main():
    x = int(input("Enter a positive integer number: "))
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
            print("not anti-prime")
            return "not anti-prime"
        d = d + 1
    print("anti-prime")
    ## THE LAST LINES OF YOUR CODE SHOULD EITHER
	## RETURN THE VALUE "anti-prime" or "not anti-prime"
	## REPLACE THE FOLLOWING LINE BY WHATEVER LINES
	## OF CODE ALLOW THIS FUNCTION TO RETURN THE VALUE
	## "anti-prime" or "not anti-prime"
    return "anti-prime"
# DO NOT REMOVE THIS LINE BELOW
if __name__ == "__main__":
	## MODIFY THE LINE BELOW AND ADD BEFORE WHATEVER LINES ARE NECESSARY
	## TO RUN THIS PROGRAM AS, FOR INSTANCE:
	## $ python antiprime.py 6
	## WHERE THE FIRST ARGUMENT IS A POSITIVE INTEGER NUMBER FOR WHICH
	## YOU WANT TO FIGURE OUT WHETHER IS ANTI-PRIME OR NOT
    print(main())