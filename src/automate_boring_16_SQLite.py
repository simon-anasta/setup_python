# Notes made during chapter 16 of Automate the Boring Stuff With Python
# 2025-12-04

# %% Connect to, or create, an SQLite database --------------------------------

import sqlite3
conn = sqlite3.connect('example.db', isolation_level = None)
# SQLite databases are stored in a single file
# isolation_level = None means database will autocommit
#  so we don't have to call `commit()` after each `execute()`

# %% create tables ------------------------------------------------------------

query = """
CREATE TABLE IF NOT EXISTS my_table (
    name TEXT NOT NULL,
    birthdate TEXT,
    hats_owned INT,
    height_m REAL,
    picture BLOB
) STRICT
"""
# blob is binary large object
# useful for storing entire files in the db
# 
# SQLite does not have a date type >> use TEXT
# nor does it have a boolean type >> use INT

# strict means data types are enforced
# otherise they are just cooerced if possible

conn.execute(query)

# %% check contents -----------------------------------------------------------

query = """
SELECT name
FROM sqlite_schema
WHERE type = 'table'
"""

conn.execute(query).fetchall()
# need `fetchall` to get results back
# otherwise just a cursor

query = """
PRAGMA TABLE_INFO(my_table)
"""
conn.execute(query).fetchall()
# column position
# column name
# data type
# NOT NULL
# default value
# is primary key

# %% CRUD = create read update delete -----------------------------------------

# create
query = """
INSERT INTO my_table VALUES
('me', '2020-02-02', 4, 1.221, NULL),
('you', '2020-10-20', 0, 1.223, NULL)
"""
conn.execute(query)

# read
query = """
SELECT rowid, *
FROM my_table
"""
conn.execute(query).fetchall()
# `*` means 'all columns except rowid'

# read into loop
for row in conn.execute(query):
    print('Row data: ', row)

# updating
query = """
UPDATE my_table
SET name = 'I'
WHERE name = 'me'
"""
conn.execute(query)

# delete
query = """
DELETE FROM my_table
WHERE rowid = 1
"""
conn.execute(query)

# also work:
# ALTER TABLE
# DROP TABLE

# %% protecting against injection ---------------------------------------------

# `?` are populated by execute after checking for injection
conn.execute(
    'SELECT ? FROM my_table WHERE name = ?',
    ['birthdate', 'me']
).fetchall()

# %% indexes ------------------------------------------------------------------

add_query = """
CREATE INDEX index_name on my_table (column)
"""
check_query = """
SELECT name
FROM sqlite_schema
WHERE type = 'index'
AND tbl_ame = 'my_table'
"""
remove_query = """
DROP INDEX index_name
"""
# index names must be globally unique
# so index_{table}_{columns} is a good format

# %% transactions -------------------------------------------------------------

conn.execute('BEGIN') # starts a transaction
conn.rollback() # undo the transaction
conn.commit() # keep the transaction

# %% backup active database ---------------------------------------------------
# is currently open, can not just copy the file

backup_con = sqlite3.connect('backup.db', isolation_level = None)
conn.backup(backup_con)

# %% in memory database -------------------------------------------------------
# fast but all lost if crashes

memory_db_conn = sqlite3.connect(':memory:', isolation_level = None)
# then use backup to copy into database

# wise setup
try:
    # some db commands that could error
    pass
except:
    backup_con = sqlite3.connect('backup.db', isolation_level = None)
    memory_db_conn.backup(backup_con)

# %% backup to source code ----------------------------------------------------

with open('db-queries.txt', 'w', encoding='utf-8') as fileObj:
    for line in conn.iterdump():
        fileObj.write(line + '\n')
# write to text file commands to recreate database

# %% end ----------------------------------------------------------------------

conn.close()
# will also run automaticly at the end of the script
