import sqlite3

import mysql.connector as mySql


class Artist:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"({self.id},{self.name})"

    def __repr__(self):
        return self.__str__()
class ArtistsDAO:
    def insert_artist(conn, artist:Artist):
        with mySql.connect(
            host="localhost",
            user="root",
            password="root",
            database="chinook"
        ) as conn:
            cursor = conn.cursor()
            # cursor.execute("INSERT INTO Artist VALUES (276,'Djamala');")
            # cursor.execute(f"INSERT INTO Artist VALUES (?,?)",(artist.id,f'{artist.name}'))
            cursor.execute(f"INSERT INTO Artist VALUES (:id,:name)",{
                                                                    "id":artist.id,
                                                                  "name":f'{artist.name}'}
                           )
            conn.commit()


    def update_artist(conn, artist:Artist):
        with mySql.connect(
                host="localhost",
                user="root",
                password="root",
                database="chinook"
        ) as conn:
            cursor = conn.cursor()
            # cursor.execute("UPDATE Artist SET Name = 'TNMK' WHERE ArtistId = 276;")
            cursor.execute(f"UPDATE Artist SET Name = '{artist.name}' WHERE ArtistId = {artist.id};")
            conn.commit()

    def delete_artist(conn, artist:Artist):
        with mySql.connect(
                host="localhost",
                user="root",
                password="root",
                database="chinook"
        ) as conn:
            cursor = conn.cursor()
            # cursor.execute("DELETE FROM Artist WHERE ArtistId = 276;")
            cursor.execute(f"DELETE FROM Artist WHERE ArtistId = {artist.id}")
            conn.commit()

    def read_artists(conn):
        with mySql.connect(
                host="localhost",
                user="root",
                password="root",
                database="chinook"
        ) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Artist")
            results = cursor.fetchall()
            artists = []
            for entry in results:
                artists.append(
                    Artist(id=entry[0], name=entry[1])
                )
            return artists

if __name__ == '__main__':
 #   conn = sqlite3.connect("Chinook_Sqlite.sqlite")
    ArtistsDAO.delete_artist(Artist(276,"Kazka"))
    id = int(input("id ="))
    name = input("name =")
    ArtistsDAO.insert_artist(Artist(id,name))
    artists = ArtistsDAO.read_artists()
    print(artists)

