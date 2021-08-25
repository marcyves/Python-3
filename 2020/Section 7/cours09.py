#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Objets itérables
    -------------------------
    Les dictionnaires

    (c) Marc Augier m.augier@me.com

"""

def titre(t):
    print "\n"+t
    print "-"*len(t)

agenda = { 'Gérard':'010101', 'Sophie':'020202', 'Jules':'030303', 'Anne':'040404' }

titre("Le contenu du dictionnaire")
for nom in agenda:
    print nom + " : " + agenda[nom]

titre("Le contenu du dictionnaire avec la methode keys()")
for nom in agenda.keys():
    print nom + " : " + agenda[nom]

titre("Recherche d'une valeur dans un dictionnaire")
if '030303' in agenda.values():
    print "Un numéro est 030303"

if '050505' in agenda.values():
    print "Un numéro est 050505"
else:
    print "Pas de 050505"
