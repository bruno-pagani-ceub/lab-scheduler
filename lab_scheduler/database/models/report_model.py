from lab_scheduler.database.sql import SQL

class ReportModel:
    def __init__(self, db):
        self.db: SQL = db

    def get_weekly_schedule(self, lab, star_of_week, end_of_week):
        
        query = """
        SELECT 
            l.id AS lab_id,
            l.ds_bloco,
            l.ds_sala,
            h.id AS horario_id,
            h.dt_dia,
            DATE_FORMAT(h.hr_inicio, '%H:%i') AS hr_inicio,
            DATE_FORMAT(h.hr_fim, '%H:%i') AS hr_fim,
            r.id AS reserva_id,
            r.cod_reserva,
            r.is_ativa,
            r.tp_reserva,
            u.nm_usuario,
            u.ds_identificacao,
            tu.ds_tipo_usuario,
            lh.id AS lab_horario_id
        FROM tb_laboratorio AS l
        JOIN ta_laboratorio_horario AS lh ON l.id = lh.id_laboratorio
        JOIN tb_horario AS h ON lh.id_horario = h.id
        LEFT JOIN tb_reserva AS r ON r.id_laboratorio_horario = lh.id
        LEFT JOIN tb_usuario AS u ON r.id_usuario = u.id
        LEFT JOIN td_tipo_usuario AS tu ON u.id_tipo_usuario = tu.id
        WHERE l.id = %s
        AND h.dt_dia BETWEEN %s AND %s
        ORDER BY h.dt_dia, h.hr_inicio;
        """
        return self.db.get_list(query, (lab, star_of_week, end_of_week))
    
    def get_labs(self):
        query = '''
            SELECT * from tb_laboratorio;
        '''
        return self.db.get_list(query)
