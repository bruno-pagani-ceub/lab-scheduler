from lab_scheduler.database.sql import SQL

class ReportModel:
    def __init__(self, db):
        self.db: SQL = db
