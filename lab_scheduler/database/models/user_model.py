from lab_scheduler.database.sql import SQL

class UserModel:
    def __init__(self, db):
        self.db: SQL = db
