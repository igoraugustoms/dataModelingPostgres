import psycopg2
from sql_queries import create_table_queries, drop_table_queries


def create_database():
    """
    - Creates and connects to the sparkifydb
    - Returns the connection and cursor to sparkifydb
    """
    
    # connect to default database
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create sparkify database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to sparkify database
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")
    cur = conn.cursor()
    
    return cur, conn


def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    drop_table_queries = ['DROP TABLE IF EXISTS time', 'DROP TABLE IF EXISTS artists', 'DROP TABLE IF EXISTS songs', 'DROP TABLE IF EXISTS users', 'DROP TABLE IF EXISTS songplays']
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()


def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list. 
    """
    create_table_queries = ['CREATE TABLE IF NOT EXISTS songplays (SONGPLAY_ID SERIAL PRIMARY KEY, START_TIME bigint NOT NULL, USER_ID INT NOT NULL, LEVEL VARCHAR, SONG_ID VARCHAR, ARTIST_ID VARCHAR, SESSION_ID VARCHAR, LOCATION VARCHAR, USER_AGENT VARCHAR);', 'CREATE TABLE IF NOT EXISTS users (USER_ID INT PRIMARY KEY, FIRST_NAME VARCHAR NOT NULL, LAST_NAME VARCHAR NOT NULL, GENDER VARCHAR, LEVEL VARCHAR);', 'CREATE TABLE IF NOT EXISTS songs (SONG_ID VARCHAR PRIMARY KEY, TITLE VARCHAR, ARTIST_ID VARCHAR, YEAR INT, DURATION DECIMAL);', 'CREATE TABLE IF NOT EXISTS artists (ARTIST_ID VARCHAR PRIMARY KEY, NAME VARCHAR NOT NULL, LOCATION VARCHAR, LATITUDE FLOAT, LONGITUDE FLOAT);', 'CREATE TABLE IF NOT EXISTS time (START_TIME TIMESTAMP PRIMARY KEY, HOUR INT NOT NULL, DAY VARCHAR NOT NULL, WEEK VARCHAR NOT NULL, MONTH VARCHAR NOT NULL, YEAR INT NOT NULL, WEEKDAY VARCHAR NOT NULL);']
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()


def main():
    """
    - Drops (if exists) and Creates the sparkify database. 
    
    - Establishes connection with the sparkify database and gets
    cursor to it.  
    
    - Drops all the tables.  
    
    - Creates all tables needed. 
    
    - Finally, closes the connection. 
    """
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()
    print('Tables were created')


if __name__ == "__main__":
    main()