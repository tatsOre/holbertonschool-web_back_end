-- 0-uniq_users.sql / 0x0C. MySQL advanced /  Web Stack programming ― Back-end
-- Context: Making an attribute unique directly in the table schema will enforce
-- the business rules and avoid bugs in an application
CREATE TABLE IF NOT EXISTS `users` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `email` VARCHAR(255) NOT NULL UNIQUE,
    `name` VARCHAR(255)
    PRIMARY KEY (id)
);
