-- Criação do banco de dados
CREATE DATABASE IF NOT EXISTS lab_scheduler;
USE lab_scheduler;

-- Tabela de tipos de usuário
CREATE TABLE td_tipo_usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ds_tipo_usuario VARCHAR(50) NOT NULL UNIQUE
);

-- Tabela de usuários
CREATE TABLE tb_usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nm_usuario VARCHAR(80) NOT NULL,
    id_tipo_usuario INT NOT NULL,
    ds_identificacao VARCHAR(50) NOT NULL,
    FOREIGN KEY (id_tipo_usuario) REFERENCES td_tipo_usuario(id)
);

-- Tabela de laboratorio
CREATE TABLE tb_laboratorio (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ds_bloco VARCHAR(10) NOT NULL,
    ds_sala VARCHAR(10) NOT NULL,
    qtd_pcs INT NOT NULL
);

-- Tabela de horario
CREATE TABLE tb_horario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dt_dia DATE NOT NULL,
    hr_inicio TIME NOT NULL,
    hr_fim TIME NOT NULL
);

-- Tabela associativa laboratorio_horario
CREATE TABLE ta_laboratorio_horario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_laboratorio INT NOT NULL,
    id_horario INT NOT NULL,
    FOREIGN KEY (id_laboratorio) REFERENCES tb_laboratorio(id),
    FOREIGN KEY (id_horario) REFERENCES tb_horario(id),
    UNIQUE (id_laboratorio, id_horario)
);

-- Tabela de reserva
CREATE TABLE tb_reserva (
    id INT AUTO_INCREMENT PRIMARY KEY,
    is_ativa BOOLEAN NOT NULL DEFAULT TRUE,
    tp_reserva VARCHAR(50) NOT NULL,
    id_usuario INT NOT NULL,
    id_laboratorio_horario INT NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES tb_usuario(id),
    FOREIGN KEY (id_laboratorio_horario) REFERENCES ta_laboratorio_horario(id)
);
