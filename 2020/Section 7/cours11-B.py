#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Gestion des fichiers
    -------------------------

    (c) Marc Augier m.augier@me.com

"""
# Bibliothèque nécessaire pour utiliser les fonctions de lecture du système de fichier
import os

racine = "/Users/marc/Documents/UDEMY/Online"

for root, subdirs, files in os.walk(racine):
    print('--\nVoici la liste des dossiers contenus dans = ' + root)
    for subdir in subdirs:
        print('\t- sous dossier = ' + subdir)

    print ("Voici la liste des fichiers")
    for filename in files:
        file_path = os.path.join(root, filename)
        # On ne s'occupe pas de ce fichier caché sur Mac
        if (filename != '.DS_Store'):
            # On affiche le contenu d'un fichier particulier
            if (filename == "cours10.py"):
                fi = open(filename,"r")
                contenu = fi.read()
                print contenu
            else:
                print('\t- fichier  %s (chemin : %s)' % (filename.decode('utf-8'), file_path.decode('utf-8')))
