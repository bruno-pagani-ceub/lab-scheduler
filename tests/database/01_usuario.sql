USE lab_scheduler ;

INSERT INTO `lab_scheduler`.`td_tipo_usuario` (`id`, `ds_tipo_usuario`) VALUES (DEFAULT, 'Aluno');
INSERT INTO `lab_scheduler`.`td_tipo_usuario` (`id`, `ds_tipo_usuario`) VALUES (DEFAULT, 'Professor');
INSERT INTO `lab_scheduler`.`td_tipo_usuario` (`id`, `ds_tipo_usuario`) VALUES (DEFAULT, 'Funcionario');
INSERT INTO `lab_scheduler`.`td_tipo_usuario` (`id`, `ds_tipo_usuario`) VALUES (DEFAULT, 'Visitante');

INSERT INTO `lab_scheduler`.`tb_usuario` (`id`, `nm_usuario`, `id_tipo_usuario`, `ds_identificacao`) VALUES (DEFAULT, 'Gustavo Vinicius', 1, 'RA11111111');
INSERT INTO `lab_scheduler`.`tb_usuario` (`id`, `nm_usuario`, `id_tipo_usuario`, `ds_identificacao`) VALUES (DEFAULT, 'Pedro Medina', 2, 'Matricula_Prof001');
INSERT INTO `lab_scheduler`.`tb_usuario` (`id`, `nm_usuario`, `id_tipo_usuario`, `ds_identificacao`) VALUES (DEFAULT, 'Vitor Marques', 3, 'Func001');
INSERT INTO `lab_scheduler`.`tb_usuario` (`id`, `nm_usuario`, `id_tipo_usuario`, `ds_identificacao`) VALUES (DEFAULT, 'Ana Clara', 4, 'CPF11111111111');
INSERT INTO `lab_scheduler`.`tb_usuario` (`id`, `nm_usuario`, `id_tipo_usuario`, `ds_identificacao`) VALUES (DEFAULT, 'Cristiane Araujo', 1, 'RA22222222');
INSERT INTO `lab_scheduler`.`tb_usuario` (`id`, `nm_usuario`, `id_tipo_usuario`, `ds_identificacao`) VALUES (DEFAULT, 'Marcelo Paiva', 2, 'Matricula_Prof002');
INSERT INTO `lab_scheduler`.`tb_usuario` (`id`, `nm_usuario`, `id_tipo_usuario`, `ds_identificacao`) VALUES (DEFAULT, 'Rafael Carvalho', 1, 'RA33333333');
INSERT INTO `lab_scheduler`.`tb_usuario` (`id`, `nm_usuario`, `id_tipo_usuario`, `ds_identificacao`) VALUES (DEFAULT, 'Carlos Eduardo', 2, 'Matricula_Prof003');
INSERT INTO `lab_scheduler`.`tb_usuario` (`id`, `nm_usuario`, `id_tipo_usuario`, `ds_identificacao`) VALUES (DEFAULT, 'Tamires Coelho', 2, 'Matricula_Prof004');
INSERT INTO `lab_scheduler`.`tb_usuario` (`id`, `nm_usuario`, `id_tipo_usuario`, `ds_identificacao`) VALUES (DEFAULT, 'Lucca Lima', 1, 'RA44444444');
INSERT INTO `lab_scheduler`.`tb_usuario` (`id`, `nm_usuario`, `id_tipo_usuario`, `ds_identificacao`) VALUES (DEFAULT, 'Enzo Amorim', 1, 'RA55555555');
INSERT INTO `lab_scheduler`.`tb_usuario` (`id`, `nm_usuario`, `id_tipo_usuario`, `ds_identificacao`) VALUES (DEFAULT, 'Divino Fernandes', 3, 'Func002');
INSERT INTO `lab_scheduler`.`tb_usuario` (`id`, `nm_usuario`, `id_tipo_usuario`, `ds_identificacao`) VALUES (DEFAULT, 'Maria Pereira', 4, 'CPF22222222222');
INSERT INTO `lab_scheduler`.`tb_usuario` (`id`, `nm_usuario`, `id_tipo_usuario`, `ds_identificacao`) VALUES (DEFAULT, 'Lurdes Almeida', 3, 'Func003');
INSERT INTO `lab_scheduler`.`tb_usuario` (`id`, `nm_usuario`, `id_tipo_usuario`, `ds_identificacao`) VALUES (DEFAULT, 'Mario Senna', 1, 'RA66666666');


-- Seleciona todos os tipos de usuário
SELECT * FROM `td_tipo_usuario`;

-- Seleciona apenas o tipo de usuário 'Aluno'
SELECT * FROM `td_tipo_usuario` WHERE `ds_tipo_usuario` = 'Aluno';

-- Conta quantos tipos de usuários existem na tabela
SELECT COUNT(*) AS total_tipos FROM `td_tipo_usuario`;

-- Seleciona os tipos de usuários com IDs maiores que 1
SELECT id, ds_tipo_usuario FROM td_tipo_usuario WHERE id > 1;





-- Seleciona todos os usuários
SELECT * FROM `tb_usuario`;

-- Seleciona os usuários que são do tipo 'Aluno'
SELECT `id`, `nm_usuario` FROM `tb_usuario` WHERE `id_tipo_usuario` = 1;

-- Seleciona o usuário com o ID 2
SELECT * FROM `tb_usuario` WHERE `id` = 2;

-- Seleciona os usuários que possuem 'Ana' no nome
SELECT id, nm_usuario, ds_identificacao FROM tb_usuario WHERE nm_usuario LIKE '%Mario%';

