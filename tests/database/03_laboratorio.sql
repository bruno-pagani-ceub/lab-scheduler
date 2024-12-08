USE lab_scheduler;

INSERT INTO `lab_scheduler`.`tb_laboratorio` (`id`, `ds_bloco`, `ds_sala`, `qtd_pcs`) VALUES (DEFAULT, 'A', '1001', 25);
INSERT INTO `lab_scheduler`.`tb_laboratorio` (`id`, `ds_bloco`, `ds_sala`, `qtd_pcs`) VALUES (DEFAULT, 'A', '1002', 30);
INSERT INTO `lab_scheduler`.`tb_laboratorio` (`id`, `ds_bloco`, `ds_sala`, `qtd_pcs`) VALUES (DEFAULT, 'B', '2001', 35);
INSERT INTO `lab_scheduler`.`tb_laboratorio` (`id`, `ds_bloco`, `ds_sala`, `qtd_pcs`) VALUES (DEFAULT, 'C', '3001', 40);
INSERT INTO `lab_scheduler`.`tb_laboratorio` (`id`, `ds_bloco`, `ds_sala`, `qtd_pcs`) VALUES (DEFAULT, 'D', '4001', 15);
INSERT INTO `lab_scheduler`.`tb_laboratorio` (`id`, `ds_bloco`, `ds_sala`, `qtd_pcs`) VALUES (DEFAULT, 'D', '4002', 28);
INSERT INTO `lab_scheduler`.`tb_laboratorio` (`id`, `ds_bloco`, `ds_sala`, `qtd_pcs`) VALUES (DEFAULT, 'D', '4003', 32);
INSERT INTO `lab_scheduler`.`tb_laboratorio` (`id`, `ds_bloco`, `ds_sala`, `qtd_pcs`) VALUES (DEFAULT, 'E', '5001', 40);
INSERT INTO `lab_scheduler`.`tb_laboratorio` (`id`, `ds_bloco`, `ds_sala`, `qtd_pcs`) VALUES (DEFAULT, 'E', '5001', 15);
INSERT INTO `lab_scheduler`.`tb_laboratorio` (`id`, `ds_bloco`, `ds_sala`, `qtd_pcs`) VALUES (DEFAULT, 'E', '5001', 22);
INSERT INTO `lab_scheduler`.`tb_laboratorio` (`id`, `ds_bloco`, `ds_sala`, `qtd_pcs`) VALUES (DEFAULT, 'F', '6001', 25);
INSERT INTO `lab_scheduler`.`tb_laboratorio` (`id`, `ds_bloco`, `ds_sala`, `qtd_pcs`) VALUES (DEFAULT, 'G', '7001', 30);
INSERT INTO `lab_scheduler`.`tb_laboratorio` (`id`, `ds_bloco`, `ds_sala`, `qtd_pcs`) VALUES (DEFAULT, 'G', '7002', 20);
INSERT INTO `lab_scheduler`.`tb_laboratorio` (`id`, `ds_bloco`, `ds_sala`, `qtd_pcs`) VALUES (DEFAULT, 'G', '7003', 35);
INSERT INTO `lab_scheduler`.`tb_laboratorio` (`id`, `ds_bloco`, `ds_sala`, `qtd_pcs`) VALUES (DEFAULT, 'H', '8001', 33);



-- Seleciona todos os laboratórios
SELECT * FROM `tb_laboratorio`;

-- Seleciona os laboratórios que estão no bloco 'A'
SELECT * FROM `tb_laboratorio` WHERE `ds_bloco` = 'A';

-- Conta quantos computadores (qtd_pcs) há no total em todos os laboratórios
SELECT SUM(`qtd_pcs`) AS total_computadores FROM `tb_laboratorio`;

-- Lista os laboratórios que possuem até 30 computadores
SELECT id, ds_bloco, ds_sala, qtd_pcs FROM tb_laboratorio WHERE qtd_pcs <= 30;
