#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Récursivité
    -------------
    Calcul de factorielle

    N! = N * (N-1)!
    0! =1

    (c) Marc Augier m.augier@me.com

"""

def factorielle(n):
    if n < 0 :
        print "Uniquement un nombre positif"
    elif n == 0 :
        return 1
    else:
        f = n * factorielle(n-1)
        return f

print factorielle(2)

print factorielle(5)

print factorielle(127)
