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

try:
    db_connect = sqlite3.connect('ma-base.db')

    cursor = db_connect.cursor()

    cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT,
    age INTEGER
)
""")

except:
    print("Erreur survenue pendant la création")
    exit(1)

print("\nLa table est prête à l'emploi")
print("-----------------------------")

# On affiche la liste des enregistrements
cursor.execute("SELECT id, name, age FROM users")

print("\t=> table user au début")
for user in cursor:
    print(user)

# On insére un enregistrement directement
cursor.execute("INSERT INTO users(name, age) VALUES (?,?)", ("Marc", 20))
db_connect.commit()

# On affiche la liste des enregistrements
cursor.execute("SELECT id, name, age FROM users")

print("\t=> table user à la fin")
for user in cursor:
    print(user)

# On libère les ressources SQLite
cursor.close()
db_connect.close()
