USE lab_scheduler;

INSERT INTO `td_tipo_usuario` (`id`, `ds_tipo_usuario`) VALUES (DEFAULT, 'Aluno');
INSERT INTO `td_tipo_usuario` (`id`, `ds_tipo_usuario`) VALUES (DEFAULT, 'Professor');
INSERT INTO `td_tipo_usuario` (`id`, `ds_tipo_usuario`) VALUES (DEFAULT, 'Funcionario');
INSERT INTO `td_tipo_usuario` (`id`, `ds_tipo_usuario`) VALUES (DEFAULT, 'Visitante');

INSERT INTO `tb_usuario` (`id`, `nm_usuario`, `id_tipo_usuario`, `ds_identificacao`) VALUES (DEFAULT, 'Gustavo Vinicius', 1, '12345678');
INSERT INTO `tb_usuario` (`id`, `nm_usuario`, `id_tipo_usuario`, `ds_identificacao`) VALUES (DEFAULT, 'Pedro Medina', 2, '123456');
INSERT INTO `tb_usuario` (`id`, `nm_usuario`, `id_tipo_usuario`, `ds_identificacao`) VALUES (DEFAULT, 'Vitor Marques', 3, '1234567');
INSERT INTO `tb_usuario` (`id`, `nm_usuario`, `id_tipo_usuario`, `ds_identificacao`) VALUES (DEFAULT, 'Ana Clara', 4, '12345678910');
INSERT INTO `tb_usuario` (`id`, `nm_usuario`, `id_tipo_usuario`, `ds_identificacao`) VALUES (DEFAULT, 'Cristiane Araujo', 1, '22222222');
INSERT INTO `tb_usuario` (`id`, `nm_usuario`, `id_tipo_usuario`, `ds_identificacao`) VALUES (DEFAULT, 'Marcelo Paiva', 2, '000002');
INSERT INTO `tb_usuario` (`id`, `nm_usuario`, `id_tipo_usuario`, `ds_identificacao`) VALUES (DEFAULT, 'Rafael Carvalho', 1, '33333333');
INSERT INTO `tb_usuario` (`id`, `nm_usuario`, `id_tipo_usuario`, `ds_identificacao`) VALUES (DEFAULT, 'Carlos Eduardo', 2, '000003');
INSERT INTO `tb_usuario` (`id`, `nm_usuario`, `id_tipo_usuario`, `ds_identificacao`) VALUES (DEFAULT, 'Tamires Coelho', 2, '000004');
INSERT INTO `tb_usuario` (`id`, `nm_usuario`, `id_tipo_usuario`, `ds_identificacao`) VALUES (DEFAULT, 'Lucca Lima', 1, '44444444');
INSERT INTO `tb_usuario` (`id`, `nm_usuario`, `id_tipo_usuario`, `ds_identificacao`) VALUES (DEFAULT, 'Enzo Amorim', 1, '55555555');
INSERT INTO `tb_usuario` (`id`, `nm_usuario`, `id_tipo_usuario`, `ds_identificacao`) VALUES (DEFAULT, 'Divino Fernandes', 3, '0000002');
INSERT INTO `tb_usuario` (`id`, `nm_usuario`, `id_tipo_usuario`, `ds_identificacao`) VALUES (DEFAULT, 'Maria Pereira', 4, '22222222222');
INSERT INTO `tb_usuario` (`id`, `nm_usuario`, `id_tipo_usuario`, `ds_identificacao`) VALUES (DEFAULT, 'Lurdes Almeida', 3, '0000003');
INSERT INTO `tb_usuario` (`id`, `nm_usuario`, `id_tipo_usuario`, `ds_identificacao`) VALUES (DEFAULT, 'Mario Senna', 1, '66666666');
INSERT INTO `tb_usuario` (`id`, `nm_usuario`, `id_tipo_usuario`, `ds_identificacao`) VALUES (DEFAULT, 'Mario Senna', 1, '66666666');
