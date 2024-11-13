from lab_scheduler.views import UserView, UserRegistrationView
from lab_scheduler.database.models import UserModel


class UserController:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.view = UserView(root, self)
        self.model = UserModel

class UserRegistrationController:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.view = UserRegistrationView(root, self)
        
    def create_user(full_name, role, doc):
        '''Inserts New User in Database.'''
        pass
        
    