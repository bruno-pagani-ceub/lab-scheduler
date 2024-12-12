from lab_scheduler.database.models import LabModel
from lab_scheduler.views import LabRegistrationView, LabView, UpdateLabView


class LabController:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.model = LabModel(db=db)
        self.view = LabView(root, self)

    def load_labs(self, ds_sala):
        return self.model.load_labs(ds_sala)

    def delete_lab(self, id):
        return self.model.delete_lab(id)

    def register_lab(self):
        LabRegistrationController(self.root, self.db)

    def update_labs(self, id, ds_bloco, ds_sala, qtd_pcs):
        UpdateLabController(
            self.root, self.db, id, ds_bloco, ds_sala, qtd_pcs
        )

class LabRegistrationController:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.model = LabModel(db=db)
        self.view = LabRegistrationView(root, self)

    def create_lab(self, ds_bloco, ds_sala, qtd_pcs):
        self.model.create_lab(ds_bloco, ds_sala, qtd_pcs)

class UpdateLabController:
    def __init__(self, root, db, id, ds_bloco, ds_sala, qtd_pcs):
        self.root = root
        self.db = db
        self.model = LabModel(db=db)
        self.view = UpdateLabView(
            root, self, id, ds_bloco, ds_sala, qtd_pcs
        )

    def update_lab(self, id, ds_bloco, ds_sala, qtd_pcs):
        self.model.update_lab(id, ds_bloco, ds_sala, qtd_pcs)
