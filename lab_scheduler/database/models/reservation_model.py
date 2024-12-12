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
        semester_dates = {
            "1": (f"{year}-01-01", f"{year}-06-30"),
            "2": (f"{year}-07-01", f"{year}-12-31"),
        }
        date_start, date_end = semester_dates[semester]

        print(timeslot)
        print(lab, weekday, date_start, date_end)

        weekday_query = """SELECT id FROM ta_laboratorio_horario WHERE id_laboratorio = %s AND id_horario IN
                        (SELECT id FROM tb_horario WHERE DAYOFWEEK(dt_dia) = %s AND dt_dia >= %s AND dt_dia <= %s AND hr_inicio IN
                        (SELECT hr_inicio FROM tb_horario WHERE id = %s)) AND id NOT IN
                        (SELECT id_laboratorio_horario FROM tb_reserva WHERE is_ativa = 1)"""

        available_weekdays = self.db.get_list(
            weekday_query, (lab, weekday, date_start, date_end, timeslot)
        )

        if len(available_weekdays) == 0:
            return False

        weekday_ids = [
            (text, user, item["id"]) for item in available_weekdays
        ]

        query = """INSERT INTO tb_reserva VALUES (DEFAULT, 0, 1, %s, %s, %s)"""
        self.db.insert(query, weekday_ids[0])

        hash_id_query = """SELECT (id * 2654435761) MOD 1000000007 AS hashed_id FROM tb_reserva WHERE id = LAST_INSERT_ID()"""
        hashed_id = self.db.get_object(hash_id_query)["hashed_id"]
        
        query_update_reserv_id = """UPDATE tb_reserva SET cod_reserva = %s WHERE id = LAST_INSERT_ID()"""
        self.db.upd_del(query_update_reserv_id, (hashed_id,))

        extra_query = """INSERT INTO tb_reserva VALUES (DEFAULT, %s, 1, %s, %s, %s)"""
        
        extra_params = []
        for item in weekday_ids[1:]:
            text_rec, user_rec, labtime_rec = item
            extra_params.append((hashed_id, text_rec, user_rec, labtime_rec))
            print(hashed_id, text_rec, user_rec, labtime_rec)
        print(extra_params)
        self.db.insert_many(extra_query, extra_params)
        return True

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

    
    def get_available_timeslots_weekday(self, lab, weekday, semester, year):
        
        query = """
        SELECT
            MAX(h.hr_inicio),
            MAX(h.hr_fim)
        FROM
            tb_reserva r
        RIGHT JOIN ta_laboratorio_horario lh 
            on
            r.id_laboratorio_horario = lh.id
        join tb_horario h 
            on
            lh.id_horario = h.id
        join tb_laboratorio l
            on
            lh.id_laboratorio = l.id
        WHERE
            l.id = %s
            and WEEKDAY(h.dt_dia) = %s
            AND h.dt_dia >= %s
            and h.dt_dia <= %s
        GROUP BY
            WEEKDAY(h.dt_dia),
            CONCAT(h.hr_inicio, ' - ', h.hr_fim)
        HAVING
            MAX(r.id) is NULL
        """

        if semester == "1":
            date_start = f"{year}-01-01"
            date_end = f"{year}-06-30"
        else:
            date_start = f"{year}-07-01"
            date_end = f"{year}-12-31"

        return self.db.get_list(query, (lab, weekday, date_start, date_end))


class ViewReservationModel:
    def __init__(self, db):
        self.db: SQL = db
        self.general_query = """SELECT tb_reserva.id AS id, tb_reserva.tp_reserva AS 'Desc', tb_laboratorio.ds_sala AS 'Sala', tb_laboratorio.ds_bloco AS 'Bloco', tb_horario.dt_dia AS 'Data', CONCAT(TIME_FORMAT(tb_horario.hr_inicio, '%H:%i'), ' - ', TIME_FORMAT(tb_horario.hr_fim, '%H:%i')) AS 'Horário', tb_usuario.nm_usuario AS 'Nome', tb_usuario.ds_identificacao AS 'ID'
                            FROM tb_reserva JOIN tb_usuario ON id_usuario = tb_usuario.id
                            JOIN ta_laboratorio_horario ON id_laboratorio_horario = ta_laboratorio_horario.id
                            JOIN tb_horario ON id_horario = tb_horario.id
                            JOIN tb_laboratorio ON id_laboratorio = tb_laboratorio.id
                            WHERE is_ativa = 1"""

    def search_all(self):
        return self.db.get_list(self.general_query)