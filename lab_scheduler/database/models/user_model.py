from lab_scheduler.database.sql import SQL


class UserModel:
    def __init__(self, db):
        self.db: SQL = db

    def save_user(self, full_name, role, doc):
        user_data = {
            "nm_usuario": full_name,
            "id_tipo_usuario": role,
            "ds_identificacao": doc,
        }

        insert_query = """
           INSERT INTO tb_usuario (nm_usuario, id_tipo_usuario, ds_identificacao)
           VALUES (%s, %s, %s)
           """

        params = (
            user_data["nm_usuario"],
            user_data["id_tipo_usuario"],
            user_data["ds_identificacao"],
        )

        return self.db.insert(insert_query, params)

    def update_user(self, id, full_name, role, doc):
        user_data = {
            "id": id,
            "nm_usuario": full_name,
            "id_tipo_usuario": role,
            "ds_identificacao": doc

        }

        update_query = """UPDATE tb_usuario
                SET nm_usuario = %s,
                    id_tipo_usuario = %s,
                    ds_identificacao = %s
                WHERE id = %s;"""

        params = (
            user_data["nm_usuario"],
            user_data["id_tipo_usuario"],
            user_data["ds_identificacao"],
            user_data["id"]
        )
        print("veio aqui 4")
        self.db.insert(update_query, params)

    def load_users(self, nm_usuario):
        load_query = """
            SELECT * FROM tb_usuario
        """
        params = []

        # Add condition if nm_usuario is provided
        if nm_usuario:
            load_query = """
                SELECT * FROM tb_usuario WHERE NM_USUARIO LIKE %s
            """
            # Use % for partial matching in LIKE
            params = (f"%{nm_usuario}%",)

        return self.db.get_list(load_query, params)

    def delete_user(self, id):
        print("delete id -> ", id)
        delete_query = """
           DELETE FROM tb_usuario WHERE ID = %s
           """

        params = (
            id,
        )

        return self.db.upd_del(delete_query, params)
