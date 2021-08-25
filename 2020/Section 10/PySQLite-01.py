#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""

    SQLite Principes de base
    ------------------------

    (c) Marc Augier m.augier@me.com
"""

import sqlite3

print("\n\t+--------------+")
print("\t| Test SQLite3 |")
print("\t+--------------+")

# On se connecte à la base de donnée de travail, qui sera créée si elle n'existe pas
db_connect = sqlite3.connect('base-marc.db')

# Pointeur sur la base de données
cursor = db_connect.cursor()

# Requête SQL de création de la table
cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT,
    age INTEGER
)
""")
