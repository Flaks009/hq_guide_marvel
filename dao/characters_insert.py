from infra.db import con
from wrap_connection import transact

sql_insert = "INSERT INTO Characters (name) VALUES (?)"

@transact(con)
def insertCharacters(characterName):
    cursor.execute(sql_insert, (characterName, ))
    cursor.commit()