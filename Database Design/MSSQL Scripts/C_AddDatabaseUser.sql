SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		Janrey Licas
-- Create date: 09/29/2019
-- Description:	Adds Database User to Newly Added Employee Data from Management and Modifier
-- =============================================
CREATE TRIGGER dbo.CD_UserData_Login
   ON  dbo.Employees
   AFTER INSERT
AS 
BEGIN
	SET NOCOUNT ON;
	
	DECLARE @Add_SelectedEmpUN VARCHAR(45), @Add_SelectedEmpPW VARCHAR(45), @Add_SelectedEmpPosCode VARCHAR(45)
	DECLARE @Add_CState#1 VARCHAR(100)
	DECLARE @Add_CState#2 VARCHAR(100)

	SET NOCOUNT ON;
	BEGIN TRY
		SELECT @Add_SelectedEmpUN = EmployeeUN FROM INSERTED
		SELECT @Add_SelectedEmpPW = EmployeePW FROM INSERTED
		SELECT @Add_SelectedEmpPosCode = PositionCode FROM INSERTED
		EXEC('CREATE LOGIN ' + @Add_SelectedEmpUN + ' WITH PASSWORD = ''' + @Add_SelectedEmpPW + '''')
		EXEC('CREATE USER ' + @Add_SelectedEmpUN + ' for LOGIN ' + @Add_SelectedEmpUN)

		IF @Add_SelectedEmpPosCode = 1 OR @Add_SelectedEmpPosCode = 2
			BEGIN
				EXEC sp_addrolemember 'db_owner', @Add_SelectedEmpUN
				EXEC sp_addsrvrolemember @Add_SelectedEmpUN, 'sysadmin'
			END
		ELSE IF @Add_SelectedEmpPosCode = 3 OR @Add_SelectedEmpPosCode = 4
			BEGIN
				EXEC ('GRANT SELECT ON CustReceipt TO ' + @Add_SelectedEmpUN)
				EXEC ('GRANT SELECT ON CustTransaction TO ' + @Add_SelectedEmpUN)
				EXEC ('GRANT SELECT ON InventoryItem TO ' + @Add_SelectedEmpUN)
				EXEC ('GRANT SELECT ON SupplierReference TO ' + @Add_SelectedEmpUN)
				EXEC ('GRANT SELECT ON SupplierTransaction TO ' + @Add_SelectedEmpUN)
			END
		ELSE IF @Add_SelectedEmpPosCode = 5 OR @Add_SelectedEmpPosCode = 6
			BEGIN
				EXEC ('GRANT INSERT ON CustReceipt TO' + @Add_SelectedEmpUN)
				EXEC ('GRANT INSERT ON CustTransaction TO' + @Add_SelectedEmpUN)
				EXEC ('GRANT INSERT, SELECT, UPDATE ON InventoryItem TO' + @Add_SelectedEmpUN)
			END
		ELSE IF @Add_SelectedEmpPosCode >= 7
			BEGIN
				EXEC sp_addrolemember 'db_denydatareader', @Add_SelectedEmpUN
			END
	END TRY
	BEGIN CATCH
		IF @@TRANCOUNT > 0
			SELECT ERROR_MESSAGE()
			ROLLBACK TRAN DBUser_Insertion
	END CATCH
END
GO
