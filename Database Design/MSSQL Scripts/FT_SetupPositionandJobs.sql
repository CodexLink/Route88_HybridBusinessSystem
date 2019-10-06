SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		Janrey Licas
-- Create date: 10/04/2019 - 1:48AM
-- Description:	Adds All Possible Position Codes and Jobs When User is in First Time Mode
-- =============================================
CREATE PROCEDURE FT_SetupPosJobs
AS
BEGIN
	SET NOCOUNT ON;
	BEGIN TRY
		BEGIN TRAN FT_SetupAttempt
			DELETE FROM JobPosition;
			INSERT INTO JobPosition VALUES (1, 'Manager');
			INSERT INTO JobPosition VALUES (2, 'General Manager');
			INSERT INTO JobPosition VALUES (3, 'Shift Manager');
			INSERT INTO JobPosition VALUES (4, 'Assistant Manager');
			INSERT INTO JobPosition VALUES (5, 'Supervisor');
			INSERT INTO JobPosition VALUES (6, 'Cashier');
			INSERT INTO JobPosition VALUES (7, 'Delivery');
			INSERT INTO JobPosition VALUES (8, 'Customer Service');
			INSERT INTO JobPosition VALUES (9, 'Food Preparer');
			INSERT INTO JobPosition VALUES (10, 'Waiter');
			INSERT INTO JobPosition VALUES (11, 'Waitress');
			COMMIT TRAN FT_SetupAttempt
	END TRY
	BEGIN CATCH
		SELECT ERROR_MESSAGE()
		IF @@TRANCOUNT > 0
			ROLLBACK TRAN FT_SetupAttempt
	END CATCH
END