USE lab_scheduler;

INSERT INTO `lab_scheduler`.`tb_reserva` (`id`, `is_ativa`, `tp_reserva`, `id_usuario`, `id_laboratorio_horario`) VALUES (DEFAULT, 1, 'aula', 1, 1);
INSERT INTO `lab_scheduler`.`tb_reserva` (`id`, `is_ativa`, `tp_reserva`, `id_usuario`, `id_laboratorio_horario`) VALUES (DEFAULT, 0, 'manutencao', 2, 2);
INSERT INTO `lab_scheduler`.`tb_reserva` (`id`, `is_ativa`, `tp_reserva`, `id_usuario`, `id_laboratorio_horario`) VALUES (DEFAULT, 1, 'reuniao', 3, 3);
INSERT INTO `lab_scheduler`.`tb_reserva` (`id`, `is_ativa`, `tp_reserva`, `id_usuario`, `id_laboratorio_horario`) VALUES (DEFAULT, 1, 'evento', 4, 4);
INSERT INTO `lab_scheduler`.`tb_reserva` (`id`, `is_ativa`, `tp_reserva`, `id_usuario`, `id_laboratorio_horario`) VALUES (DEFAULT, 0, 'aula', 5, 5);
INSERT INTO `lab_scheduler`.`tb_reserva` (`id`, `is_ativa`, `tp_reserva`, `id_usuario`, `id_laboratorio_horario`) VALUES (DEFAULT, 1, 'aula', 6, 6);
INSERT INTO `lab_scheduler`.`tb_reserva` (`id`, `is_ativa`, `tp_reserva`, `id_usuario`, `id_laboratorio_horario`) VALUES (DEFAULT, 1, 'aula', 7, 7);
INSERT INTO `lab_scheduler`.`tb_reserva` (`id`, `is_ativa`, `tp_reserva`, `id_usuario`, `id_laboratorio_horario`) VALUES (DEFAULT, 1, 'aula', 8, 8);
INSERT INTO `lab_scheduler`.`tb_reserva` (`id`, `is_ativa`, `tp_reserva`, `id_usuario`, `id_laboratorio_horario`) VALUES (DEFAULT, 0, 'reuniao', 9, 9);
INSERT INTO `lab_scheduler`.`tb_reserva` (`id`, `is_ativa`, `tp_reserva`, `id_usuario`, `id_laboratorio_horario`) VALUES (DEFAULT, 1, 'reuniao', 10, 10);
INSERT INTO `lab_scheduler`.`tb_reserva` (`id`, `is_ativa`, `tp_reserva`, `id_usuario`, `id_laboratorio_horario`) VALUES (DEFAULT, 1, 'manutencao', 11, 11);
INSERT INTO `lab_scheduler`.`tb_reserva` (`id`, `is_ativa`, `tp_reserva`, `id_usuario`, `id_laboratorio_horario`) VALUES (DEFAULT, 0, 'aula', 12, 12);
INSERT INTO `lab_scheduler`.`tb_reserva` (`id`, `is_ativa`, `tp_reserva`, `id_usuario`, `id_laboratorio_horario`) VALUES (DEFAULT, 0, 'aula', 13, 13);
INSERT INTO `lab_scheduler`.`tb_reserva` (`id`, `is_ativa`, `tp_reserva`, `id_usuario`, `id_laboratorio_horario`) VALUES (DEFAULT, 1, 'evento', 14, 14);
INSERT INTO `lab_scheduler`.`tb_reserva` (`id`, `is_ativa`, `tp_reserva`, `id_usuario`, `id_laboratorio_horario`) VALUES (DEFAULT, 1, 'aula', 15, 15);



-- Seleciona todas as reservas
SELECT * FROM `tb_reserva`;

-- Seleciona as reservas ativas
SELECT * FROM `tb_reserva` WHERE `is_ativa` = 1;

-- Seleciona as reservas do tipo 'Aula'
SELECT * FROM `tb_reserva` WHERE `tp_reserva` = 'Aula';

-- Seleciona todas as reservas inativas
SELECT id, tp_reserva, is_ativa FROM tb_reserva WHERE is_ativa = 0;
