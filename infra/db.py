import sqlite3
from wrap_connection import transact
from infra.characters import characters_list

create_sqls = """
CREATE TABLE IF NOT EXISTS Characters
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL

);"""

def con():
    return sqlite3.connect("marvel.db")

@transact(con)
def cria_db():
    cursor.execute(create_sqls)
    connection.commit()
    characters_list()
