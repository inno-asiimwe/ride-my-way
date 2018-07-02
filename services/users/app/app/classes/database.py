import psycopg2


class db:
    """ Class handles all database operations """
    def __init__(self, name, host, user, password):
        self.name = name
        self.host = host
        self.user = user
        self.password = password

    def connect(self):
        conn = psycopg2.connect(host=self.host, dbname=self.name,
                                user=self.user, password=self.password)
        return conn

    def get_all
