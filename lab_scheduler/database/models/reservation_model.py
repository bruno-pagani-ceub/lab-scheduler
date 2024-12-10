from lab_scheduler.database.sql import SQL


class ReservationModel:
    def __init__(self, db):
        self.db: SQL = db

    def get_lab_list(self):

        query = """
        SELECT *
        FROM tb_laboratorio
        """

        return self.db.get_list(query)

    def get_user(self, name, ident):

        query = """
        SELECT tb_usuario.id, tb_usuario.nm_usuario, td_tipo_usuario.ds_tipo_usuario, tb_usuario.ds_identificacao
        FROM tb_usuario
        JOIN td_tipo_usuario ON tb_usuario.id_tipo_usuario = td_tipo_usuario.id
        WHERE nm_usuario = %s AND ds_identificacao = %s
        """

        return self.db.get_list(query, (name, ident))

    def get_available_lab_times(self, date, lab):

        query = """
        SELECT *
        FROM tb_horario
        WHERE dt_dia = %s
        AND id IN (
            SELECT id_horario
            FROM ta_laboratorio_horario
            WHERE id_laboratorio = %s
            AND id IN (
                SELECT id_laboratorio_horario
                FROM tb_reserva
                WHERE is_ativa = 0))
        """

        return self.db.get_list(query, (date, lab))


class LabReservationModel:
    def __init__(self, db):
        self.db: SQL = db

    def make_single_reservation(self, user, type, lab, time):

        lab_time_query = """SELECT id FROM ta_laboratorio_horario WHERE id_laboratorio = %s AND id_horario = %s"""
        lab_time = self.db.get_object(lab_time_query, (lab, time))

        query = """INSERT INTO tb_reserva VALUES (DEFAULT, 0, 1, %s, %s, %s)"""

        self.db.insert(query, (type, user, lab_time["id"]))

        query_update_reserv_id = """UPDATE tb_reserva SET cod_reserva = (LAST_INSERT_ID() * 2654435761) MOD 1000000007 WHERE id = LAST_INSERT_ID()"""

        self.db.upd_del(query_update_reserv_id)

    def make_recurrent_reservation(
        self, user, text, lab, weekday, timeslot, semester, year
    ):
        if semester == "1":
            date_start = f"{year}-01-01"
            date_end = f"{year}-06-30"
        else:
            date_start = f"{year}-07-01"
            date_end = f"{year}-12-31"

        weekday_query = """SELECT id FROM ta_laboratorio_horario WHERE id_laboratorio = %s AND id_horario IN
                        (SELECT id FROM tb_horario WHERE DAYOFWEEK(dt_dia) = %s AND dt_dia >= %s AND dt_dia <= %s) AND id NOT IN
                        (SELECT id_laboratorio_horario FROM tb_reserva WHERE is_ativa = 1)"""

        all_weekdays = self.db.get_list(
            weekday_query, (lab, weekday, date_start, date_end)
        )

        weekday_ids = []
        for item in all_weekdays:
            weekday_ids.append((text, user, item["id"]))

        query = """INSERT INTO tb_reserva VALUES (DEFAULT, 0, 1, %s, %s, %s)"""
        self.db.insert(query, weekday_ids[0])
        first_id = self.db.get_object(
            "SELECT (id * 2654435761) MOD 1000000007 FROM tb_reserva AS hash_id WHERE id = LAST_INSERT_ID()"
        )
        print(first_id['(id * 2654435761) MOD 1000000007'])
        query_update_reserv_id = """UPDATE tb_reserva SET cod_reserva = (LAST_INSERT_ID() * 2654435761) MOD 1000000007 WHERE id = LAST_INSERT_ID()"""
        self.db.upd_del(query_update_reserv_id)

        extra_query = """INSERT INTO tb_reserva VALUES (DEFAULT, %s, 1, %s, %s, %s)"""
        extra_params = []
        for item in weekday_ids[1:]:
            text_rec, user_rec, labtime_rec = item
            extra_params.append((first_id['(id * 2654435761) MOD 1000000007'], text_rec, user_rec, labtime_rec))
        self.db.insert_many(extra_query, extra_params)

    def get_user(self, id):
        param = []
        param.append(id)
        query = """
        SELECT tb_usuario.id, tb_usuario.nm_usuario, td_tipo_usuario.ds_tipo_usuario
        FROM tb_usuario
        JOIN td_tipo_usuario ON id_tipo_usuario = td_tipo_usuario.id
        WHERE tb_usuario.ds_identificacao = %s
        """
        return self.db.get_list(query, param)

    def get_lab_list(self):
        query = """SELECT id, ds_sala AS Sala, ds_bloco AS Bloco, qtd_pcs AS "PCs disp" FROM tb_laboratorio"""

        return self.db.get_list(query)

    def get_available_timeslots(self, date, lab):

        query = """SELECT id, hr_inicio, hr_fim FROM tb_horario WHERE dt_dia = %s AND id IN (
	            SELECT id_horario FROM ta_laboratorio_horario WHERE id_laboratorio = %s AND id NOT IN (
		        SELECT id_laboratorio_horario FROM tb_reserva WHERE is_ativa = 1))"""

        return self.db.get_list(query, (date, lab))

    def get_base_date(self, weekday, semester, year):

        if semester == "1":
            date_start = f"{year}-01-01"
            date_end = f"{year}-06-30"
        else:
            date_start = f"{year}-07-01"
            date_end = f"{year}-12-31"

        query = """SELECT MIN(dt_dia) AS base_date FROM tb_horario WHERE DAYOFWEEK(dt_dia) = %s AND dt_dia >= %s AND dt_dia <= %s"""

        return self.db.get_object(query, (weekday, date_start, date_end))

    def get_available_timeslots_weekday(self, date):
        query = """SELECT id, hr_inicio, hr_fim FROM tb_horario WHERE dt_dia = %s"""

        return self.db.get_list(query, (date,))
