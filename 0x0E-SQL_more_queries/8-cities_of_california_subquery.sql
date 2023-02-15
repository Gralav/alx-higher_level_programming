-- Script that lists all the cities of California that can be found in the database hbtn_0d_usa
SELECT `cities`.`id`, `cities`.`name`
FROM `cities`, `states`
WHERE `cities`.`state_id` = `states`.`id`
AND `states`.`name` = "California"
ORDER BY `cities`.`id` ASC;

-- Does NOT work because in the "states table the state_id can be different than what shown in the example":
-- SELECT `id`, `name` FROM `cities` WHERE `state_id` = 1 ORDER BY `id` ASC;
