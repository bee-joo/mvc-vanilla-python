import sqlite3
from sqlite3 import Error

class DB():

    def __init__(self, path):
        self.conn = sqlite3.connect(path)
        self.cursor = self.conn.cursor()
    
    def create(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS data 
                        (id integer PRIMARY KEY, first_name text, last_name text, email text, city text, mail_index integer, address text)
                        """)
            
        self.conn.commit()

    def input_data(self, obj):
        entity = (obj.first_name, obj.last_name, obj.email, obj.city, obj.index, obj.address)
        self.cursor.execute("""INSERT INTO data(first_name, last_name, email, city, mail_index, address)
                       VALUES(?, ?, ?, ?, ?, ?) 
                       """, entity)

        self.conn.commit()
        id = self.cursor.lastrowid
        
        return id

    def get_by_id(self, id):
        res = self.cursor.execute("SELECT * FROM data WHERE id = ?", (id,)).fetchone()
        return res

    def get_all(self):
        res = self.cursor.execute("SELECT * FROM data").fetchall()
        return res


class Client():

    def __init__(self, first_name, last_name, email, city, index, address):
        self.__client = {"first_name": first_name, "last_name": last_name, "email": email, "city": city, "index": index, "address": address}

    def __str__(self):
        return f'{str(self.__client.get("first_name"))}'

    @property
    def full_name(self):
        return f"{self.__client.get('first_name')} {self.__client.get('last_name')}"

    @property
    def first_name(self):
        return f"{self.__client.get('first_name')}"

    @property
    def last_name(self):
        return f"{self.__client.get('last_name')}"

    @property
    def email(self):
        return f"{self.__client.get('email')}"

    @property
    def city(self):
        return f"{self.__client.get('city')}"

    @property
    def index(self):
        return int(self.__client.get('index'))

    @property
    def address(self):
        return f"{self.__client.get('address')}"