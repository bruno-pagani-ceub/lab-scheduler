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

        lab_time = self.db.get_object(f"SELECT id FROM ta_laboratorio_horario WHERE id_laboratorio = {lab} AND id_horario = {time}")

        query = """
        INSERT INTO tb_reserva
        VALUES (DEFAULT, 1, %s, %s, %s)
        """

        return self.db.insert(query, (type, user, lab_time["id"]))
    
    def make_recurrent_reservation(self, user, text, lab, weekday, timeslot, semester, year):
        if semester == "1":
            all_weekdays = self.db.get_list(f"SELECT id FROM ta_laboratorio_horario WHERE id_horario IN (SELECT id FROM tb_horario WHERE DAYOFWEEK(dt_dia) = '{weekday}' AND dt_dia >= '{year}-01-01' AND dt_dia <= '{year}-06-30')")
        else:
            all_weekdays = self.db.get_list(f"SELECT id FROM ta_laboratorio_horario WHERE id_horario IN (SELECT id FROM tb_horario WHERE DAYOFWEEK(dt_dia) = '{weekday}' AND dt_dia >= '{year}-07-01' AND dt_dia <= '{year}-12-31')")
        print(all_weekdays)


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
            query = f"SELECT MIN(dt_dia) AS base_date FROM tb_horario WHERE DAYOFWEEK(dt_dia) = {weekday} AND dt_dia >= '{year}-01-01' AND dt_dia <= '{year}-06-30'"
        else:
            query = f"SELECT MIN(dt_dia) AS base_date FROM tb_horario WHERE DAYOFWEEK(dt_dia) = {weekday} AND dt_dia >= '{year}-07-01' AND dt_dia <= '{year}-12-31'"
            
        return self.db.get_object(query)
    
    def get_available_timeslots_weekday(self, date):
        query = f"SELECT id, hr_inicio, hr_fim FROM tb_horario WHERE dt_dia = '{date}'"

        return self.db.get_list(query)