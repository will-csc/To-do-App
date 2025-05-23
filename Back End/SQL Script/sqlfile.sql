DROP DATABASE IF EXISTS todo_app;
CREATE DATABASE IF NOT EXISTS todo_app;
USE todo_app;

/*------------------ TABELA DE USUARIOS ----------------*/
CREATE TABLE IF NOT EXISTS users(
	id_user INT PRIMARY KEY AUTO_INCREMENT,
	username VARCHAR(50) NOT NULL UNIQUE,
    e_mail VARCHAR(50) NOT NULL UNIQUE,
    phone BIGINT NOT NULL,
    userpassword VARCHAR(50) NOT NULL,
    retrieve_code BIGINT NOT NULL,
    user_rank INT DEFAULT 1 NOT NULL
);
ALTER TABLE users ADD CONSTRAINT chk_retrieve_code CHECK (retrieve_code > 999999999);
ALTER TABLE users ADD CONSTRAINT chk_user_rank CHECK (user_rank IN (1,2));

/*------------------ TABELA DE DOCUMENTOS RELACIONADOS AO USUÁRIO ----------------*/
CREATE TABLE IF NOT EXISTS documents(
	id_docs INT PRIMARY KEY AUTO_INCREMENT,
    id_user INT NOT NULL,
    doc_name VARCHAR(100) NOT NULL,
    doc_path VARCHAR(500) NOT NULL UNIQUE,
    deadline DATE NOT NULL,
    week_day VARCHAR(10) NOT NULL,
    FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE
    CASCADE ON UPDATE CASCADE
);

/*---------------- FUNÇÃO PARA PREENCHER NOME DO DIA --------------------------*/
DELIMITER $$

CREATE FUNCTION nome_dia_semana(data DATE) RETURNS VARCHAR(10)
DETERMINISTIC
BEGIN
    DECLARE dia_semana INT;
    SET dia_semana = WEEKDAY(data); -- Segunda = 0, Domingo = 6

    RETURN CASE dia_semana
        WHEN 0 THEN 'Segunda'
        WHEN 1 THEN 'Terça'
        WHEN 2 THEN 'Quarta'
        WHEN 3 THEN 'Quinta'
        WHEN 4 THEN 'Sexta'
        WHEN 5 THEN 'Sábado'
        WHEN 6 THEN 'Domingo'
    END;
END$$

DELIMITER ;

/*------------ TRIGGER PARA INSERÇÃO AUTOMÁTICA -----------------*/
DELIMITER $$

CREATE TRIGGER before_insert_documents
BEFORE INSERT ON documents
FOR EACH ROW
BEGIN
    SET NEW.week_day = nome_dia_semana(NEW.deadline);
END$$

DELIMITER ;
