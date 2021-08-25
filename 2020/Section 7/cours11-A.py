#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Gestion des fichiers
    -------------------------

    (c) Marc Augier m.augier@me.com

"""

# Création et écriture d'un fichier
# Ouverture en mode a pour append, ajouter
# Vous pouvez essayer de voir la différence avec le mode w pour write, écrire
fi = open("mon_fichier.txt","a")

# On écrit dans le fichier
fi.write("Une ligne et son retour chariot final\n")
fi.write("Une ligne avec \tune tabulation\n")

# On ferme le fichier
fi.close()

# on ouvre le ficher en mode r read, lecture
fi = open("mon_fichier.txt","r")
# On lit et on affiche le contenu
fichier = fi.read()
print fichier
