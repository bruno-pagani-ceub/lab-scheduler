import time

import mysql.connector
from mysql.connector import Error

CONNECTION_RETRIES = 10


class SQL:
    def __init__(
        self,
        host: str,
        user: str,
        password: str,
        database: str,
        port: int,
    ):
        self.conn = self.connect(host, user, password, database, port)

    def connect(self, host, user, password, database, port):
        retry_count = 0
        while True:
            try:
                conn = mysql.connector.connect(
                    host=host,
                    port=port,
                    user=user,
                    password=password,
                    database=database,
                )
                if conn.is_connected():
                    print("Connected to MySQL database")
                    return conn
            except Error as err:
                if retry_count >= CONNECTION_RETRIES:
                    print(f"Error connecting to MySQL: {err}")
                    exit(1)
                print(
                    f"Attempt {retry_count + 1}: Unable to connect, retrying in 2 seconds..."
                )
                time.sleep(2)
                retry_count += 1

    def __del__(self):
        if self.conn:
            self.conn.close()

    def insert(self, query, params=()):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            self.conn.commit()
            idt = cursor.lastrowid
            cursor.close()
            return idt
        except mysql.connector.Error:
            self.conn.rollback()
            raise
        finally:
            if cursor:
                cursor.close()

    def insert_many(self, query, params_list):
        cursor = self.conn.cursor()
        try:
            cursor.executemany(query, params_list)
            self.conn.commit()
            # Retrieve the IDs of the inserted rows
            inserted_ids = cursor.lastrowid
            num_rows = cursor.rowcount
            first_id = inserted_ids - num_rows + 1
            inserted_ids = list(range(first_id, inserted_ids + 1))
        except Exception as e:
            self.conn.rollback()
            raise e
        finally:
            cursor.close()
        return inserted_ids

    def upd_del(self, query, params=()):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query, params)
            self.conn.commit()
            num = cursor.rowcount
            cursor.close()
            return num
        except mysql.connector.Error:
            self.conn.rollback()
            raise
        finally:
            if cursor:
                cursor.close()

    def upd_del_many(self, query, params):
        try:
            cursor = self.conn.cursor()
            cursor.executemany(query, params)
            self.conn.commit()
        except mysql.connector.Error:
            self.conn.rollback()
            raise
        finally:
            if cursor:
                cursor.close()

    def get_cursor(self, query, params=()):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        return cursor

    def get_int(self, query, params=()):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        ret = int(cursor.fetchone()[0])
        cursor.close()
        return ret

    def get_float(self, query, params=()):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        ret = float(cursor.fetchone()[0])
        cursor.close()
        return ret

    def get_date(self, query, params=()):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        date = cursor.fetchone()[0]
        ret = (
            str(date.day).zfill(2)
            + "/"
            + str(date.month).zfill(2)
            + "/"
            + str(date.year)
        )
        cursor.close()
        return ret

    def get_string(self, query, params=()):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        ret = str(cursor.fetchone()[0])
        cursor.close()
        return ret

    def get_object(self, query, params=()):
        cursor = self.conn.cursor(buffered=True)
        cursor.execute(query, params)
        dados = cursor.fetchone()
        if dados is None:
            dic = None
        else:
            md = cursor.description
            dic = {col[0]: valor for col, valor in zip(md, dados)}
        cursor.close()
        return dic

    def get_list(self, query, params=()):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        md = cursor.description
        catalog = []
        for reg in cursor:
            dic = {col[0]: valor for col, valor in zip(md, reg)}
            catalog.append(dic)
        cursor.close()
        return catalog
