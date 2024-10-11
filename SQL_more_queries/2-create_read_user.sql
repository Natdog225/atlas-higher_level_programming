-- Creates the database `hbtn_0d_2` if it doesn't exist.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Creates the user `user_0d_2` with the specified password and grants SELECT privileges on the database `hbtn_0d_2`.
CREATE USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';