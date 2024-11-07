from math import sqrt

#### Fonction secondaire


def isprime(p):
    """
    "renvoit true si le nombre est premier
    """
    premier = True
    if x <=1:
        return False
    for i in range(2,int(sqrt(x))+1):
        if x % i == 0:
            premier = False
            break
    return premier
    pass

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
