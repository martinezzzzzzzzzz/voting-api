-- schema.sql

DROP DATABASE IF EXISTS voting_db;
CREATE DATABASE voting_db;
USE voting_db;

CREATE TABLE voters (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    has_voted BOOLEAN DEFAULT FALSE
);

CREATE TABLE candidates (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    party VARCHAR(255),
    votes_count INT DEFAULT 0
);

CREATE TABLE votes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    voter_id INT NOT NULL UNIQUE,
    candidate_id INT NOT NULL,
    FOREIGN KEY (voter_id) REFERENCES voters(id) ON DELETE CASCADE,
    FOREIGN KEY (candidate_id) REFERENCES candidates(id) ON DELETE CASCADE
);

-- Insert some test voters
INSERT INTO voters (name, email, has_voted) VALUES
('Juan Pérez', 'juan@example.com', FALSE),
('Ana López', 'ana@example.com', FALSE);

-- Insert some test candidates
INSERT INTO candidates (name, party, votes_count) VALUES
('Carlos Sánchez', 'Partido Azul', 0),
('María Gómez', 'Partido Rojo', 0);
