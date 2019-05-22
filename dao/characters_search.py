from infra.db import con
from wrap_connection import transact

sql_search = "SELECT COUNT(*) FROM Characters"

@transact(con)
def totalCharacters():
    cursor.execute(sql_search)
    qtyCharacters = int(cursor.fetchone())
    
    return qtyCharacters