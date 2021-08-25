#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    Les itérations avec FOR
    -----------------------

    (c) Marc Augier m.augier@me.com
"""

def calculPerimetre(Rayon):
    if Rayon < 0:
        print "ERREUR : Le rayon doit etre positif"
        return False
    else:
        pi = 3.14159
        perimetre = 2 * pi * Rayon
    return perimetre

msg = "Calcul géométrique"


print msg

Rayons = [ 10, 20, 30, 40, 50]

for R in Rayons:
    print calculPerimetre(R)
