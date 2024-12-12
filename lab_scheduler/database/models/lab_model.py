from lab_scheduler.database.sql import SQL

class LabModel:
    def __init__(self, db):
        self.db: SQL = db

    def create_lab(self, ds_bloco, ds_sala, qtd_pcs):
        lab_data = {
            "ds_bloco": ds_bloco,
            "ds_sala": ds_sala,
            "qtd_pcs": qtd_pcs,
        }

        insert_query = """
              INSERT INTO tb_laboratorio (ds_bloco, ds_sala, qtd_pcs)
              VALUES (%s, %s, %s)
              """

        params = (
            lab_data["ds_bloco"],
            lab_data["ds_sala"],
            lab_data["qtd_pcs"],
        )

        return self.db.insert(insert_query, params)

    def update_lab(self, id, ds_bloco, ds_sala, qtd_pcs):
        lab_data = {
            "id": id,
            "ds_bloco": ds_bloco,
            "ds_sala": ds_sala,
            "qtd_pcs": qtd_pcs,

        }

        update_query = """UPDATE tb_laboratorio
                SET 
                    ds_sala = %s,
                    ds_bloco = %s,
                    qtd_pcs = %s
                WHERE id = %s;"""

        params = (
            lab_data["ds_bloco"],
            lab_data["ds_sala"],
            lab_data["qtd_pcs"],
            lab_data["id"]
        )
        self.db.insert(update_query, params)

    def load_labs(self, ds_sala):
        load_query = """
            SELECT * FROM tb_laboratorio
        """
        params = []

        if ds_sala:
            load_query = """
                SELECT * FROM tb_laboratorio WHERE ds_sala LIKE %s
            """
            # Use % for partial matching in LIKE
            params = (f"%{ds_sala}%",)

        return self.db.get_list(load_query, params)

    def delete_lab(self, id):
        delete_horario_query = """
            DELETE FROM ta_laboratorio_horario WHERE id_laboratorio = %s
        """

        params_horario = (id,)
        self.db.upd_del(delete_horario_query, params_horario)

        delete_lab_query = """
            DELETE FROM tb_laboratorio WHERE ID = %s
        """

        params_lab = (id,)
        return self.db.upd_del(delete_lab_query, params_lab)
