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
                > This was implemented right after setupUi(). Because, we have to   initialize every value from the database which would then be shown after  UI has been render. So that when the engine initiates .show(). All   values is already there. So in sort, setup Values and Elements.
'''
from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from PyQt5.QtMultimedia import QSound
import MySQLdb as MySQL
import sys
from os import system as sysCmdArgumentHandler

from Route88_LoginCmpnt import Ui_Route88_Login_Window
from Route88_DataViewerCmpnt import Ui_Route88_DataViewer_Window
from Route88_DataManipCmpnt import Ui_Route88_DataManipulation_Window
from Route88_ControllerCmpnt import Ui_Route88_Controller_Window
#from Route88_POSSystem import %s%s%s

# This class is a database controller by wrapping all confusing parts into a callable function... and any other such that requires global function calling.
class Route88_TechnicalCore(object):
    def __init__(self, Parent=None):
        super().__init__()

    def MySQL_OpenCon(self, HostServerIP='localhost', SQL_UCredential=None, SQL_PCredential=None, SQLDatabase_Target=None):
        try:
            self.MySQLDataWire = MySQL.connect(host=HostServerIP, user=SQL_UCredential, passwd=SQL_PCredential, db=SQLDatabase_Target)
            print("[MySQL Database] Connection Attempt: Staff '{}' with Username '{}' is now logged as {}.".format("...", SQL_UCredential, '...'))

        except (Exception, MySQL.OperationalError, MySQL.Error, MySQL.Warning, MySQL.DatabaseError) as MySQL_ErrorMessage:
            self.TechnicalCore_Beep()
            self.StatusLabel.setText("Database Error: Cannot Connect to the SQL Database. Please restart.")
            print('[Exception @ MySQL_OpenCon] > Cannot Open / Establish Connection with the MySQL Database. Detailed Info |> {}'.format(str(MySQL_ErrorMessage)))
            QtWidgets.QMessageBox.critical(self, 'Route88 System | Database Error', "Error, cannot connect to the database, here is the following error prompt that the program encountered. '{}'. Please restart the program and re-run the XAMPP MySQL Instance.".format(str(MySQL_ErrorMessage)), QtWidgets.QMessageBox.Ok)
            sys.exit() # Terminate the program 

    def MySQL_CursorSet(self, CursorType=None):
        try:
            self.MySQLDataWireCursor = self.MySQLDataWire.cursor(CursorType)
        except (Exception, MySQL.OperationalError, MySQL.Error, MySQL.Warning, MySQL.DatabaseError) as CursorErrMsg:
            self.TechnicalCore_Beep()
            print('[Exception @ MySQL_CursorSet] > Invalid Cursor Set. Report this problem to the developers. Detailed Info |> {}'.format(str(CursorErrMsg)))

    def MySQL_ExecuteState(self, MySQLStatement):
        try:
            return self.MySQLDataWireCursor.execute(MySQLStatement)
        except (Exception, MySQL.OperationalError, MySQL.Error, MySQL.Warning, MySQL.DatabaseError) as MySQL_ExecError:
            self.TechnicalCore_Beep()
            print('[Exception @ MySQL_ExecuteState] > Error in SQL Statements. Double check your statements. Detailed Info |> {}'.format(str(MySQL_ExecError))) # Style This One Soon.
    
    def MySQL_FetchOneData(self, TupleIndex):
        try:
            return self.MySQLDataWireCursor.fetchone()[TupleIndex]
        except (Exception, MySQL.OperationalError, MySQL.Error, MySQL.Warning, MySQL.DatabaseError) as MySQL_FetchOError:
            self.TechnicalCore_Beep()
            print('[Exception @ MySQL_FetchOneData] > Cannot Fetch Data from a Specified Index. Detailed Info |> {}'.format(str(MySQL_FetchOError)))
    
    def MySQL_FetchAllData(self):
        try:
            return self.MySQLDataWireCursor.fetchall()
        except (Exception, MySQL.OperationalError, MySQL.Error, MySQL.Warning, MySQL.DatabaseError) as MySQL_FetchAError:
            self.TechnicalCore_Beep()
            print('[Exception @ MySQL_FetchAllData] > Unable to Fetch Data, Check your ExecuteState statements. Detailed Info |> {}'.format(str(MySQL_FetchAError)))
    
    def MySQL_CommitData(self):
        try:
            return self.MySQLDataWire.commit()
        except (Exception, MySQL.OperationalError, MySQL.Error, MySQL.Warning, MySQL.DatabaseError) as MySQL_CommitError:
            self.TechnicalCore_Beep()
            print('[Exception @ MySQL_CommitData] > Unable To Commit Data... Check your MySQL Connection and try again.Detailed Info |> {}'.format(str(MySQL_CommitError)))

    def MySQL_CloseCon(self):
        try:
            return self.MySQLDataWire.close()
        except (Exception, MySQL.OperationalError, MySQL.Error, MySQL.Warning, MySQL.DatabaseError) as ClosingErr:
            self.TechnicalCore_Beep()
            print('[Exception @ MySQL_CloseCon] > Unable to Close Connection with the MySQL Statements. Please Terminate XAMPP or Some Statements are still running. Terminate Immediately. Detailed Info |> {}'.format(str(ClosingErr)))
    
    #Non Database Callable Function
    def TechnicalCore_Beep(self):
        return QtWidgets.QApplication.beep()

    #Not sure for this one...
    def TechnicalCore_MessageBox(self, MsgType, MsgString, MsgDetailInfo, MsgButtons):
        pass

    def TechnicalCore_ColResp(self):
        try:
            self.DataTable_View.resizeColumnsToContents()
            for SetCellFixedElem in range(self.DataTable_View.columnCount()):
                self.DataTable_View.horizontalHeader().setSectionResizeMode(SetCellFixedElem,   QtWidgets.QHeaderView.Stretch)
        except Exception as ResponseError:
            print('[Exception @ TechnicalCore_ColResp] > Error Responsive Rendering in Table View. Detailed Info |> {}'.format(ResponseError))
    
    def TechnicalCore_RowClear(self):
        try:
            self.DataTable_View.clearContents()
            self.DataTable_View.setRowCount(0)

        except Exception as RowClearMsg:
            print('[Exception @ TechnicalCore_RowClear] > Row Clearing Returns Error. Detailed Info |> {}'.format(str(RowClearMsg)))

    def DataVCore_ColOptClear(self):
        try:
            ColOptIndex = 1
            self.Query_ColumnOpt.setCurrentIndex(0)
            while self.Query_ColumnOpt.count() != 2:
                self.Query_ColumnOpt.removeItem(ColOptIndex + 1)

        except Exception as ColOptClearMsg:
            print('[Exception @ DataVCore_ColOptClear] > Column Clearing Returns Error. Detailed Info |> {}'.format(str(ColOptClearMsg)))
        
    def TechnicalCore_PosCodeToName(self, PosCode):
        try:
            self.MySQL_CursorSet(None)
            self.MySQL_ExecuteState("SELECT JobName FROM JobPosition WHERE PositionCode = %s" % (PosCode,))
            return self.MySQL_FetchOneData(0)

        except (Exception, MySQL.OperationalError, MySQL.Error, MySQL.Warning, MySQL.DatabaseError) as ProcessError:
            print('[Exception @ TechnicalCore_PosCodeToName] > Error Processing PositionCode to JobName. Detailed Info |> {}'.format(str(ProcessError)))



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
            self.MySQL_OpenCon(SQL_UCredential='Route_TempUser', SQL_PCredential='123456789', SQLDatabase_Target='route88_employees')
            self.MySQL_CursorSet(MySQL.cursors.DictCursor)
            self.LoginCore_CheckEnlisted()

        except Exception as ErrorHandler:
            self.TechnicalCore_Beep()
            print('[Exception @ LoginCore_RunAfterRender] > One of the MySQL Required Components Returns Error. Detailed Info |> {}'.format(str(ErrorHandler)))
            QtWidgets.QMessageBox.critical(self, 'Route88 Login Form | Database Error', "Error, cannot connect to the database. Please restart the program and re-run the XAMPP MySQL Instance. Detailed Info |> {}".format(str(ErrorHandler)), QtWidgets.QMessageBox.Ok)
            sys.exit() # Terminate the program at all cost.

    #Route88_LoginForm UI Window Functions - StartPoint
    def LoginCore_CheckEnlisted(self):
        try:
            self.MySQL_CursorSet(None)
            self.MySQL_ExecuteState("SELECT COUNT(*) FROM Employees")
            self.UserEnlistedCount = self.MySQL_FetchOneData(0)
            print('[Report @ LoginCore_CheckEnlisted] > User Account Count: {}'.format(self.UserEnlistedCount))
            self.StatusLabel.setText("Database Loaded. Ready~!")

            if self.UserEnlistedCount == 0:
                self.MySQL_ExecuteState("INSERT INTO Employees (EmployeeCode, FirstName, LastName, PositionCode, EmployeePassword) VALUES (%s, %s, %s, %s, %s)" % (1, 'Janrey', 'Licas', 1, '123',))
                #  Create if and else here.
                self.MySQL_ExecuteState("INSERT INTO JobPosition VALUES (%s, %s)" % (1, 'Manager',))
                self.MySQL_CommitData()
                self.UserAcc_SubmitData.setDisabled(False)
            else:
                self.UserAcc_SubmitData.setDisabled(False)

        except (Exception, MySQL.OperationalError, MySQL.Error, MySQL.Warning, MySQL.DatabaseError) as LoginQueryErrorMsg:
            self.TechnicalCore_Beep()

            print('[Exception @ LoginCore_CheckEnlisted] > Error Checking User in Database. Check MySQL Database Connection. Detailed Info |> {}'.format(str(LoginQueryErrorMsg)))
            self.StatusLabel.setText("Database Error: Cannot Connect. Please restart.")

            QtWidgets.QMessageBox.critical(self, 'Route88 Login Form | Database Error', "Error, cannot connect to the database, here is the following error prompt that the program encountered. '{}'. Please restart the program and re-run the XAMPP MySQL Instance.".format(str(LoginQueryErrorMsg)), QtWidgets.QMessageBox.Ok)
            sys.exit() # Terminate the program at all cost.

    def LoginCore_DataSubmission(self):
        try:
            self.MySQL_CursorSet(MySQL.cursors.DictCursor)
            self.QueryReturn = self.MySQL_ExecuteState("SELECT * FROM Employees WHERE EmployeeCode = '%s' AND EmployeePassword = '%s'" % (self.UserAcc_UserCode.text(), self.UserAcc_Password.text()))

            self.UserData = self.MySQL_FetchAllData()
            if self.QueryReturn:
                QSound.play("SysSounds/LoginSuccessNotify.wav")
                self.StatusLabel.setText("Login Success: Credential Input Matched!")
                self.UserAcc_SubmitData.setDisabled(True)
                
                for UserRawData in self.UserData:
                    self.UserLiteralName = "{} {}".format(UserRawData['FirstName'], UserRawData['LastName'])
                    self.UserPosInfo = self.TechnicalCore_PosCodeToName(UserRawData['PositionCode'])
                # = self.MySQL
                #self.UserInfo_JobPos = self.
                
                QtWidgets.QMessageBox.information(self, 'Route88 Login Form | Login Success', "Login Success! You have are now logged in as ... '{} | Job Info |> {}.".format(self.UserLiteralName, self.UserPosInfo), QtWidgets.QMessageBox.Ok)
                self.StatusLabel.setText("Successfully Logged in ... {}".format(''))

                QtTest.QTest.qWait(1300)
                self.MySQL_CloseCon() # Reconnect to Anothe SQ: Usage with Specific User Parameters
                self.close()

                self.Route88_MCInst = Route88_WindowController(Staff_Name=self.UserLiteralName, Staff_Job=self.UserPosInfo, Staff_DBUser='Route_TempUser', Staff_DBPass='123456789')
                self.Route88_MCInst.show()

            else:
                self.TechnicalCore_Beep()
                self.StatusLabel.setText("Login Error: Credential Input Not Matched!")
                self.UserAcc_SubmitData.setDisabled(False)

                QtWidgets.QMessageBox.critical(self, 'Route88 Login Form | Login Failed', "Login Failed! Credential Input Not Matched. Check your User Code or your Password which may be written in Caps Lock. Please Try Again.", QtWidgets.QMessageBox.Ok)

                

        except (Exception, MySQL.OperationalError, MySQL.Error, MySQL.Warning, MySQL.DatabaseError) as LoginSubmissionErrorMsg:
            self.TechnicalCore_Beep()
            self.StatusLabel.setText(str(LoginSubmissionErrorMsg))
            print('[Exception @ LoginCore_DataSubmission] > Data Submission Failed. Detailed Info |> {}'.format(str(LoginSubmissionErrorMsg)))

    # Route88_LoginForm UI Window Functions - EndPoint

class Route88_ManagementCore(Ui_Route88_DataViewer_Window, QtWidgets.QMainWindow, Route88_TechnicalCore):
    def __init__(self, Parent=None, InCharge_Name=None, InCharge_Job=None, InCharge_DBUser=None, InCharge_DBPass=None):
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

        # Table Seelection Binds
        self.TableSystem_Selection.currentIndexChanged.connect(self.DataVCore_LoadTableSets)

        # Staff Action Binds 
        self.StaffAct_Add.clicked.connect(self.DataVCore_AddEntry)
        self.StaffAct_Edit.clicked.connect(self.DataVCore_EditEntry)
        self.StaffAct_Delete.clicked.connect(self.DataVCore_DeleteEntry)
        self.StaffAct_RefreshData.clicked.connect(self.DataVCore_RefreshData)

        self.Window_Quit.triggered.connect(self.DataVCore_ReturnWindow)

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
        except (Exception, MySQL.OperationalError, MySQL.Error, MySQL.Warning, MySQL.DatabaseError) as RenderErrorMsg:
            self.InventoryStatus.showMessage('Application Error: {0}'.format(RenderErrorMsg))
            print('[Exception Thrown @ DataVCore_RenderExplicits] > Detailed Info |> {0}'.format(RenderErrorMsg))

    def DataVCore_RunAfterRender(self):
        try:
            self.MySQL_OpenCon(SQL_UCredential='Route_TempUser', SQL_PCredential='123456789', SQLDatabase_Target='Route88_Management')
            self.MySQL_CursorSet(MySQL.cursors.DictCursor)
            self.MySQL_ExecuteState('SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED')
            #Set All Parameters Without User Touching it for straight searching...
            self.DataVCore_PatternEnabler()
            self.DataVCore_SearchFieldSet()
            self.DataVCore_OperatorSet()
            self.DataVCore_PatternSetter()
            self.DataVCore_LoadTableSets()
            
        except (Exception, MySQL.OperationalError, MySQL.Error, MySQL.Warning, MySQL.DatabaseError) as FunctionErrorMsg:
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
                self.TargetParameter = "%{}".format(self.Query_ValueToSearch.text())
            elif self.SearchPattern_ComboBox.currentText() == 'Ends With':
                self.TargetParameter = "{}%".format(self.Query_ValueToSearch.text())

    #Render Table Columns

    def DataVCore_LoadTableSets(self):
        try:
            self.ActiveTable = self.TableSystem_Selection.currentText()

            if self.ActiveTable == "None":
                self.DataVCore_ColOptClear()
                self.Query_ColumnOpt.setEnabled(False)
                self.DataTable_View.setRowCount(0)
                self.DataTable_View.setColumnCount(0)
                self.DataTableTarget = None

            elif self.ActiveTable == "Inventory Data":
                self.DataVCore_ColOptClear()
                self.Query_ColumnOpt.setEnabled(True)
                self.Query_ColumnOpt.addItem("ItemCode")
                self.Query_ColumnOpt.addItem("ItemName")
                self.Query_ColumnOpt.addItem("Cost")
                self.Query_ColumnOpt.addItem("ExpiryDate")
                self.Query_ColumnOpt.addItem("AvailableStock")
                self.Query_ColumnOpt.addItem("CreationTime")
                self.Query_ColumnOpt.addItem("LastUpdate")

                self.DataTable_View.setColumnCount(7)
                self.DataTable_View.setHorizontalHeaderLabels(("ItemCode", "ItemName", "Cost", "ExpiryDate", "AvailableStock", "CreationTime", "LastUpdate"))
                self.TechnicalCore_ColResp()
                self.DataTableTarget = "InventoryItem"


            elif self.ActiveTable == "Item Transaction Data":
                self.DataVCore_ColOptClear()
                self.Query_ColumnOpt.setEnabled(True)
                self.Query_ColumnOpt.addItem("TransactionCode")
                self.Query_ColumnOpt.addItem("MenuCode")
                self.Query_ColumnOpt.addItem("Cost")
                self.Query_ColumnOpt.addItem("CreationTime")

                self.DataTable_View.setColumnCount(4)
                self.DataTable_View.setHorizontalHeaderLabels(("ItemCode", "Transaction Code", "MenuCode", "Cost", "CreationTime"))
                self.TechnicalCore_ColResp()
                self.DataTableTarget = "ItemTransaction"

            elif self.ActiveTable == "Supplier Data":
                self.DataVCore_ColOptClear()
                self.Query_ColumnOpt.setEnabled(True)
                self.Query_ColumnOpt.addItem("SupplierCode")
                self.Query_ColumnOpt.addItem("Name")
                self.Query_ColumnOpt.addItem("LastDeliveryDate")
                self.Query_ColumnOpt.addItem("NextDeliveryDate")
                self.Query_ColumnOpt.addItem("CreationTime")
                self.Query_ColumnOpt.addItem("LastUpdate")

                self.DataTable_View.setColumnCount(6)
                self.DataTable_View.setHorizontalHeaderLabels(("SupplierCode", "Name", "Cost", "LastDeliveryDate", "NextDeliveryDate", "CreationTime", "LastUpdate"))
                self.TechnicalCore_ColResp()
                self.DataTableTarget = "SupplierReference"

            elif self.ActiveTable == "Supplier Transaction Data":
                self.DataVCore_ColOptClear()
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
                self.TechnicalCore_ColResp()
                self.DataTable_View.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
                self.DataTableTarget = "SupplierTransaction"

            elif self.ActiveTable == "Customer Receipt Data":
                self.DataVCore_ColOptClear()
                self.Query_ColumnOpt.setEnabled(True)
                self.Query_ColumnOpt.addItem("TransactionCode")
                self.Query_ColumnOpt.addItem("TotalCost")
                self.Query_ColumnOpt.addItem("VATableCost")
                self.Query_ColumnOpt.addItem("VATExempt")
                self.Query_ColumnOpt.addItem("ZeroRated")
                self.Query_ColumnOpt.addItem("NetVAT")
                self.Query_ColumnOpt.addItem("VATRate")
                self.Query_ColumnOpt.addItem("CreationTime")

                self.DataTable_View.setColumnCount(8)
                self.DataTable_View.setHorizontalHeaderLabels(("TrasanctionCode", "TotalCost", "VatableCost", "VatExempt", "ZeroRated", "NetVat", "VatRate", "CreationTime"))
                self.DataTable_View.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.Stretch)
                self.DataTableTarget = "CustReceipts"

            elif self.ActiveTable == "Employee Data":
                self.DataVCore_ColOptClear()
                self.Query_ColumnOpt.setEnabled(True)
                self.Query_ColumnOpt.addItem("EmployeeCode")
                self.Query_ColumnOpt.addItem("FirstName")
                self.Query_ColumnOpt.addItem("LastName")
                self.Query_ColumnOpt.addItem("PositionCode")
                self.Query_ColumnOpt.addItem("DOB")
                self.Query_ColumnOpt.addItem("Address")
                self.Query_ColumnOpt.addItem("SSS")
                self.Query_ColumnOpt.addItem("TIN")
                self.Query_ColumnOpt.addItem("PhilHealth")
                self.Query_ColumnOpt.addItem("TIN")
                self.Query_ColumnOpt.addItem("CreationTime")
                self.Query_ColumnOpt.addItem("LastUpdate")

                self.DataTable_View.setColumnCount(12)
                self.DataTable_View.setHorizontalHeaderLabels(("EmployeeCode", "FirstName", "LastName",  "PositionCode", "DOB", "Address", "SSS", "TIN", "PhilHealth", "TIN", "CreationTime", "LastUpdate"))
                self.DataTableTarget = "Employees"

            elif self.ActiveTable == "Job Position Data":
                self.DataVCore_ColOptClear()
                self.Query_ColumnOpt.setEnabled(True)
                self.Query_ColumnOpt.addItem("PositionCode")
                self.Query_ColumnOpt.addItem("JobName")

                self.DataTable_View.setColumnCount(2)
                self.DataTable_View.setHorizontalHeaderLabels(("Position Code", "Job Name"))
                self.TechnicalCore_ColResp()
                self.DataTableTarget = "JobPosition"

            self.DataVCore_LoadTableData()

        except Exception as RenderTableViewMsg:
            self.TechnicalCore_Beep()
            print('[Exception @ DataVCore_LoadTableSets] > Table Sets Rendering Error. Check your arguments. Detailed Info |> {}'.format(str(RenderTableViewMsg)))

    def DataVCore_LoadTableData(self):
        try:
            if self.ActiveTable == "None":
                self.TechnicalCore_RowClear()
                print('[Report @ DataVCore_RenderTable] > Active Data Table is None. Nothing to show.')
                self.InventoryStatus.showMessage('[Report @ DataVCore_RenderTable] > Active Data Table is None. Nothing to show.')
            else:
                self.TechnicalCore_RowClear()
                self.MySQL_ExecuteState("SELECT * FROM %s" % (self.DataTableTarget,))
                self.DataVCore_RenderTable(self.MySQL_FetchAllData())    
                self.InventoryStatus.showMessage('Query Process > Data Table View for {} has been refreshed from MySQL Database. Ready~!'.format(self.DataTableTarget))
                print('[Report @ DataVCore_LoadTableData] > Data Table View for {} has been refreshed from MySQL Database. Ready~!'.format(self.DataTableTarget))

        except (Exception, MySQL.OperationalError, MySQL.Error, MySQL.Warning, MySQL.DatabaseError) as FunctionErrorMsg:
            self.InventoryStatus.showMessage('Application Error: {}'.format(FunctionErrorMsg))
            print('[Exception Thrown @ DataVCore_LoadTableData] > {}'.format(FunctionErrorMsg))
    
        # Actual Search Function
    def DataVCore_ValSearch(self): # This function is fired every time there will be changes on the QLineEdit -> Query_ValueToSearch
        try:
            if len(self.Query_ValueToSearch.text()) < 1:
                self.InventoryStatus.showMessage('Query Empty... Resetting View...')
                self.DataVCore_RefreshData()

            elif self.Query_ColumnOpt.currentText() == "None":
                print('Search Query Selected Column is None. Search Operation is Cancelled.')
                self.InventoryStatus.showMessage('Search Query Selected Column is None. Search Operation is Cancelled.')
            else:
                self.InventoryStatus.showMessage('Looking At This Requested Target Value {} @ {}.'.format(str(self.Query_ValueToSearch.text()), self.Query_ColumnOpt.currentText()))
                
                self.DataTable_View.clearContents()

                print('[Search Operation] Field -> {} | Operator -> {} | Target Value -> {}'.format(self.FieldParameter, self.OperatorParameter, self.TargetParameter))
                print('[Search Query] SELECT * FROM {} WHERE {} {} {}'.format(self.DataTableTarget, self.FieldParameter, self.OperatorParameter, self.TargetParameter))

                self.MySQL_ExecuteState("SELECT * FROM %s WHERE %s %s '%s'" % (self.DataTableTarget, self.FieldParameter, self.OperatorParameter, self.TargetParameter,))
                self.DataVCore_RenderTable(self.MySQL_FetchAllData())

        except (Exception, MySQL.Error, MySQL.OperationalError) as SearchQueryError:
            self.InventoryStatus.showMessage('Application Error: Value Searching Returns Error. Detailed Info > {}'.format(SearchQueryError))
            print('[Exception Thrown @ DataVCore_ValSearch] > Value Searching Returns Error. Detailed Info > {}'.format(SearchQueryError))

    def DataVCore_RenderTable(self, FunctionCall_DataFetch):
        currentRow = 0
        if self.ActiveTable == "None":
            self.TechnicalCore_RowClear()
            print('[Report @ DataVCore_RenderTable] > Active Data Table is None. Nothing to show.')
            self.InventoryStatus.showMessage('[Report @ DataVCore_RenderTable] > Active Data Table is None. Nothing to show.')

        elif self.ActiveTable == "Inventory Data":
            for InventoryData in FunctionCall_DataFetch:
                self.DataTable_View.setRowCount(currentRow + 1)

                self.DataTable_View.setItem(currentRow, 0, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['ItemCode'])))
                self.DataTable_View.setItem(currentRow, 1, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['ItemName'])))
                self.DataTable_View.setItem(currentRow, 2, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['Cost'])))
                self.DataTable_View.setItem(currentRow, 3, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['ExpiryDate'])))
                self.DataTable_View.setItem(currentRow, 4, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['AvailableStock'])))
                self.DataTable_View.setItem(currentRow, 5, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['CreationTime'])))
                self.DataTable_View.setItem(currentRow, 6, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['LastUpdate'])))

                for SetCellFixedWidth in range(0, self.DataTable_View.columnCount()):
                    ColumnPosFixer = self.DataTable_View.item(currentRow, SetCellFixedWidth)
                    ColumnPosFixer.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                currentRow += 1

        elif self.ActiveTable == "Item Transaction Data":
            for InventoryData in FunctionCall_DataFetch:
                self.DataTable_View.setRowCount(currentRow + 1)

                self.DataTable_View.setItem(currentRow, 0, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['TransactionCode'])))
                self.DataTable_View.setItem(currentRow, 1, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['MenuCode'])))
                self.DataTable_View.setItem(currentRow, 2, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['Cost'])))
                self.DataTable_View.setItem(currentRow, 3, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['CreationTime'])))

                for SetCellFixedWidth in range(0, self.DataTable_View.columnCount()):
                    ColumnPosFixer = self.DataTable_View.item(currentRow, SetCellFixedWidth)
                    ColumnPosFixer.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                currentRow += 1

        elif self.ActiveTable == "Supplier Data":
            for InventoryData in FunctionCall_DataFetch:
                self.DataTable_View.setRowCount(currentRow + 1)

                self.DataTable_View.setItem(currentRow, 0, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['SupplierCode'])))
                self.DataTable_View.setItem(currentRow, 1, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['Name'])))
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

        elif self.ActiveTable == "Employee Data":
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
                
        elif self.ActiveTable == "Job Position Data":
            for InventoryData in FunctionCall_DataFetch:
                self.DataTable_View.setRowCount(currentRow + 1)

                self.DataTable_View.setItem(currentRow, 0, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['TransactionCode'])))
                self.DataTable_View.setItem(currentRow, 1, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['TotalCost'])))
                self.DataTable_View.setItem(currentRow, 2, QtWidgets.QTableWidgetItem('{}'.format(InventoryData['VATableCost'])))

                for SetCellFixedWidth in range(0, self.DataTable_View.columnCount()):
                    ColumnPosFixer = self.DataTable_View.item(currentRow, SetCellFixedWidth)
                    ColumnPosFixer.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignHCenter)
                currentRow += 1
    
    # Staff Action Functions

    def DataVCore_AddEntry(self):
        self.ModifierDialog = Route88_ModifierCore()
        self.ModifierDialog.exec_()
        self.DataVCore_RefreshData()

    def DataVCore_EditEntry(self):
        pass

    def DataVCore_DeleteEntry(self):
        try:
            if self.DataTable_View.rowCount() == 0:
                self.StaffAct_Delete.setEnabled(False)
                self.InventoryStatus.showMessage('Table Data Error > Table View is currently empty. You cannot delete any data anymore.')
                print('Report @ DataVCore_DeleteEntry] Table View is currently empty. You cannot delete any data anymore.')
            else:
                self.StaffAct_Delete.setEnabled(True)
                self.selectedRow = self.DataTable_View.currentRow()
                self.selectedStatic_ItemCode = 0
                self.selectedData = self.DataTable_View.item(self.selectedRow, self.selectedStatic_ItemCode).text()
                # Make IL_ItemCode as Temporary here, change it into a variable next time.
                print('[Database Query Process: Deletion Query] -> DELETE FROM {} WHERE IL_ItemCode = {}'.format(self.DataTableTarget, self.selectedData))
                self.InventoryStatus.showMessage('Deletion Query: Processing to Delete Row {0}'.format(self.selectedRow))

                self.MySQLDataWireCursor.execute('DELETE FROM {} WHERE IL_ItemCode = {}'.format(self.DataTableTarget, self.selectedData))
                self.DataTable_View.removeRow(self.selectedRow)
                self.MySQLDataWire.commit()
                self.InventoryStatus.showMessage('Deletion Query Process Success! > Row {} Deleted.'.format(self.selectedRow + 1))

        except (Exception, MySQL.Error, MySQL.OperationalError) as DelectionErrMsg:
            self.InventoryStatus.showMessage('Deletion Query Process Error -> {}'.format(DelectionErrMsg))
            print('[Exception Thrown @ DataVCore_DeleteEntry] -> {0}'.format(str(DelectionErrMsg)))
    
    # Exit Function
    def DataVCore_ReturnWindow(self):
        self.close()
        self.ReturnWinInst = Route88_WindowController(Staff_Name=self.InCharge_LiteralName, Staff_Job=self.InCharge_JobPos, Staff_DBUser=self.InCharge_DBUser, Staff_DBPass=self.InCharge_DBPass)
        self.ReturnWinInst.show()



    def DataVCore_RefreshData(self):
        try:
            self.TechnicalCore_RowClear()

            self.InventoryStatus.showMessage('[Data Query Process @ DataVCore_RefreshData] > Attempting To Refresh Data from MySQL Database...')
            self.InventoryStatus.showMessage('Database Query Process: Attempting To Refresh Data from MySQL Database...')
            QtTest.QTest.qWait(800)
            self.DataVCore_LoadTableData()

        except (Exception, MySQL.Error, MySQL.OperationalError) as RefreshError:
            self.InventoryStatus.showMessage('Application Error: {0}'.format(str(RefreshError)))
            raise Exception('[Exception Thrown @ DataVCore_RefreshData] -> {0}'.format(str(RefreshError)))


class Route88_ModifierCore(Ui_Route88_DataManipulation_Window, QtWidgets.QDialog, Route88_TechnicalCore):
    def __init__(self, Parent=None):
        super(Route88_ModifierCore, self).__init__(Parent=Parent)
        self.setupUi(self)
        self.DataMCore_RenderExplicits()
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.WindowShadeButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        self.setWindowIcon(QtGui.QIcon('IcoDisplay/r_88.ico'))


    # Button Binds to Functions
        #for SetDisability in range(1, 5):
        #    self.Tab_SelectionSelectives.setTabEnabled(SetDisability, False)
        
        self.Modifier_CloseWindow.clicked.connect(self.close)
        self.Modifier_AddEntry.clicked.connect(self.DataMCore_AddEntry)
        self.Modifier_ClearEntry.clicked.connect(self.DataMCore_ClearEntry)

        self.DataMCore_RunAfterRender()

        # Technical Functions
    def DataMCore_RenderExplicits(self):
        self.AddEntry_DateExpiry.setDateTime(QtCore.QDateTime.currentDateTime())

    def DataMCore_RunAfterRender(self):
        self.MySQL_OpenCon(SQL_UCredential='Route_TempUser', SQL_PCredential='123456789',SQLDatabase_Target='route88_management')
        self.MySQL_CursorSet(None)


    # Staff Action Function Declarations
    def DataMCore_AddEntry(self):
        try:
            # Add Check of Active Table Here
            self.MySQL_CursorSet(None)
            QDateGet = self.AddEntry_DateExpiry.date() 
            formattedDate = QDateGet.toPyDate()
            # Add More Options Here
            #appendRowLast = self.DataTable_View.rowCount()
            if len(self.AddEntry_ItemCode.text()) == 0:
                self.DataMCore_Status.showMessage('Adding Entry Error: Constraint (> 0 Characters) Not Met @ Item Code Entry.')
                raise Exception('Adding Entry Error: Constraint (> 0 Characters) Not Met @ Item Code Entry.')
            elif len(self.AddEntry_SupplierCode.text()) == 0:
                self.DataMCore_Status.showMessage('Adding Entry Error: Constraint (> 0 Characters) Not Met @ Supplier Code Entry')
                raise Exception('Adding Entry Error: Constraint (> 0 Characters) Not Met @ Supplier Code Entry')
            elif len(self.AddEntry_ItemName.text()) < 2:
                self.DataMCore_Status.showMessage('Adding Entry Error: Constraint (> 2 Characters) Not Met @ Item Name Entry')
                raise Exception('Adding Entry Error: Constraint (> 2 Characters) Not Met @ Item Name Entry')
            elif len(self.AddEntry_ItemType.text()) < 2:
                self.DataMCore_Status.showMessage('Adding Entry Error: Constraint (> 2 Characters) Not Met @ Item Type Entry')
                raise Exception('Adding Entry Error: Constraint (> 2 Characters) Not Met @ Item Type Entry')
            #elif len()
            else:
                TargetTable_Param = self.DataMCore_GetTargetTable()
                print('[Pushing Value to Table @ InventoryList] -> INSERT INTO {} VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {})'.format(TargetTable_Param, self.AddEntry_ItemCode.text(), self.AddEntry_SupplierCode.text(), self.AddEntry_ItemName.text(), self.AddEntry_ItemType.text(), self.AddEntry_Quantity.value(), self.AddEntry_Cost.value(), formattedDate, 1,formattedDate, formattedDate))

                #self.MySQLDataWireCursor.execute("INSERT INTO {} VALUES ({}, {}, '{}', '{}', {}, {}, '{}', {}, '{}', '{}')".format(str(TargetTable_Param), str(self.AddEntry_ItemCode.text()), str(self.AddEntry_SupplierCode.text()), str(self.AddEntry_ItemName.text()), str(self.AddEntry_ItemType.text()), str(self.AddEntry_Quantity.value()), str(self.AddEntry_Cost.value()), str(formattedDate), 1,str(formattedDate), str(formattedDate)))
                #self.MySQLDataWire.commit()
                print('[Report @DataMCore_AddEntry] > Successful Execution -> Data Successfully Added to Database~!')
                self.DataMCore_Status.showMessage('Successful Execution -> Data Successfully Added to Database~!')



        
        except (Exception, MySQL.Error, MySQL.OperationalError) as PushEntryErrMsg:
            self.TechnicalCore_Beep()
            self.DataMCore_Status.showMessage('Add Entry Execution Error: Please check your SQL connection or your fields!')
            QtWidgets.QMessageBox.critical(self, 'Route88 System | Data Manipulation Insertion Error', "Error, cannot push data from the database. Check your fields or your database connection. But in any case, here is the error output: {}".format(str(PushEntryErrMsg)), QtWidgets.QMessageBox.Ok)
            print('[Technical Information @ DataMCore_AddEntry] -> {}'.format(PushEntryErrMsg))
    
    def DataMCore_ClearEntry(self, ActiveEntryWindow):
        if self.Tab_SelectionSelectives.currentIndex() == 0:
            self.AddEntry_ItemCode.clear()
            self.AddEntry_SupplierCode.clear()
            self.AddEntry_ItemName.clear()
            self.AddEntry_ItemType.clear()
            self.AddEntry_Quantity.setValue(0)
            self.AddEntry_Cost.setValue(0.0)
            self.AddEntry_DateExpiry.setDateTime(QtCore.QDateTime.currentDateTime())
            self.DataMCore_Status.showMessage('Fields Cleared. Ready To Get Inputs~!')
            #(self.Tab_SelectionSelectives.tabText(self.Tab_SelectionSelectives.currentIndex()))) WTF is this%s
            print('[Execution @ DataMCore_ClearEntry] ->  Finished. Ready!'.format(self.Tab_SelectionSelectives.tabText(self.Tab_SelectionSelectives.currentIndex())))
        elif self.Tab_SelectionSelectives.currentIndex() == 1:
            pass
        elif self.Tab_SelectionSelectives.currentIndex() == 2:
            pass
        elif self.Tab_SelectionSelectives.currentIndex() == 3:
            pass
        elif self.Tab_SelectionSelectives.currentIndex() == 4:
            pass
        elif self.Tab_SelectionSelectives.currentIndex() == 5:
            pass
        else:
            raise ValueError('[Exception @ Modifier_ClearEntry] Current Index of Selected Tab does not match from any defined conditions.')
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
        self.ctrl_ManageSystem.clicked.connect(self.ShowManagementCore)
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
        pass

    def ShowAboutCore(self):
        pass

    def ControllerCore_RunAfterRender(self):
        self.StatusLabel.setText('Staff Restrictions has been activated for Staff {}.'.format(self.StaffLiteralName))
        self.user_StaffName.setText(self.StaffLiteralName) 
        self.user_JobPosition.setText(self.StaffCurrentJob)
# Literal Procedural Programming Part
if __name__ == "__main__":
    sysCmdArgumentHandler('CLS')
    print('[Application App Startup] Route88 Hybrid Application, Debugger Output')
    app = QtWidgets.QApplication(sys.argv)
    Route88_InitialInst = Route88_LoginCore()
    Route88_InitialInst.show()
    sys.exit(app.exec_())