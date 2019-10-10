SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		Janrey Licas
-- Create date: 10/10/2019
-- Description:	Inserts Time Creation and Modification in SupplierReference Table
-- =============================================
CREATE TRIGGER dbo.DateManipulate_SR
   ON  dbo.SupplierReference
   AFTER INSERT, UPDATE
AS 
BEGIN
	SET NOCOUNT ON;
	BEGIN TRY
		IF EXISTS (SELECT * FROM INSERTED) AND NOT EXISTS (SELECT * FROM DELETED)
			BEGIN
				UPDATE SupplierReference SET CreationTime = getdate() WHERE SupplierCode = (SELECT SupplierCode FROM INSERTED)
			END
		ELSE IF EXISTS (SELECT * FROM DELETED) AND EXISTS (SELECT * FROM INSERTED)
			BEGIN
				UPDATE SupplierReference SET LastUpdate = getdate() WHERE SupplierCode = (SELECT SupplierCode FROM INSERTED)
			END
	END TRY
	BEGIN CATCH
		IF @@TRANCOUNT > 0
		SELECT ERROR_MESSAGE()
			ROLLBACK TRAN DateManipulator
	END CATCH
END
GO
