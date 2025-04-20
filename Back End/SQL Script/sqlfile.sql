DROP DATABASE IF EXISTS todo_app;
CREATE DATABASE IF NOT EXISTS todo_app;
USE todo_app;

/*------------------ TABELA DE USUARIOS ----------------*/
CREATE TABLE IF NOT EXISTS users(
	id_user INT PRIMARY KEY AUTO_INCREMENT,
	username VARCHAR(50) NOT NULL,
    e_mail VARCHAR(50) NOT NULL,
    phone BIGINT NOT NULL,
    userpassword VARCHAR(50) NOT NULL,
    image VARCHAR(1000),
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
    deadline DATE,
    FOREIGN KEY (id_user) REFERENCES users(id_user) ON DELETE
    CASCADE ON UPDATE CASCADE
);
