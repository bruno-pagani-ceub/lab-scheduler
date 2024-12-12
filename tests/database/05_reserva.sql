INSERT INTO tb_reserva (cod_reserva, is_ativa, tp_reserva, id_usuario, id_laboratorio_horario)
SELECT 1 as cod_reserva, TRUE as is_ativa, 'aula' as tp_reserva, 8 as id_usuario, lh.id as id_laboratorio_horario
FROM ta_laboratorio_horario lh
JOIN tb_laboratorio l ON lh.id_laboratorio = l.id
JOIN tb_horario h ON lh.id_horario = h.id
WHERE YEAR(h.dt_dia) = 2025
  AND MONTH(h.dt_dia) BETWEEN 1 AND 6
  AND DAYOFWEEK(h.dt_dia) IN (3, 5)
  AND h.hr_inicio = CAST('16:00' AS TIME) 
  AND h.hr_fim = CAST('17:40' AS TIME)
  AND l.id = 3;

INSERT INTO tb_reserva (cod_reserva, is_ativa, tp_reserva, id_usuario, id_laboratorio_horario)
SELECT 1 as cod_reserva, TRUE as is_ativa, 'aula' as tp_reserva, 2 as id_usuario, lh.id as id_laboratorio_horario
FROM ta_laboratorio_horario lh
JOIN tb_laboratorio l ON lh.id_laboratorio = l.id
JOIN tb_horario h ON lh.id_horario = h.id
WHERE YEAR(h.dt_dia) = 2025
  AND MONTH(h.dt_dia) BETWEEN 1 AND 6
  AND DAYOFWEEK(h.dt_dia) IN (3, 5)
  AND h.hr_inicio = CAST('16:00' AS TIME) 
  AND h.hr_fim = CAST('17:40' AS TIME)
  AND l.id = 4;

INSERT INTO tb_reserva (cod_reserva, is_ativa, tp_reserva, id_usuario, id_laboratorio_horario)
SELECT 2 as cod_reserva, TRUE as is_ativa, 'aula' as tp_reserva, 6 as id_usuario, lh.id as id_laboratorio_horario
FROM ta_laboratorio_horario lh
JOIN tb_laboratorio l ON lh.id_laboratorio = l.id
JOIN tb_horario h ON lh.id_horario = h.id
WHERE YEAR(h.dt_dia) = 2025
  AND MONTH(h.dt_dia) BETWEEN 1 AND 6
  AND DAYOFWEEK(h.dt_dia) IN (2, 4)
  AND h.hr_inicio = CAST('14:00' AS TIME) 
  AND h.hr_fim = CAST('15:40' AS TIME)
  AND l.id = 4;

INSERT INTO tb_reserva (cod_reserva, is_ativa, tp_reserva, id_usuario, id_laboratorio_horario)
SELECT 3 as cod_reserva, TRUE as is_ativa, 'aula' as tp_reserva, 2 as id_usuario, lh.id as id_laboratorio_horario
FROM ta_laboratorio_horario lh
JOIN tb_laboratorio l ON lh.id_laboratorio = l.id
JOIN tb_horario h ON lh.id_horario = h.id
WHERE YEAR(h.dt_dia) = 2025
  AND MONTH(h.dt_dia) BETWEEN 1 AND 6
  AND DAYOFWEEK(h.dt_dia) IN (2, 4)
  AND h.hr_inicio = CAST('09:40' AS TIME) 
  AND h.hr_fim = CAST('11:20' AS TIME)
  AND l.id = 4;

INSERT INTO tb_reserva (cod_reserva, is_ativa, tp_reserva, id_usuario, id_laboratorio_horario)
SELECT 4 as cod_reserva, TRUE as is_ativa, 'manutencao' as tp_reserva, 3 as id_usuario, lh.id as id_laboratorio_horario
FROM ta_laboratorio_horario lh
JOIN tb_laboratorio l ON lh.id_laboratorio = l.id
JOIN tb_horario h ON lh.id_horario = h.id
WHERE h.dt_dia = '2025-01-06'
  AND h.hr_inicio = CAST('11:30' AS TIME) 
  AND h.hr_fim = CAST('13:00' AS TIME)
  AND l.id = 4;

INSERT INTO tb_reserva (cod_reserva, is_ativa, tp_reserva, id_usuario, id_laboratorio_horario)
SELECT 5 as cod_reserva, TRUE as is_ativa, 'manutencao' as tp_reserva, 3 as id_usuario, lh.id as id_laboratorio_horario
FROM ta_laboratorio_horario lh
JOIN tb_laboratorio l ON lh.id_laboratorio = l.id
JOIN tb_horario h ON lh.id_horario = h.id
WHERE h.dt_dia = '2025-01-07'
  AND h.hr_inicio = CAST('11:30' AS TIME) 
  AND h.hr_fim = CAST('13:00' AS TIME)
  AND l.id = 4;

INSERT INTO tb_reserva (cod_reserva, is_ativa, tp_reserva, id_usuario, id_laboratorio_horario)
SELECT 6 as cod_reserva, TRUE as is_ativa, 'manutencao' as tp_reserva, 3 as id_usuario, lh.id as id_laboratorio_horario
FROM ta_laboratorio_horario lh
JOIN tb_laboratorio l ON lh.id_laboratorio = l.id
JOIN tb_horario h ON lh.id_horario = h.id
WHERE h.dt_dia = '2025-01-08'
  AND h.hr_inicio = CAST('11:30' AS TIME) 
  AND h.hr_fim = CAST('13:00' AS TIME)
  AND l.id = 4;


INSERT INTO tb_reserva (cod_reserva, is_ativa, tp_reserva, id_usuario, id_laboratorio_horario)
SELECT 7 as cod_reserva, TRUE as is_ativa, 'manutencao' as tp_reserva, 3 as id_usuario, lh.id as id_laboratorio_horario
FROM ta_laboratorio_horario lh
JOIN tb_laboratorio l ON lh.id_laboratorio = l.id
JOIN tb_horario h ON lh.id_horario = h.id
WHERE h.dt_dia = '2025-01-09'
  AND h.hr_inicio = CAST('11:30' AS TIME) 
  AND h.hr_fim = CAST('13:00' AS TIME)
  AND l.id = 4;


INSERT INTO tb_reserva (cod_reserva, is_ativa, tp_reserva, id_usuario, id_laboratorio_horario)
SELECT 8 as cod_reserva, TRUE as is_ativa, 'manutencao' as tp_reserva, 3 as id_usuario, lh.id as id_laboratorio_horario
FROM ta_laboratorio_horario lh
JOIN tb_laboratorio l ON lh.id_laboratorio = l.id
JOIN tb_horario h ON lh.id_horario = h.id
WHERE h.dt_dia = '2025-01-10'
  AND h.hr_inicio = CAST('11:30' AS TIME) 
  AND h.hr_fim = CAST('13:00' AS TIME)
  AND l.id = 4;


INSERT INTO tb_reserva (cod_reserva, is_ativa, tp_reserva, id_usuario, id_laboratorio_horario)
SELECT 9 as cod_reserva, TRUE as is_ativa, 'reuniao' as tp_reserva, 1 as id_usuario, lh.id as id_laboratorio_horario
FROM ta_laboratorio_horario lh
JOIN tb_laboratorio l ON lh.id_laboratorio = l.id
JOIN tb_horario h ON lh.id_horario = h.id
WHERE h.dt_dia = '2025-01-11'
  AND h.hr_inicio = CAST('14:00' AS TIME) 
  AND h.hr_fim = CAST('15:30' AS TIME)
  AND l.id = 4;


INSERT INTO tb_reserva (cod_reserva, is_ativa, tp_reserva, id_usuario, id_laboratorio_horario)
SELECT 10 as cod_reserva, TRUE as is_ativa, 'evento' as tp_reserva, 4 as id_usuario, lh.id as id_laboratorio_horario
FROM ta_laboratorio_horario lh
JOIN tb_laboratorio l ON lh.id_laboratorio = l.id
JOIN tb_horario h ON lh.id_horario = h.id
WHERE h.dt_dia = '2025-01-11'
  AND h.hr_inicio = CAST('16:00' AS TIME) 
  AND h.hr_fim = CAST('17:30' AS TIME)
  AND l.id = 4;

INSERT INTO tb_reserva (cod_reserva, is_ativa, tp_reserva, id_usuario, id_laboratorio_horario)
SELECT 11 as cod_reserva, TRUE as is_ativa, 'evento' as tp_reserva, 4 as id_usuario, lh.id as id_laboratorio_horario
FROM ta_laboratorio_horario lh
JOIN tb_laboratorio l ON lh.id_laboratorio = l.id
JOIN tb_horario h ON lh.id_horario = h.id
WHERE h.dt_dia = '2025-01-12'
  AND h.hr_inicio = CAST('16:00' AS TIME) 
  AND h.hr_fim = CAST('17:30' AS TIME)
  AND l.id = 4;