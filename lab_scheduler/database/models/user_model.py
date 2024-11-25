from lab_scheduler.database.sql import SQL

class UserModel:
    def __init__(self, db):
        self.db: SQL = db
        
    def save_user(self, full_name, role, doc):
        # result = self.db.get_list(
        #     '''
        #     INSERT INTO ...
        #     '''
        # )
        pass
