SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		Janrey Licas
-- Create date: 09/28/2019
-- Description:	Returns Count of Users from the Employee Table To Check If Program is opened for the first time.
-- =============================================
CREATE FUNCTION return_CountEmp 
(
)
RETURNS int
AS
BEGIN
	DECLARE @EmployeeValidCount int
	SELECT @EmployeeValidCount = COUNT(*) FROM Employees
	RETURN @EmployeeValidCount
END
GO

