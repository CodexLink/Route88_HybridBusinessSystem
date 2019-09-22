USE Route88_Management

if exists (select name from sys.tables where name = 'ItemMenu')
DELETE FROM ItemMenu
GO

INSERT INTO ItemMenu VALUES (101, 'Classic Buffalo', 148.00, 148, '01/01/2020 11:00:00', '01/01/2020 20:00:00');
INSERT INTO ItemMenu VALUES (102, 'Creamy Carbonara', 90.00, 90, '02/02/2020 12:00:00', '02/02/2020 20:00:00');
INSERT INTO ItemMenu VALUES (103, 'Salisbury Steak', 110.00, 110, '03/03/2020 11:00:00', '03/03/2020 20:00:00');
INSERT INTO ItemMenu VALUES (104, 'Pork Sisig', 108.00, 108, '04/04/2020 12:00:00', '04/04/2020 20:00:00');
INSERT INTO ItemMenu VALUES (105, 'Sizzling Buttered', 128.00, 128, '05/05/2020 11:00:00', '05/05/2020 20:00:00');
INSERT INTO ItemMenu VALUES (106, 'Lechon Kawali', 148.00, 148, '06/06/2020 12:00:00', '06/06/2020 20:00:00');
INSERT INTO ItemMenu VALUES (107, 'Mais Con Yelo', 35.00, 35, '07/07/2020 11:00:00', '07/07/2020 20:00:00');
INSERT INTO ItemMenu VALUES (108, 'Glazzed Banana', 60.00, 60, '08/08/2020 12:00:00', '08/08/2020 20:00:00');
INSERT INTO ItemMenu VALUES (109, 'Wicked Oreos', 88.00, 88, '09/09/2020 11:00:00', '09/09/2020 20:00:00');
INSERT INTO ItemMenu VALUES (110, 'Grand Tour Ribs', 248.00, 248, '10/10/2020 12:00:00', '10/10/2020 20:00:00');


GO
if exists (select name from sys.tables where name = 'InventoryItem ')
DELETE FROM InventoryItem
GO

INSERT INTO InventoryItem VALUES (1, 'Chicken', 'Thigh', '85.00', '01/05/2020', 5, '01/02/2020 13:00:00', '01/02/2020 20:00:00');
INSERT INTO InventoryItem VALUES (2, 'Fish', 'Bangus', '120.00', '02/06/2020', 5, '02/03/2020 13:00:00', '01/03/2020 20:00:00');
INSERT INTO InventoryItem VALUES (3, 'Sisig', 'Tuna', '90.00', '03/07/2020', 5, '03/04/2020 13:00:00', '03/04/2020 20:00:00');
INSERT INTO InventoryItem VALUES (4, 'Ice Cream', 'Chocolate', '110.00', '04/08/2020', 5, '04/05/2020 13:00:00', '04/05/2020 20:00:00');
INSERT INTO InventoryItem VALUES (5, 'Juice', 'Pineapple', '50.00', '05/09/2020', 5, '05/06/2020 13:00:00', '05/06/2020 20:00:00');
INSERT INTO InventoryItem VALUES (6, 'Cake', 'Ube', '99.00', '06/10/2020', 5, '06/07/2020 13:00:00', '06/07/2020 20:00:00');
INSERT INTO InventoryItem VALUES (7, 'Pasta', 'Spaghetti', '95.00', '07/11/2020', 5, '07/08/2020 13:00:00', '07/08/2020 20:00:00');
INSERT INTO InventoryItem VALUES (8, 'Burger', 'Longganisa burger', '115.00', '08/12/2020', 5, '08/09/2020 13:00:00', '08/09/2020 20:00:00');
INSERT INTO InventoryItem VALUES (9, 'Fries', 'Fries barbeque', '80.00', '09/13/2020', 5, '09/10/2020 13:00:00', '09/10/2020 20:00:00');
INSERT INTO InventoryItem VALUES (10, 'Wings', 'Chili garlic', '130.00', '10/14/2020', 5, '10/11/2020 13:00:00', '10/11/2020 20:00:00');

GO


if exists (select name from sys.tables where name = 'SupplierReference')
DELETE FROM SupplierReference
GO

INSERT INTO SupplierReference VALUES (1111, 'Honey Garlic', '01/15/2020', '01/16/2020', '01/16/2020 11:00:00', '01/16/2020 20:00:00');
INSERT INTO SupplierReference VALUES (2222, 'Creamy Carbonara', '02/20/2020', '02/21/2020', '02/21/2020 12:00:00', '02/21/2020 20:00:00');
INSERT INTO SupplierReference VALUES (3333, 'Banana Con Yelo', '03/25/2020', '03/26/2020', '03/26/2020 13:00:00', '03/26/2020 20:00:00');
INSERT INTO SupplierReference VALUES (4444, 'Sizzling Hotdog', '04/05/2020', '04/06/2020', '04/06/2020 11:00:00', '04/06/2020 20:00:00');
INSERT INTO SupplierReference VALUES (5555, 'Chicken Burger', '05/10/2020', '05/11/2020', '05/11/2020 12:00:00', '05/11/2020 20:00:00');
INSERT INTO SupplierReference VALUES (6666, 'Cheesy Garlic', '06/15/2020', '06/16/2020', '06/16/2020 13:00:00', '06/16/2020 20:00:00');
INSERT INTO SupplierReference VALUES (7777, 'Inihaw na Liempo', '07/22/2020', '07/23/2020', '07/23/2020 11:00:00', '07/23/2020 20:00:00');
INSERT INTO SupplierReference VALUES (8888, 'Smoky Barbeque', '08/27/2020', '08/28/2020', '08/28/2020 12:00:00', '08/28/2020 20:00:00');
INSERT INTO SupplierReference VALUES (9999, 'Wicked Oreos', '09/02/2020', '09/03/2020', '09/03/2020 13:00:00', '09/03/2020 20:00:00');
INSERT INTO SupplierReference VALUES (1010, 'Spaghetti Bolognese', '10/13/2020', '10/14/2020', '10/14/2020 11:00:00', '10/14/2020 20:00:00');


GO

if exists (select name from sys.tables where name = 'SupplierTransaction')
DELETE FROM SupplierTransaction
GO

INSERT INTO SupplierTransaction VALUES (1, 123, 1111, '01/02/2020', 148, '01/02/2020 12:00:00', '01/02/2020 20:00:00');
INSERT INTO SupplierTransaction VALUES (2, 234, 2222, '02/04/2020', 90, '02/04/2020 11:00:00', '02/04/2020 20:00:00');
INSERT INTO SupplierTransaction VALUES (3, 345, 3333, '03/06/2020', 35, '03/06/2020 12:00:00', '03/06/2020 20:00:00');
INSERT INTO SupplierTransaction VALUES (4, 456, 4444, '04/08/2020', 108, '04/08/2020 11:00:00', '04/08/2020 20:00:00');
INSERT INTO SupplierTransaction VALUES (5, 567, 5555, '05/10/2020', 90, '05/10/2020 12:00:00', '05/10/2020 20:00:00');
INSERT INTO SupplierTransaction VALUES (6, 678, 6666, '06/12/2020', 148, '06/12/2020 11:00:00', '06/12/2020 20:00:00');
INSERT INTO SupplierTransaction VALUES (7, 789, 7777, '07/14/2020', 148, '07/14/2020 12:00:00', '07/14/2020 20:00:00');
INSERT INTO SupplierTransaction VALUES (8, 890, 8888, '08/16/2020', 148, '08/16/2020 11:00:00', '08/16/2020 20:00:00');
INSERT INTO SupplierTransaction VALUES (9, 901, 9999, '09/18/2020', 88, '09/18/2020 12:00:00', '09/18/2020 20:00:00');
INSERT INTO SupplierTransaction VALUES (10, 012, 1010, '10/20/2020', 90, '10/20/2020 13:00:00', '10/20/2020 20:00:00');

GO

Select * from ItemMenu
Select * from InventoryItem
Select * from SupplierReference
Select * from SupplierTransaction

GO