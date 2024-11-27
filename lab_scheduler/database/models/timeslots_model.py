from lab_scheduler.database.sql import SQL


class TimeSlotsModel:
    def __init__(self, db):
        self.db: SQL = db

    def update_time_slots(self, old_times, updates):
        old_start_time, old_end_time = old_times

        update_query = """
        UPDATE tb_horario
        SET hr_inicio = %s, hr_fim = %s
        WHERE dt_dia = %s AND hr_inicio = %s AND hr_fim = %s
        """

        params_list = []
        for dt_dia, new_start_time, new_end_time in updates:
            params = (
                new_start_time,
                new_end_time,
                dt_dia,
                old_start_time,
                old_end_time,
            )
            params_list.append(params)
        return self.db.upd_del_many(update_query, params_list)

    def delete_time_slots(self, records):
        placeholders = ", ".join(["%s"] * len(records))
        select_query = f"""
            SELECT id
            FROM tb_horario
            WHERE dt_dia IN ({placeholders}) AND hr_inicio = %s AND hr_fim = %s
        """
        start_time = records[0][1]
        end_time = records[0][2]
        days = [record[0] for record in records]
        params = (*days, start_time, end_time)
        results = self.db.get_list(select_query, params)
        ids = [result["id"] for result in results]

        query = (
            f"DELETE FROM ta_laboratorio_horario WHERE id_horario IN ({placeholders})"
        )

        self.db.upd_del(query, ids)

        query = f"DELETE FROM tb_horario WHERE id IN ({placeholders})"

        return self.db.upd_del(query, ids)

    def save_time_slots(self, inserts):
        query = "INSERT INTO tb_horario (dt_dia, hr_inicio, hr_fim) VALUES (%s, %s, %s)"
        inserted_ids = self.db.insert_many(query, inserts)

        lab_query = "SELECT id FROM tb_laboratorio;"
        lab_records = self.db.get_list(lab_query)
        lab_ids = [lab["id"] for lab in lab_records]
        if not lab_ids:
            return inserted_ids

        lab_horario_inserts = []
        for horario_id in inserted_ids:
            for lab_id in lab_ids:
                lab_horario_inserts.append((lab_id, horario_id))

        lab_horario_query = "INSERT INTO ta_laboratorio_horario (id_laboratorio, id_horario) VALUES (%s, %s)"
        self.db.insert_many(lab_horario_query, lab_horario_inserts)

        return inserted_ids

    def get_time_slots_summary(self, weekdays, start_month, end_month, year):
        placeholders = ", ".join(["%s"] * len(weekdays))
        query = f"""
            SELECT DISTINCT
                WEEKDAY(dt_dia) AS nr_dia_semana,
                DATE_FORMAT(hr_inicio, '%H:%i') AS hr_ini,
                DATE_FORMAT(hr_fim, '%H:%i') AS hr_fim
            FROM
                tb_horario
            WHERE
                WEEKDAY(dt_dia) IN ({placeholders})
                AND MONTH(dt_dia) BETWEEN %s AND %s
                AND YEAR(dt_dia) = %s
            ORDER BY 
                nr_dia_semana,
                hr_ini,
                hr_fim;
        """

        params = tuple([*weekdays, start_month, end_month, year])
        return self.db.get_list(query, params)
