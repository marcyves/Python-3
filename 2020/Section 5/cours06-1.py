#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    Les itérations avec WHILE
    -------------------------

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

P = True
while P:
    R = input('Rayon SVP ==> ')
    P = calculPerimetre(R)
    if P:
        print "Le périmètre est : %s " % calculPerimetre(R)
print "Au revoir"
