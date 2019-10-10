SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		Janrey Licas
-- Create date: 10/10/2019
-- Description:	Removes All Data Associated with SupplierReference
-- =============================================
CREATE TRIGGER dbo.RM_SupplierAssociated
   ON  dbo.SupplierReference 
   AFTER DELETE
AS 
BEGIN
	SET NOCOUNT ON;

END
GO
