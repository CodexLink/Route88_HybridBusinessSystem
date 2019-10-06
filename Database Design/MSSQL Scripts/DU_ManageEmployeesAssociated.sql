SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		Janrey Licas
-- Create date: 09/29/2019
-- Description:	Removes or Modifies Any Employee Associated With Job Description OR PositionCode
-- =============================================
CREATE TRIGGER dbo.DU_ManageEmpAssociate 
   ON  dbo.JobPosition 
   AFTER DELETE, UPDATE
AS
BEGIN
	SET NOCOUNT ON;
	DECLARE @EMPCount INT;
	SELECT @EMPCount = dbo.return_CountEmp()

	IF EXISTS (SELECT * FROM INSERTED)
		BEGIN
			IF @EMPCount > 0
				BEGIN
					UPDATE Employees SET PositionCode = JobPosition.PositionCode FROM Employees
					INNER JOIN JobPosition ON Employees.PositionCode = JobPosition.PositionCode
				END
		END
	ELSE IF EXISTS (SELECT * FROM DELETED)
		BEGIN
			IF @EMPCount > 0
				BEGIN
					DELETE FROM Employees WHERE PositionCode = (SELECT PositionCode FROM DELETED)
				END
		END
END
GO