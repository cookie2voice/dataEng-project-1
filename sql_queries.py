# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""
    CREATE TABLE songplays (
        songplay_id serial PRIMARY KEY,
        start_time bigint NOT NULL,
        user_id integer REFERENCES users (user_id) NOT NULL,
        level varchar,
        song_id text,
        artist_id text REFERENCES artists (artist_id),
        session_id integer,
        location varchar,
        user_agent varchar
    );
""")

user_table_create = ("""
    CREATE TABLE users (
        user_id integer PRIMARY KEY,
        first_name varchar,
        last_name varchar,
        gender varchar,
        level varchar
    );
""")

song_table_create = ("""
    CREATE TABLE songs (
        id serial PRIMARY KEY,
        song_id text,
        title text NOT NULL,
        year integer,
        duration float NOT NULL,
        artist_id text
    );
""")

artist_table_create = ("""
    CREATE TABLE artists (
        artist_id text PRIMARY KEY,
        name text NOT NULL,
        location text,
        latitude float,
        longitude float
    );
""")

time_table_create = ("""
    CREATE TABLE time (
        start_time timestamp PRIMARY KEY,
        hour integer,
        day integer,
        week integer,
        month integer,
        year integer,
        weekday integer
    );
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO songplays (start_time, user_id, level, 
    song_id, artist_id, session_id, location, user_agent)
    values (%s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (songplay_id)
    DO NOTHING
""")

user_table_insert = ("""
    INSERT INTO users (user_id, first_name, last_name, gender, level)
    values (%s, %s, %s, %s, %s)
    ON CONFLICT (user_id)
    DO UPDATE SET level = EXCLUDED.level
""")

song_table_insert = ("""
    INSERT INTO songs (song_id, title, artist_id, year, duration)
    values (%s, %s, %s, %s, %s)
    ON CONFLICT (id)
    DO NOTHING
""")

artist_table_insert = ("""
    INSERT INTO artists (artist_id, name, location, latitude, longitude) 
    values (%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id)
    DO UPDATE SET location = EXCLUDED.location,
                   latitude = EXCLUDED.latitude,
                   longitude = EXCLUDED.longitude
""")


time_table_insert = ("""
    INSERT INTO time (start_time, hour, day, week, month, year, weekday)
    values (TO_TIMESTAMP(%s::DOUBLE PRECISION/1000), %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time)
    DO NOTHING
""")

# FIND SONGS

song_select = ("""
    SELECT s.song_id, a.artist_id
    FROM songs s
    JOIN artists a 
    USING (artist_id)
    WHERE s.title=%s
        AND a.name=%s
        AND s.duration=%s
""")

# QUERY LISTS

create_table_queries = [artist_table_create, user_table_create, song_table_create,  time_table_create,  songplay_table_create]
drop_table_queries = [songplay_table_drop, song_table_drop, artist_table_drop, time_table_drop]