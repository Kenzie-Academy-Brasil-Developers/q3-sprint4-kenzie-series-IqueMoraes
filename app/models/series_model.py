from platform import release
from app.models import DatabaseConnector
from typing import Literal, Union
from psycopg2 import sql




class Series(DatabaseConnector):

    series_table_keys = ["id", "serie", "seasons", "released_date", "genre", "imdb_rating"]

    def __init__(self, *args, **kwargs) -> None:
        self.serie = kwargs['serie'].title()
        self.seasons = kwargs['seasons']
        self.released_date = kwargs['released_date']
        self.genre = kwargs['genre'].title()
        self.imdb_rating = kwargs['imdb_rating']


    def create_series(self) -> tuple:
        self.get_conn_cur()
        print(self.conn, self.cur)

        query = sql.SQL(""" 
        INSERT INTO
            ka_series (serie, seasons, released_date, genre, imdb_rating)
        VALUES
            ({serie}, {seasons}, {released_date}, {genre}, {imdb_rating})
        RETURNING *;
        """).format(
            serie = sql.Literal(self.serie),
            seasons = sql.Literal(self.seasons),
            released_date = sql.Literal(self.released_date),
            genre = sql.Literal(self.genre),
            imdb_rating = sql.Literal(self.imdb_rating)
        )

        y = self.cur.execute("SELECT 2*2 soma;")
        print("=" *100)
        print(y)
        print("=" *100)
        self.cur.execute(query)
        
        created_serie = self.cur.fetchone()

        self.commit_and_close()

        return created_serie



    @staticmethod
    def serialize_series(data, keys: list = series_table_keys) -> Union[dict, list]:

        if type(data) is tuple:
            return dict(zip(keys, data))

        elif type(data) is list:
            return [dict(zip(keys, serie)) for serie in data]



    @classmethod
    def get_serie_data(cls, id: int = None):
        cls.get_conn_cur()

        query = " SELECT * FROM ka_series"

        if id:
            where = "WHERE id = %s"%id
            cls.cur.execute(' '.join([query, where, ';']))
            serie_db= cls.cur.fetchone()

        else:
            cls.cur.execute(''.join([query, ";"]))
            serie_db = cls.cur.fetchall()

        cls.commit_and_close()

        return serie_db

    

    

        

        