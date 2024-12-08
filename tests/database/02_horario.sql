USE lab_scheduler;

INSERT INTO `lab_scheduler`.`tb_horario` (`id`, `dt_dia`, `hr_inicio`, `hr_fim`) VALUES (DEFAULT, '2024-11-20', '08:00:00', '10:00:00');
INSERT INTO `lab_scheduler`.`tb_horario` (`id`, `dt_dia`, `hr_inicio`, `hr_fim`) VALUES (DEFAULT, '2024-11-20', '09:00:00', '10:30:00');
INSERT INTO `lab_scheduler`.`tb_horario` (`id`, `dt_dia`, `hr_inicio`, `hr_fim`) VALUES (DEFAULT, '2024-11-21', '16:00:00', '17:00:00');
INSERT INTO `lab_scheduler`.`tb_horario` (`id`, `dt_dia`, `hr_inicio`, `hr_fim`) VALUES (DEFAULT, '2024-11-22', '19:00:00', '22:00:00');
INSERT INTO `lab_scheduler`.`tb_horario` (`id`, `dt_dia`, `hr_inicio`, `hr_fim`) VALUES (DEFAULT, '2024-11-23', '15:00:00', '15:00:00');
INSERT INTO `lab_scheduler`.`tb_horario` (`id`, `dt_dia`, `hr_inicio`, `hr_fim`) VALUES (DEFAULT, '2024-11-25', '08:00:00', '10:00:00');
INSERT INTO `lab_scheduler`.`tb_horario` (`id`, `dt_dia`, `hr_inicio`, `hr_fim`) VALUES (DEFAULT, '2024-11-25', '10:30:00', '11:30:00');
INSERT INTO `lab_scheduler`.`tb_horario` (`id`, `dt_dia`, `hr_inicio`, `hr_fim`) VALUES (DEFAULT, '2024-11-25', '14:00:00', '16:00:00');
INSERT INTO `lab_scheduler`.`tb_horario` (`id`, `dt_dia`, `hr_inicio`, `hr_fim`) VALUES (DEFAULT, '2024-11-25', '18:00:00', '19:00:00');
INSERT INTO `lab_scheduler`.`tb_horario` (`id`, `dt_dia`, `hr_inicio`, `hr_fim`) VALUES (DEFAULT, '2024-11-25', '20:00:00', '22:00:00');
INSERT INTO `lab_scheduler`.`tb_horario` (`id`, `dt_dia`, `hr_inicio`, `hr_fim`) VALUES (DEFAULT, '2024-11-26', '10:00:00', '12:00:00');
INSERT INTO `lab_scheduler`.`tb_horario` (`id`, `dt_dia`, `hr_inicio`, `hr_fim`) VALUES (DEFAULT, '2024-11-27', '15:00:00', '17:00:00');
INSERT INTO `lab_scheduler`.`tb_horario` (`id`, `dt_dia`, `hr_inicio`, `hr_fim`) VALUES (DEFAULT, '2024-11-27', '18:00:00', '20:00:00');
INSERT INTO `lab_scheduler`.`tb_horario` (`id`, `dt_dia`, `hr_inicio`, `hr_fim`) VALUES (DEFAULT, '2024-11-27', '20:30:00', '21:30:00');
INSERT INTO `lab_scheduler`.`tb_horario` (`id`, `dt_dia`, `hr_inicio`, `hr_fim`) VALUES (DEFAULT, '2024-11-28', '09:00:00', '10:00:00');
INSERT INTO `lab_scheduler`.`tb_horario` (`id`, `dt_dia`, `hr_inicio`, `hr_fim`) VALUES (DEFAULT, '2024-11-28', '11:30:00', '12:00:00');



-- Seleciona todos os horários
SELECT * FROM `tb_horario`;

-- Seleciona os horários em que o dia é '2024-11-25'
SELECT * FROM `tb_horario` WHERE `dt_dia` = '2024-11-25';

-- Seleciona os horários que começam antes das 10:00
SELECT * FROM `tb_horario` WHERE `hr_inicio` < '10:00:00';

-- Seleciona os horários que terminam antes das 18:00
SELECT id, dt_dia, hr_inicio, hr_fim FROM tb_horario WHERE hr_fim < '18:00:00';
