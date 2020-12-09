# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (SONGPLAY_ID SERIAL PRIMARY KEY, START_TIME bigint NOT NULL, USER_ID INT NOT NULL, LEVEL VARCHAR, SONG_ID VARCHAR, ARTIST_ID VARCHAR, SESSION_ID VARCHAR, LOCATION VARCHAR, USER_AGENT VARCHAR);""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (USER_ID INT PRIMARY KEY, FIRST_NAME VARCHAR NOT NULL, LAST_NAME VARCHAR NOT NULL, GENDER VARCHAR, LEVEL VARCHAR);""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (SONG_ID VARCHAR PRIMARY KEY, TITLE VARCHAR, ARTIST_ID VARCHAR, YEAR INT, DURATION DECIMAL);""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (ARTIST_ID VARCHAR PRIMARY KEY, NAME VARCHAR NOT NULL, LOCATION VARCHAR, LATITUTE FLOAT, LONGITUDE FLOAT);""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (START_TIME TIMESTAMP PRIMARY KEY, HOUR TIME NOT NULL, DAY VARCHAR NOT NULL, WEEK VARCHAR NOT NULL, MONTH VARCHAR NOT NULL, YEAR INT NOT NULL, WEEKDAY VARCHAR NOT NULL);""")

# INSERT RECORDS

songplay_table_insert = ("""INSERT INTO songplays (start_time, user_id, level,song_id,artist_id,session_id,location,user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level""")

song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING""")

artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s) ON CONFLICT DO NOTHING""")


time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT DO NOTHING""")

# FIND SONGS

song_select = ("""SELECT s.song_id, a.artist_id FROM  songs s INNER JOIN artists a ON s.artist_id = a.artist_id WHERE s.title = %s AND a.name = %s AND s.duration = %s;""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]