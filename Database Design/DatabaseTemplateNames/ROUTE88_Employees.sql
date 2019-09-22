USE Route88_Employees

if exists (select name from sys.tables where name = 'Employees')
DELETE FROM Employees
GO

INSERT INTO Employees VALUES (0001, 'Janrey', 'Licas', 111, '01/10/2000', 'Antipolo City', NULL, NULL, NULL, '01/01/2020 11:00:00', '01/01/2020 20:00:00', 'janreylicas123');
INSERT INTO Employees VALUES (0002, 'Charles', 'Mascarenas', 222, '05/19/2000', 'Marikina City', NULL, NULL, NULL, '02/02/2020 12:00:00', '02/02/2020 20:00:00', 'charlesmascarenas123');
INSERT INTO Employees VALUES (0003, 'Patrick', 'Moreno', 333, '09/24/2000', 'Caloocan City', NULL, NULL, NULL, '03/03/2020 13:00:00', '03/03/2020 20:00:00', 'patrickmoreno123');
INSERT INTO Employees VALUES (0004, 'Brenda', 'Hernandez', 444, '06/03/2000', 'Quezon City', NULL, NULL, NULL, '04/04/2020 11:00:00', '04/04/2020 20:00:00', 'brendahernandez123');
INSERT INTO Employees VALUES (0005, 'Reinhart', 'Regulacion', 555, '04/13/2000', 'Bulacan City', NULL, NULL, NULL, '05/05/2020 12:00:00', '05/05/2020 20:00:00', 'reinhartregulacion123');
INSERT INTO Employees VALUES (0006, 'Charlie', 'Gonzales', 666, '10/27/2000', 'Pasig City', NULL, NULL, NULL, '06/06/2020 13:00:00', '06/06/2020 20:00:00', 'charliegonzales123');
INSERT INTO Employees VALUES (0007, 'Emerson', 'Bautista', 777, '02/08/2000', 'Quezon City', NULL, NULL, NULL, '07/07/2020 11:00:00', '07/07/2020 20:00:00', 'emersonbautista123');
INSERT INTO Employees VALUES (0008, 'Ronald', 'Langaoan', 888, '07/17/2000', 'Makati City', NULL, NULL, NULL, '08/08/2020 12:00:00', '08/08/2020 20:00:00', 'ronaldlangaoan123');
INSERT INTO Employees VALUES (0009, 'Janos', 'Jantoc', 999, '01/21/2000', 'Antipolo City', NULL, NULL, NULL, '09/09/2020 13:00:00', '09/09/2020 20:00:00', 'janosjantoc123');
INSERT INTO  Employees VALUES (0010, 'Yrah', 'Olicia', 000, '12/05/2000', 'Caloocan City', NULL, NULL, NULL, '10/10/2020 11:00:00', '10/10/2020 20:00:00', 'yraholicia123');

GO

if exists (select name from sys.tables where name = 'JobPositin')
DELETE FROM JobPosition
GO

INSERT INTO JobPosition VALUES (111, 'General Manager');
INSERT INTO JobPosition VALUES (222, 'Shift Manager');
INSERT INTO JobPosition VALUES (333, 'Assistant Manager');
INSERT INTO JobPosition VALUES (444, 'Supervisor');
INSERT INTO JobPosition VALUES (555, 'Cashier');
INSERT INTO JobPosition VALUES (666, 'Delivery');
INSERT INTO JobPosition VALUES (777, 'Customer Service');
INSERT INTO JobPosition VALUES (888, 'Food Preparer');
INSERT INTO JobPosition VALUES (999, 'Waiter');
INSERT INTO JobPosition VALUES (000, 'Waitress');

GO

Select * from Employees 
Select * from JobPosition 

GO