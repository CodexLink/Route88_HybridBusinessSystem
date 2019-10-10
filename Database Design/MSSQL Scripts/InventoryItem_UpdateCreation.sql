SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		Janrey Licas
-- Create date: 10/10/2019
-- Description:	Inserts Time Creation and Modification in SupplierReference Table
-- =============================================
CREATE TRIGGER dbo.DateManipulate_II
   ON  dbo.InventoryItem
   AFTER INSERT, UPDATE
AS 
BEGIN
	SET NOCOUNT ON;
	BEGIN TRY
		IF EXISTS (SELECT * FROM INSERTED) AND NOT EXISTS (SELECT * FROM DELETED)
			BEGIN
				UPDATE InventoryItem SET CreationTime = getdate() WHERE ItemCode = (SELECT ItemCode FROM INSERTED)
			END
		ELSE IF EXISTS (SELECT * FROM DELETED) AND EXISTS (SELECT * FROM INSERTED)
			BEGIN
				UPDATE InventoryItem SET LastUpdate = getdate() WHERE ItemCode = (SELECT ItemCode FROM INSERTED)
			END
	END TRY
	BEGIN CATCH
		IF @@TRANCOUNT > 0
		SELECT ERROR_MESSAGE()
			ROLLBACK TRAN DateManipulator
	END CATCH
END
GO