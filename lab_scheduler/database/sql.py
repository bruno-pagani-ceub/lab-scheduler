import mysql.connector


class SQL:
    def __init__(
        self,
        host: str,
        user: str,
        password: str,
        database: str,
        port: int,
    ):
        try:
            self.conn = mysql.connector.connect(
                host=host, user=user, password=password, database=database, port=port
            )
            if self.conn.is_connected():
                print("Connected to MySQL database")
        except mysql.connector.Error as e:
            print(f"Error connecting to MySQL: {e}")
            return None

    def __del__(self):
        self.conn.close()

    def insert(self, query, params=()):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        self.conn.commit()
        idt = cursor.lastrowid
        cursor.close()
        return idt

    def upd_del(self, query, params=()):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        self.conn.commit()
        num = cursor.rowcount
        cursor.close()
        return num

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

    ## TODO: Não é Exatamente o que precisamos, precisa ser alterado para ler os horários
    # def get_time(self, query, params=()):
    #     cursor = self.conn.cursor()
    #     cursor.execute(query, params)
    #     hora = cursor.fetchone()[0]
    #     total = hora.total_seconds()
    #     hour = int(total // 3600)
    #     minutes = int((total % 3600) // 60)
    #     seconds = int(total % 60)
    #     ret = f"{hour:02}:{minutes:02}"
    #     cursor.close()
    #     return ret

    def get_string(self, query, params=()):
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        ret = str(cursor.fetchone()[0])
        cursor.close()
        return ret

    def get_object(self, query, params=()):
        cursor = self.conn.cursor()
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
