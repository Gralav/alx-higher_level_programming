-- script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server
ALTER DATABASE `hbtn_0c_0` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE `hbtn_0c_0`.`first_table` CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE `hbtn_0c_0`.`first_table` CHANGE `name` `name` VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
-- SELECT CONVERT(CAST(`name` AS BINARY) USING utf8mb4 COLLATE utf8mb4_unicode_ci) AS `name` FROM `first_table`;
