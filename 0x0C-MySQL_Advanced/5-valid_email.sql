-- 5-valid_email.sql / 0x0C. MySQL advanced /  Web Stack programming ― Back-end
--  Creates a trigger that resets the attribute valid_email only when the email has been changed
DELIMITER $$
CREATE
    TRIGGER `email_validation`
    BEFORE UPDATE ON `users`
    FOR EACH ROW
    BEGIN
        IF NEW.email <> OLD.email
            THEN
                SET NEW.valid_email = !OLD.valid_email;
        END IF;
    END$$
DELIMITER ;
