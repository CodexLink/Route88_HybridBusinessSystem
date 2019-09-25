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
from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from PyQt5.QtMultimedia import QSound
import qdarkstyle
from os import sys
import subprocess as sysHandler
import pyodbc as MSSQL

from Route88_LoginCmpnt import Ui_Route88_Login_Window
from Route88_DataViewerCmpnt import Ui_Route88_DataViewer_Window
from Route88_DataManipCmpnt import Ui_Route88_DataManipulation_Window
from Route88_ControllerCmpnt import Ui_Route88_Controller_Window
#from Route88_POSSystem import %s%s%s

# This class is a database controller by wrapping all confusing parts into a callable function... and any other such that requires global function calling.
class Route88_TechnicalCore(object):
    def __init__(self, Parent=None):
        super().__init__()

    def MSSQL_OpenCon(self, OBDCDriver='{ODBC Driver 17 for SQL Server}', ServerHost='localhost', UCredential=None, PCredential=None, DB_Target='Route88_Database'):
        try:
            self.MSSQLDataWire = MSSQL.connect("DRIVER=%s; SERVER=%s; DATABASE=%s;UID=%s; PWD=%s" % (OBDCDriver, ServerHost, DB_Target, UCredential, PCredential))
            print("[MSSQL Database] Connection Attempt: Staff '%s' with Username '%s' is connected @ Database %s." % ("...", UCredential, DB_Target))

        except (Exception, MSSQL.DatabaseError) as MSSQL_OpenConErrorMsg:
            self.TechCore_Beep()
            self.StatusLabel.setText("Database Error: Cannot Connect to the MSSQL Database. Please restart.")
            print('[Exception @ MSSQL_OpenCon] > Cannot Open / Establish Connection with the MSSQL Database. Detailed Info |> %s' % (MSSQL_OpenConErrorMsg))
            QtWidgets.QMessageBox.critical(self, 'Route88 System | Database Connection Error', "An error occured while connecting to the database.\n\nDetailed Error: '%s'.\n\n Try restarting or re-connecting to MSSQL Server and try again." % (MSSQL_OpenConErrorMsg), QtWidgets.QMessageBox.Ok)
            sys.exit() # Terminate the program 

    def MSSQL_InitCursor(self):
        try:
            self.MSSQLDataWireCursor = self.MSSQLDataWire.cursor()
        except (Exception, MSSQL.DatabaseError) as CursorErrMsg:
            self.TechCore_Beep()
            print('[Exception @ MSSQL_InitCursor] > Invalid Cursor Set. Report this problem to the developers. Detailed Info |> %s' % (CursorErrMsg))

    def MSSQL_ExecuteState(self, MySQLStatement, FetchType=None):
        try:
            if FetchType == 'One':
                return self.MSSQLDataWireCursor.execute(MySQLStatement).fetchone()[0]
            elif FetchType == 'All':
                return self.MSSQLDataWireCursor.execute(MySQLStatement).fetchall()
            else:
                return self.MSSQLDataWireCursor.execute(MySQLStatement)

        except (Exception, MSSQL.DatabaseError) as MSSQL_ExecError:
            self.TechCore_Beep()
            print('[Exception @ MSSQL_ExecuteState] > Error in SQL Statements. Double check your statements. Detailed Info |> %s' % (MSSQL_ExecError))
    
    
    def MSSQL_CommitData(self):
        try:
            return self.MSSQLDataWire.commit()
        except (Exception, MSSQL.DatabaseError) as MSSQL_CommitError:
            self.TechCore_Beep()
            print('[Exception @ MSSQL_CommitData] > Unable To Commit Data... Check your MySQL Connection and try again.Detailed Info |> %s' % (MSSQL_CommitError))

    # Optional Function, but according to the documentation, we don't need to call this one explicitly. It tends to happen automatically.
    def MSSQL_CloseCon(self):
        try:
            return self.MSSQLDataWire.close()
        except (Exception, MSSQL.DatabaseError) as ClosingErr:
            self.TechCore_Beep()
            print('[Exception @ MSSQL_CloseCon] > Unable to Close Connection with the MySQL Statements. Please Terminate XAMPP or Some Statements are still running. Terminate Immediately. Detailed Info |> %s' (ClosingErr))
    
    #Non Database Callable Function
    def TechCore_Beep(self):
        return QtWidgets.QApplication.beep()

    #Not sure for this one...
    def TechCore_MessageBox(self, ObjType=None, WindTitle=None, MsgDetailInfo=None, MsgButtons=None):
        try:
            return ObjType(self, WindTitle, MsgDetailInfo, MsgButtons)
            
        except Exception as MsgSpawnError:
            print('[Exception @ TechCore_MessageBox] >  Error Occured While Spawning QMessageBox. Detailed Error: %s' % (MsgSpawnError))
            
    def TechCore_ColResp(self):
        try:
            self.DataTable_View.resizeColumnsToContents()
            for SetCellFixedElem in range(self.DataTable_View.columnCount()):
                self.DataTable_View.horizontalHeader().setSectionResizeMode(SetCellFixedElem,   QtWidgets.QHeaderView.Stretch)
        except Exception as ResponseError:
            print('[Exception @ TechCore_ColResp] > Error Responsive Rendering in Table View. Detailed Info |> %s' % (ResponseError))
    
    def TechCore_RowClear(self):
        try:
            self.DataTable_View.clearContents()
            self.DataTable_View.setRowCount(0)

        except Exception as RowClearMsg:
            print('[Exception @ TechCore_RowClear] > Row Clearing Returns Error. Detailed Info |> %s' % (RowClearMsg))
    
    def TechCore_RowClearSelected(self, rowIndex):
        return self.DataTable_View.removeRow(rowIndex)

    def TechCore_ColOptClear(self):
        try:
            ColOptIndex = 1
            self.Query_ColumnOpt.setCurrentIndex(0)
            while self.Query_ColumnOpt.count() != 2:
                self.Query_ColumnOpt.removeItem(ColOptIndex + 1)

        except Exception as ColOptClearMsg:
            print('[Exception @ TechCore_ColOptClear] > Column Clearing Returns Error. Detailed Info |> %s' % (ColOptClearMsg))

    def TechCore_DisableExcept(self, ExceptGivenNum):
        for TabIndex in range(self.Tab_SelectionSelectives.count()):
            if TabIndex == ExceptGivenNum:
                continue
            else:
                self.Tab_SelectionSelectives.setTabEnabled(TabIndex, False)
        
    # Two Exact Functions Can Be Encapsulated Into One.
    def TechCore_PosCodeToName(self, PosCode):
        try:
            self.MSSQL_InitCursor()
            ConvertedToName = self.MSSQL_ExecuteState("SELECT JobName FROM JobPosition WHERE PositionCode = %s" % (PosCode,), "One")
            return ConvertedToName

        except (Exception, MSSQL.DatabaseError) as ProcessError:
            print('[Exception @ TechCore_PosCodeToName] > Error Processing PositionCode to JobName. Detailed Info |> %s' % (ProcessError))

    def TechCore_NameToPosCode(self, JobName):
        try:
            self.MSSQL_InitCursor()
            ConvertedToPosCode = self.MSSQL_ExecuteState("SELECT PositionCode FROM JobPosition WHERE JobName = '%s'" % (JobName,), "One")
            return ConvertedToPosCode

        except (Exception, MSSQL.DatabaseError) as ProcessError:
            print('[Exception @ TechCore_NameToPosCode] > Error Processing PositionCode to JobName. Detailed Info |> %s' % (ProcessError))

    def TechCore_RespectSchema(self, SchemaBaseName):
        # Close Any Existing...
        try:
            if SchemaBaseName == "Management":
                self.MSSQL_OpenCon(UCredential='Route88_TempAuth', PCredential='Route88_Group7')
                self.MSSQL_InitCursor()
                self.MSSQL_ExecuteState('SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED')

            elif SchemaBaseName == "EmployeeInfo":
                self.MSSQL_OpenCon(UCredential='Route88_TempAuth', PCredential='Route88_Group7')
                self.MSSQL_InitCursor()
                self.MSSQL_ExecuteState('SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED')

        except (Exception, MSSQL.DatabaseError) as DynamicSchemaErr:
            print('[Exception @ TechCore_RespectSchema] > Error Changing Database Schema. Detailed Error > %s.' % (DynamicSchemaErr))



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
            self.MSSQL_OpenCon(UCredential='Route88_TempAuth', PCredential='Route88_Group7')
            self.MSSQL_InitCursor()
            self.LoginCore_CheckEnlisted()

        except Exception as ErrorHandler:
            self.TechCore_Beep()
            print('[Exception @ LoginCore_RunAfterRender] > One of the MySQL Required Components Returns Error. Detailed Info |> {}'.format(str(ErrorHandler)))
            QtWidgets.QMessageBox.critical(self, 'Route88 Login Form | Database Error', "Error, cannot connect to the database. Please restart the program and re-run the XAMPP MySQL Instance. Detailed Info |> {}".format(str(ErrorHandler)), QtWidgets.QMessageBox.Ok)
            sys.exit() # Terminate the program at all cost.

    #Route88_LoginForm UI Window Functions - StartPoint
    def LoginCore_CheckEnlisted(self):
        try:
            self.MSSQL_InitCursor()
            self.UserEnlistedCount = self.MSSQL_ExecuteState("SELECT COUNT(*) FROM Employees", 'One')
            print('[Report @ LoginCore_CheckEnlisted] > User Account Count: %s' % (self.UserEnlistedCount))

            if self.UserEnlistedCount == 0:
                self.TechCore_Beep()
                #self.MSSQL_ExecuteState("INSERT INTO JobPosition VALUES (%s, '%s')" % (1, 'Manager'))
                #self.MSSQL_CommitData()
                
                QtWidgets.QMessageBox.information(self, 'Route88 System', "Welcome to Route88 Hybrid System! The system detected that there is no user account recorded according to it's database. Since you launch the system with no other accounts, you will have register first as a 'Manager' in this particular time.", QtWidgets.QMessageBox.Ok)

                self.Route88_FirstTimerInst = Route88_ModifierCore(ModifierMode="PushEntry", isFirstTime=True)
                self.Route88_FirstTimerInst.exec_()
                self.UserEnlistedCount = self.MSSQL_ExecuteState("SELECT COUNT(*) FROM Employees", 'One')
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
            self.MSSQL_InitCursor()
            self.QueryReturn = self.MSSQL_ExecuteState("SELECT * FROM Employees WHERE EmployeeUN = '%s' AND EmployeePW = '%s'" % (self.UserAcc_UserCode.text(),self.UserAcc_Password.text()), 'One')

            #self.UserData = self.MSSQL_FetchAllData()
            if self.QueryReturn:
                QSound.play("SysSounds/LoginSuccessNotify.wav")
                self.StatusLabel.setText("Login Success: Credential Input Matched!")
                self.UserAcc_SubmitData.setDisabled(True)
                
                for UserRawData in self.QueryReturn:
                    self.UserLiteralName = "%s %s" % (UserRawData.FirstName, UserRawData.LastName)
                    self.UserPosInfo = self.TechCore_PosCodeToName(UserRawData.PositionCode)
                # = self.MySQL
                #self.UserInfo_JobPos = self.
                
                QtWidgets.QMessageBox.information(self, 'Route88 Login Form | Login Success', "Login Success! You have are now logged in as ... '{} | Job Info |> {}.".format(self.UserLiteralName, self.UserPosInfo), QtWidgets.QMessageBox.Ok)
                self.StatusLabel.setText("Successfully Logged in ... {}".format(''))

                QtTest.QTest.qWait(1300)
                self.MSSQL_CloseCon() # Reconnect to Anothe SQ: Usage with Specific User Parameters
                self.close()

                self.Route88_MCInst = Route88_WindowController(Staff_Name=self.UserLiteralName, Staff_Job=self.UserPosInfo, Staff_DBUser='Route_TempUser', Staff_DBPass='123456789')
                self.Route88_MCInst.show()

            else:
                self.TechCore_Beep()
                self.StatusLabel.setText("Login Error: Credential Input Not Matched!")
                self.UserAcc_SubmitData.setDisabled(False)

                QtWidgets.QMessageBox.critical(self, 'Route88 Login Form | Login Failed', "Login Failed! Credential Input Not Matched. Check your User Code or your Password which may be written in Caps Lock. Please Try Again.", QtWidgets.QMessageBox.Ok)

                

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
        self.DataVCore_PatternEnabler(FirstTimer)
        self.DataVCore_RunAfterRender() #Run This Function After UI Initialization

    #Function Definitions for Route88_InventoryDesign
    def DataVCore_RenderExplicits(self): # Turn This To Render Columns According To Active Window
        try:
            #self.currentRow = 1
            self.InventoryStatus = QtWidgets.QStatusBar()
            self.setStatusBar(self.InventoryStatus)
            #self.DataTable_View.setRowCount(self.currentRow)

            # Add Function To Detect And Fix Column Based on Selected Table
            #for SetCellFixedElem in range(10):
            #    self.DataTable_View.horizontalHeader().setSectionResizeMode(SetCellFixedElem, QtWidgets.QHeaderView.ResizeToContents)
#
            #self.Query_ColumnOpt.model().item(1).setEnabled(False)
#
            #self.DataTable_View.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
            #self.DataTable_View.horizontalHeader().setSectionResizeMode(9, QtWidgets.QHeaderView.Stretch)
        except (Exception, MSSQL.DatabaseError) as RenderErrorMsg:
            self.InventoryStatus.showMessage('Application Error: {0}'.format(RenderErrorMsg))
            print('[Exception Thrown @ DataVCore_RenderExplicits] > Detailed Info |> {0}'.format(RenderErrorMsg))

    def DataVCore_RunAfterRender(self):
        try:

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
                self.TargetParameter = "%{}".format(self.Query_ValueToSearch.text())

    #Render Table Columns

    def DataVCore_LoadTableSets(self):
        try:
            self.ActiveTable = self.TableSystem_Selection.currentText()
            SchemaCandidate = None
            if self.ActiveTable == "None":
                self.TechCore_ColOptClear()
                self.Query_ColumnOpt.setEnabled(False)
                self.DataTable_View.setRowCount(0)
                self.DataTable_View.setColumnCount(0)
                self.DataTableTarget = None
                self.Target_TableCol = None

            elif self.ActiveTable == "Inventory Reference Data":
                self.TechCore_ColOptClear()
                self.Query_ColumnOpt.setEnabled(True)
                self.Query_ColumnOpt.addItem("ItemCode")
                self.Query_ColumnOpt.addItem("ItemName")
                self.Query_ColumnOpt.addItem("ItemCost")
                self.Query_ColumnOpt.addItem("ExpiryDate")
                self.Query_ColumnOpt.addItem("AvailableStock")
                self.Query_ColumnOpt.addItem("CreationTime")
                self.Query_ColumnOpt.addItem("LastUpdate")
                self.DataTable_View.setColumnCount(7)
                self.DataTable_View.setHorizontalHeaderLabels(("ItemCode", "ItemName", "Cost", "ExpiryDate", "AvailableStock", "CreationTime", "LastUpdate"))
                self.TechCore_ColResp()
                self.DataTableTarget = "InventoryItem"
                self.Target_TableCol = "ItemCode"
                SchemaCandidate = "Management"


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
                self.DataTable_View.setHorizontalHeaderLabels(("SupplierCode", "Name", "LastDeliveryDate", "NextDeliveryDate", "CreationTime", "LastUpdate"))
                self.TechCore_ColResp()
                self.DataTableTarget = "SupplierReference"
                self.Target_TableCol = "SupplierCode"
                SchemaCandidate = "Management"

            elif self.ActiveTable == "Supplier Transaction Data":
                self.TechCore_ColOptClear()
                self.Query_ColumnOpt.setEnabled(True)
                self.Query_ColumnOpt.addItem("ItemCode")
                self.Query_ColumnOpt.addItem("OrderCode")
                self.Query_ColumnOpt.addItem("SupplierCode")
                self.Query_ColumnOpt.addItem("OrderDate")
                self.Query_ColumnOpt.addItem("QuantityReceived")
                self.Query_ColumnOpt.addItem("CreationTime")
                self.Query_ColumnOpt.addItem("LastUpdate")

                self.DataTable_View.setColumnCount(7)
                self.DataTable_View.setHorizontalHeaderLabels(("ItemCode", "ItemName", "Cost", "ExpiryDate", "AvailableStock", "CreationTime", "LastUpdate"))
                self.TechCore_ColResp()
                self.DataTable_View.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
                self.DataTableTarget = "SupplierTransaction"
                self.Target_TableCol = "ItemCode"
                SchemaCandidate = "Management"

            elif self.ActiveTable == "Customer Transaction Data":
                self.TechCore_ColOptClear()
                self.Query_ColumnOpt.setEnabled(True)
                self.Query_ColumnOpt.addItem("TransactCode")
                self.Query_ColumnOpt.addItem("ItemCode")
                self.Query_ColumnOpt.addItem("CreationTime")
                self.Query_ColumnOpt.addItem("LastUpdate")

                self.DataTable_View.setColumnCount(4)
                self.DataTable_View.setHorizontalHeaderLabels(("TransactCode", "ItemCode Code", "CreationTime", "LastUpdate"))
                self.TechCore_ColResp()
                self.DataTableTarget = "CustTransaction"
                self.Target_TableCol = "TransactCode"
                SchemaCandidate = "Management"

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
                self.DataTable_View.setHorizontalHeaderLabels(("TransactCode_Pri", "TransactCode_Sec", "TotalCost", "VatableCost", "VatExempt", "ZeroRated", "NetVat", "VatRate", "CreationTime"))
                self.TechCore_ColResp()

                self.DataTable_View.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
                self.DataTableTarget = "CustReceipt"
                self.Target_TableCol = "TransactionCode"
                SchemaCandidate = "Management"

            elif self.ActiveTable == "Employee Reference Data":
                self.TechCore_ColOptClear()
                self.Query_ColumnOpt.setEnabled(True)
                self.Query_ColumnOpt.addItem("EmployeeCode")
                self.Query_ColumnOpt.addItem("EmployeeUN")
                self.Query_ColumnOpt.addItem("EmployeePW")
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
                
                self.DataTable_View.setColumnCount(13)
                self.DataTable_View.setHorizontalHeaderLabels(("EmployeeCode", "EmployeeUN", "EmployeePW", "FirstName", "LastName",  "PositionCode", "DOB", "Address", "SSS", "TIN", "PhilHealth", "TIN", "CreationTime", "LastUpdate"))
                self.TechCore_ColResp()

                self.DataTableTarget = "Employees"
                self.Target_TableCol = "EmployeeCode"
                SchemaCandidate = "EmployeeInfo"

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
                SchemaCandidate = "EmployeeInfo"

            self.TechCore_RespectSchema(SchemaCandidate)
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
                self.MSSQL_ExecuteState("SELECT * FROM %s" % (self.DataTableTarget,))
                self.DataVCore_RenderTable(self.MSSQL_FetchAllData())
                
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
                self.InventoryStatus.showMessage('Looking At Requested Target Value {} @ {}...'.format(str(self.Query_ValueToSearch.text())), self.Query_ColumnOpt.currentText())
                
                self.TechCore_RowClear()

                print('[Search Operation] Field -> {} | Operator -> {} | Target Value -> {}'.format(self.FieldParameter, self.OperatorParameter, self.TargetParameter))
                print('[Search Query] SELECT * FROM {} WHERE {} {} {}'.format(self.DataTableTarget, self.FieldParameter, self.OperatorParameter, self.TargetParameter))

                self.MSSQL_ExecuteState("SELECT * FROM %s WHERE %s %s '%s'" % (self.DataTableTarget, self.FieldParameter, self.OperatorParameter, self.TargetParameter,))
                self.DataVCore_RenderTable(self.MSSQL_FetchAllData())

        except (Exception, MSSQL.Error, MSSQL.OperationalError) as SearchQueryError:
            self.InventoryStatus.showMessage('Application Error: Value Searching Returns Error. Detailed Info > {}'.format(SearchQueryError))
            print('[Exception Thrown @ DataVCore_ValSearch] > Value Searching Returns Error. Detailed Info > {}'.format(SearchQueryError))

    def DataVCore_RenderTable(self, FunctionCall_DataFetch):
        currentRow = 0
        if self.ActiveTable == "None":
            self.TechCore_RowClear()
            print('[Report @ DataVCore_RenderTable] > Active Data Table is None. Nothing to show.')
            self.InventoryStatus.showMessage('[Report @ DataVCore_RenderTable] > Active Data Table is None. Nothing to show.')

        elif self.ActiveTable == "Inventory Reference Data":
            for InventoryData in FunctionCall_DataFetch:
                self.DataTable_View.setRowCount(currentRow + 1)

                self.DataTable_View.setItem(currentRow, 0, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['ItemCode'])))
                self.DataTable_View.setItem(currentRow, 1, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['ItemName'])))
                self.DataTable_View.setItem(currentRow, 2, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['ItemCost'])))
                self.DataTable_View.setItem(currentRow, 3, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['ExpiryDate'])))
                self.DataTable_View.setItem(currentRow, 4, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['AvailableStock'])))
                self.DataTable_View.setItem(currentRow, 5, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['CreationTime'])))
                self.DataTable_View.setItem(currentRow, 6, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['LastUpdate'])))

                for SetCellFixedWidth in range(0, self.DataTable_View.columnCount()):
                    ColumnPosFixer = self.DataTable_View.item(currentRow, SetCellFixedWidth)
                    ColumnPosFixer.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                currentRow += 1


        elif self.ActiveTable == "Supplier Reference Data":
            for InventoryData in FunctionCall_DataFetch:
                self.DataTable_View.setRowCount(currentRow + 1)

                self.DataTable_View.setItem(currentRow, 0, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['SupplierCode'])))
                self.DataTable_View.setItem(currentRow, 1, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['SupplierName'])))
                self.DataTable_View.setItem(currentRow, 2, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['LastDeliveryDate'])))
                self.DataTable_View.setItem(currentRow, 3, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['NextDeliveryDate'])))
                self.DataTable_View.setItem(currentRow, 4, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['CreationTime'])))
                self.DataTable_View.setItem(currentRow, 5, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['LastUpdate'])))

                for SetCellFixedWidth in range(0, self.DataTable_View.columnCount()):
                    ColumnPosFixer = self.DataTable_View.item(currentRow, SetCellFixedWidth)
                    ColumnPosFixer.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                currentRow += 1

        elif self.ActiveTable == "Supplier Transaction Data":
            for InventoryData in FunctionCall_DataFetch:
                self.DataTable_View.setRowCount(currentRow + 1)

                self.DataTable_View.setItem(currentRow, 0, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['ItemCode'])))
                self.DataTable_View.setItem(currentRow, 1, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['OrderCode'])))
                self.DataTable_View.setItem(currentRow, 2, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['SupplierCode'])))
                self.DataTable_View.setItem(currentRow, 3, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['OrderDate'])))
                self.DataTable_View.setItem(currentRow, 4, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['QuantityReceived'])))
                self.DataTable_View.setItem(currentRow, 5, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['CreationTime'])))
                self.DataTable_View.setItem(currentRow, 6, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['LastUpdate'])))

                for SetCellFixedWidth in range(0, self.DataTable_View.columnCount()):
                    ColumnPosFixer = self.DataTable_View.item(currentRow, SetCellFixedWidth)
                    ColumnPosFixer.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                currentRow += 1

        elif self.ActiveTable == "Customer Transaction Data":
            for InventoryData in FunctionCall_DataFetch:
                self.DataTable_View.setRowCount(currentRow + 1)

                self.DataTable_View.setItem(currentRow, 0, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['TransactionCode'])))
                self.DataTable_View.setItem(currentRow, 1, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['ItemCode'])))
                self.DataTable_View.setItem(currentRow, 2, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['CreationTime'])))
                self.DataTable_View.setItem(currentRow, 3, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['LastUpdate'])))

                for SetCellFixedWidth in range(0, self.DataTable_View.columnCount()):
                    ColumnPosFixer = self.DataTable_View.item(currentRow, SetCellFixedWidth)
                    ColumnPosFixer.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                currentRow += 1

        elif self.ActiveTable == "Customer Receipt Data":
            for InventoryData in FunctionCall_DataFetch:
                self.DataTable_View.setRowCount(currentRow + 1)

                self.DataTable_View.setItem(currentRow, 0, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['TransactionCode'])))
                self.DataTable_View.setItem(currentRow, 1, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['TotalCost'])))
                self.DataTable_View.setItem(currentRow, 2, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['VATableCost'])))
                self.DataTable_View.setItem(currentRow, 3, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['VATExempt'])))
                self.DataTable_View.setItem(currentRow, 4, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['ZeroRated'])))
                self.DataTable_View.setItem(currentRow, 5, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['NetVAT'])))
                self.DataTable_View.setItem(currentRow, 6, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['VATRate'])))
                self.DataTable_View.setItem(currentRow, 7, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['CreationTime'])))

                for SetCellFixedWidth in range(0, self.DataTable_View.columnCount()):
                    ColumnPosFixer = self.DataTable_View.item(currentRow, SetCellFixedWidth)
                    ColumnPosFixer.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                currentRow += 1

        elif self.ActiveTable == "Employee Reference Data":
            for InventoryData in FunctionCall_DataFetch:
                self.DataTable_View.setRowCount(currentRow + 1)

                self.DataTable_View.setItem(currentRow, 0, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['EmployeeCode'])))
                self.DataTable_View.setItem(currentRow, 1, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['FirstName'])))
                self.DataTable_View.setItem(currentRow, 2, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['LastName'])))
                self.DataTable_View.setItem(currentRow, 3, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['PositionCode'])))
                self.DataTable_View.setItem(currentRow, 4, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['DOB'])))
                self.DataTable_View.setItem(currentRow, 5, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['Address'])))
                self.DataTable_View.setItem(currentRow, 6, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['SSS'])))
                self.DataTable_View.setItem(currentRow, 7, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['TIN'])))
                self.DataTable_View.setItem(currentRow, 8, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['PhilHealth'])))
                self.DataTable_View.setItem(currentRow, 9, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['TIN'])))
                self.DataTable_View.setItem(currentRow, 10, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['CreationTime'])))
                self.DataTable_View.setItem(currentRow, 11, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['LastUpdate'])))

                for SetCellFixedWidth in range(0, self.DataTable_View.columnCount()):
                    ColumnPosFixer = self.DataTable_View.item(currentRow, SetCellFixedWidth)
                    ColumnPosFixer.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                currentRow += 1
                
        elif self.ActiveTable == "Job Reference Data":
            for InventoryData in FunctionCall_DataFetch:
                self.DataTable_View.setRowCount(currentRow + 1)

                self.DataTable_View.setItem(currentRow, 0, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['PositionCode'])))
                self.DataTable_View.setItem(currentRow, 1, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['JobName'])))

                for SetCellFixedWidth in range(0, self.DataTable_View.columnCount()):
                    ColumnPosFixer = self.DataTable_View.item(currentRow, SetCellFixedWidth)
                    ColumnPosFixer.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                currentRow += 1

    def DataVCore_Encap_RowData(self):
        if self.DataTable_View.currentRow() != -1:
            self.StaffAct_Delete.setEnabled(True)
            self.StaffAct_Edit.setEnabled(True)
        else:
            self.StaffAct_Delete.setEnabled(False)
            self.StaffAct_Edit.setEnabled(False)

    
    # Staff Action Functions

    def DataVCore_AddEntry(self):
        self.ModifierDialog = Route88_ModifierCore(RecentTableActive=self.DataTableTarget, ModifierMode="PushEntry") #SelectedRowData)
        self.ModifierDialog.exec_()
        self.DataVCore_RefreshData()

    def DataVCore_EditEntry(self):
        # Add Data To Pass or To Fetch...
        self.ModifierDialog = Route88_ModifierCore(RecentTableActive=self.DataTableTarget, ModifierMode="ModifyDataExists")
        self.ModifierDialog.exec_()
        self.DataVCore_RefreshData()

    def DataVCore_DeleteEntry(self):
        try:
            if self.DataTable_View.rowCount() == 0:
                self.StaffAct_Delete.setEnabled(False)
                self.InventoryStatus.showMessage('Table Data Error > Table View is currently empty. You cannot delete any data anymore.')
                print('Report @ DataVCore_DeleteEntry] Table View is currently empty. You cannot delete any data anymore.')
            else:
                self.StaffAct_Delete.setEnabled(True)
                selectedData = self.DataTable_View.item(self.DataTable_View.currentRow(), 0).text()
                print('[Database Query Process | Deletion Query] -> DELETE FROM %s WHERE %s = %s' %(self.DataTableTarget, self.Target_TableCol, selectedData))
                self.InventoryStatus.showMessage('Deletion Query: Processing to Delete Row %s' % (self.DataTable_View.currentRow()))

                self.MSSQLDataWireCursor.execute('DELETE FROM %s WHERE %s = %s' % (self.DataTableTarget, self.Target_TableCol, selectedData))

                self.TechCore_RowClearSelected(self.DataTable_View.currentRow())

                self.MSSQL_CommitData()

                self.InventoryStatus.showMessage('Deletion Query | > Row %s has been deleted!' % (self.DataTable_View.currentRow() + 1))
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

class Route88_POSCore(QtWidgets.QMainWindow, Route88_TechnicalCore):
    def __init__(self, Parent=None, StaffInCharge_Name=None, StaffInCharge_Job=None, StaffInCharge_DBUser=None, StaffInCharge_DBPass=None):
        super(Route88_POSCore, self).__init__(Parent=Parent)
        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('IcoDisplay/r_88.ico'))
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.WindowShadeButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)

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

class Route88_ModifierCore(Ui_Route88_DataManipulation_Window, QtWidgets.QDialog, Route88_TechnicalCore):
    def __init__(self, Parent=None, ModifierMode=None, RecentTableActive=None, DataPayload_AtRow=None, isFirstTime=None):
        super(Route88_ModifierCore, self).__init__(Parent=Parent)
        self.setupUi(self)
        self.DataMCore_RenderExplicits()
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.WindowShadeButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowIcon(QtGui.QIcon('IcoDisplay/r_88.ico'))


    # Button Binds to Functions
        #for SetDisability in range(1, 5):
        #    self.Tab_SelectionSelectives.setTabEnabled(SetDisability, False)
        
        self.DataManip_CloseWindow.clicked.connect(self.close)
        self.DataManip_PushData.clicked.connect(self.DataMCore_AddEntry)
        self.DataManip_ResetActiveData.clicked.connect(self.DataMCore_ClearEntry)

        self.DataPayload = DataPayload_AtRow
        self.ModifierMode = ModifierMode
        self.ActiveTargetTable = RecentTableActive

        self.DataMCore_isReallyFT(isFirstTime)
        self.DataMCore_RunAfterRender()

        # Technical Functions
    def DataMCore_RenderExplicits(self):
        pass


    def DataMCore_RunAfterRender(self):
        try:
            if (self.ActiveTargetTable == "Employees" or self.ActiveTargetTable == "JobPosition"):
                self.MSSQL_OpenCon(UCredential='Route88_TempAuth', PCredential='Route88_Group7')
                self.MSSQL_InitCursor()
            else:
                self.MSSQL_OpenCon(UCredential='Route88_TempAuth', PCredential='Route88_Group7')
                self.MSSQL_InitCursor()

            if self.ActiveTargetTable == "InventoryItem":
                self.resize(820, 420)
                self.Tab_SelectionSelectives.setCurrentIndex(0)
                self.TechCore_DisableExcept(0)
                self.InvEntry_DE.setDateTime(QtCore.QDateTime.currentDateTime())
            

            elif self.ActiveTargetTable == "SupplierReference":
                self.resize(820, 620)
                self.Tab_SelectionSelectives.setCurrentIndex(3)
                self.TechCore_DisableExcept(3)
                self.SuppEntry_LDD.setDateTime(QtCore.QDateTime.currentDateTime())
                self.SuppEntry_NDD.setDateTime(QtCore.QDateTime.currentDateTime())

            elif self.ActiveTargetTable == "SupplierTransaction":
                self.resize(820, 540)
                self.Tab_SelectionSelectives.setCurrentIndex(4)
                self.TechCore_DisableExcept(4)
                self.SuppTrEntry_OD.setDateTime(QtCore.QDateTime.currentDateTime())

            elif self.ActiveTargetTable == "CustReceipt":
                self.resize(820, 600)
                self.Tab_SelectionSelectives.setCurrentIndex(1)
                self.TechCore_DisableExcept(1)

            elif self.ActiveTargetTable == "CustTransaction":
                self.resize(820, 510)
                self.Tab_SelectionSelectives.setCurrentIndex(2)
                self.TechCore_DisableExcept(2)

            elif self.ActiveTargetTable == "Employees":
                self.resize(820, 740)
                self.Tab_SelectionSelectives.setCurrentIndex(5)
                self.TechCore_DisableExcept(5)
                self.EmpEntry_DOB.setDateTime(QtCore.QDateTime.currentDateTime())
                # Restrict These QLineEdit Object to Accept Only Integer.
                self.EmpEntry_SSS.setValidator(QtGui.QIntValidator())
                self.EmpEntry_TIN.setValidator(QtGui.QIntValidator())
                self.EmpEntry_PH.setValidator(QtGui.QIntValidator())

                for JobDataFetch in self.MSSQL_ExecuteState("SELECT * FROM JobPosition", "All"):
                    self.EmpEntry_PC.addItem(JobDataFetch.JobName)

            elif self.ActiveTargetTable == "JobPosition":
                self.resize(820, 380)
                self.Tab_SelectionSelectives.setCurrentIndex(6)
                self.TechCore_DisableExcept(6)

            #Preloads Data Received, Ternary Operator
            self.DataMCore_EditEntry() if self.ModifierMode == "ModifyDataExists" else None
                

        except (Exception, MSSQL.DatabaseError) as DataMCore_ARErr:
            self.TechCore_Beep()
            print('[Exception @ DataMCore_RunAfterRender] > Error Rendering Modifier Core: RunAfterRender. Detailed Error: %s' % (DataMCore_ARErr))
        
    def DataMCore_isReallyFT(self, isReallyLFT):
        if isReallyLFT:
            self.ActiveTargetTable = "Employees"

    # Staff Action Function Declarations
    def DataMCore_AddEntry(self):
        try:
            self.MSSQL_InitCursor()

            if self.ActiveTargetTable == "InventoryItem":
                pass
            elif self.ActiveTargetTable == "SupplierReference":
                pass
            elif self.ActiveTargetTable == "SupplierTransaction":
                pass
            elif self.ActiveTargetTable == "CustReceipt":
                pass
            elif self.ActiveTargetTable == "CustTransaction":
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
                    self.MSSQL_ExecuteState("INSERT INTO Employees(EmployeeUN, EmployeePW, FirstName, LastName, PositionCode, DOB, Address, SSS, TIN, PhilHealth) VALUES ('%s', '%s', '%s', '%s', %s, '%s', '%s', '%s', '%s', '%s')" % 
                    (self.EmpEntry_UN.text(), self.EmpEntry_PW.text(), self.EmpEntry_FN.text(), self.EmpEntry_LN.text(), self.TechCore_NameToPosCode(self.EmpEntry_PC.currentText()), self.EmpEntry_DOB.date().toString("MM/dd/yyyy"), self.EmpEntry_Adrs.text(), self.EmpEntry_SSS.text(), self.EmpEntry_TIN.text(), self.EmpEntry_PH.text()))

                    self.MSSQL_CommitData()

                    self.MSSQL_ExecuteState("CREATE LOGIN %s WITH PASSWORD = '%s'" % (self.EmpEntry_UN.text(), self.EmpEntry_PW.text()))
                    self.MSSQL_ExecuteState("CREATE USER %s for LOGIN %s" % (self.EmpEntry_UN.text(), self.EmpEntry_UN.text()))
                    self.MSSQL_CommitData()

                    self.Modifier_StatusLabel.setText("Staff %s %s is added to the database!" % (self.EmpEntry_FN.text(), self.EmpEntry_LN.text())) 
                    QtWidgets.QMessageBox.information(self, 'Route88 System | Data Manipulation Error', "Staff %s %s is added to the database!" % (self.EmpEntry_FN.text(), self.EmpEntry_LN.text()), QtWidgets.QMessageBox.Ok)

            elif self.ActiveTargetTable == "JobPosition":
                pass
    




            #if self.AddEntry_ItemCode.text() == 0:
            #    self.DataMCore_Status.showMessage('Adding Entry Error: Constraint (> 0 Characters) Not Met @ Item Code Entry.')
            #    raise Exception('Adding Entry Error: Constraint (> 0 Characters) Not Met @ Item Code Entry.')
            #elif self.AddEntry_SupplierCode.text() == 0:
            #    self.DataMCore_Status.showMessage('Adding Entry Error: Constraint (> 0 Characters) Not Met @ Supplier Code Entry')
            #    raise Exception('Adding Entry Error: Constraint (> 0 Characters) Not Met @ Supplier Code Entry')
            #elif self.AddEntry_ItemName.text() < 2:
            #    self.DataMCore_Status.showMessage('Adding Entry Error: Constraint (> 2 Characters) Not Met @ Item Name Entry')
            #    raise Exception('Adding Entry Error: Constraint (> 2 Characters) Not Met @ Item Name Entry')
            #elif self.AddEntry_ItemType.text() < 2:
            #    self.DataMCore_Status.showMessage('Adding Entry Error: Constraint (> 2 Characters) Not Met @ Item Type Entry')
            #    raise Exception('Adding Entry Error: Constraint (> 2 Characters) Not Met @ Item Type Entry')
            ##elif len()
            #else:
            #    TargetTable_Param = self.DataMCore_GetTargetTable()
            #    print('[Pushing Value to Table @ InventoryList] -> INSERT INTO {} VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {})'.format(TargetTable_Param, self.AddEntry_ItemCode.text()), self.AddEntry_SupplierCode.text(), #self.AddEntry_ItemName.text(), self.AddEntry_ItemType.text(), self.AddEntry_Quantity.value(), self.AddEntry_Cost.value(), formattedDate, 1,formattedDate, formattedDate)
#
            #    #self.MSSQLDataWireCursor.execute("INSERT INTO {} VALUES ({}, {}, '{}', '{}', {}, {}, '{}', {}, '{}', '{}')".format(str(TargetTable_Param), str(self.AddEntry_ItemCode.text())), str(self.AddEntry_SupplierCode.text#())), str(self.AddEntry_ItemName.text())), str(self.AddEntry_ItemType.text())), str(self.AddEntry_Quantity.value()), str(self.AddEntry_Cost.value()), str(formattedDate), 1,str(formattedDate), str(formattedDate)))
            #    #self.MSSQLDataWire.commit()
            #    print('[Report @DataMCore_AddEntry] > Successful Execution -> Data Successfully Added to Database~!')
            #    self.DataMCore_Status.showMessage('Successful Execution -> Data Successfully Added to Database~!')



        
        except (Exception, MSSQL.Error, MSSQL.OperationalError) as PushEntryErrMsg:
            self.TechCore_Beep()
            QtWidgets.QMessageBox.critical(self, 'Route88 System | Data Manipulation Insertion Error', "Error, cannot push data from the database. Check your fields or your database connection. Detailed Error: {}".format(str(PushEntryErrMsg)), QtWidgets.QMessageBox.Ok)

            print('[Exemption @ DataMCore_AddEntry] > %s' % (PushEntryErrMsg))

    def DataMCore_EditEntry(self):
        for i in self.DataPayload:
            print(i)


    def DataMCore_ClearEntry(self, ActiveEntryWindow):
        if self.Tab_SelectionSelectives.currentIndex() == 0:
            self.InvEntry_IC.clear()
            self.InvEntry_IN.clear()
            self.InvEntry_IT.setCurrentIndex(0)
            self.InvEntry_MT.setCurrentIndex(0)
            self.InvEntry_Q.setValue(0)
            self.InvEntry_C.setValue(0.0)
            self.InvEntry_ED.setDateTime(QtCore.QDateTime.currentDateTime())
            self.Modifier_StatusLabel.setText('Fields Cleared on Inventory Reference Window. Ready!')
            print('[Execution @ DataMCore_ClearEntry] -> Finished Clearing Up Fields @ Inventory Reference Window. Ready!')

        elif self.Tab_SelectionSelectives.currentIndex() == 1:
            self.SuppEntry_SC.clear()
            self.SuppEntry_SN.clear()
            self.SuppEntry_LDD.setDateTime(QtCore.QDateTime.currentDateTime())
            self.SuppEntry_NDD.setDateTime(QtCore.QDateTime.currentDateTime())
            self.Modifier_StatusLabel.setText('Fields Cleared on Supplier Reference Window. Ready!')
            print('[Execution @ DataMCore_ClearEntry] -> Finished Clearing Up Fields @ Supplier Reference Window. Ready!')

        elif self.Tab_SelectionSelectives.currentIndex() == 2:
            self.SuppTrEntry_IC.setCurrentIndex(0)
            self.SuppTrEntry_OC.setCurrentIndex(0)
            self.SuppTrEntry_SC.setCurrentIndex(0)
            self.SuppTrEntry_OD.setDateTime(QtCore.QDateTime.currentDateTime())
            self.SuppTrEntry_QOR.setValue(0)
            self.Modifier_StatusLabel.setText('Fields Cleared on Supplier Transaction Window. Ready!')
            print('[Execution @ DataMCore_ClearEntry] -> Finished Clearing Up Fields @ Supplier Transaction Window. Ready!')
            
        elif self.Tab_SelectionSelectives.currentIndex() == 3:
            self.CustREntry_TrC.setCurrentIndex(0)
            self.CustREntry_TC.clear()
            self.CustREntry_VC.clear()
            self.CustREntry_VE.clear()
            self.CustREntry_ZR.clear()
            self.CustREntry_NV.clear()
            self.CustREntry_VR.clear()
            self.Modifier_StatusLabel.setText('Fields Cleared on Customer Receipt Window. Ready!')
            print('[Execution @ DataMCore_ClearEntry] -> Finished Clearing Up Fields @ Customer Receipt Window. Ready!')

        elif self.Tab_SelectionSelectives.currentIndex() == 4:
            self.CustTr_TC.clear()
            self.CustTr_IC.setCurrentIndex(0)
            self.SuppTrEntry_OD.setDateTime(QtCore.QDateTime.currentDateTime())
            self.Modifier_StatusLabel.setText('Fields Cleared on Customer Transaction Window. Ready!')
            print('[Execution @ DataMCore_ClearEntry] -> Finished Clearing Up Fields @ Customer Transaction Window. Ready!')

        elif self.Tab_SelectionSelectives.currentIndex() == 5:
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

        elif self.Tab_SelectionSelectives.currentIndex() == 6:
            self.JobPEntry_PC.clear()
            self.JobPEntry_PN.clear()
            self.Modifier_StatusLabel.setText('Fields Cleared on Job Reference Window. Ready!')
            print('[Execution @ DataMCore_ClearEntry] -> Finished Clearing Up Fields @ Job Reference Window. Ready!')

        else:
            self.Modifier_StatusLabel.setText('[Exception @ Modifier_ClearEntry] Current Index of Selected Tab does not match from any defined conditions.')
            print('[Exception @ Modifier_ClearEntry] Current Index of Selected Tab does not match from any defined conditions.')

    def GetDataVCore_ItemValue(self): # For Edit Functions
        pass

    # We use this one to identify which table are we going to push some actions.
    # Going to be deprecated. Onces we are able to pass a user from another table then we are good to go.
    def DataMCore_GetTargetTable(self):
        TabWindowCandidate = self.Tab_SelectionSelectives.tabText(self.Tab_SelectionSelectives.currentIndex())
        if TabWindowCandidate == 'Inventory Entries':
            return 'InventoryList'
        elif TabWindowCandidate == 'Employee Entries':
            return 'Employees'
        elif TabWindowCandidate == 'Supplier Entries':
            return 'SupplierList'
        elif TabWindowCandidate == 'Transaction Entries':
            return 'Transaction_Total'
        elif TabWindowCandidate == 'Position Entries':
            return 'JobPosition'
        else:
            print('[Exception @ GetDataVCore_ItemValue] -> Selected Candidate does not exist from List of QTabWidgetItem Names')
            raise ValueError('[Exception @ GetDataVCore_ItemValue] -> Selected Candidate does not exist from List of QTabWidgetItem Names')


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
        #self.ctrl_POSSystem.clicked.connect(self.)
        #self.ctrl_AboutSystem.clicked.connect(self.)
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
        pass

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

            QtWidgets.QMessageBox.critical(self, 'Route88 Window Controller | User Error', "Staff Logged On But Staff Cannot Used Any Of The Systems. Sorry!", QtWidgets.QMessageBox.Ok)
            self.StatusLabel.setText('Staff Logged On But Staff Cannot Used Any Of The Systems. Sorry!'.format(self.StaffLiteralName))

# Literal Procedural Programming Part
if __name__ == "__main__":
    sysHandler.Popen('CLS', shell=True)
    print('[Startup @ Procedural] Route88 Hybrid System Application, Debugger Output')
    app = QtWidgets.QApplication(sys.argv)
    Route88_InitialInst = Route88_LoginCore()
    Route88_InitialInst.show()
    sys.exit(app.exec_())