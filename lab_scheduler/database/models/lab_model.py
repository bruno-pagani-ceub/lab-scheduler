from lab_scheduler.database.sql import SQL

class LabModel:
    def __init__(self, db):
        self.db: SQL = db
        
    def find_overlaping_lab(self, ds_bloco, ds_sala):
        query = "SELECT count(1) FROM tb_laboratorio WHERE ds_bloco = %s AND ds_sala = %s"
        return self.db.get_int(query, (ds_bloco, ds_sala))

    def create_lab(self, ds_bloco, ds_sala, qtd_pcs):
        if self.find_overlaping_lab(ds_bloco, ds_sala):
            raise ValueError(f"Laboratório no bloco {ds_bloco} e sala {ds_sala} já havia sido cadastrado")
        insert_query = """
              INSERT INTO tb_laboratorio (ds_bloco, ds_sala, qtd_pcs)
              VALUES (%s, %s, %s)
        """
        params = (
            ds_bloco,
            ds_sala,
            qtd_pcs,
        )
        inserted_id = self.db.insert(insert_query, params)
        
        timeslot_query = "SELECT id FROM tb_horario;"
        timeslot_records = self.db.get_list(timeslot_query)
        timeslot_ids = [timeslot["id"] for timeslot in timeslot_records]
        if not timeslot_ids:
            return inserted_id

        lab_horario_inserts = []
        for timeslot_id in timeslot_ids:
            lab_horario_inserts.append((inserted_id, timeslot_id))
        
        insert_query = """
            INSERT INTO ta_laboratorio_horario (id_laboratorio, id_horario) VALUES (%s, %s)
        """
        

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
            SELECT * FROM tb_laboratorio ORDER BY ds_bloco, ds_sala, qtd_pcs DESC;
        """
        params = []

        if ds_sala:
            load_query = """
                SELECT * FROM tb_laboratorio WHERE ds_sala LIKE %s
            """
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
