SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		Janrey Licas
-- Create date: 10/10/2019
-- Description:	Inserts Time Creation and Modification in Customer Transaction Table
-- =============================================
CREATE TRIGGER dbo.DateManipulate_CT
   ON  dbo.CustTransaction
   AFTER INSERT, UPDATE
AS 
BEGIN
	SET NOCOUNT ON;
	BEGIN TRY
		IF EXISTS (SELECT * FROM INSERTED) AND NOT EXISTS (SELECT * FROM DELETED)
			BEGIN
				UPDATE CustTransaction SET CreationTime = getdate() WHERE TransactionCode = (SELECT TransactionCode FROM INSERTED)
			END
		ELSE IF EXISTS (SELECT * FROM DELETED) AND EXISTS (SELECT * FROM INSERTED)
			BEGIN
				UPDATE CustTransaction SET LastUpdate = getdate() WHERE TransactionCode = (SELECT TransactionCode FROM INSERTED)
			END
	END TRY
	BEGIN CATCH
		IF @@TRANCOUNT > 0
		SELECT ERROR_MESSAGE()
			ROLLBACK TRAN DateManipulator
	END CATCH
END
GO