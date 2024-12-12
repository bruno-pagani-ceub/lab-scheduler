from lab_scheduler.views import UserView, UserRegistrationView, UpdateUserView
from lab_scheduler.database.models import UserModel


class UserController:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.view = UserView(root, self)
        self.model = UserModel(db=db)

    def load_users(self, nm_usuario):
        return self.model.load_users(nm_usuario)

    def delete_user(self, id):
        return self.model.delete_user(id)

    def register_user(self):
        UserRegistrationController(self.root, self.db)

    def update_users(self, id, nm_usuario, id_tipo_usuario, ds_identificacao):
        UpdateUserController(
            self.root, self.db, id, nm_usuario, id_tipo_usuario, ds_identificacao
        )


class UserRegistrationController:
    def __init__(self, root, db):
        self.root = root
        self.db = db
        self.view = UserRegistrationView(root, self)
        self.model = UserModel(db=db)

    def create_user(self, full_name, role, doc):
        self.model.save_user(full_name, role, doc)


class UpdateUserController:
    def __init__(self, root, db, id, nm_usuario, id_tipo_usuario, ds_identificacao):
        self.root = root
        self.db = db
        self.model = UserModel(db=db)
        self.view = UpdateUserView(
            root, self, id, nm_usuario, id_tipo_usuario, ds_identificacao
        )

    def update_user(self, id, nm_usuario, id_tipo_usuario, ds_identificacao):
        self.model.update_user(id, nm_usuario, id_tipo_usuario, ds_identificacao)
