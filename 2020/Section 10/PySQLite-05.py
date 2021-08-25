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
print("\t=> Table users avant les INSERT")
cursor.execute("SELECT id, name, age FROM users")
for user in cursor:
    print(user)

# On insére un enregistrement directement
cursor.execute("""INSERT INTO users(name, age) VALUES(?, ?)""", ("Olivier", 30))

print("\t=> Table users après 1")
cursor.execute("SELECT id, name ,age FROM users ORDER BY id")
for user in cursor:
    print(user)


# On Insére un enregistrement à partir d'une liste
data = {"name" : "Pierre", "age" : 40}
cursor.execute("""INSERT INTO users(name, age) VALUES(:name, :age)""", data)

print("\t=> Table users après 2")
cursor.execute("SELECT id, name ,age FROM users ORDER BY id")
for user in cursor:
    print(user)

# On insere plusieurs enregistrements à partir d'un tableau
users = []
users.append(("Laurent", 35))
users.append(("Sabine", 20))
cursor.executemany("""
INSERT INTO users(name, age) VALUES(?, ?)""", users)

print("\t=> Table users après 3")
cursor.execute("SELECT id, name ,age FROM users ORDER BY id")
for user in cursor:
    print(user)

# On valide l'écriture définitive de tous les enregistrements précédents
db_connect.commit()

# On libère les ressources SQLite
cursor.close()
db_connect.close()
