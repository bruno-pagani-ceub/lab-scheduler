from lab_scheduler.database.sql import SQL

class ReportModel:
    def __init__(self, db):
        self.db = db

    def get_weekly_schedule(self):
        query = """
        SELECT
            DATE_FORMAT(tb_horario.dt_dia, '%d-%m-%Y') AS data,
            DATE_FORMAT(tb_horario.hr_inicio, '%H:%i') AS inicio,
            DATE_FORMAT(tb_horario.hr_fim, '%H:%i') AS fim,
            COALESCE(tb_reserva.tp_reserva, 'Disponível') AS atividade,
            COALESCE(tb_laboratorio.ds_sala, 'Nenhum') AS laboratorio
        FROM tb_horario
        LEFT JOIN ta_laboratorio_horario ON tb_horario.id = ta_laboratorio_horario.id_horario
        LEFT JOIN tb_reserva ON ta_laboratorio_horario.id = tb_reserva.id_laboratorio_horario
        LEFT JOIN tb_laboratorio ON ta_laboratorio_horario.id_laboratorio = tb_laboratorio.id
        ORDER BY tb_horario.dt_dia, tb_horario.hr_inicio;
        """
        return self.db.get_list(query)
