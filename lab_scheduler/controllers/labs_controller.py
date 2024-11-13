from lab_scheduler.database.models import LabModel
from lab_scheduler.views import LabRegistrationView, LabView


class LabController:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.view = LabView(root, self)
        self.model = LabModel

class LabRegistrationController:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.view = LabRegistrationView(root, self)
        
    