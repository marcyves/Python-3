#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    Les opérateurs de comparaison
    -------------------------------------------------
    <  Strictement inférieur à
    > Strictement supérieur à
    <= Inférieur ou égal à
    >= Supérieur ou égal à
    == Égal à                     Attention! il y a bien 2 signes '='
    != Différent de

    (c) Marc Augier m.augier@me.com
"""

def calculPerimetre1(Rayon):
    if (Rayon < 0):
        print "Erreur Rayon négatif"
        perimetre = 0
    else:
        pi = 3.14159
        perimetre = 2 * pi * Rayon
    return perimetre

def calculPerimetre2(Rayon):
    if (Rayon < 0):
        return False
    else:
        pi = 3.14159
        perimetre = 2 * pi * Rayon
    return perimetre

msg = "Calcul géométrique"
P = True

print msg
R = input('Rayon SVP ==> ')

# C'est beau à voir mais une très mauvaise idée pour les performances
# On appelle 2 fois la même fonction avec les mêmes paramètres...
#
if calculPerimetre2(R):
    print "le périmètre d'un cercle de Rayon %i est %i" %(R, calculPerimetre2(R))
else:
    print "Erreur Rayon négatif"
