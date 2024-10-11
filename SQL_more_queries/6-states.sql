-- Creates the database `hbtn_0d_usa` if it doesn't exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Creates the table `states` in the `hbtn_0d_usa` database if it doesn't exist.
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);