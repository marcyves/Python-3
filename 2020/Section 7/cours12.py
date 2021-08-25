#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Les bibliothèques
    -----------------

    (c) Marc Augier m.augier@me.com

"""
import os # Bibliothèque nécessaire pour utiliser les fonctions de lecture du système de fichier
import this

# Il y a 3 différentes manières d'importer des fonctions depuis un module
# Utilisez les commentaires pour choisi un style parmi les trois

import math
# import math as M
# from math import sqrt, pi

# ----------------------------------------------------------
# Bien que ce soit syntaxiquement valide, on ne fera JAMAIS:
from math import *
# parce que ce n'est pas Pythonesque !
# ----------------------------------------------------------

# Style 1
print math.sqrt(2)

# Style 2
# print M.sqrt(2)

Style 3
# print sqrt(2)
# print pi
