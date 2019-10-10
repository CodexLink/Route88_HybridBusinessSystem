SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		Janrey Licas
-- Create date: 09/29/2019
-- Description:	Deletes Database User with Respect Employees Table
-- =============================================
CREATE TRIGGER dbo.RM_UserData_Login
   ON  dbo.Employees 
   AFTER DELETE
AS 
BEGIN
	DECLARE @rm_SelectedEmpUN VARCHAR(45),
	DECLARE @CountEmpPosCandidate INT

	SET NOCOUNT ON;
	SELECT @rm_SelectedEmpUN = EmployeeUN FROM DELETED
	EXEC('DROP ROLE ' + @rm_SelectedEmpUN)
	EXEC('DROP LOGIN ' + @rm_SelectedEmpUN)
	EXEC('DROP USER ' + @rm_SelectedEmpUN)

END