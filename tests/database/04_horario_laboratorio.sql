INSERT INTO ta_laboratorio_horario (id_laboratorio, id_horario)
SELECT l.id, h.id
FROM tb_laboratorio l
CROSS JOIN tb_horario h;