-- =============================================
-- Author:		Jan Patrick Moreno
-- Create date: 09/26/2019
-- Sub-Author:	Janrey Licas
-- Description:	Inserts All Other Table Data That Associated with the Management Part of Database.
-- =============================================

USE Route88_Database

DBCC CHECKIDENT(InventoryItem, RESEED, 0)
DBCC CHECKIDENT(SupplierReference, RESEED, 0)
DBCC CHECKIDENT(SupplierTransaction, RESEED, 0)
DBCC CHECKIDENT(CustTransaction, RESEED, 0)
DBCC CHECKIDENT(CustReceipt, RESEED, 0)

IF EXISTS (SELECT NAME FROM SYS.TABLES WHERE NAME = 'CustReceipt')
DELETE FROM CustReceipt
GO

IF EXISTS (SELECT NAME FROM SYS.TABLES WHERE NAME = 'CustTransaction')
DELETE FROM CustTransaction
GO


IF EXISTS (SELECT NAME FROM SYS.TABLES WHERE NAME = 'SupplierTransaction')
DELETE FROM SupplierTransaction
GO

IF EXISTS (SELECT NAME FROM SYS.TABLES WHERE NAME = 'SupplierReference')
DELETE FROM SupplierReference
GO

IF EXISTS (SELECT NAME FROM SYS.TABLES WHERE NAME = 'InventoryItem')
DELETE FROM InventoryItem
GO

INSERT SupplierReference VALUES ('Honey Garlic', '01/15/2020', '01/16/2020', '01/16/2020 11:00:00', '01/16/2020 20:00:00')
INSERT SupplierReference VALUES ('Creamy Carbonara', '02/20/2020', '02/21/2020', '02/21/2020 12:00:00', '02/21/2020 20:00:00')
INSERT SupplierReference VALUES ('Banana Con Yelo', '03/25/2020', '03/26/2020', '03/26/2020 13:00:00', '03/26/2020 20:00:00')
INSERT SupplierReference VALUES ('Sizzling Hotdog', '04/05/2020', '04/06/2020', '04/06/2020 11:00:00', '04/06/2020 20:00:00')
INSERT SupplierReference VALUES ('Chicken Burger', '05/10/2020', '05/11/2020', '05/11/2020 12:00:00', '05/11/2020 20:00:00')
INSERT SupplierReference VALUES ('Cheesy Garlic', '06/15/2020', '06/16/2020', '06/16/2020 13:00:00', '06/16/2020 20:00:00')
INSERT SupplierReference VALUES ('Inihaw na Liempo', '07/22/2020', '07/23/2020', '07/23/2020 11:00:00', '07/23/2020 20:00:00')
INSERT SupplierReference VALUES ('Smoky Barbeque', '08/27/2020', '08/28/2020', '08/28/2020 12:00:00', '08/28/2020 20:00:00')
INSERT SupplierReference VALUES ('Wicked Oreos', '09/02/2020', '09/03/2020', '09/03/2020 13:00:00', '09/03/2020 20:00:00')
INSERT SupplierReference VALUES ('Spaghetti Bolognese', '10/13/2020', '10/14/2020', '10/14/2020 11:00:00', '10/14/2020 20:00:00')
GO

INSERT InventoryItem VALUES ('Chicken', 'Ingredient Item', 'Food Part', 5, 85.00, '01/05/2020', '01/02/2020 13:00:00', '01/02/2020 20:00:00')
INSERT InventoryItem VALUES ('Fish', 'Ingredient Item', 'Food', 5, 120.00, '02/06/2020', '02/03/2020 13:00:00', '01/03/2020 20:00:00')
INSERT InventoryItem VALUES ('Sisig', 'Menu Item', 'Food Menu', 5, 90.00, '03/07/2020', '03/04/2020 13:00:00', '03/04/2020 20:00:00')
INSERT InventoryItem VALUES ('Ice Cream', 'Menu Item', 'Dessert', 5, 110.00, '04/08/2020', '04/05/2020 13:00:00', '04/05/2020 20:00:00')
INSERT InventoryItem VALUES ('Juice', 'Menu Item', 'Drinks', 5, 50.00, '05/09/2020', '05/06/2020 13:00:00', '05/06/2020 20:00:00')
INSERT InventoryItem VALUES ('Cake', 'Menu Item', 'Dessert', 5, 99.00, '06/10/2020', '06/07/2020 13:00:00', '06/07/2020 20:00:00')
INSERT InventoryItem VALUES ('Pasta', 'Menu Item', 'Dessert', 5, 95.00, '07/11/2020', '07/08/2020 13:00:00', '07/08/2020 20:00:00')
INSERT InventoryItem VALUES ('Burger', 'Menu Item', 'Food Menu', 5, 115.00, '08/12/2020', '08/09/2020 13:00:00', '08/09/2020 20:00:00')
INSERT InventoryItem VALUES ('Fries', 'Menu Item', 'Snacks', 5, 80.00, '09/13/2020', '09/10/2020 13:00:00', '09/10/2020 20:00:00')
INSERT InventoryItem VALUES ('Wings', 'Menu Item', 'Food Part', 5, 130.00, '10/14/2020', '10/11/2020 13:00:00', '10/11/2020 20:00:00')
GO

INSERT SupplierTransaction VALUES (1, 1, '01/02/2020', 148, '01/02/2020 12:00:00', '01/02/2020 20:00:00')
INSERT SupplierTransaction VALUES (2, 2, '02/04/2020', 90, '02/04/2020 11:00:00', '02/04/2020 20:00:00')
INSERT SupplierTransaction VALUES (3, 3, '03/06/2020', 35, '03/06/2020 12:00:00', '03/06/2020 20:00:00')
INSERT SupplierTransaction VALUES (4, 4, '04/08/2020', 108, '04/08/2020 11:00:00', '04/08/2020 20:00:00')
INSERT SupplierTransaction VALUES (5, 5, '05/10/2020', 90, '05/10/2020 12:00:00', '05/10/2020 20:00:00')
INSERT SupplierTransaction VALUES (6, 6, '06/12/2020', 148, '06/12/2020 11:00:00', '06/12/2020 20:00:00')
INSERT SupplierTransaction VALUES (7, 7, '07/14/2020', 148, '07/14/2020 12:00:00', '07/14/2020 20:00:00')
INSERT SupplierTransaction VALUES (8, 8, '08/16/2020', 148, '08/16/2020 11:00:00', '08/16/2020 20:00:00')
INSERT SupplierTransaction VALUES (9, 9, '09/18/2020', 88, '09/18/2020 12:00:00', '09/18/2020 20:00:00')
INSERT SupplierTransaction VALUES (10, 10, '10/20/2020', 90, '10/20/2020 13:00:00', '10/20/2020 20:00:00')
GO

INSERT CustTransaction VALUES (1, '01/20/2020 11:00:00', '01/20/2020 20:00:00')
INSERT CustTransaction VALUES (2, '03/23/2020 12:00:00', '03/23/2020 20:00:00')
INSERT CustTransaction VALUES (3, '05/25/2020 11:00:00', '05/25/2020 20:00:00')
INSERT CustTransaction VALUES (4, '07/27/2020 12:00:00', '07/27/2020 20:00:00')
INSERT CustTransaction VALUES (5, '09/29/2020 11:00:00', '09/29/2020 20:00:00')
INSERT CustTransaction VALUES (6, '11/21/2020 12:00:00', '11/21/2020 20:00:00')
INSERT CustTransaction VALUES (7, '02/22/2020 11:00:00', '02/22/2020 20:00:00')
INSERT CustTransaction VALUES (8, '04/24/2020 12:00:00', '04/24/2020 20:00:00')
INSERT CustTransaction VALUES (9, '06/26/2020 11:00:00', '06/26/2020 20:00:00')
INSERT CustTransaction VALUES (10, '08/28/2020 12:00:00', '08/28/2020 20:00:00')
GO

INSERT CustReceipt VALUES (1, '148.00', '29.6', '0.00', '0.00', '29.6', '0.2', '01/20/2020 11:00:00', '01/20/2020 20:00:00')
INSERT CustReceipt VALUES (2, '90.00', '18.00', '0.00', '0.00', '18.00', '0.25', '03/23/2020 12:00:00', '03/23/2020 20:00:00')
INSERT CustReceipt VALUES (3, '35.00', '7.00', '0.00', '0.00', '7.00', '0.2', '05/25/2020 11:00:00', '05/25/2020 20:00:00')
INSERT CustReceipt VALUES (4, '108.00', '21.6', '0.00', '0.00', '21.6', '0.2', '07/27/2020 12:00:00', '07/27/2020 20:00:00')
INSERT CustReceipt VALUES (5, '90.00', '18.00', '0.00', '0.00', '18.00', '0.25', '09/29/2020 11:00:00', '09/29/2020 20:00:00')
INSERT CustReceipt VALUES (6, '148.00', '29.6', '0.00', '0.00', '29.6', '0.25', '11/21/2020 12:00:00', '11/21/2020 20:00:00')
INSERT CustReceipt VALUES (7, '148.00', '29.6', '0.00', '0.00', '29.6', '0.2', '02/22/2020 11:00:00', '02/22/2020 20:00:00')
INSERT CustReceipt VALUES (8, '148.00', '29.6', '0.00', '0.00', '29.6', '0.25', '04/24/2020 12:00:00', '04/24/2020 20:00:00')
INSERT CustReceipt VALUES (9, '88.00', '17.6', '0.00', '0.00', '17.6', '0.2', '06/26/2020 11:00:00', '06/26/2020 20:00:00')
INSERT CustReceipt VALUES (10, '90.00', '18.00', '0.00', '0.00', '18.00', '0.25', '08/28/2020 12:00:00', '08/28/2020 20:00:00')
GO

SELECT * FROM InventoryItem
SELECT * FROM SupplierReference
SELECT * FROM SupplierTransaction
SELECT * FROM CustTransaction
SELECT * FROM CustReceipt 

GO