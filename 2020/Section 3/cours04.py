#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Les fonctions
    -------------

    (c) Marc Augier m.augier@me.com

"""

def calculPerimetre(Rayon):
    pi = 3.14159
    perimetre = 2 * pi * Rayon
    return perimetre


msg = "Calcul géométrique"


print msg
R = input('Rayon SVP ==> ')
print calculPerimetre(R)
