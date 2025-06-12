CREATE TABLE contratos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    data_inicio DATE NOT NULL,
    data_fim DATE NOT NULL
);

INSERT INTO contratos (nome, data_inicio, data_fim)
VALUES ('Contrato Exemplo', '2024-06-01', '2025-06-01');