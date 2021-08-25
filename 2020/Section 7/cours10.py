#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Traitement des exceptions
    -------------------------

    (c) Marc Augier m.augier@me.com

"""

x = 120
y = 0
try:
    z = x / y
    z = a
except:
    print "Il y a une erreur, laquelle ?"


try:
    z = x / y
#    z = a
except ZeroDivisionError:
    print "Il y a une erreur de division par zero"
    z = x
except NameError, Argument:
    print "une variable n'existe pas : ", Argument
    z = 0
else:
    print "nous avons calulé la valeur de z"+str(z)
# cours normal des choses
print "x et y valent %i,%i" % (x, y)
print "après le bloc de traitement nous avons z = "+str(z)
