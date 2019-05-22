from infra.db import con
from wrap_connection import transact

sql_compare = "SELECT name FROM Characters WHERE INSTR(?, name) >= 1"

@transact(con)
def totalCharacters(stringToCompare):
    
    cursor.execute(sql_compare, (stringToCompare, ))
    nameCharacters = []
    
    for name in cursor.fetchall():
        nameCharacters.append(name)

    return nameCharacters