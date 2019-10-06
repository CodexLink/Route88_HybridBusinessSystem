'''
    Filename: Route88_CoreFunc.py - Route 88 POS and Inventory System Core Functions
    Project File: Route88 POS and Inventory System
    Initially Created by Janrey Licas
    GUI Framework: PyQt5
    Github: https://github.com/CodexLink/DMBS_Route88_POSSystem

    Members:    Janrey Licas "CodexLink" - https://github.com/CodexLink
                Charles Ian Mascarenas "ci-mascarenas" - https://github.com/ci-mascarenas
                Jan Patrick Moreno "jaypeemrn" - https://github.com/jaypeemrn
                Brenda Hernandez "imbrendzzz" - https://github.com/imbrendzzz

    Multi-Level Inheritance Method of Application Architecture: 
        -> 
    Core Component Structure:
        Class Route88_TechnicalCore()
            Methods:
                -> __init__()
        Class Route88_LoginCore()
            Methods:
                -> __init__()
                    Includes
                -> <ClassShortName>_RenderExplicits
                -> <ClassShortName>_RunAfterRender

        Class Route88_ManagementCore()
            Methods:
                -> __init__()
                    Includes
                -> <ClassShortName>_RenderExplicits
                -> <ClassShortName>_RunAfterRender

        Class Route88_POSCore()
            Methods:
                -> __init__()
                    Includes
                -> <ClassShortName>_RenderExplicits
                -> <ClassShortName>_RunAfterRender
    Legends:
        Definitions:
            _RenderExplicits -> Render Explicit Elements
            _RunAfterRender -> Run Function After Render
        Functions:
            __init__() -> Class Initializers, Possibly Constructors
            <ClassShortName>_RenderExplicits -> Load Extra Elements from 'That' UI
                > This was implemented to ensure that changes from the UI file will not     affect any additional elements that we just manually added which cannot be initiated with Qt Designer, this would result to extra elements  remains whatver UI file changes after generating using 'pyuic5' module.
            <ClassShortName>_RunAfterRender -> Condition, Must Be After setupUi()
                > This was implemented right after setupUi(). Because, we have to   initialize every value from the database which would then be shown after  UI has been render. So that when the engine initiates .show(). All values is already there. So in sort, setup Values and Elements.
'''
import subprocess as sysHandler
from os import sys

from PyQt5 import QtCore, QtGui, QtTest, QtWidgets
from PyQt5.QtMultimedia import QSound

import pyodbc as MSSQL
from Route88_ControllerCmpnt import Ui_Route88_Controller_Window
from Route88_DataManipCmpnt import Ui_Route88_DataManipulation_Window
from Route88_DataViewerCmpnt import Ui_Route88_DataViewer_Window
from Route88_LoginCmpnt import Ui_Route88_Login_Window
from Route88_POSCmpnt import Ui_Route88_POS_SystemWindow
from Route88_AboutSystemCmpnt import Ui_Route88_AboutUsWindow

# This class is a database controller by wrapping all confusing parts into a callable function... and any other such that requires global function calling.
class Route88_TechnicalCore(object):
    def __init__(self, Parent=None):
        super().__init__()

    # * Python to MSSQL Adaptation
    def MSSQL_OpenCon(self, OBDCDriver='{ODBC Driver 17 for SQL Server}', ServerHost='localhost', UCredential=None, PCredential=None, DB_Target='Route88_Database', ActiveStaffName="???", SourceFunction=None):
        try:
            self.MSSQLDataWire = MSSQL.connect("DRIVER=%s; SERVER=%s; DATABASE=%s;UID=%s; PWD=%s" % (OBDCDriver, ServerHost, DB_Target, UCredential, PCredential), autocommit=True)
            print("[MSSQL Database Report @ MSSQL_OpenCon, %s] Staff '%s' with Username '%s' is connected @ Database %s." % (SourceFunction, ActiveStaffName, UCredential, DB_Target))

        except (Exception, MSSQL.DatabaseError) as MSSQL_OpenConErrorMsg:
            self.TechCore_Beep()
            #self.StatusLabel.setText("Database Error: Cannot Connect to the MSSQL Database. Please restart.")
            print('[MSSQL Database Report @ MSSQL_OpenCon, %s] > Cannot Open / Establish Connection with the MSSQL Database. Detailed Info |> %s' % (SourceFunction, MSSQL_OpenConErrorMsg))
            QtWidgets.QMessageBox.critical(self, 'Route88 System | Database Connection Error', "An error occured while connecting to the database.\n\nDetailed Error: '%s'.\n\n Try restarting or re-connecting to MSSQL Server and try again." % (MSSQL_OpenConErrorMsg), QtWidgets.QMessageBox.Ok)
            sys.exit() # Terminate the program 

    # * Data Selector Initializer
    def MSSQL_InitCursor(self, SourceFunction=None):
        try:
            self.MSSQLDataWireCursor = self.MSSQLDataWire.cursor()

        except (Exception, MSSQL.DatabaseError) as CursorErrMsg:
            self.TechCore_Beep()
            print('[Exception @ MSSQL_InitCursor, %s] > Invalid Cursor Set. Report this problem to the developers. Detailed Info |> %s' % (SourceFunction, CursorErrMsg))

    # * Executes Multiple Types of Choice of Execute. This was an actual nice wrapper with specific exception being catched.
    def MSSQL_ExecuteState(self, MSSQLStatement=None, FetchType=None, TableTarget=None, SourceFunction=None):
        try:
            if FetchType == 'One':
                print("[Statement Execution @ MSSQL_ExecuteState, %s | Table -> %s] > FetchType: %s, Statement | %s |" % (SourceFunction, TableTarget, FetchType, MSSQLStatement))
                return self.MSSQLDataWireCursor.execute(MSSQLStatement).fetchone()
            elif FetchType == 'All':
                print("[Statement Execution @ MSSQL_ExecuteState, %s | Table -> %s] > FetchType: %s, Statement | %s |" % (SourceFunction, TableTarget, FetchType, MSSQLStatement))
                return self.MSSQLDataWireCursor.execute(MSSQLStatement).fetchall()
            elif FetchType == 'FetchVal':
                print("[Statement Execution @ MSSQL_ExecuteState, %s | Table -> %s] > FetchType: %s, Statement | %s |" % (SourceFunction, TableTarget, FetchType, MSSQLStatement))
                return self.MSSQLDataWireCursor.execute(MSSQLStatement).fetchval()
            else:
                print("[Statement Execution @ MSSQL_ExecuteState, %s | Table -> %s] > FetchType: %s, Statement | %s |" % (SourceFunction, TableTarget, FetchType, MSSQLStatement))
                return self.MSSQLDataWireCursor.execute(MSSQLStatement)

        except MSSQL.IntegrityError as MSSQL_ExecError:
            self.TechCore_Beep()
            print("[Exception (MSSQL.IntegrityError) @ MSSQL_ExecuteState, %s] > Error, Cannot Push Data @ %s. Check if you are pushing an already existing data. Data must be unique." % (SourceFunction, TableTarget))
            #self.Modifier_StatusLabel.setText("Error, Cannot Push Data @ %s. Check if you pushing an already existing data. Data must be unique." % (TableTarget))
            QtWidgets.QMessageBox.critical(self, 'Route88 System | Data Manipulation Insertion Error', "Error, Cannot Push Data @ %s. Check if you pushing an already existing data. Data must be unique. Detailed Error: %s" % (TableTarget, MSSQL_ExecError), QtWidgets.QMessageBox.Ok)
            raise Exception
    
        except MSSQL.ProgrammingError as MSSQL_ExecError:
            self.TechCore_Beep()
            print("[Exception (MSSQL.ProgrammingError) @ MSSQL_ExecuteState, %s] > Error, Cannot Access Table %s. You don't have sufficient permission to do so..." % (SourceFunction, TableTarget))
            #self.InventoryStatus.showMessage("Error, Cannot Access Table %s. You don't have sufficient permission to do so..." % (TableTarget))
            QtWidgets.QMessageBox.critical(self, 'Route88 System | Data Manipulation Insertion Error', "Error, Cannot Access Table %s. You don't have sufficient permission to do so... Detailed Error: %s" % (TableTarget, MSSQL_ExecError), QtWidgets.QMessageBox.Ok)
            #raise Exception


        except MSSQL.DatabaseError as MSSQL_ExecError:
            self.TechCore_Beep()
            print('[Exception (MSSQL.DatabaseError) @ MSSQL_ExecuteState, %s] > Error in SQL Statements. Double check your statements. Detailed Info |> %s' % (SourceFunction, MSSQL_ExecError))


    # * Explicit Transaction Function Call. Useful for Actual Execution Transaction ON Function Local Scope (NOT from SQL Server Studio)
    def MSSQL_CommitData(self, SourceFunction=None):
        try:
            return self.MSSQLDataWire.commit()

        except MSSQL.DatabaseError as MSSQL_CommitError:
            self.TechCore_Beep()
            print('[Exception @ MSSQL_CommitData, %s] > Unable To Commit Data... Check your MySQL Connection and try again.Detailed Info |> %s' % (SourceFunction, MSSQL_CommitError))

    # * Explicit Transaction Function Call. Useful for Actual Execution Transaction ON Function Local Scope (NOT from SQL Server Studio)
    def MSSQL_RollbackData(self, SourceFunction=None):
        try:
            return self.MSSQLDataWire.rollback()

        except MSSQL.DatabaseError as RollbackErrMsg:
            self.TechCore_Beep()
            print('[Exception @ MSSQL_RollbackData, %s] > Unable To Commit Data... Check your MSSQL Connection and try again. Detailed Info |> %s' % (SourceFunction, RollbackErrMsg))
            
    # * Optional Function, but according to the documentation, we don't need to call this one explicitly. It tends to happen automatically.
    def MSSQL_CloseCon(self, SourceFunction=None):
        try:
            return self.MSSQLDataWire.close()
        except (Exception, MSSQL.DatabaseError) as ClosingErr:
            self.TechCore_Beep()
            print('[Exception @ MSSQL_CloseCon, %s] > Unable to Close Connection with the MSSQL Statements. Program Terminates Immediately. Detailed Info |> %s' (SourceFunction, ClosingErr))
    
    # * Assured Non-Throwing Function Error. use of Try-Except Cluase is not needed.
    def TechCore_Beep(self):
        return QtWidgets.QApplication.beep()

    # ! Not sure for this one...
    def TechCore_MessageBox(self, ObjType=None, WindTitle=None, MsgDetailInfo=None, MsgButtons=None, SourceFunction=None):
        try:
            # TODO > For Future Usage.
                #ConfirmDelMsg = QtWidgets.QMessageBox()
                #ConfirmDelMsg.setIcon(QtWidgets.QMessageBox.information)
                #ConfirmDelMsg.setWindowTitle('Route88 System | Data Deletion')
                #ConfirmDelMsg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)
            return ObjType(self, WindTitle, MsgDetailInfo, MsgButtons)
            
        except Exception as MsgSpawnError:
            print('[Exception @ TechCore_MessageBox] > An Error Occured While Spawning QMessageBox. Detailed Error: %s' % (MsgSpawnError))
    
    # * Side Component function To Call For Renderingn Tables with Respective Column Count from Explicit UI Integration of Data.
    def TechCore_ColResp(self, SourceFunction=None):
        try:
            self.DataTable_View.resizeColumnsToContents()
            for SetCellFixedElem in range(self.DataTable_View.columnCount()):
                self.DataTable_View.horizontalHeader().setSectionResizeMode(SetCellFixedElem, QtWidgets.QHeaderView.Stretch)
        
        except Exception as ResponseError:
            print('[Exception @ TechCore_ColResp, %s] > Error Responsive Rendering in Table View. Detailed Info |> %s' % (SourceFunction, ResponseError))
    
    # * Side Component Function To Call When One Of The TextChanged Detected Changes on Mangaement View Window
    def TechCore_RowClear(self, SourceFunction=None):
        try:
            self.DataTable_View.clearContents()
            self.DataTable_View.setRowCount(0)

        except Exception as RowClearMsg:
            print('[Exception @ TechCore_RowClear, %s] > Row Clearing Returns Error. Detailed Info |> %s' % (SourceFunction, RowClearMsg))
    
    # * Side Component To Remove Selected Row After Successfull Operation Other Functions.
    def TechCore_RowClearSelected(self, rowIndex, SourceFunction=None):
        try:
            return self.DataTable_View.removeRow(rowIndex)
        
        except Exception as Err:
            print('[Exception @ TechCore_RowClearSelected, %s] > Row Clearing Returns Error. Detailed Info |> %s' % (SourceFunction, Err))


    # * Clears All Search Query Candidate Except for Index[0] Which Is None
    def TechCore_ColOptClear(self, SourceFunction=None):
        try:
            ColOptIndex = 0 # Offset Column To Remove
            self.Query_ColumnOpt.setCurrentIndex(0)
            while self.Query_ColumnOpt.count() != 1:
                self.Query_ColumnOpt.removeItem(ColOptIndex + 1)

        except Exception as ColOptClearMsg:
            print('[Exception @ TechCore_ColOptClear, %s] > Column Clearing Returns Error. Detailed Info |> %s' % (SourceFunction, ColOptClearMsg))

    # * Useful for Disabling Other Tabs Other Than Active or Selected Table
    def TechCore_DisableExcept(self, ExceptGivenNum, SourceFunction=None):
        try:
            for TabIndex in range(self.Tab_SelectionSelectives.count()):
                if TabIndex == ExceptGivenNum:
                    continue
                else:
                    self.Tab_SelectionSelectives.setTabEnabled(TabIndex, False)
        except Exception as Err:
            print('[Exception @ TechCore_DisableExcept, %s] > Tab Disabling Process occured an Error. Detailed Info |> %s' % (SourceFunction, Err))


    # * Turns String To An Index Based Specifically Used For QComboBox on Modifier Instance
    def TechCore_StrToIndex(self, RespectiveComboBox=None, StrToCompare=None, SourceFunction=None):
        DefaultIndex = 0
        try:
            if self.ActiveTargetTable == "InventoryItem":
                if RespectiveComboBox == "Item Type":
                    for IndexCandidate in range(self.InvEntry_IT.count()):
                        if StrToCompare == self.InvEntry_IT.itemText(IndexCandidate):
                            return IndexCandidate
                    return DefaultIndex
                else:
                    for IndexCandidate in range(0, self.InvEntry_MT.count()):
                        if StrToCompare == self.InvEntry_MT.itemText(IndexCandidate):
                            return IndexCandidate
                    return DefaultIndex
    
            elif self.ActiveTargetTable == "SupplierTransaction":
                if RespectiveComboBox == "Item Code":
                    for IndexCandidate in range(0, self.SuppTrEntry_IC.count()):
                        if StrToCompare == self.SuppTrEntry_IC.itemText(IndexCandidate):
                            return IndexCandidate
                    return DefaultIndex
                else:
                    for IndexCandidate in range(0, self.SuppTrEntry_SC.count()):
                        if StrToCompare == self.SuppTrEntry_SC.itemText(IndexCandidate):
                            return IndexCandidate
                    return DefaultIndex
    
            elif self.ActiveTargetTable == "CustTransaction":
                for IndexCandidate in range(0, self.CustTr_IC.count()):
                    if StrToCompare == self.CustTr_IC.itemText(IndexCandidate):
                        return IndexCandidate
                return DefaultIndex
    
            elif self.ActiveTargetTable == "CustReceipt":
                if RespectiveComboBox == "Primary Transaction Code":
                    for IndexCandidate in range(0, self.CustREntry_PTrC.count()):
                        if StrToCompare == self.CustREntry_PTrC.itemText(IndexCandidate):
                            return IndexCandidate
                    return DefaultIndex
                else:
                    for IndexCandidate in range(0, self.CustREntry_STrC.count()):
                        if StrToCompare == self.CustREntry_STrC.itemText(IndexCandidate):
                            return IndexCandidate
                    return DefaultIndex
    
        except Exception as Err:
            print('[Exception @ TechCore_StrToIndex, %s] > Existing Data Rendering Error (Specifically for QComboBox). Detailed Info |> %s' % (SourceFunction, Err))
    
    # TODO: Two Exact Functions Can Be Encapsulated Into One.
    # * Gets PosCode and Retuns String Name with Respect to PositionCode.

    def TechCore_PosCodeToName(self, PosCode, SourceFunction=None):
        try:
            self.MSSQL_InitCursor(SourceFunction=self.TechCore_PosCodeToName.__name__)
            ConvertedToName = self.MSSQL_ExecuteState(MSSQLStatement="SELECT JobName FROM JobPosition WHERE PositionCode = %s" % (PosCode), FetchType="FetchVal", TableTarget="JobPosition", SourceFunction=self.TechCore_PosCodeToName.__name__)
            return ConvertedToName

        except Exception as Err:
            print('[Exception @ TechCore_PosCodeToName, %s] Error Processing Position Code String Literal... Detailed Error |> %s' % (SourceFunction, Err))

    # * Gets String Name and Retuns PositionCOde with Respect to String Name
    def TechCore_NameToPosCode(self, JobName, SourceFunction=None):
        try:
            self.MSSQL_InitCursor(SourceFunction=self.TechCore_NameToPosCode.__name__)
            ConvertedToPosCode = self.MSSQL_ExecuteState(MSSQLStatement="SELECT PositionCode FROM JobPosition WHERE JobName = '%s'" % (JobName), FetchType="One", TableTarget="JobPosition", SourceFunction=self.TechCore_PosCodeToName.__name__)
            return ConvertedToPosCode[0]
            
        except Exception as Err:
            print('[Exception @ TechCore_NameToPosCode, %s] Error Processing String Literal to Position Code... Detailed Error |> %s' % (SourceFunction, Err))
    
    # * Iterates Through Specific Tables Set on 'self.ActiveTargetTable' And Fills Up Specific ComboBox
    def TechCore_FillUpBox(self):
        try:
            if self.ActiveTargetTable == "SupplierReference":
                pass
    
            elif self.ActiveTargetTable == "InventoryItem":
                pass
    
            elif self.ActiveTargetTable == "SupplierTransaction":
                self.DataHandler_Load = self.MSSQL_ExecuteState(MSSQLStatement="SELECT SupplierCode FROM SupplierReference", FetchType="All", TableTarget=self.ActiveTargetTable, SourceFunction=self.TechCore_FillUpBox.__name__)
                for ItemCandidate in self.DataHandler_Load:
                    self.SuppTrEntry_IC.addItem(str(ItemCandidate.SupplierCode))
                self.DataHandler_Load = self.MSSQL_ExecuteState(MSSQLStatement="SELECT ItemCode FROM InventoryItem", FetchType="All", TableTarget=self.ActiveTargetTable, SourceFunction=self.TechCore_FillUpBox.__name__)
                for ItemCandidate in self.DataHandler_Load:
                    self.SuppTrEntry_SC.addItem(str(ItemCandidate.ItemCode))

            elif self.ActiveTargetTable == "CustTransaction":
                self.DataHandler_Load = self.MSSQL_ExecuteState(MSSQLStatement="SELECT ItemCode FROM InventoryItem", FetchType="All", TableTarget=self.ActiveTargetTable, SourceFunction=self.TechCore_FillUpBox.__name__)
                for ItemCandidate in self.DataHandler_Load:
                    self.CustTr_IC.addItem(str(ItemCandidate.ItemCode))
    
            elif self.ActiveTargetTable == "CustReceipt":
                self.DataHandler_Load = self.MSSQL_ExecuteState(MSSQLStatement="SELECT TransactCode_Pri FROM CustReceipt", FetchType="All", TableTarget=self.ActiveTargetTable, SourceFunction=self.TechCore_FillUpBox.__name__)
                for ItemCandidate in self.DataHandler_Load:
                    self.CustREntry_PTrC.addItem(str(ItemCandidate.TransactCode_Pri))

                self.DataHandler_Load = self.MSSQL_ExecuteState(MSSQLStatement="SELECT TransactCode_Sec FROM CustReceipt", FetchType="All", TableTarget=self.ActiveTargetTable, SourceFunction=self.TechCore_FillUpBox.__name__)
                for ItemCandidate in self.DataHandler_Load:
                    self.CustREntry_STrC.addItem(str(ItemCandidate.TransactCode_Sec))
    
            elif self.ActiveTargetTable == "JobPosition":
                pass
    
            elif self.ActiveTargetTable == "Employees":
                pass
        except (Exception, MSSQL.Error) as IterToBoxErr:
            pass

    # * Sets Current QComboBox Index Based On User's Data from Job Position Code
    def TechCore_EditBindComboBox(self, PosCode, SourceFunction=None):
        try:
            if self.ActiveTargetTable == "SupplierReference":
                pass
    
            elif self.ActiveTargetTable == "InventoryItem":
                pass
    
            elif self.ActiveTargetTable == "SupplierTransaction":
                pass
    
            elif self.ActiveTargetTable == "CustTransaction":
                pass
    
            elif self.ActiveTargetTable == "CustReceipt":
                pass
    
            elif self.ActiveTargetTable == "JobPosition":
                pass
    
            elif self.ActiveTargetTable == "Employees":
                for SetIndexCandidate in range(self.EmpEntry_PC.count()):
                    print(SetIndexCandidate)
                    if int(PosCode) == SetIndexCandidate:
                        print(SetIndexCandidate, PosCode)
                        return self.EmpEntry_PC.setCurrentIndex(SetIndexCandidate)
        except Exception as Err:
            print('[Exception @ TechCore_NameToPosCode, %s] Error Binding Data to QComboBox by Index. Detailed Error |> %s' % (SourceFunction, Err))



class Route88_LoginCore(Ui_Route88_Login_Window, QtWidgets.QDialog, Route88_TechnicalCore):
    def __init__(self, Parent=None):
        super(Route88_LoginCore, self).__init__(Parent=Parent)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('IcoDisplay/r_88.ico'))
        # Window Flags
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowShadeButtonHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        # Button Binds for Window 'Route88_LoginForm'
        self.UserAcc_UserCode.returnPressed.connect(self.UserAcc_SubmitData.click)
        self.UserAcc_Password.returnPressed.connect(self.UserAcc_SubmitData.click)
        self.UserAcc_SubmitData.clicked.connect(self.LoginCore_DataSubmission)
        # RunAfterRender Slot
        self.LoginCore_RunAfterRender()

    def LoginCore_RunAfterRender(self):
        try:
            self.MSSQL_OpenCon(UCredential='Route88_TempAuth', PCredential='Route88_Group7', SourceFunction=self.LoginCore_RunAfterRender.__name__)
            self.MSSQL_InitCursor(SourceFunction=self.LoginCore_RunAfterRender.__name__)
            self.LoginCore_CheckEnlisted()

        except Exception as ErrorHandler:
            self.TechCore_Beep()
            print('[Exception @ LoginCore_RunAfterRender] > One of the MySQL Required Components Returns Error. Detailed Info |> {}'.format(str(ErrorHandler)))
            QtWidgets.QMessageBox.critical(self, 'Route88 Login Form | Database Error', "Error, cannot connect to the database. Please restart the program and re-run the XAMPP MySQL Instance. Detailed Info |> {}".format(str(ErrorHandler)), QtWidgets.QMessageBox.Ok)
            sys.exit() # Terminate the program at all cost.

    #Route88_LoginForm UI Window Functions - StartPoint
    def LoginCore_CheckEnlisted(self):
        try:
            self.MSSQL_InitCursor(SourceFunction=self.LoginCore_CheckEnlisted.__name__)
            self.UserEnlistedCount = self.MSSQL_ExecuteState(MSSQLStatement="SELECT dbo.return_CountEmp()", FetchType='FetchVal', TableTarget='Employees', SourceFunction=self.LoginCore_CheckEnlisted.__name__)
            print('[Report @ LoginCore_CheckEnlisted] > User Account Count: %s' % (self.UserEnlistedCount))

            if self.UserEnlistedCount == 0:
                self.TechCore_Beep()
                self.MSSQL_ExecuteState(MSSQLStatement="{CALL FT_SetupPosJobs}")
                self.MSSQL_CommitData()

                QtWidgets.QMessageBox.information(self, 'Route88 System', "Welcome to Route88 Hybrid System! The system detected that there is no user account recorded according to it's database. Since you launch the system with no other accounts, you will have register first as a 'Manager' in this particular time.", QtWidgets.QMessageBox.Ok)

                self.Route88_FirstTimerInst = Route88_ModifierCore(ModifierMode="PushEntry", isFirstTime=True, StaffInCharge_Name="???")
                self.Route88_FirstTimerInst.exec_()

                self.UserEnlistedCount = self.MSSQL_ExecuteState(MSSQLStatement="SELECT dbo.return_CountEmp()", FetchType='FetchVal', TableTarget='Employees', SourceFunction=self.LoginCore_CheckEnlisted.__name__)
                self.UserAcc_SubmitData.setDisabled(False)
                # If it is still zero then...
                if self.UserEnlistedCount == 0:
                    self.TechCore_Beep()
                    QtWidgets.QMessageBox.critical(self, 'Route88 Login Form | General Error', "Error, have you registered? We still detected that there is no user registered in database. Login is Disabled. Please try again on startup. ", QtWidgets.QMessageBox.Ok)
                    sys.exit()
                else:
                    self.UserAcc_SubmitData.setDisabled(False)
                    self.StatusLabel.setText("Database Loaded. Ready~!")
            else:
                #Check if there is no manager as well. and launch Modifier Core
                self.UserAcc_SubmitData.setDisabled(False)
                self.StatusLabel.setText("Database Loaded. Ready~!")

        except (Exception, MSSQL.DatabaseError) as LoginQueryErrorMsg:
            self.TechCore_Beep()

            print('[Exception @ LoginCore_CheckEnlisted] > Error Checking User in Database. Check MSSQL Database Connection. Detailed Info |> {}'.format(str(LoginQueryErrorMsg)))
            self.StatusLabel.setText("Database Error: Cannot Connect. Please restart.")

            QtWidgets.QMessageBox.critical(self, 'Route88 Login Form | Database Error', "Error, cannot connect to the database, here is the following error prompt that the program encountered. '{}'. Please restart the program and re-run the XAMPP MySQL Instance.".format(str(LoginQueryErrorMsg)), QtWidgets.QMessageBox.Ok)
            sys.exit() # Terminate the program at all cost.

    def LoginCore_DataSubmission(self):
        try:
            self.MSSQL_InitCursor(SourceFunction=self.LoginCore_DataSubmission.__name__)
            self.QueryReturn = self.MSSQL_ExecuteState(MSSQLStatement="SELECT TOP 1 * FROM Employees WHERE EmployeeUN = '%s' AND EmployeePW = '%s'" % (self.UserAcc_UserCode.text(),self.UserAcc_Password.text()), FetchType='One', TableTarget='Employees', SourceFunction=self.LoginCore_DataSubmission.__name__)
            #self.UserData = self.MSSQL_FetchAllData()
            if self.QueryReturn:
                QSound.play("SysSounds/LoginSuccessNotify.wav")
                self.StatusLabel.setText("Login Success: Credential Input Matched!")
                self.UserAcc_SubmitData.setDisabled(True)
                
                self.UserLiteralName = "%s %s" % (self.QueryReturn.FirstName, self.QueryReturn.LastName)
                self.UserPosInfo = self.TechCore_PosCodeToName(self.QueryReturn.PositionCode)
                self.UserUN = self.QueryReturn.EmployeeUN
                self.UserPW = self.QueryReturn.EmployeePW
                QtWidgets.QMessageBox.information(self, 'Route88 Login Form | Login Success', "Login Success! You have are now logged in as ... '%s | Job Info |> %s." % (self.UserLiteralName, self.UserPosInfo), QtWidgets.QMessageBox.Ok)
                self.StatusLabel.setText("Successfully Logged in as %s %s" % (self.QueryReturn.FirstName, self.QueryReturn.LastName))

                QtTest.QTest.qWait(1300)
                self.MSSQL_CloseCon() # Reconnect to Anothe SQ: Usage with Specific User Parameters
                self.close()

                self.Route88_MCInst = Route88_WindowController(Staff_Name=self.UserLiteralName, Staff_Job=self.UserPosInfo, Staff_DBUser=self.UserUN, Staff_DBPass=self.UserPW)
                self.Route88_MCInst.show()

            else:
                self.TechCore_Beep()
                self.StatusLabel.setText("Login Error: Credential Input Not Matched!")
                self.UserAcc_SubmitData.setDisabled(True)

                QtWidgets.QMessageBox.critical(self, 'Route88 Login Form | Login Failed', "Login Failed! Credential Input Not Matched. Check your User Code or your Password which may be written in Caps Lock. Please Try Again.", QtWidgets.QMessageBox.Ok)
                
                self.UserAcc_SubmitData.setDisabled(False)

        except (Exception, MSSQL.DatabaseError) as LoginSubmissionErrorMsg:
            self.TechCore_Beep()
            self.StatusLabel.setText(str(LoginSubmissionErrorMsg))
            print('[Exception @ LoginCore_DataSubmission] > Data Submission Failed. Detailed Info |> {}'.format(str(LoginSubmissionErrorMsg)))

    # Route88_LoginForm UI Window Functions - EndPoint

class Route88_ManagementCore(Ui_Route88_DataViewer_Window, QtWidgets.QMainWindow, Route88_TechnicalCore):
    def __init__(self, Parent=None, InCharge_Name=None, InCharge_Job=None, InCharge_DBUser=None, InCharge_DBPass=None, FirstTimer=False):
        super(Route88_ManagementCore, self).__init__(Parent=Parent)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowMaximizeButtonHint)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('IcoDisplay/r_88.ico'))
        # Button Binds for Window 'Route88_InventoryDesign'
        # > Search Query Binds

        self.InCharge_LiteralName = InCharge_Name
        self.InCharge_JobPos = InCharge_Job
        self.InCharge_DBUser = InCharge_DBUser
        self.InCharge_DBPass = InCharge_DBPass
        self.DataTableTarget = None # Sets Current Table Tempporarily
        self.DatabaseSelection = None
        self.Target_TableCol = None

        self.DataVCore_RenderExplicits()

        self.Query_ColumnOpt.currentIndexChanged.connect(self.DataVCore_SearchFieldSet)
        self.Query_Operator.currentIndexChanged.connect(self.DataVCore_OperatorSet)

        self.Query_ColumnOpt.currentIndexChanged.connect(self.DataVCore_ValSearch)
        self.Query_Operator.currentIndexChanged.connect(self.DataVCore_ValSearch)

        self.Query_ValueToSearch.textChanged.connect(self.DataVCore_PatternSetter)
        self.Query_ValueToSearch.textChanged.connect(self.DataVCore_ValSearch)

        self.SearchPattern_ExactOpt.clicked.connect(self.DataVCore_PatternEnabler)
        self.SearchPattern_ContainOpt.clicked.connect(self.DataVCore_PatternEnabler)

        self.SearchPattern_ExactOpt.clicked.connect(self.DataVCore_ValSearch)
        self.SearchPattern_ContainOpt.clicked.connect(self.DataVCore_ValSearch)
        
        self.SearchPattern_ComboBox.currentIndexChanged.connect(self.DataVCore_PatternSetter)
        self.SearchPattern_ComboBox.currentIndexChanged.connect(self.DataVCore_ValSearch)

        # Table Seelection Binds
        self.TableSystem_Selection.currentIndexChanged.connect(self.DataVCore_LoadTableSets)
        self.DataTable_View.itemSelectionChanged.connect(self.DataVCore_Encap_RowData)

        # Staff Action Binds 
        self.StaffAct_Add.clicked.connect(self.DataVCore_AddEntry)
        self.StaffAct_Edit.clicked.connect(self.DataVCore_EditEntry)
        self.StaffAct_Delete.clicked.connect(self.DataVCore_DeleteEntry)
        self.StaffAct_RefreshData.clicked.connect(self.DataVCore_RefreshData)

        self.Window_Quit.triggered.connect(self.DataVCore_ReturnWindow)
        self.DataVCore_PatternEnabler()
        self.DataVCore_RunAfterRender() #Run This Function After UI Initialization

    #Function Definitions for Route88_InventoryDesign
    def DataVCore_RenderExplicits(self): # Turn This To Render Columns According To Active Window
        try:
            #self.currentRow = 1
            self.InventoryStatus = QtWidgets.QStatusBar()
            self.setStatusBar(self.InventoryStatus)

        except (Exception, MSSQL.DatabaseError) as RenderErrorMsg:
            self.InventoryStatus.showMessage('Application Error: {0}'.format(RenderErrorMsg))
            print('[Exception Thrown @ DataVCore_RenderExplicits] > Detailed Info |> {0}'.format(RenderErrorMsg))

    def DataVCore_RunAfterRender(self):
        try:
            self.MSSQL_OpenCon(UCredential=self.InCharge_DBUser, PCredential=self.InCharge_DBPass, ActiveStaffName=self.InCharge_LiteralName, SourceFunction=self.DataVCore_RunAfterRender.__name__)
            self.MSSQL_InitCursor(SourceFunction=self.DataVCore_RunAfterRender.__name__)
            #Set All Parameters Without User Touching it for straight searching...
            self.DataVCore_PatternEnabler()
            self.DataVCore_SearchFieldSet()
            self.DataVCore_OperatorSet()
            self.DataVCore_PatternSetter()
            self.DataVCore_LoadTableSets()
            
        except (Exception, MSSQL.DatabaseError) as FunctionErrorMsg:
            self.InventoryStatus.showMessage('Application Error: RunAfterRender Returns an Error. Detailed Info |> {}'.format(FunctionErrorMsg))
            print('[Exception Thrown @ DataVCore_RunAfterRender] > RunAfterRender Returns an Error. Detailed Info |>  {}'.format(FunctionErrorMsg))
            
        # Pattern Enabler, Function for Switching Methods
    def DataVCore_PatternEnabler(self):
        if self.SearchPattern_ExactOpt.isChecked():
            self.SearchPattern_ComboBox.setEnabled(False)
            self.Query_Operator.setEnabled(True)
            self.DataVCore_OperatorSet()
            self.DataVCore_PatternSetter()
            self.InventoryStatus.showMessage('Search Pattern: Switched to Exact Mode...')
        elif self.SearchPattern_ContainOpt.isChecked():
            self.Query_Operator.setEnabled(False)
            self.DataVCore_OperatorSet()
            self.DataVCore_PatternSetter()
            self.SearchPattern_ComboBox.setEnabled(True)
            self.InventoryStatus.showMessage('Search Pattern: Switched to Pattern String Mode...')
        else:
            self.InventoryStatus.showMessage('Application Error: No Other Radio Buttons has a state of Bool(True).')
            print('[Exception Thrown @ DataVCore_PatternSetter] > No Other Radio Buttons has a state of Bool(True).')

    # Table Search Functions / Logical Function
    def DataVCore_SearchFieldSet(self):
        if self.Query_ColumnOpt.currentText() == 'None':
            self.Query_Operator.setEnabled(False)
            self.Query_ValueToSearch.setEnabled(False)
            self.SearchPattern_ContainOpt.setEnabled(False)
            self.SearchPattern_ExactOpt.setEnabled(False)
            self.SearchPattern_ComboBox.setEnabled(False)
            self.Query_ValueToSearch.clear()
        else:
            self.FieldParameter = self.Query_ColumnOpt.currentText()
            self.Query_Operator.setEnabled(True)
            self.Query_ValueToSearch.setEnabled(True)
            self.SearchPattern_ContainOpt.setEnabled(True)
            self.SearchPattern_ExactOpt.setEnabled(True)

            if self.SearchPattern_ContainOpt.isChecked():
                self.Query_Operator.setEnabled(False)
                self.SearchPattern_ComboBox.setEnabled(True)

    # Sets Operator When Using Exact Method
    def DataVCore_OperatorSet(self):
        if self.SearchPattern_ExactOpt.isChecked():
            self.OperatorParameter = self.Query_Operator.currentText()
        elif self.SearchPattern_ContainOpt.isChecked():
            self.OperatorParameter = 'LIKE'


    def DataVCore_PatternSetter(self):
        if self.SearchPattern_ExactOpt.isChecked():
            #self.Query_ColumnOpt.model().item(1).setEnabled(False)
            self.TargetParameter = '{}'.format(self.Query_ValueToSearch.text())

        elif self.SearchPattern_ContainOpt.isChecked():
            #self.Query_ColumnOpt.model().item(1).setEnabled(True)
            if self.SearchPattern_ComboBox.currentText() == 'Between':
                self.TargetParameter = "%{}%".format(self.Query_ValueToSearch.text())
            elif self.SearchPattern_ComboBox.currentText() == 'Starting With':
                self.TargetParameter = "{}%".format(self.Query_ValueToSearch.text())
            elif self.SearchPattern_ComboBox.currentText() == 'Ends With':
                self.TargetParameter = "%{}".format(self.Query_ValueToSearch.text())

    #Render Table Columns

    def DataVCore_LoadTableSets(self):
        try:
            self.ActiveTable = self.TableSystem_Selection.currentText()
            if self.ActiveTable == "None":
                self.TechCore_ColOptClear()
                self.Query_ColumnOpt.setEnabled(False)
                self.DataTable_View.setRowCount(0)
                self.DataTable_View.setColumnCount(0)
                self.DataTableTarget = None
                self.Target_TableCol = None

            elif self.ActiveTable == "Supplier Reference Data":
                self.TechCore_ColOptClear()
                self.Query_ColumnOpt.setEnabled(True)
                self.Query_ColumnOpt.addItem("SupplierCode")
                self.Query_ColumnOpt.addItem("SupplierName")
                self.Query_ColumnOpt.addItem("LastDeliveryDate")
                self.Query_ColumnOpt.addItem("NextDeliveryDate")
                self.Query_ColumnOpt.addItem("CreationTime")
                self.Query_ColumnOpt.addItem("LastUpdate")

                self.DataTable_View.setColumnCount(6)
                self.DataTable_View.setHorizontalHeaderLabels(("Supplier Code", "Supplier Name", "Last Delivery Date", "Next Delivery Date", "Creation Time", "Last Update"))
                self.TechCore_ColResp()
                self.DataTable_View.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
                self.DataTableTarget = "SupplierReference"
                self.Target_TableCol = "SupplierCode"

            elif self.ActiveTable == "Inventory Reference Data":
                self.TechCore_ColOptClear()
                self.Query_ColumnOpt.setEnabled(True)
                self.Query_ColumnOpt.addItem("ItemCode")
                self.Query_ColumnOpt.addItem("ItemName")
                self.Query_ColumnOpt.addItem("ItemType")
                self.Query_ColumnOpt.addItem("MaterialType")
                self.Query_ColumnOpt.addItem("AvailableStock")
                self.Query_ColumnOpt.addItem("ItemCost")
                self.Query_ColumnOpt.addItem("ExpiryDate")
                self.Query_ColumnOpt.addItem("CreationTime")
                self.Query_ColumnOpt.addItem("LastUpdate")
                self.DataTable_View.setColumnCount(9)
                self.DataTable_View.setHorizontalHeaderLabels(("Item Code", "Item Name", "Item Type", "Material Type", "Available Stock", "Item Cost", "Expiry Date", "Creation Time", "Last Update"))
                self.TechCore_ColResp()
                self.DataTableTarget = "InventoryItem"
                self.Target_TableCol = "ItemCode"

            elif self.ActiveTable == "Supplier Transaction Data":
                self.TechCore_ColOptClear()
                self.Query_ColumnOpt.setEnabled(True)
                self.Query_ColumnOpt.addItem("ItemCode")
                self.Query_ColumnOpt.addItem("OrderCode")
                self.Query_ColumnOpt.addItem("SupplierCode")
                self.Query_ColumnOpt.addItem("QuantityReceived")
                self.Query_ColumnOpt.addItem("OrderDate")
                self.Query_ColumnOpt.addItem("CreationTime")
                self.Query_ColumnOpt.addItem("LastUpdate")

                self.DataTable_View.setColumnCount(7)
                self.DataTable_View.setHorizontalHeaderLabels(("Item Code", "Order Code", "Supplier Code", "Quantities Received", "Order Date", "Creation Time", "Last Update"))
                self.TechCore_ColResp()
                self.DataTable_View.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
                self.DataTableTarget = "SupplierTransaction"
                self.Target_TableCol = "ItemCode"


            elif self.ActiveTable == "Customer Transaction Data":
                self.TechCore_ColOptClear()
                self.Query_ColumnOpt.setEnabled(True)
                self.Query_ColumnOpt.addItem("TransactCode")
                self.Query_ColumnOpt.addItem("ItemCode")
                self.Query_ColumnOpt.addItem("CreationTime")
                self.Query_ColumnOpt.addItem("LastUpdate")

                self.DataTable_View.setColumnCount(4)
                self.DataTable_View.setHorizontalHeaderLabels(("Transaction Code", "Item Code", "Creation Time", "Last Update"))
                self.TechCore_ColResp()
                self.DataTableTarget = "CustTransaction"
                self.Target_TableCol = "TransactionCode"

            elif self.ActiveTable == "Customer Receipt Data":
                self.TechCore_ColOptClear()
                self.Query_ColumnOpt.setEnabled(True)
                self.Query_ColumnOpt.addItem("TransactCode_Pri")
                self.Query_ColumnOpt.addItem("TransactCode_Sec")
                self.Query_ColumnOpt.addItem("TotalCost")
                self.Query_ColumnOpt.addItem("VATableCost")
                self.Query_ColumnOpt.addItem("VATExempt")
                self.Query_ColumnOpt.addItem("ZeroRated")
                self.Query_ColumnOpt.addItem("NetVAT")
                self.Query_ColumnOpt.addItem("VATRate")
                self.Query_ColumnOpt.addItem("CreationTime")
                self.Query_ColumnOpt.addItem("LastUpdate")

                self.DataTable_View.setColumnCount(10)
                self.TechCore_ColResp()
                self.DataTable_View.setHorizontalHeaderLabels(("Primary TransactCode", "Secondary TransactCode", "Total Cost", "Vatable Cost", "Vat Exempt", "Zero Rated", "Net Vat", "Vat Rate", "Creation Time", "Last Update"))
                self.DataTableTarget = "CustReceipt"
                self.Target_TableCol = "TransactCode_Pri"


            elif self.ActiveTable == "Job Reference Data":
                self.TechCore_ColOptClear()
                self.Query_ColumnOpt.setEnabled(True)
                self.Query_ColumnOpt.addItem("PositionCode")
                self.Query_ColumnOpt.addItem("JobName")

                self.DataTable_View.setColumnCount(2)
                self.DataTable_View.setHorizontalHeaderLabels(("Position Code", "Job Name"))
                self.TechCore_ColResp()
                self.DataTableTarget = "JobPosition"
                self.Target_TableCol = "PositionCode"

            elif self.ActiveTable == "Employee Reference Data":
                self.TechCore_ColOptClear()
                self.Query_ColumnOpt.setEnabled(True)
                self.Query_ColumnOpt.addItem("EmployeeCode")
                self.Query_ColumnOpt.addItem("EmployeeUN")
                self.Query_ColumnOpt.addItem("FirstName")
                self.Query_ColumnOpt.addItem("LastName")
                self.Query_ColumnOpt.addItem("PositionCode")
                self.Query_ColumnOpt.addItem("DOB")
                self.Query_ColumnOpt.addItem("Address")
                self.Query_ColumnOpt.addItem("SSS")
                self.Query_ColumnOpt.addItem("TIN")
                self.Query_ColumnOpt.addItem("PhilHealth")
                self.Query_ColumnOpt.addItem("CreationTime")
                self.Query_ColumnOpt.addItem("LastUpdate")
                
                self.DataTable_View.setColumnCount(12)
                self.DataTable_View.setHorizontalHeaderLabels(("Employee Code", "Employee UN", "First Name", "Last Name",  "Position Code", "DOB", "Address", "SSS", "TIN", "PhilHealth", "Creation Time", "Last Update"))
                self.TechCore_ColResp()
                self.DataTableTarget = "Employees"
                self.Target_TableCol = "EmployeeCode"

            self.DataVCore_Encap_RowData()
            self.DataVCore_LoadTableData()

        except Exception as RenderTableViewMsg:
            self.TechCore_Beep()
            print('[Exception @ DataVCore_LoadTableSets] > Table Sets Rendering Error. Check your arguments. Detailed Info |> {}'.format(str(RenderTableViewMsg)))

    def DataVCore_LoadTableData(self):
        try:
            if self.ActiveTable == "None":
                self.TechCore_RowClear()
                self.StaffAct_Add.setEnabled(False)
                self.StaffAct_Edit.setEnabled(False)
                self.StaffAct_Delete.setEnabled(False)
                self.StaffAct_RefreshData.setEnabled(False)
                print('[Report @ DataVCore_RenderTable] > Active Data Table is None. Nothing to show.')
                self.InventoryStatus.showMessage('Application Report: Active Data Table is None. Nothing to show at the moment.')
            else:
                self.TechCore_RowClear()
                self.DataVCore_RenderTable("SELECT * FROM %s" % (self.DataTableTarget))
                
                if self.DataTable_View.rowCount() == 0:
                    self.StaffAct_Add.setEnabled(True)
                    self.StaffAct_Edit.setEnabled(False)
                    self.StaffAct_Delete.setEnabled(False)
                    self.StaffAct_RefreshData.setEnabled(True)
                    self.Query_ColumnOpt.setEnabled(False)
                else:
                    self.StaffAct_Add.setEnabled(True)
                    #self.StaffAct_Edit.setEnabled(False)
                    self.StaffAct_RefreshData.setEnabled(True)
                    self.Query_ColumnOpt.setEnabled(True)

                self.InventoryStatus.showMessage('Query Process > Data Table View for {} has been refreshed from MSSQL Database. Ready~!'.format(self.DataTableTarget))
                print('[Report @ DataVCore_LoadTableData] > Data Table View for {} has been refreshed from MSSQL Database. Ready~!'.format(self.DataTableTarget))

        except (Exception, MSSQL.DatabaseError) as FunctionErrorMsg:
            self.InventoryStatus.showMessage('Application Error: Error Loading Table Data to Application. Detailed Error > {}'.format(FunctionErrorMsg))
            print('[Exception Thrown @ DataVCore_LoadTableData] > Error Loading Table Data to Application. Detailed Error > {}'.format(FunctionErrorMsg))
    
        # Actual Search Function
    def DataVCore_ValSearch(self): # This function is fired every time there will be changes on the QLineEdit -> Query_ValueToSearch
        try:
            if len(self.Query_ValueToSearch.text()) < 1:
                self.InventoryStatus.showMessage('Query is Now Empty. Resetting Data Table View...')
                self.DataVCore_RefreshData()

            elif self.Query_ColumnOpt.currentText() == "None":
                print('Search Query Selected Column is None. Search Operation is Cancelled.')
                self.InventoryStatus.showMessage('Search Query Selected Column is None. Search Operation is Cancelled.')
            else:
                self.InventoryStatus.showMessage('Looking At Requested Target Value %s @ %s...' % (self.Query_ValueToSearch.text(), self.Query_ColumnOpt.currentText()))
                
                self.TechCore_RowClear()

                print('[Search Operation] Field -> %s | Operator -> %s | Target Value -> %s' % (self.FieldParameter, self.OperatorParameter, self.TargetParameter))
                print('[Search Query] SELECT * FROM %s WHERE %s %s %s' % (self.DataTableTarget, self.FieldParameter, self.OperatorParameter, self.TargetParameter))

                self.DataVCore_RenderTable("SELECT * FROM %s WHERE %s %s '%s'" % (self.DataTableTarget, self.FieldParameter, self.OperatorParameter, self.TargetParameter))

        except MSSQL.DataError as SearchQueryError:
            self.InventoryStatus.showMessage('Application Error: Value Searching Returns Error. Detailed Info > %s' (SearchQueryError))
            print('[Exception Thrown @ DataVCore_ValSearch] > Value Searching Returns Error. Detailed Info > %s' (SearchQueryError))

    def DataVCore_RenderTable(self, FunctionCall_DataFetch):
        try:
            self.DataFetchExec = self.MSSQL_ExecuteState(MSSQLStatement=FunctionCall_DataFetch, FetchType='All', TableTarget=self.ActiveTable, SourceFunction=self.DataVCore_RenderTable.__name__)
            currentRow = 0
            if self.ActiveTable == "None":
                self.TechCore_RowClear()
                print('[Report @ DataVCore_RenderTable] > Active Data Table is None. Nothing to show.')
                self.InventoryStatus.showMessage('[Report @ DataVCore_RenderTable] > Active Data Table is None. Nothing to show.')
    
            elif self.ActiveTable == "Inventory Reference Data":
                for InventoryData in self.DataFetchExec:
                    self.DataTable_View.setRowCount(currentRow + 1)
    
                    self.DataTable_View.setItem(currentRow, 0, QtWidgets.QTableWidgetItem('%s' % (InventoryData.ItemCode)))
                    self.DataTable_View.setItem(currentRow, 1, QtWidgets.QTableWidgetItem('%s' % (InventoryData.ItemName)))
                    self.DataTable_View.setItem(currentRow, 2, QtWidgets.QTableWidgetItem('%s' % (InventoryData.ItemType)))
                    self.DataTable_View.setItem(currentRow, 3, QtWidgets.QTableWidgetItem('%s' % (InventoryData.MaterialType)))
                    self.DataTable_View.setItem(currentRow, 4, QtWidgets.QTableWidgetItem('%s' % (InventoryData.AvailableStock)))
                    self.DataTable_View.setItem(currentRow, 5, QtWidgets.QTableWidgetItem('%s' % (InventoryData.ItemCost)))
                    self.DataTable_View.setItem(currentRow, 6, QtWidgets.QTableWidgetItem('%s' % (InventoryData.ExpiryDate)))
                    self.DataTable_View.setItem(currentRow, 7, QtWidgets.QTableWidgetItem('%s' % (InventoryData.CreationTime)))
                    self.DataTable_View.setItem(currentRow, 8, QtWidgets.QTableWidgetItem('%s' % (InventoryData.LastUpdate)))
    
                    for SetCellFixedWidth in range(0, self.DataTable_View.columnCount()):
                        ColumnPosFixer = self.DataTable_View.item(currentRow, SetCellFixedWidth)
                        ColumnPosFixer.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    currentRow += 1
    

            elif self.ActiveTable == "Supplier Reference Data":
                for InventoryData in self.DataFetchExec:
                    self.DataTable_View.setRowCount(currentRow + 1)
    
                    self.DataTable_View.setItem(currentRow, 0, QtWidgets.QTableWidgetItem('%s' % (InventoryData.SupplierCode)))
                    self.DataTable_View.setItem(currentRow, 1, QtWidgets.QTableWidgetItem('%s' % (InventoryData.SupplierName)))
                    self.DataTable_View.setItem(currentRow, 2, QtWidgets.QTableWidgetItem('%s' % (InventoryData.LastDeliveryDate)))
                    self.DataTable_View.setItem(currentRow, 3, QtWidgets.QTableWidgetItem('%s' % (InventoryData.NextDeliveryDate)))
                    self.DataTable_View.setItem(currentRow, 4, QtWidgets.QTableWidgetItem('%s' % (InventoryData.CreationTime)))
                    self.DataTable_View.setItem(currentRow, 5, QtWidgets.QTableWidgetItem('%s' % (InventoryData.LastUpdate)))
    
                    for SetCellFixedWidth in range(0, self.DataTable_View.columnCount()):
                        ColumnPosFixer = self.DataTable_View.item(currentRow, SetCellFixedWidth)
                        ColumnPosFixer.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    currentRow += 1
    
            elif self.ActiveTable == "Supplier Transaction Data":
                for InventoryData in self.DataFetchExec:
                    self.DataTable_View.setRowCount(currentRow + 1)
    
                    self.DataTable_View.setItem(currentRow, 0, QtWidgets.QTableWidgetItem('%s' % (InventoryData.ItemCode)))
                    self.DataTable_View.setItem(currentRow, 1, QtWidgets.QTableWidgetItem('%s' % (InventoryData.OrderCode)))
                    self.DataTable_View.setItem(currentRow, 2, QtWidgets.QTableWidgetItem('%s' % (InventoryData.SupplierCode)))
                    self.DataTable_View.setItem(currentRow, 3, QtWidgets.QTableWidgetItem('%s' % (InventoryData.QuantityReceived)))
                    self.DataTable_View.setItem(currentRow, 4, QtWidgets.QTableWidgetItem('%s' % (InventoryData.OrderDate)))
                    self.DataTable_View.setItem(currentRow, 5, QtWidgets.QTableWidgetItem('%s' % (InventoryData.CreationTime)))
                    self.DataTable_View.setItem(currentRow, 6, QtWidgets.QTableWidgetItem('%s' % (InventoryData.LastUpdate)))
    
                    for SetCellFixedWidth in range(0, self.DataTable_View.columnCount()):
                        ColumnPosFixer = self.DataTable_View.item(currentRow, SetCellFixedWidth)
                        ColumnPosFixer.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    currentRow += 1
    
            elif self.ActiveTable == "Customer Receipt Data":
                for InventoryData in self.DataFetchExec:
                    self.DataTable_View.setRowCount(currentRow + 1)
    
                    self.DataTable_View.setItem(currentRow, 0, QtWidgets.QTableWidgetItem('%s' % (InventoryData.TransactCode_Pri)))
                    self.DataTable_View.setItem(currentRow, 1, QtWidgets.QTableWidgetItem('%s' % (InventoryData.TransactCode_Sec)))
                    self.DataTable_View.setItem(currentRow, 2, QtWidgets.QTableWidgetItem('%s' % (InventoryData.TotalCost)))
                    self.DataTable_View.setItem(currentRow, 3, QtWidgets.QTableWidgetItem('%s' % (InventoryData.VatableCost)))
                    self.DataTable_View.setItem(currentRow, 4, QtWidgets.QTableWidgetItem('%s' % (InventoryData.VatExempt)))
                    self.DataTable_View.setItem(currentRow, 5, QtWidgets.QTableWidgetItem('%s' % (InventoryData.ZeroRated)))
                    self.DataTable_View.setItem(currentRow, 6, QtWidgets.QTableWidgetItem('%s' % (InventoryData.NetVat)))
                    self.DataTable_View.setItem(currentRow, 7, QtWidgets.QTableWidgetItem('%s' % (InventoryData.VatRate)))
                    self.DataTable_View.setItem(currentRow, 8, QtWidgets.QTableWidgetItem('%s' % (InventoryData.CreationTime)))
                    self.DataTable_View.setItem(currentRow, 9, QtWidgets.QTableWidgetItem('%s' % (InventoryData.LastUpdate)))
    
                    for SetCellFixedWidth in range(0, self.DataTable_View.columnCount()):
                        ColumnPosFixer = self.DataTable_View.item(currentRow, SetCellFixedWidth)
                        ColumnPosFixer.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    currentRow += 1

            elif self.ActiveTable == "Customer Transaction Data":
                for InventoryData in self.DataFetchExec:
                    self.DataTable_View.setRowCount(currentRow + 1)
    
                    self.DataTable_View.setItem(currentRow, 0, QtWidgets.QTableWidgetItem('%s' % (InventoryData.TransactionCode)))
                    self.DataTable_View.setItem(currentRow, 1, QtWidgets.QTableWidgetItem('%s' % (InventoryData.ItemCode)))
                    self.DataTable_View.setItem(currentRow, 2, QtWidgets.QTableWidgetItem('%s' % (InventoryData.CreationTime)))
                    self.DataTable_View.setItem(currentRow, 3, QtWidgets.QTableWidgetItem('%s' % (InventoryData.LastUpdate)))
    
                    for SetCellFixedWidth in range(0, self.DataTable_View.columnCount()):
                        ColumnPosFixer = self.DataTable_View.item(currentRow, SetCellFixedWidth)
                        ColumnPosFixer.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    currentRow += 1
    
    
            elif self.ActiveTable == "Job Reference Data":
                for InventoryData in self.DataFetchExec:
                    self.DataTable_View.setRowCount(currentRow + 1)
    
                    self.DataTable_View.setItem(currentRow, 0, QtWidgets.QTableWidgetItem('%s' % (InventoryData.PositionCode)))
                    self.DataTable_View.setItem(currentRow, 1, QtWidgets.QTableWidgetItem('%s' % (InventoryData.JobName)))
    
                    for SetCellFixedWidth in range(0, self.DataTable_View.columnCount()):
                        ColumnPosFixer = self.DataTable_View.item(currentRow, SetCellFixedWidth)
                        ColumnPosFixer.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    currentRow += 1

            elif self.ActiveTable == "Employee Reference Data":
                for InventoryData in self.DataFetchExec:
                    self.DataTable_View.setRowCount(currentRow + 1)
    
                    self.DataTable_View.setItem(currentRow, 0, QtWidgets.QTableWidgetItem('%s' % (InventoryData.EmployeeCode)))
                    self.DataTable_View.setItem(currentRow, 1, QtWidgets.QTableWidgetItem('%s' % (InventoryData.EmployeeUN)))
                    self.DataTable_View.setItem(currentRow, 2, QtWidgets.QTableWidgetItem('%s' % (InventoryData.FirstName)))
                    self.DataTable_View.setItem(currentRow, 3, QtWidgets.QTableWidgetItem('%s' % (InventoryData.LastName)))
                    self.DataTable_View.setItem(currentRow, 4, QtWidgets.QTableWidgetItem('%s' % (InventoryData.PositionCode)))
                    self.DataTable_View.setItem(currentRow, 5, QtWidgets.QTableWidgetItem('%s' % (InventoryData.DOB)))
                    self.DataTable_View.setItem(currentRow, 6, QtWidgets.QTableWidgetItem('%s' % (InventoryData.Address)))
                    self.DataTable_View.setItem(currentRow, 7, QtWidgets.QTableWidgetItem('%s' % (InventoryData.SSS)))
                    self.DataTable_View.setItem(currentRow, 8, QtWidgets.QTableWidgetItem('%s' % (InventoryData.TIN)))
                    self.DataTable_View.setItem(currentRow, 9, QtWidgets.QTableWidgetItem('%s' % (InventoryData.PhilHealth)))
                    self.DataTable_View.setItem(currentRow, 10, QtWidgets.QTableWidgetItem('%s' % (InventoryData.TIN)))
                    self.DataTable_View.setItem(currentRow, 11, QtWidgets.QTableWidgetItem('%s' % (InventoryData.CreationTime)))
                    self.DataTable_View.setItem(currentRow, 12, QtWidgets.QTableWidgetItem('%s' % (InventoryData.LastUpdate)))
    
                    for SetCellFixedWidth in range(0, self.DataTable_View.columnCount()):
                        ColumnPosFixer = self.DataTable_View.item(currentRow, SetCellFixedWidth)
                        ColumnPosFixer.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                    currentRow += 1
                    
        except MSSQL.DataError as IterError:
            self.InventoryStatus.showMessage('[Database Query Process | Search Query] -> An Error Occured While Searching Value. Data Type might not be the same.')
            print('[Exception Thrown @ DataVCore_RenderTable] ->  An Error Occured While Searching Value. Data Type might not be the same. Detailed Error |> %s' % IterError)
    

    def DataVCore_Encap_RowData(self):
        if self.DataTable_View.currentRow() != -1:
            self.StaffAct_Delete.setEnabled(True)
            self.StaffAct_Edit.setEnabled(True)
        else:
            self.StaffAct_Delete.setEnabled(False)
            self.StaffAct_Edit.setEnabled(False)

    # Staff Action Functions

    def DataVCore_AddEntry(self):
        self.ModifierDialog = Route88_ModifierCore(RecentTableActive=self.DataTableTarget, ModifierMode="PushEntry", StaffInCharge_Name=self.InCharge_LiteralName, Staff_DBUser=self.InCharge_DBUser, Staff_DBPass=self.InCharge_DBPass)
        self.ModifierDialog.exec_()
        self.DataVCore_RefreshData()

    def DataVCore_EditEntry(self):
        try:
            SelectedColData = [] 
            for ColIndexData in range(self.DataTable_View.columnCount()):
                SelectedColData.append(self.DataTable_View.item(self.DataTable_View.currentRow(), ColIndexData).text())

            self.ModifierDialog = Route88_ModifierCore(RecentTableActive=self.DataTableTarget, ModifierMode="ModifyDataExists", DataPayload_AtRow=SelectedColData, StaffInCharge_Name=self.InCharge_LiteralName, Staff_DBUser=self.InCharge_DBUser, Staff_DBPass=self.InCharge_DBPass)
            self.ModifierDialog.exec_()
            self.DataVCore_RefreshData()
        except Exception:
            self.StaffAct_Edit.setEnabled(False)
            self.StaffAct_Delete.setEnabled(False)
            self.InventoryStatus.showMessage('Select Data Error > Selected Data is Forgotten, Please Select The Data You Wish To Delete or Edit again.')


    def DataVCore_DeleteEntry(self):
        try:
            if self.DataTable_View.rowCount() == 0:
                self.StaffAct_Delete.setEnabled(False)
                self.InventoryStatus.showMessage('Table Data Error > Table View is currently empty. You cannot delete any data anymore.')
                print('Report @ DataVCore_DeleteEntry] Table View is currently empty. You cannot delete any data anymore.')
            else:
                self.StaffAct_Delete.setEnabled(True)
                ConfirmDelMsg = QtWidgets.QMessageBox()
                ConfirmDelMsg.setIcon(QtWidgets.QMessageBox.Information)
                ConfirmDelMsg.setWindowTitle('Route88 System | Data Deletion')
                ConfirmDelMsg.setStandardButtons(QtWidgets.QMessageBox.Discard | QtWidgets.QMessageBox.Abort)

                if self.ActiveTable == "Inventory Reference Data":
                    ConfirmDelMsg.setText("Are you sure you want to delete / discard your selected data? This data associated from other data will be affected as well such as Customer Receipts and Supplier Transactions might delete this item from the history as well~! Please Proceed with Caution!")
                
                elif self.ActiveTable == "Supplier Reference Data":
                    ConfirmDelMsg.setText("Are you sure you want to delete / discard your selected data? This data associated with Supplier Transaction will be deleted as well. Please Proceed with Caution!")

                elif self.ActiveTable == "Supplier Transaction Data":
                    ConfirmDelMsg.setText("Are you sure you want to delete / discard your selected data? This data has significance over histories of item orders from the suppliers~! Please Proceed with Caution!")

                elif self.ActiveTable == "Customer Transaction Data":
                    ConfirmDelMsg.setText("Are you sure you want to delete / discard your selected data? This data is associated with Customer Receipts. Deleting it will delete / discard it's associated data from Customer Receipts. Please Proceed with Caution!")

                elif self.ActiveTable == "Customer Receipt Data":
                    ConfirmDelMsg.setText("Are you sure you want to delete / discard your selected data? This data associated with Customer Transaction will delete / discard any associated data from Customer Transaction~! Please Proceed with Caution!")

                elif self.ActiveTable == "Employee Reference Data":
                    ConfirmDelMsg.setText("Are you sure you want to delete / discard your selected data? Deleting this data will result to dropping the selected user login, which unables to perform executions in the program and access as well. Please Proceed with Caution!")

                elif self.ActiveTable == "Job Reference Data":
                    ConfirmDelMsg.setText("Are you sure you want to delete / discard your selected data? Any employee that is under from the selected position code will result to dropping their data as well~! Please Proceed with Caution!")

                ConfirmDeletion = ConfirmDelMsg.exec_()

                if ConfirmDeletion == QtWidgets.QMessageBox.Abort:
                    print('[Report @ DataVCore_DeleteEntry] > Operation Data Deletion @ %s is Cancelled.' % (self.ActiveTable))
                    self.InventoryStatus.showMessage('Operation Data Deletion @ %s is Cancelled.' % (self.ActiveTable))

                else:
                    selectedData = self.DataTable_View.item(self.DataTable_View.currentRow(), 0).text()
                    print('[Database Query Process | Deletion Query] -> DELETE FROM %s WHERE %s = %s' % (self.DataTableTarget, self.Target_TableCol, selectedData))
                    self.InventoryStatus.showMessage('Deletion Query: Processing to Delete Row %s' % (self.DataTable_View.currentRow()))

                    self.MSSQLDataWireCursor.execute('DELETE FROM %s WHERE %s = %s' % (self.DataTableTarget, self.Target_TableCol, selectedData))

                    self.TechCore_RowClearSelected(self.DataTable_View.currentRow())

                    self.MSSQL_CommitData()

                    self.InventoryStatus.showMessage('Deletion Query | > Data Row %s has been deleted!' % (self.DataTable_View.currentRow() + 1))
                    if self.DataTable_View.rowCount() == 0:
                        self.StaffAct_Delete.setEnabled(False)
                    else:
                        self.StaffAct_Delete.setEnabled(True)


        except (Exception, MSSQL.Error, MSSQL.OperationalError) as DelectionErrMsg:
            self.InventoryStatus.showMessage('[Database Query Process | Deletion Query] -> No Selected Row To Delete...')
            print('[Exception Thrown @ DataVCore_DeleteEntry] -> There Might Be No Selected Row To Delete... Detailed Error |> {}'.format(str(DelectionErrMsg)))
    
    # Exit Function
    def DataVCore_ReturnWindow(self):
        self.close()
        self.ReturnWinInst = Route88_WindowController(Staff_Name=self.InCharge_LiteralName, Staff_Job=self.InCharge_JobPos, Staff_DBUser=self.InCharge_DBUser, Staff_DBPass=self.InCharge_DBPass)
        self.ReturnWinInst.show()

    def DataVCore_RefreshData(self):
        try:
            self.TechCore_RowClear()
            self.DataVCore_LoadTableData()

        except (Exception, MSSQL.Error, MSSQL.OperationalError) as RefreshError:
            self.InventoryStatus.showMessage('Application Error: {0}'.format(str(RefreshError)))
            raise Exception('[Exception Thrown @ DataVCore_RefreshData] -> {0}'.format(str(RefreshError)))

class Route88_POSCore(Ui_Route88_POS_SystemWindow, QtWidgets.QMainWindow, Route88_TechnicalCore):
    def __init__(self, Parent=None, StaffInCharge_Name=None, StaffInCharge_Job=None, StaffInCharge_DBUser=None, StaffInCharge_DBPass=None):
        super(Route88_POSCore, self).__init__(Parent=Parent)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('IcoDisplay/r_88.ico'))
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.WindowShadeButtonHint | QtCore.Qt.WindowStaysOnTopHint)
        
        self.POS_StaffName = StaffInCharge_Name
        self.POS_StaffJob = StaffInCharge_Job
        self.POS_Staff_DBU = StaffInCharge_DBUser
        self.POS_Staff_DBP = StaffInCharge_DBPass

        self.actionSwitch_System_User.triggered.connect(self.POSCore_ReturnWindow)


    def POSCore_QtyIncrement(self):
        self.qty += 1
        return self.label_5.setText("Quantity Increased.")

    def POSCore_QtyDecrement(self):
        self.qty -= 1
        return self.label_5.setText("Quantity Decreased.")

    def POSCore_FetchData_Scanner(self):
            #with connection:
            #    cur = connection.cursor()
            #    cur.execute("SELECT ItemCode,ItemName,Cost from inventorylist where ItemCode=%s",#self.lineEdit.text()))
            #    fetch_row = cur.fetchone()
            #    
            #    numRows = self.Order_ItemPickTable.rowCount()
            #    self.qty=1
            #    if fetch_row != None:
            #        self.total=fetch_row[2]+self.total
            #        
            #        self.Order_ItemPickTable.insertRow(numRows)
            #        self.Order_ItemPickTable.setItem(numRows, 0, QtWidgets.QTableWidgetItem(str#(fetch_row[0])))
            #        self.Order_ItemPickTable.setItem(numRows, 1, QtWidgets.QTableWidgetItem(fetch_row#[1]))
            #        self.Order_ItemPickTable.setItem(numRows, 2, QtWidgets.QTableWidgetItem(str#(self.qty)))
            #        self.Order_ItemPickTable.setItem(numRows, 3, QtWidgets.QTableWidgetItem(str#(fetch_row[2])))
            #        self.lineEdit.clear()
            #        self.label_5.setText("Item#: "+str(fetch_row[0])+"\n"+str(fetch_row[1])+" @ "+str#(fetch_row[2]))
            #        self.label_3.setText("₱"+str(self.total))
            #        print(fetch_row)
            #    else:
            #        self.label_5.setText(" Item not found.\n Please try again. ")
            #        self.lineEdit.clear()
        pass

    def POSCore_ReturnWindow(self):
        self.close()
        self.ReturnWinParent = Route88_WindowController(Staff_Name=self.POS_StaffName, Staff_Job=self.POS_StaffJob, Staff_DBUser=self.POS_Staff_DBU, Staff_DBPass=self.POS_Staff_DBP)
        self.ReturnWinParent.show()

class Route88_AboutUsCore(Ui_Route88_AboutUsWindow, QtWidgets.QDialog, Route88_TechnicalCore):
    def __init__(self, Parent=None):
        super(Route88_AboutUsCore, self).__init__(Parent=Parent)
        self.setupUi(self)
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.WindowShadeButtonHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowIcon(QtGui.QIcon('IcoDisplay/r_88.ico'))

        self.AboutSystem_CloseWnd.clicked.connect(self.AboutUs_ReturnWindow)

    def AboutUs_ReturnWindow(self):
        self.close()

class Route88_ModifierCore(Ui_Route88_DataManipulation_Window, QtWidgets.QDialog, Route88_TechnicalCore):
    def __init__(self, Parent=None, ModifierMode=None, RecentTableActive=None, DataPayload_AtRow=None, StaffInCharge_Name=None, isFirstTime=None, Staff_DBUser=None, Staff_DBPass=None):
        super(Route88_ModifierCore, self).__init__(Parent=Parent)
        self.setupUi(self)
        self.DataMCore_RenderExplicits()
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.WindowShadeButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowIcon(QtGui.QIcon('IcoDisplay/r_88.ico'))
        
        self.DataManip_CloseWindow.clicked.connect(self.close)
        self.DataManip_PushData.clicked.connect(self.DataMCore_AddEntry)
        self.DataManip_ResetActiveData.clicked.connect(self.DataMCore_ClearEntry)

        self.DataPayload = DataPayload_AtRow
        self.ModifierMode = ModifierMode
        self.ActiveTargetTable = RecentTableActive
        self.ActiveStaffName = StaffInCharge_Name
        self.ActiveStaffUN = Staff_DBUser
        self.ActiveStaffPW = Staff_DBPass

        self.DataMCore_RunAfterRender(isFirstTime)

        # Technical Functions
    def DataMCore_RenderExplicits(self):
        pass

    def DataMCore_RunAfterRender(self, isReallyLFT):
        try:
            if isReallyLFT:
                self.ActiveTargetTable = "Employees"
                self.MSSQL_OpenCon(UCredential='Route88_TempAuth', PCredential='Route88_Group7', ActiveStaffName=self.ActiveStaffName, SourceFunction=self.DataMCore_RunAfterRender.__name__)
                self.MSSQL_InitCursor(SourceFunction=self.DataMCore_RunAfterRender.__name__)
            else:
                self.MSSQL_OpenCon(UCredential=self.ActiveStaffUN, PCredential=self.ActiveStaffPW, ActiveStaffName=self.ActiveStaffName, SourceFunction=self.DataMCore_RunAfterRender.__name__)
                self.MSSQL_InitCursor(SourceFunction=self.DataMCore_RunAfterRender.__name__)

            if self.ActiveTargetTable == "SupplierReference":
                self.resize(820, 620)
                self.Tab_SelectionSelectives.setCurrentIndex(0)
                self.TechCore_DisableExcept(self.Tab_SelectionSelectives.currentIndex())
                self.SuppEntry_LDD.setDateTime(QtCore.QDateTime.currentDateTime())
                self.SuppEntry_NDD.setDateTime(QtCore.QDateTime.currentDateTime())
                self.SuppEntry_SC.setValidator(QtGui.QIntValidator())

            elif self.ActiveTargetTable == "InventoryItem":
                self.resize(820, 420)
                self.Tab_SelectionSelectives.setCurrentIndex(1)
                self.TechCore_DisableExcept(self.Tab_SelectionSelectives.currentIndex())
                self.InvEntry_ED.setDateTime(QtCore.QDateTime.currentDateTime())
                self.InvEntry_IC.setValidator(QtGui.QIntValidator())
            
            elif self.ActiveTargetTable == "SupplierTransaction":
                self.resize(820, 540)
                self.Tab_SelectionSelectives.setCurrentIndex(2)
                self.TechCore_DisableExcept(self.Tab_SelectionSelectives.currentIndex())
                self.SuppTrEntry_OD.setDateTime(QtCore.QDateTime.currentDateTime())
                self.SuppTrEntry_OC.setValidator(QtGui.QIntValidator())
                self.TechCore_FillUpBox()

            elif self.ActiveTargetTable == "CustTransaction":
                self.resize(820, 450)
                self.Tab_SelectionSelectives.setCurrentIndex(3)
                self.TechCore_DisableExcept(self.Tab_SelectionSelectives.currentIndex())
                self.CustTr_TC.setValidator(QtGui.QIntValidator())

            elif self.ActiveTargetTable == "CustReceipt":
                self.resize(820, 600)
                self.Tab_SelectionSelectives.setCurrentIndex(4)
                self.TechCore_DisableExcept(self.Tab_SelectionSelectives.currentIndex())


            elif self.ActiveTargetTable == "JobPosition":
                self.resize(820, 380)
                self.Tab_SelectionSelectives.setCurrentIndex(5)
                self.TechCore_DisableExcept(self.Tab_SelectionSelectives.currentIndex())
                self.JobPEntry_PC.setValidator(QtGui.QIntValidator())

            elif self.ActiveTargetTable == "Employees":
                self.resize(820, 740)
                self.Tab_SelectionSelectives.setCurrentIndex(6)
                self.TechCore_DisableExcept(self.Tab_SelectionSelectives.currentIndex())
                self.EmpEntry_DOB.setDateTime(QtCore.QDateTime.currentDateTime())
                # Restrict These QLineEdit Object to Accept Only Integer.
                self.EmpEntry_SSS.setValidator(QtGui.QDoubleValidator())
                self.EmpEntry_TIN.setValidator(QtGui.QDoubleValidator())
                self.EmpEntry_PH.setValidator(QtGui.QDoubleValidator())
                # ! Loads All Possible Job To Enroll for Employees
                try:
                    for JobDataFetch in self.MSSQL_ExecuteState(MSSQLStatement="SELECT * FROM JobPosition", FetchType="All", TableTarget="JobPosition", SourceFunction=self.DataMCore_RunAfterRender.__name__):
                        self.EmpEntry_PC.addItem(JobDataFetch.JobName)
                except MSSQL.Error as Error:
                    pass

            #Preloads Data Received, Ternary Operator
            self.DataMCore_LoadEntry() if self.ModifierMode == "ModifyDataExists" else None

        except (Exception, MSSQL.DatabaseError) as DataMCore_ARErr:
            self.TechCore_Beep()
            print('[Exception @ DataMCore_RunAfterRender] > Error Rendering Modifier Core: RunAfterRender. Detailed Error: %s' % (DataMCore_ARErr))
    

        #for DisableIndex in range(1, self.EmpEntry_PC.maxCount()):
        #    pass
            #self.EmpEntry_PC.setEnabled(False)

    # Staff Action Function Declarations
    def DataMCore_AddEntry(self):
        self.MSSQL_InitCursor(SourceFunction=self.DataMCore_AddEntry.__name__)

        if self.ActiveTargetTable == "SupplierReference":
            pass
        elif self.ActiveTargetTable == "InventoryItem":
            pass
        elif self.ActiveTargetTable == "SupplierTransaction":
            pass
        elif self.ActiveTargetTable == "CustTransaction":
            pass
        elif self.ActiveTargetTable == "CustReceipt":
            pass
        elif self.ActiveTargetTable == "JobPosition":
            if len(self.JobPEntry_PC.text()) == 0:
                self.TechCore_Beep()
                self.Modifier_StatusLabel.setText("Error, cannot push data from the database. Job Position Code Should Not Be Empty!")
                QtWidgets.QMessageBox.critical(self, 'Route88 System | Data Manipulation Error', "Error, cannot push data from the database. Job Position Code Should Not Be Empty!", QtWidgets.QMessageBox.Ok)
            elif len(self.JobPEntry_PN.text()) < 2:
                self.TechCore_Beep()
                self.Modifier_StatusLabel.setText("Error, cannot push data from the database. Job Position Name Description Should Be More Than 2 Characters.")
                QtWidgets.QMessageBox.critical(self, 'Route88 System | Data Manipulation Error', "Error, cannot push data from the database. Job Position Name Description Should Be More Than 2 Characters.", QtWidgets.QMessageBox.Ok)
            else:
                try:
                    self.MSSQL_ExecuteState("INSERT INTO JobPosition VALUES ('%s', '%s')" % (self.JobPEntry_PC.text(), self.JobPEntry_PN.text()),TableTarget="JobPosition", SourceFunction=self.DataMCore_AddEntry.__name__)
                    self.MSSQL_CommitData()
                    self.Modifier_StatusLabel.setText("Position Code %s with Job Name of %s is added to the database! Clear Data To Add More Staff." % (self.JobPEntry_PC.text(), self.JobPEntry_PN.text())) 
                    self.DataManip_PushData.setEnabled(False)
                    QtWidgets.QMessageBox.information(self, 'Route88 System | Data Manipulation', "Position Code %s with Job Name of %s is added to the database! Clear Data To Add More Staff." % (self.JobPEntry_PC.text(), self.JobPEntry_PN.text()), QtWidgets.QMessageBox.Ok)
                except Exception:
                    pass
        elif self.ActiveTargetTable == "Employees":
            if len(self.EmpEntry_FN.text()) < 2:
                self.TechCore_Beep()
                self.Modifier_StatusLabel.setText("Error, cannot push data from the database. Employee's First Name Should Be More Than 2 Characters.")
                QtWidgets.QMessageBox.critical(self, 'Route88 System | Data Manipulation Error', "Error, cannot push data from the database. Employee's First Name Should Be More Than 2 Characters.", QtWidgets.QMessageBox.Ok)

            elif len(self.EmpEntry_LN.text()) < 2:
                self.TechCore_Beep()
                self.Modifier_StatusLabel.setText("Error, cannot push data from the database. Employee's Last Name Should Be More Than 2 Characters.")
                QtWidgets.QMessageBox.critical(self, 'Route88 System | Data Manipulation Error', "Error, cannot push data from the database. Employee's Last Name Should Be More Than 2 Characters.", QtWidgets.QMessageBox.Ok)

            elif self.EmpEntry_PC.currentIndex() == -1:
                self.TechCore_Beep()
                self.Modifier_StatusLabel.setText("Error, cannot push data from the database. Employee's Position Code is not yet selected.")
                QtWidgets.QMessageBox.critical(self, 'Route88 System | Data Manipulation Error', "Error, cannot push data from the database. Employee's Position Code is not yet selected.", QtWidgets.QMessageBox.Ok)

            elif len(self.EmpEntry_Adrs.text()) < 10:
                self.TechCore_Beep()
                self.Modifier_StatusLabel.setText("Error, cannot push data from the database. Employee's Address Should Be More Than 10 Characters.")
                QtWidgets.QMessageBox.critical(self, 'Route88 System | Data Manipulation Error', "Error, cannot push data from the database. Employee's Address Should Be More Than 10 Characters.", QtWidgets.QMessageBox.Ok)
            
            elif len(self.EmpEntry_SSS.text()) != self.EmpEntry_SSS.maxLength():
                self.TechCore_Beep()
                self.Modifier_StatusLabel.setText("Error, cannot push data from the database. Employee's SSS must be 10 Numbers.")
                QtWidgets.QMessageBox.critical(self, 'Route88 System | Data Manipulation Error', "Error, cannot push data from the database. Employee's SSS must be 10 Numbers.", QtWidgets.QMessageBox.Ok)

            elif len(self.EmpEntry_TIN.text()) != self.EmpEntry_TIN.maxLength():
                self.TechCore_Beep()
                self.Modifier_StatusLabel.setText("Error, cannot push data from the database. Employee's TIN must be 10 Numbers.")
                QtWidgets.QMessageBox.critical(self, 'Route88 System | Data Manipulation Error', "Error, cannot push data from the database. Employee's TIN must be 12 Numbers.", QtWidgets.QMessageBox.Ok)
        
            elif len(self.EmpEntry_PH.text()) != self.EmpEntry_PH.maxLength():
                self.TechCore_Beep()
                self.Modifier_StatusLabel.setText("Error, cannot push data from the database. Employee's PhilHealth must be 10 Numbers.")
                QtWidgets.QMessageBox.critical(self, 'Route88 System | Data Manipulation Error', "Error, cannot push data from the database. Employee's PhilHealth must be 10 Numbers.", QtWidgets.QMessageBox.Ok)

            elif len(self.EmpEntry_UN.text()) < 5:
                self.TechCore_Beep()
                self.Modifier_StatusLabel.setText("Error, cannot push data from the database. Employee's Username must be more than 5 characters.")
                QtWidgets.QMessageBox.critical(self, 'Route88 System | Data Manipulation Error', "Error, cannot push data from the database. Employee's Username must be more than 5 characters.", QtWidgets.QMessageBox.Ok)

            elif len(self.EmpEntry_PW.text()) < 5:
                self.TechCore_Beep()
                self.Modifier_StatusLabel.setText("Error, cannot push data from the database. Employee's Password must be more than 5 characters.")
                QtWidgets.QMessageBox.critical(self, 'Route88 System | Data Manipulation Error', "Error, cannot push data from the database. Employee's Password must be more than 5 characters.", QtWidgets.QMessageBox.Ok)

            elif self.EmpEntry_PW.text() != self.EmpEntry_CPW.text():
                self.TechCore_Beep()
                self.Modifier_StatusLabel.setText("Error, cannot push data from the database. Employee's Password and Confirm Password is not match.")
                QtWidgets.QMessageBox.critical(self, 'Route88 System | Data Manipulation Error', "Error, cannot push data from the database. Employee's Password and Confirm Password is not match.", QtWidgets.QMessageBox.Ok)

            else:
                try:
                    self.MSSQL_ExecuteState(MSSQLStatement="INSERT INTO Employees(EmployeeUN, EmployeePW, FirstName, LastName, PositionCode, DOB, Address, SSS, TIN, PhilHealth) VALUES ('%s', '%s', '%s', '%s', %s, '%s', '%s', '%s', '%s', '%s')" % 
                    (self.EmpEntry_UN.text(), self.EmpEntry_PW.text(), self.EmpEntry_FN.text(), self.EmpEntry_LN.text(), self.TechCore_NameToPosCode(self.EmpEntry_PC.currentText()), self.EmpEntry_DOB.date().toString("MM/dd/yyyy"), self.EmpEntry_Adrs.text(), self.EmpEntry_SSS.text(), self.EmpEntry_TIN.text(), self.EmpEntry_PH.text()), TableTarget="Employees", SourceFunction=self.DataMCore_AddEntry.__name__)

                    #self.MSSQL_ExecuteState(MSSQLStatement="CREATE LOGIN %s WITH PASSWORD = '%s'" % (self.EmpEntry_UN.text(), self.EmpEntry_PW.text()), TableTarget="<Classified>", SourceFunction=self.DataMCore_AddEntry.__name__)
                    #if self.EmpEntry_PC.currentIndex() == 0:
                    #    self.MSSQL_ExecuteState(MSSQLStatement="{CALL sp_addrolemember '%s', '%s'}" % ('db_accessadmin', self.EmpEntry_UN.text()), TableTarget="<Classified>", SourceFunction=self.DataMCore_AddEntry.__name__)

                    self.MSSQL_CommitData()
                except (Exception, MSSQL.Error):
                    self.MSSQL_RollbackData(SourceFunction=self.DataMCore_AddEntry.__name__)

                self.Modifier_StatusLabel.setText("Staff %s %s is added to the database! Clear Data To Add More Staff." % (self.EmpEntry_FN.text(), self.EmpEntry_LN.text())) 
                self.DataManip_PushData.setEnabled(False)
                QtWidgets.QMessageBox.information(self, 'Route88 System | Data Manipulation', "Staff %s %s is added to the database!" % (self.EmpEntry_FN.text(), self.EmpEntry_LN.text()), QtWidgets.QMessageBox.Ok)

    def DataMCore_LoadEntry(self):
        self.DataManip_PushData.setText("Apply Modified Entry")
        self.DataManip_ResetActiveData.setEnabled(False)
        if self.ActiveTargetTable == "SupplierReference":
            self.SuppEntry_SC.setText(self.DataPayload[0])
            self.SuppEntry_SN.setText(self.DataPayload[1])
            self.SuppEntry_LDD.setDate(QtCore.QDate.fromString(self.DataPayload[2], "yyyy-MM-dd"))
            self.SuppEntry_NDD.setDate(QtCore.QDate.fromString(self.DataPayload[3], "yyyy-MM-dd"))
            
        elif self.ActiveTargetTable == "InventoryItem":
            self.InvEntry_IC.setText(self.DataPayload[0])
            self.InvEntry_IN.setText(self.DataPayload[1])
            self.InvEntry_IT.setCurrentIndex(self.TechCore_StrToIndex(RespectiveComboBox="Item Type", StrToCompare=self.DataPayload[2], SourceFunction=self.DataMCore_LoadEntry.__name__))
            self.InvEntry_MT.setCurrentIndex(self.TechCore_StrToIndex(RespectiveComboBox="Material Type", StrToCompare=self.DataPayload[3], SourceFunction=self.DataMCore_LoadEntry.__name__))
            
            self.InvEntry_Q.setValue(int(self.DataPayload[4]))
            self.InvEntry_C.setValue(float(self.DataPayload[5]))
            self.InvEntry_ED.setDate(QtCore.QDate.fromString(self.DataPayload[6], "yyyy-MM-dd"))

        elif self.ActiveTargetTable == "SupplierTransaction":
            self.TechCore_FillUpBox()
            self.SuppTrEntry_IC.setCurrentIndex(self.TechCore_StrToIndex(RespectiveComboBox="Item Code", StrToCompare=self.DataPayload[0], SourceFunction=self.DataMCore_LoadEntry.__name__))
            self.SuppTrEntry_OC.setText(self.DataPayload[1])
            self.SuppTrEntry_SC.setCurrentIndex(self.TechCore_StrToIndex(RespectiveComboBox="Supplier Code", StrToCompare=self.DataPayload[2], SourceFunction=self.DataMCore_LoadEntry.__name__))
            self.SuppTrEntry_QOR.setValue(int(self.DataPayload[3]))
            self.SuppTrEntry_OD.setDate(QtCore.QDate.fromString(self.DataPayload[4], "yyyy-MM-dd"))

        elif self.ActiveTargetTable == "CustTransaction":
            self.TechCore_FillUpBox()
            self.CustTr_TC.setText(self.DataPayload[0])
            self.CustTr_IC.setCurrentIndex(self.TechCore_StrToIndex(StrToCompare=self.DataPayload[1], SourceFunction=self.DataMCore_LoadEntry.__name__))

        elif self.ActiveTargetTable == "CustReceipt":
            self.TechCore_FillUpBox()
            self.CustREntry_PTrC.setCurrentIndex(self.TechCore_StrToIndex(RespectiveComboBox="Primary Transaction Code", StrToCompare=self.DataPayload[0], SourceFunction=self.DataMCore_LoadEntry.__name__))
            self.CustREntry_STrC.setCurrentIndex(self.TechCore_StrToIndex(RespectiveComboBox="Secondary Transaction Code", StrToCompare=self.DataPayload[1], SourceFunction=self.DataMCore_LoadEntry.__name__))
            self.CustREntry_TC.setText(self.DataPayload[2])
            self.CustREntry_VC.setText(self.DataPayload[3])
            self.CustREntry_VE.setText(self.DataPayload[4])
            self.CustREntry_ZR.setText(self.DataPayload[5])
            self.CustREntry_NV.setText(self.DataPayload[6])
            self.CustREntry_VR.setText(self.DataPayload[7])

        elif self.ActiveTargetTable == "JobPosition":
           self.JobPEntry_PC.setText(self.DataPayload[0])
           self.JobPEntry_PN.setText(self.DataPayload[1])

        elif self.ActiveTargetTable == "Employees":
            # self.DataPayload Index #2 is Ignored Due To Displaying Employees Password
            self.EmpEntry_UN.setText(self.DataPayload[1])
            self.EmpEntry_FN.setText(self.DataPayload[3])
            self.EmpEntry_LN.setText(self.DataPayload[4])
            self.TechCore_EditBindComboBox(self.DataPayload[5])
            self.EmpEntry_DOB.setDate(QtCore.QDate.fromString(self.DataPayload[6], "yyyy-MM-dd"))
            self.EmpEntry_Adrs.setText(self.DataPayload[7])
            self.EmpEntry_SSS.setText(self.DataPayload[8])
            self.EmpEntry_TIN.setText(self.DataPayload[9])
            self.EmpEntry_PH.setText(self.DataPayload[10])
            
            self.EmpEntry_UN.setEnabled(False)

    def DataMCore_ClearEntry(self, ActiveEntryWindow):
        self.DataManip_PushData.setEnabled(True)

        if self.Tab_SelectionSelectives.currentIndex() == 0:
            self.SuppEntry_SC.clear()
            self.SuppEntry_SN.clear()
            self.SuppEntry_LDD.setDateTime(QtCore.QDateTime.currentDateTime())
            self.SuppEntry_NDD.setDateTime(QtCore.QDateTime.currentDateTime())
            self.Modifier_StatusLabel.setText('Fields Cleared on Supplier Reference Window. Ready!')
            print('[Execution @ DataMCore_ClearEntry] -> Finished Clearing Up Fields @ Supplier Reference Window. Ready!')

        if self.Tab_SelectionSelectives.currentIndex() == 1:
            self.InvEntry_IC.clear()
            self.InvEntry_IN.clear()
            self.InvEntry_IT.setCurrentIndex(0)
            self.InvEntry_MT.setCurrentIndex(0)
            self.InvEntry_Q.setValue(0)
            self.InvEntry_C.setValue(0.0)
            self.InvEntry_ED.setDateTime(QtCore.QDateTime.currentDateTime())
            self.Modifier_StatusLabel.setText('Fields Cleared on Inventory Reference Window. Ready!')
            print('[Execution @ DataMCore_ClearEntry] -> Finished Clearing Up Fields @ Inventory Reference Window. Ready!')

        elif self.Tab_SelectionSelectives.currentIndex() == 2:
            self.SuppTrEntry_IC.setCurrentIndex(0)
            self.SuppTrEntry_OC.setCurrentIndex(0)
            self.SuppTrEntry_SC.setCurrentIndex(0)
            self.SuppTrEntry_OD.setDateTime(QtCore.QDateTime.currentDateTime())
            self.SuppTrEntry_QOR.setValue(0)
            self.Modifier_StatusLabel.setText('Fields Cleared on Supplier Transaction Window. Ready!')
            print('[Execution @ DataMCore_ClearEntry] -> Finished Clearing Up Fields @ Supplier Transaction Window. Ready!')

        elif self.Tab_SelectionSelectives.currentIndex() == 3:
            self.CustTr_TC.clear()
            self.CustTr_IC.setCurrentIndex(0)
            self.SuppTrEntry_OD.setDateTime(QtCore.QDateTime.currentDateTime())
            self.Modifier_StatusLabel.setText('Fields Cleared on Customer Transaction Window. Ready!')
            print('[Execution @ DataMCore_ClearEntry] -> Finished Clearing Up Fields @ Customer Transaction Window. Ready!')

        elif self.Tab_SelectionSelectives.currentIndex() == 4:
            self.CustREntry_PTrC.setCurrentIndex(0)
            self.CustREntry_STrC.setCurrentIndex(0)
            self.CustREntry_TC.clear()
            self.CustREntry_VC.clear()
            self.CustREntry_VE.clear()
            self.CustREntry_ZR.clear()
            self.CustREntry_NV.clear()
            self.CustREntry_VR.clear()
            self.Modifier_StatusLabel.setText('Fields Cleared on Customer Receipt Window. Ready!')
            print('[Execution @ DataMCore_ClearEntry] -> Finished Clearing Up Fields @ Customer Receipt Window. Ready!')


        elif self.Tab_SelectionSelectives.currentIndex() == 5:
            self.JobPEntry_PC.clear()
            self.JobPEntry_PN.clear()
            self.Modifier_StatusLabel.setText('Fields Cleared on Job Reference Window. Ready!')
            print('[Execution @ DataMCore_ClearEntry] -> Finished Clearing Up Fields @ Job Reference Window. Ready!')

        elif self.Tab_SelectionSelectives.currentIndex() == 6:
            self.EmpEntry_FN.clear()
            self.EmpEntry_LN.clear()
            self.EmpEntry_PC.setCurrentIndex(0)
            self.EmpEntry_DOB.setDateTime(QtCore.QDateTime.currentDateTime())
            self.EmpEntry_Adrs.clear()
            self.EmpEntry_SSS.clear()
            self.EmpEntry_TIN.clear()
            self.EmpEntry_PH.clear()
            self.EmpEntry_UN.clear()
            self.EmpEntry_PW.clear()
            self.EmpEntry_CPW.clear()
            self.EmpEntry_DOB.setDateTime(QtCore.QDateTime.currentDateTime())
            self.Modifier_StatusLabel.setText('Fields Cleared on Employee Reference Window. Ready!')
            print('[Execution @ DataMCore_ClearEntry] -> Finished Clearing Up Fields @ Employee Reference Window. Ready!')

        else:
            self.Modifier_StatusLabel.setText('[Exception @ Modifier_ClearEntry] Current Index of Selected Tab does not match from any defined conditions.')
            print('[Exception @ Modifier_ClearEntry] Current Index of Selected Tab does not match from any defined conditions.')

    def GetDataVCore_ItemValue(self): # For Edit Functions
        pass


class Route88_WindowController(Ui_Route88_Controller_Window, QtWidgets.QDialog, Route88_TechnicalCore):
    def __init__(self, Parent=None, Staff_Name=None, Staff_Job=None, Staff_DBUser=None, Staff_DBPass=None):
        super(Route88_WindowController, self).__init__(Parent=Parent)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('IcoDisplay/r_88.ico'))
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowShadeButtonHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)

        self.StaffLiteralName = Staff_Name
        self.StaffCurrentJob = Staff_Job
        self.StaffDBUser = Staff_DBUser
        self.StaffDBPass = Staff_DBPass
        
        self.ctrl_UserLogout.clicked.connect(self.ShowLoginCore)
        self.ctrl_ExitProgram.clicked.connect(self.close)
        self.ctrl_ManagementSystem.clicked.connect(self.ShowManagementCore)
        self.ctrl_POSSystem.clicked.connect(self.ShowPOSCore)
        self.ctrl_AboutSystem.clicked.connect(self.ShowAboutCore)
        self.ControllerCore_RunAfterRender()

    def ShowLoginCore(self):
        self.Route88_LoginInst = Route88_LoginCore()
        self.Route88_LoginInst.show()
        self.close()

    def ShowManagementCore(self):
        self.Route88_ManageInst = Route88_ManagementCore(InCharge_Name=self.StaffLiteralName, InCharge_Job=self.StaffCurrentJob, InCharge_DBUser=self.StaffDBUser, InCharge_DBPass=self.StaffDBPass)
        self.Route88_ManageInst.show()
        self.close()

    def ShowPOSCore(self):
        self.Route88_POSInst = Route88_POSCore(StaffInCharge_Name=self.StaffLiteralName, StaffInCharge_Job=self.StaffCurrentJob, StaffInCharge_DBUser=self.StaffDBUser, StaffInCharge_DBPass=self.StaffDBPass)
        self.Route88_POSInst.show()
        self.close()

    def ShowAboutCore(self):
        self.Route88_AboutInst = Route88_AboutUsCore()
        self.Route88_AboutInst.show()

    def ControllerCore_RunAfterRender(self):
        self.user_StaffName.setText(self.StaffLiteralName)
        self.user_JobPosition.setText(self.StaffCurrentJob)

        if self.StaffCurrentJob == "Manager" or self.StaffCurrentJob == "General Manager" or self.StaffCurrentJob == "Assistant Manager":
            self.ctrl_ManagementSystem.setEnabled(True)
            self.ctrl_POSSystem.setEnabled(True)
            self.StatusLabel.setText('Staff {} is logged on. Welcome~!'.format(self.StaffLiteralName))

        elif self.StaffCurrentJob == "Cashier":
            self.ctrl_ManagementSystem.setEnabled(False)
            self.ctrl_POSSystem.setEnabled(True)
            self.StatusLabel.setText('Staff Restrictions has been activated for Staff {}.'.format(self.StaffLiteralName))

        else:
            self.ctrl_ManagementSystem.setEnabled(False)
            self.ctrl_POSSystem.setEnabled(False)
            self.TechCore_Beep()
            QtWidgets.QMessageBox.critical(self, 'Route88 Window Controller | User Error', "Staff is Logged Successfully but Not Permitted To Use Any Of The Systems. Sorry!", QtWidgets.QMessageBox.Ok)
            self.StatusLabel.setText('Staff is Logged Successfully but Not Permitted To Use Any Of The Systems. Sorry!'.format(self.StaffLiteralName))

# Literal Procedural Programming Part
if __name__ == "__main__":
    sysHandler.Popen('CLS', shell=True)
    print('[Startup @ Procedural] Route88 Hybrid System Application, Debugger Output')
    app = QtWidgets.QApplication(sys.argv)
    Route88_InitialInst = Route88_LoginCore()
    Route88_InitialInst.show()
    sys.exit(app.exec_())