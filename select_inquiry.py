import sqlalchemy
def show_me(database):
    engine = sqlalchemy.create_engine(database)
    connection = engine.connect()
    albums_2018 = f'Название и год выхода альбомов, вышедших в 2018 году - {connection.execute(f"select album_name, album_year from albums a where album_year = 2018;").fetchall()}'
    name_and_max_timing_track = f'название и продолжительность самого длительного трека - {connection.execute(f"select track_name, timing from tracks where timing = (select max(timing) from tracks);").fetchall()}'
    name_and_timing_track = f'название треков, продолжительность которых не менее 3,5 минуты - {connection.execute(f"select timing, track_name from tracks where timing < 3.5;").fetchall()}'
    collection_name_2018_2020 = f'названия сборников, вышедших в период с 2018 по 2020 год включительно - {connection.execute(f"select album_name, album_year from albums a where album_year between 2018 and 2020;").fetchall()}'
    my_track = 'название треков, которые содержат слово "мой"/"my"' + str(connection.execute(f"select track_name from tracks where track_name like '%%My%%';").fetchall())
    one_word_artist = f'исполнители, чье имя состоит из 1 слова - {artist_search(connection.execute(f"SELECT * FROM artists").fetchall())}'
    one_word_artist_var2= connection.execute(f"select artist_name from artists where artist_name not like '%% %%';").fetchall()
    return albums_2018, name_and_max_timing_track, name_and_timing_track, collection_name_2018_2020, my_track, one_word_artist, one_word_artist_var2

def artist_search(artists):
    artists_list = []
    for name in artists:
        if len(name[1].split()) == 1:
            artists_list.append(name[1])

    return artists_list






