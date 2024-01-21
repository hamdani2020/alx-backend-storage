-- This script creates a trigger that decreases the quantity of an 
-- item adding a new order.

DROP TRIGGER IF EXISTS reduce_quantity;
DELIMITER $$
CREATE TRIGGER reduce_quantity
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
        SET amount = amount - NEW.number
	WHERE name = NEW.item_name;
END $$
DELIMITER ;
