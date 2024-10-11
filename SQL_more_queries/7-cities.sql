-- Creates the database `hbtn_0d_usa` if it doesn't exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Creates the table `cities` in the `hbtn_0d_usa` database if it doesn't exist.
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id)
);