#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Objets itérables
    -------------------------
    Les listes

    (c) Marc Augier m.augier@me.com

"""

def titre(t):
    print "\n"+t
    print "-"*len(t)

shopping = [ 'pommes', 'poires', 'oranges', 'ananas', 'abricots' ]

titre("Liste simple")
for fruit in shopping:
    print fruit

titre( "Liste avec enumerate")
for fruit in enumerate(shopping):
    print fruit

titre("Liste avec enumerate et indice")
for i,fruit in enumerate(shopping):
    print "Le numéro %i est %s" % (i,fruit)

liste_des_courses = sorted(shopping)

titre("Liste triée")
for item  in liste_des_courses:
    print "Le numéro %i est %s" % (i,item)
