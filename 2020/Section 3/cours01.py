#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    Principes de base
    -----------------

    (c) Marc Augier m.augier@me.com
"""

print ("Bonjour le monde !")

a = 1  # ici un entier
b = 2. # ici un réel

c = a * b
print c

while (a<15):
    a = c*b + a
    if (a > 10):
        print ("a est plus grand que 10")
    else:
        print("a est plus petit que 10")
