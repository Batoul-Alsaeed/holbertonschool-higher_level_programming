-- Create database hbtn_0d_usa and table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT NOT NULL UNIQUE PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
