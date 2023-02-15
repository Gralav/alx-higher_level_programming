-- Script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` (`id` INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
`state_id` INT NOT NULL,
`name` VARCHAR(256) NOT NULL,
FOREIGN KEY (`state_id`) REFERENCES `hbtn_0d_usa`.`states`(`id`));

-- Does NOT work on MySQL, but would work on some other DB management systems (SQL Server / Oracle / MS Access):
-- CREATE TABLE IF NOT EXISTS `hbtn_0d_usa`.`cities` (`id` INT NOT NULL UNIQUE AUTO_INCREMENT PRIMARY KEY,
-- `state_id` INT NOT NULL FOREIGN KEY REFERENCES `hbtn_0d_usa`.`states`(`id`),
-- `name` VARCHAR(256) NOT NULL);
