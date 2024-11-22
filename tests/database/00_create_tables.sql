-- Tabela de usuario
CREATE TABLE tb_usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nm_usuario VARCHAR(80) NOT NULL,
    tp_posicao ENUM('aluno', 'professor', 'funcionario', 'visitante') NOT NULL,
    ds_identificacao VARCHAR(30) NOT NULL );

-- Tabela de laboratorio
CREATE TABLE tb_laboratorio (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ds_bloco VARCHAR(10) NOT NULL,
    ds_sala VARCHAR(10) NOT NULL,
    qtd_pcs INT NOT NULL );

-- Tabela de horario
CREATE TABLE tb_horario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dt_dia DATE NOT NULL,
    ds_dia_semana ENUM('segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado', 'domingo') NOT NULL,
    hr_inicio TIME NOT NULL,
    hr_fim TIME NOT NULL,
    ds_semestre VARCHAR(10) NOT NULL,
    nr_ano YEAR NOT NULL );

-- Tabela associativa laboratorio_horario
CREATE TABLE ta_laboratorio_horario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_laboratorio INT NOT NULL,
    id_horario INT NOT NULL,
    is_reservado BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (id_laboratorio) REFERENCES tb_laboratorio(id),
    FOREIGN KEY (id_horario) REFERENCES tb_horario(id) );

-- Tabela de reserva
CREATE TABLE tb_reserva (
    id INT AUTO_INCREMENT PRIMARY KEY,
    st_reserva ENUM('confirmada', 'finalizada', 'cancelada') NOT NULL,
    tp_reserva VARCHAR(50) DEFAULT NULL,
    id_usuario INT NOT NULL,
    id_laboratorio_horario INT NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES tb_usuario(id),
    FOREIGN KEY (id_laboratorio_horario) REFERENCES ta_laboratorio_horario(id) );
