import sqlite3
from wrap_connection import transact

sql_search = "SELECT COUNT(*) FROM Characters"
sql_compare = "SELECT name FROM Characters WHERE INSTR(UPPER(name), UPPER(?)) >= 1"
sql_insert = "INSERT INTO Characters (name) VALUES (?)"
sql_delete = "DELETE FROM Characters"


def totalCharacters():

    try:
        connection = sqlite3.connect("marvel.db")
        cursor = connection.cursor()
        cursor.execute(sql_search)
        qtyCharacters = cursor.fetchone()
        qtyCharacters = int(qtyCharacters[0])
        connection.commit()
        cursor.close()
        connection.close()

        return qtyCharacters

    except Exception:
    
        return 0

def insertCharacters(characterName):
    connection = sqlite3.connect("marvel.db")
    cursor = connection.cursor()
    cursor.execute(sql_insert, (characterName, ))
    connection.commit()
    cursor.close()
    connection.close()

def searchCharacters(stringToCompare):
    connection = sqlite3.connect("marvel.db")
    cursor = connection.cursor()
    cursor.execute(sql_compare, (stringToCompare, ))
    nameCharacters = []
    
    for name in cursor.fetchall():
        nameCharacters.append(name)

    connection.commit()
    cursor.close()
    connection.close()

    return nameCharacters

def truncateCharacters():
    connection = sqlite3.connect("marvel.db")
    cursor = connection.cursor()
    cursor.execute(sql_delete)
    connection.commit()
    cursor.close()
    connection.close()
