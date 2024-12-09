SET @USER_ID = 8; 
SET @LAB_ID = 3;
SET @TP_RESERVA = 'aula';
SET @IS_ATIVA = TRUE;
SET @COD_RESERVA = 1;
SET @HR_INICIO = '16:00';
SET @HR_FIM = '17:40';
INSERT INTO tb_reserva (cod_reserva, is_ativa, tp_reserva, id_usuario, id_laboratorio_horario)
SELECT @COD_RESERVA as cod_reserva, @IS_ATIVA as is_ativa, @TP_RESERVA as tp_reserva, @USER_ID as id_usuario, lh.id as id_laboratorio_horario
FROM ta_laboratorio_horario lh
join tb_laboratorio l on lh.id_laboratorio = l.id
join tb_horario h on lh.id_horario = l.id
where YEAR(h.dt_dia) = 2025
  AND MONTH(h.dt_dia) BETWEEN 1 AND 6
  AND DAYOFWEEK(h.dt_dia) IN (3, 5)
  AND h.hr_inicio = CAST(@HR_INICIO AS TIME) 
  and h.hr_fim = CAST(@HR_FIM AS TIME)
  AND l.id = @LAB_ID;
 
SET @USER_ID = 2; 
SET @LAB_ID = 4;
SET @TP_RESERVA = 'aula';
SET @IS_ATIVA = TRUE;
SET @COD_RESERVA = 1;
SET @HR_INICIO = '16:00';
SET @HR_FIM = '17:40';
INSERT INTO tb_reserva (cod_reserva, is_ativa, tp_reserva, id_usuario, id_laboratorio_horario)
SELECT @COD_RESERVA as cod_reserva, @IS_ATIVA as is_ativa, @TP_RESERVA as tp_reserva, @USER_ID as id_usuario, lh.id as id_laboratorio_horario
FROM ta_laboratorio_horario lh
join tb_laboratorio l on lh.id_laboratorio = l.id
join tb_horario h on lh.id_horario = l.id
where YEAR(h.dt_dia) = 2025
  AND MONTH(h.dt_dia) BETWEEN 1 AND 6
  AND DAYOFWEEK(h.dt_dia) IN (3, 5)
  AND h.hr_inicio = CAST(@HR_INICIO AS TIME) 
  and h.hr_fim = CAST(@HR_FIM AS TIME)
  AND l.id = @LAB_ID;

SET @USER_ID = 6; 
SET @LAB_ID = 4;
SET @TP_RESERVA = 'aula';
SET @IS_ATIVA = TRUE;
SET @COD_RESERVA = @COD_RESERVA + 1;
SET @HR_INICIO = '14:00';
SET @HR_FIM = '15:40';
INSERT INTO tb_reserva (cod_reserva, is_ativa, tp_reserva, id_usuario, id_laboratorio_horario)
SELECT @COD_RESERVA as cod_reserva, @IS_ATIVA as is_ativa, @TP_RESERVA as tp_reserva, @USER_ID as id_usuario, lh.id as id_laboratorio_horario
FROM ta_laboratorio_horario lh
join tb_laboratorio l on lh.id_laboratorio = l.id
join tb_horario h on lh.id_horario = l.id
where YEAR(h.dt_dia) = 2025
  AND MONTH(h.dt_dia) BETWEEN 1 AND 6
  AND DAYOFWEEK(h.dt_dia) IN (2, 4)
  AND h.hr_inicio = CAST(@HR_INICIO AS TIME) 
  and h.hr_fim = CAST(@HR_FIM AS TIME)
  AND l.id = @LAB_ID;

SET @USER_ID = 2; 
SET @LAB_ID = 4;
SET @TP_RESERVA = 'aula';
SET @IS_ATIVA = TRUE;
SET @COD_RESERVA = @COD_RESERVA + 1;
SET @HR_INICIO = '09:40';
SET @HR_FIM = '11:20';
INSERT INTO tb_reserva (cod_reserva, is_ativa, tp_reserva, id_usuario, id_laboratorio_horario)
SELECT @COD_RESERVA as cod_reserva, @IS_ATIVA as is_ativa, @TP_RESERVA as tp_reserva, @USER_ID as id_usuario, lh.id as id_laboratorio_horario
FROM ta_laboratorio_horario lh
join tb_laboratorio l on lh.id_laboratorio = l.id
join tb_horario h on lh.id_horario = l.id
where YEAR(h.dt_dia) = 2025
  AND MONTH(h.dt_dia) BETWEEN 1 AND 6
  AND DAYOFWEEK(h.dt_dia) IN (2, 4)
  AND h.hr_inicio = CAST(@HR_INICIO AS TIME) 
  and h.hr_fim = CAST(@HR_FIM AS TIME)
  AND l.id = @LAB_ID;

SET @USER_ID = 3; 
SET @LAB_ID = 4;
SET @DT_DATE = '2025-01-06';
SET @TP_RESERVA = 'manutencao';
SET @IS_ATIVA = TRUE;
SET @COD_RESERVA = @COD_RESERVA + 1;
SET @HR_INICIO = '09:40';
SET @HR_FIM = '11:20';
INSERT INTO tb_reserva (cod_reserva, is_ativa, tp_reserva, id_usuario, id_laboratorio_horario)
SELECT @COD_RESERVA as cod_reserva, @IS_ATIVA as is_ativa, @TP_RESERVA as tp_reserva, @USER_ID as id_usuario, lh.id as id_laboratorio_horario
FROM ta_laboratorio_horario lh
join tb_laboratorio l on lh.id_laboratorio = l.id
join tb_horario h on lh.id_horario = l.id
where h.dt_dia = @DT_DATE
  AND h.hr_inicio = CAST(@HR_INICIO AS TIME) 
  and h.hr_fim = CAST(@HR_FIM AS TIME)
  AND l.id = @LAB_ID;

SET @USER_ID = 3; 
SET @LAB_ID = 4;
SET @DATE = '2025-01-07';
SET @TP_RESERVA = 'manutencao';
SET @IS_ATIVA = TRUE;
SET @COD_RESERVA = @COD_RESERVA + 1;
SET @HR_INICIO = '09:40';
SET @HR_FIM = '11:20';
INSERT INTO tb_reserva (cod_reserva, is_ativa, tp_reserva, id_usuario, id_laboratorio_horario)
SELECT @COD_RESERVA as cod_reserva, @IS_ATIVA as is_ativa, @TP_RESERVA as tp_reserva, @USER_ID as id_usuario, lh.id as id_laboratorio_horario
FROM ta_laboratorio_horario lh
join tb_laboratorio l on lh.id_laboratorio = l.id
join tb_horario h on lh.id_horario = l.id
where h.dt_dia = @DT_DATE
  AND h.hr_inicio = CAST(@HR_INICIO AS TIME) 
  and h.hr_fim = CAST(@HR_FIM AS TIME)
  AND l.id = @LAB_ID;

SET @USER_ID = 3; 
SET @LAB_ID = 4;
SET @DATE = '2025-01-08';
SET @TP_RESERVA = 'manutencao';
SET @IS_ATIVA = TRUE;
SET @COD_RESERVA = @COD_RESERVA + 1;
SET @HR_INICIO = '09:40';
SET @HR_FIM = '11:20';
INSERT INTO tb_reserva (cod_reserva, is_ativa, tp_reserva, id_usuario, id_laboratorio_horario)
SELECT @COD_RESERVA as cod_reserva, @IS_ATIVA as is_ativa, @TP_RESERVA as tp_reserva, @USER_ID as id_usuario, lh.id as id_laboratorio_horario
FROM ta_laboratorio_horario lh
join tb_laboratorio l on lh.id_laboratorio = l.id
join tb_horario h on lh.id_horario = l.id
where h.dt_dia = @DT_DATE
  AND h.hr_inicio = CAST(@HR_INICIO AS TIME) 
  and h.hr_fim = CAST(@HR_FIM AS TIME)
  AND l.id = @LAB_ID;

SET @USER_ID = 3; 
SET @LAB_ID = 4;
SET @DATE = '2025-01-09';
SET @TP_RESERVA = 'manutencao';
SET @IS_ATIVA = TRUE;
SET @COD_RESERVA = @COD_RESERVA + 1;
SET @HR_INICIO = '09:40';
SET @HR_FIM = '11:20';
INSERT INTO tb_reserva (cod_reserva, is_ativa, tp_reserva, id_usuario, id_laboratorio_horario)
SELECT @COD_RESERVA as cod_reserva, @IS_ATIVA as is_ativa, @TP_RESERVA as tp_reserva, @USER_ID as id_usuario, lh.id as id_laboratorio_horario
FROM ta_laboratorio_horario lh
join tb_laboratorio l on lh.id_laboratorio = l.id
join tb_horario h on lh.id_horario = l.id
where h.dt_dia = @DT_DATE
  AND h.hr_inicio = CAST(@HR_INICIO AS TIME) 
  and h.hr_fim = CAST(@HR_FIM AS TIME)
  AND l.id = @LAB_ID;

SET @USER_ID = 3; 
SET @LAB_ID = 4;
SET @DATE = '2025-01-10';
SET @TP_RESERVA = 'manutencao';
SET @IS_ATIVA = TRUE;
SET @COD_RESERVA = @COD_RESERVA + 1;
SET @HR_INICIO = '09:40';
SET @HR_FIM = '11:20';
INSERT INTO tb_reserva (cod_reserva, is_ativa, tp_reserva, id_usuario, id_laboratorio_horario)
SELECT @COD_RESERVA as cod_reserva, @IS_ATIVA as is_ativa, @TP_RESERVA as tp_reserva, @USER_ID as id_usuario, lh.id as id_laboratorio_horario
FROM ta_laboratorio_horario lh
join tb_laboratorio l on lh.id_laboratorio = l.id
join tb_horario h on lh.id_horario = l.id
where h.dt_dia = @DATE
  AND h.hr_inicio = CAST(@HR_INICIO AS TIME) 
  and h.hr_fim = CAST(@HR_FIM AS TIME)
  AND l.id = @LAB_ID;
 
SET @USER_ID = 1; 
SET @LAB_ID = 4;
SET @DATE = '2025-01-11';
SET @TP_RESERVA = 'reuniao';
SET @IS_ATIVA = TRUE;
SET @COD_RESERVA = @COD_RESERVA + 1;
SET @HR_INICIO = '14:00';
SET @HR_FIM = '15:30';
INSERT INTO tb_reserva (cod_reserva, is_ativa, tp_reserva, id_usuario, id_laboratorio_horario)
SELECT @COD_RESERVA as cod_reserva, @IS_ATIVA as is_ativa, @TP_RESERVA as tp_reserva, @USER_ID as id_usuario, lh.id as id_laboratorio_horario
FROM ta_laboratorio_horario lh
join tb_laboratorio l on lh.id_laboratorio = l.id
join tb_horario h on lh.id_horario = l.id
where h.dt_dia = @DATE
  AND h.hr_inicio = CAST(@HR_INICIO AS TIME) 
  and h.hr_fim = CAST(@HR_FIM AS TIME)
  AND l.id = @LAB_ID;
 
SET @USER_ID = 4; 
SET @LAB_ID = 4;
SET @DATE = '2025-01-11';
SET @TP_RESERVA = 'evento';
SET @IS_ATIVA = TRUE;
SET @COD_RESERVA = @COD_RESERVA + 1;
SET @HR_INICIO = '16:00';
SET @HR_FIM = '17:30';
INSERT INTO tb_reserva (cod_reserva, is_ativa, tp_reserva, id_usuario, id_laboratorio_horario)
SELECT @COD_RESERVA as cod_reserva, @IS_ATIVA as is_ativa, @TP_RESERVA as tp_reserva, @USER_ID as id_usuario, lh.id as id_laboratorio_horario
FROM ta_laboratorio_horario lh
join tb_laboratorio l on lh.id_laboratorio = l.id
join tb_horario h on lh.id_horario = l.id
where h.dt_dia = @DATE
  AND h.hr_inicio = CAST(@HR_INICIO AS TIME) 
  and h.hr_fim = CAST(@HR_FIM AS TIME)
  AND l.id = @LAB_ID;
