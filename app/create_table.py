from app.models import DatabaseConnector




def create_table_if_not_exists():


    conn_obj = DatabaseConnector()
    conn_obj.get_conn_cur()

    query_create_table = """
    CREATE TABLE IF NOT EXISTS 
    ka_series(
        id        BIGSERIAL     PRIMARY KEY,
        serie     VARCHAR(100)  UNIQUE NOT NULL,
        seasons   INTEGER       NOT NULL,
        released_date DATE      NOT NULL,
        genre     VARCHAR(50)   NOT NULL,
        Imdb_rating FLOAT       NOT NULL
    );
    """

    conn_obj.cur.execute(query_create_table)

    conn_obj.commit_and_close()


