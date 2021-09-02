#! /usr/bin/python

"""
    Suite de Fibonacci
    ------------------
    (c) Marc Augier 2021

    Ce programme calcule la suite de Fibonacci 
    qui se définit de la façon suivante

    U(0) = 0
    U(1) = 1

    Si n>2 U(n+1) = U(n) + U(n-1)

    Démonstration de code récursif, avec entrée au clavier de l'entier
    à utiliser pour le calcul.

    Attention à ne pas être trop gourmand !
    
"""

def fibonacci(n):
    if n<=1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("\n\tLa suite de Fibonacci")
print("\t" + "="*21 + '\n\n')

n = -1
while(n<0):
    n = int(input("Entrez un nombre entier positif ==> "))

print(f'Fibonacci({n}) = {fibonacci(n)}')