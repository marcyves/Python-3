#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Programmation Orienté Objet
# Les classes

"""
    Programmation Orienté Objet
    ---------------------------
    Les classes
    Instanciation et méthodes

    (c) Marc Augier m.augier@me.com

"""

class contact():
    """
    Classe permettant de représenter un contact
    """
    def __init__(self, nom, prenom, telephone):
        self.nom       = nom
        self.prenom    = prenom
        self.telephone = telephone

    def quelNumero(self):
        return self.telephone

    def modifierNumero(self, tel):
        self.telephone = tel

    def quelNom(self):
        return self.nom

    def quelPrenom(self):
        return self.prenom

# Ici commence le code principal

Marc = contact("Marc","Augier","0102030405")
Sophie = contact("Sophie","Telle","0611111111")

# Accès direct aux variables
print "Le numéro du contact %s est : %s" % (Marc.nom, Marc.telephone)

Marc.modifierNumero("1111111111")

# En utilisant une methode
print "Le numéro du contact %s est : %s" % (Marc.quelNom(), Marc.quelNumero())
