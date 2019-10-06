SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
-- =============================================
-- Author:		Janrey Licas
-- Create date: 10/03/2019
-- Description:	Returns TransactionCount. This enables functionality button of 'Rollback Changes @ Data Viewer Window'
-- =============================================
CREATE FUNCTION TransCount_Checker 
() RETURNS INT AS
BEGIN
	RETURN @@TRANCOUNT
END
GO