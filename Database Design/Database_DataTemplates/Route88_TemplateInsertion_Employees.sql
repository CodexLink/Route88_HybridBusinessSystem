-- =============================================
-- Author:		Jan Patrick Moreno
-- Create date: 09/26/2019
-- Sub-Author:	Janrey Licas
-- Description:	Inserts All Template Data for JobPosition and Employees
-- =============================================
USE Route88_Database

IF EXISTS (SELECT NAME FROM SYS.TABLES WHERE NAME = 'Employees')
DELETE FROM Employees
GO

IF EXISTS (SELECT NAME FROM SYS.TABLES WHERE NAME = 'JobPosition')
DELETE FROM JobPosition
GO

INSERT JobPosition VALUES (111, 'General Manager');
INSERT JobPosition VALUES (222, 'Shift Manager');
INSERT JobPosition VALUES (333, 'Assistant Manager');
INSERT JobPosition VALUES (444, 'Supervisor');
INSERT JobPosition VALUES (555, 'Cashier');
INSERT JobPosition VALUES (666, 'Delivery');
INSERT JobPosition VALUES (777, 'Customer Service');
INSERT JobPosition VALUES (888, 'Food Preparer');
INSERT JobPosition VALUES (999, 'Waiter');
INSERT JobPosition VALUES (000, 'Waitress');
GO
/* TODO: Insert Some User Database Soon...*/
INSERT Employees VALUES ('Janrey01', 'Janreylicas123', 'Janrey', 'Licas', 111, '01/10/2000', 'Antipolo City', '01-2345679-0', '123-567-435-789', '12-452135897-5', '01/01/2020 11:00:00', '01/01/2020 20:00:00');
INSERT Employees VALUES ('Charles02', 'Charlesmascarenas123', 'Charles', 'Mascarenas', 222, '05/19/2000', 'Marikina City', '02-2345678-9', '482-631-954-852', '34-125489637-2', '02/02/2020 12:00:00', '02/02/2020 20:00:00');
INSERT Employees VALUES ('Patrick03', 'Patrickmoreno123', 'Patrick', 'Moreno', 333, '09/24/2000', 'Caloocan City', '03-2345679-5', '059-326-765-023', '56-268435917-2', '03/03/2020 13:00:00', '03/03/2020 20:00:00');
INSERT Employees VALUES ('Brenda04', 'Brendahernandez123', 'Brenda', 'Hernandez', 444, '06/03/2000', 'Quezon City', '04-6325894-6', '257-871-789-567', '78-652318945-3', '04/04/2020 11:00:00', '04/04/2020 20:00:00');
INSERT Employees VALUES ('Reinhart05', 'Reinhartregulacion123', 'Reinhart', 'Regulacion', 555, '04/13/2000', 'Bulacan City', '05-4523689-3', '234-675-314-790', '90-492736185-5', '05/05/2020 12:00:00', '05/05/2020 20:00:00');
INSERT Employees VALUES ('Charlie06', 'Charliegonzales123', 'Charlie', 'Gonzales', 666, '10/27/2000', 'Pasig City', '06-7526394-8', '145-654-768-346', '12-423650891-6', '06/06/2020 13:00:00', '06/06/2020 20:00:00');
INSERT Employees VALUES ('Emerson07', 'Emersonbautista123', 'Emerson', 'Bautista', 777, '02/08/2000', 'Quezon City', '07-2536189-7', '527-947-026-978', '34-125693480-7', '07/07/2020 11:00:00', '07/07/2020 20:00:00');
INSERT Employees VALUES ('Ronald08', 'Ronaldlangaoan123', 'Ronald', 'Langaoan', 888, '07/17/2000', 'Makati City', '08-4185736-2', '145-678-372-095', '56-489236175-9', '08/08/2020 12:00:00', '08/08/2020 20:00:00');
INSERT Employees VALUES ('Janos09', 'Janosjantoc123', 'Janos', 'Jantoc', 999, '01/21/2000', 'Antipolo City', '09-8521469-1', '195-174-268-869', '78-426315983-5', '09/09/2020 13:00:00', '09/09/2020 20:00:00');
INSERT Employees VALUES ('Yrah10', 'Yraholicia123', 'Yrah', 'Olicia', 000, '12/05/2000', 'Caloocan City', '10-4569827-4', '564-679-092-168', '90-236591851-2', '10/10/2020 11:00:00', '10/10/2020 20:00:00');


GO

SELECT * FROM Employees 
SELECT * FROM JobPosition 

GO