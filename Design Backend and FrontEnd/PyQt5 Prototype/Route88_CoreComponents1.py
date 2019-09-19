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
                -> <ClassShortName>_RenderExplicitElem
                -> <ClassShortName>_RFAR

        Class Route88_ManagementCore()
            Methods:
                -> __init__()
                    Includes
                -> <ClassShortName>_RenderExplicitElem
                -> <ClassShortName>_RFAR

        Class Route88_POSCore()
            Methods:
                -> __init__()
                    Includes
                -> <ClassShortName>_RenderExplicitElem
                -> <ClassShortName>_RFAR

    
    Legends:
        Definitions:
            _RenderExplicitElem -> Render Explicit Elements
            _RFAR -> Run Function After Render
        Functions:
            __init__() -> Class Initializers, Possibly Constructors
            <ClassShortName>_RenderExplicitElem -> Load Extra Elements from 'That' UI
                > This was implemented to ensure that changes from the UI file will not     affect any additional elements that we just manually added which cannot be initiated with Qt Designer, this would result to extra elements  remains whatver UI file changes after generating using 'pyuic5' module.
            <ClassShortName>_RFAR -> Condition, Must Be After setupUi()
                > This was implemented right after setupUi(). Because, we have to   initialize every value from the database which would then be shown after  UI has been render. So that when the engine initiates .show(). All   values is already there. So in sort, setup Values and Elements.
'''
from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from PyQt5.QtMultimedia import QSound
import MySQLdb as MySQL
import sys
from os import system as sysCmdArgumentHandler
from Route88_LoginForm import Ui_Route88_LoginWindow
from Route88_InventorySystem import Ui_Route88_InventorySystemView 

from Route88_Inventory_ModifierEntry import Ui_Route88_Management_Modifier
#from Route88_POSSystem import ???

# This class contains all technical function that would be used by these multiple class of multiple window.

class Route88_TechnicalCore(object):
    def __init__(self, Parent=None):
        super().__init__()

    # MySQL Mainstream Functions, Functions That Requires Calling MySQLdb Library
    # Initialize MySQL Server Twice, One for Login and Last.... ???
    def MySQL_ConnectDatabase(self, HostServerIP='localhost', SQL_UCredential='Route_TempUser', SQL_PCredential='123456789', SQLDatabase_Target='Route88_EmployeeInfo'):
        try:
            self.MySQLDataWire = MySQL.connect(host=HostServerIP, user=SQL_UCredential, passwd=SQL_PCredential, db=SQLDatabase_Target)
            print('MySQL Database Connection Attempt: User {0} is now logged as {1} with Database Role of {2}.'.format('???', SQL_UCredential, '???'))
        except MySQL.OperationalError as MySQL_ErrorMessage:
            self.StatusLabel.setText("Database Error: Cannot Connect to the SQL Database. Please restart.")
            print(MySQL_ErrorMessage)

    # Sets CursorType for Iteration which outputs the following CursorType
    def MySQL_CursorSet(self, CursorType=None):
        try:
            self.MySQLDataWireCursor = self.MySQLDataWire.cursor(CursorType)
        except (Exception, MySQL.OperationalError) as CursorErrMsg:
            print(CursorErrMsg)


class Route88_LoginCore(Ui_Route88_LoginWindow, Route88_TechnicalCore):
    # Class Initializer, __init__
    def __init__(self, Parent=None):
        super(Route88_LoginCore, self).__init__(Parent=Parent)
        '''
            LoginWindow is Not Initialized / Seperate as a Function for Initialization.
                Note: The reason why we did this is because I don't things to be more complicated as it should be.
                So that when my other members start to read my code, it is exactly stated here that we want first to initialize LoginWindow
                other than anything that they thought, 'what the hell is this argument that you pass?'
                ~ All other window will be seperately initialized...
        '''
        #self.Route88_LoginWindow = Ui_Route88_LoginWindow()
        #self.Login_TechnicalCoreHandler = Route88_TechnicalCore()

        self.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('IcoDisplay/r_88.ico'))

        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowShadeButtonHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        # Button Binds for Window 'Route88_LoginForm'
        self.UserAcc_Password.returnPressed.connect(self.UserAcc_SubmitData.click)
        self.UserAcc_SubmitData.clicked.connect(self.LoginForm_DataSubmission)
        #Run The Following Functions for Initializing User Data @ Window 'Route88_LoginForm'

        self.LoginForm_RFAR()
    # Technical Functions
    # Load Function After UI Rendering.
    def LoginForm_RFAR(self):
        try:
            self.MySQL_ConnectDatabase(SQL_UCredential='Route_TempUser', SQL_PCredential='123456789', SQLDatabase_Target='route88_employees')
            self.MySQL_CursorSet(MySQL.cursors.DictCursor)
            self.LoginForm_ReadUserEnlisted()
        except Exception as ErrorHandler:
            print(ErrorHandler)
            QSound.play("SysSounds/LoginFailedNotify.wav")
            QtWidgets.QMessageBox.critical(self, 'Route88 Login Form | Database Error', "Error, cannot connect to the database, here is the following error prompt that the program encountered. '{}'. Please restart the program and re-run the XAMPP MySQL Instance.".format(str(ErrorHandler)), QtWidgets.QMessageBox.Ok)
            sys.exit() # Terminate the program at all cost.
    #Route88_LoginForm UI Window Functions - StartPoint
    def LoginForm_ReadUserEnlisted(self):
        try:
            currentRow = 0
            self.MySQL_CursorSet()
            self.MySQLDataWireCursor.execute("SELECT COUNT(*) FROM Employees")
            self.UserEnlistedCount = self.MySQLDataWireCursor.fetchone()[0]
            self.StatusLabel.setText("Database Loaded. Ready~!")
            if self.UserEnlistedCount == 0:
                self.MySQLDataWireCursor.execute("INSERT INTO Employees (EmployeeCode, FirstName, LastName, PositionCode, EmployeePassword) VALUES (1, 'Janrey', 'Licas', 1, 'CdxLnk121')")
                self.MySQLDataWireCursor.execute("INSERT INTO JobPosition VALUES (1, 'Manager')") # Remove Comment If Necessary
                self.MySQLDataWire.commit()
                self.UserAcc_SubmitData.setDisabled(False)
                # Insert Windwo of that window here.
            else:
                self.UserAcc_SubmitData.setDisabled(False)

        except MySQL.OperationalError as LoginQueryErrorMsg:
            print('MySQL.OperationalError -> {0}'.format(str(LoginQueryErrorMsg)))
            self.StatusLabel.setText("Database Error: Cannot Connect. Please restart.")
            QSound.play("SysSounds/LoginFailedNotify.wav")
            QtWidgets.QMessageBox.critical(self, 'Route88 Login Form | Database Error', "Error, cannot connect to the database, here is the following error prompt that the program encountered. '{}'. Please restart the program and re-run the XAMPP MySQL Instance.".format(str(LoginQueryErrorMsg)), QtWidgets.QMessageBox.Ok)
            sys.exit() # Terminate the program at all cost.

    def LoginForm_DataSubmission(self):
        try:
            self.MySQL_CursorSet(None)
            QueryReturn = self.MySQLDataWireCursor.execute("SELECT * FROM Employees WHERE EmployeeCode = %s AND EmployeePassword = %s", (self.UserAcc_Username.text(), self.UserAcc_Password.text()))
                # After query we need to check if QueryReturn contains non-zero values. If it contains non-zero we proceed. Else not...
                # We need to store the credentials that is equalled to what we expect.
            if QueryReturn:
                self.StatusLabel.setText("Login Success: Credential Input Matched!")
                QSound.play("SysSounds/LoginSuccessNotify.wav")
                QtWidgets.QMessageBox.information(self, 'Route88 Login Form | Login Success', "Login Success! You have are now logged in as ... '{}'. ".format('NA'), QtWidgets.QMessageBox.Ok)
                self.StatusLabel.setText("Successfully Logged in ... {}".format(''))
                QtTest.QTest.qWait(1500)
                self.MySQLDataWire.close() # Reconnect to Anothe SQ: Usage with Specific User Parameters
                self.hide()
                self.Route88_InventoryInstance = Route88_ManagementCore() #'RouteTemp_FirstTimer', 'route88_group7')
                self.Route88_InventoryInstance.show()
            else:
                self.StatusLabel.setText("Login Error: Credential Input Not Matched!")
                QSound.play("SysSounds/LoginFailedNotify.wav")
                QtWidgets.QMessageBox.critical(self, 'Route88 Login Form | Login Failed', "Login Failed! Credential Input Not Matched. Check your User Code or your Password which may be written in Caps Lock. Please Try Again.", QtWidgets.QMessageBox.Ok)

                

        except Exception as LoginSubmissionErrorMsg:
            print(LoginSubmissionErrorMsg)
            self.StatusLabel.setText(str(LoginSubmissionErrorMsg))
            QSound.play("SysSounds/LoginFailedNotify.wav")

    # Route88_LoginForm UI Window Functions - EndPoint


class Route88_ManagementCore(Ui_Route88_InventorySystemView, Route88_TechnicalCore):
    def __init__(self, Parent=None):
        super(Route88_ManagementCore, self).__init__(Parent=Parent)
        self.setWindowFlags(QtCore.Qt.Window | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowMaximizeButtonHint)
        self.setupUi(self)
        self.ManagementSys_RenderExplicitElem()
        self.setWindowIcon(QtGui.QIcon('IcoDisplay/r_88.ico'))
        # Button Binds for Window 'Route88_InventoryDesign'
        # > Search Query Binds
        self.Query_ColumnOpt.currentIndexChanged.connect(self.ManagementSys_SearchFieldSet)
        self.Query_Operator.currentIndexChanged.connect(self.ManagementSys_OperatorSet)

        self.Query_ColumnOpt.currentIndexChanged.connect(self.ManagementSys_SearchVal)
        self.Query_Operator.currentIndexChanged.connect(self.ManagementSys_SearchVal)

        self.Query_ValueToSearch.textChanged.connect(self.ManagementSys_PatternSet)
        self.Query_ValueToSearch.textChanged.connect(self.ManagementSys_SearchVal)

        self.SearchPattern_ExactOpt.clicked.connect(self.ManagementSys_PatternEnabler)
        self.SearchPattern_ContainOpt.clicked.connect(self.ManagementSys_PatternEnabler)

        self.SearchPattern_ExactOpt.clicked.connect(self.ManagementSys_SearchVal)
        self.SearchPattern_ContainOpt.clicked.connect(self.ManagementSys_SearchVal)
        
        self.SearchPattern_ComboBox.currentIndexChanged.connect(self.ManagementSys_PatternSet)

        # > Staff Action Binds 
        self.StaffAct_Add.clicked.connect(self.ManagementSys_AddEntry)
        self.StaffAct_Edit.clicked.connect(self.ManagementSys_EditEntry_Selected)
        self.StaffAct_Delete.clicked.connect(self.ManagementSys_DeleteEntry_Selected)
        self.StaffAct_RefreshData.clicked.connect(self.ManagementSys_RefreshData)

        self.Window_Quit.triggered.connect(self.close)
        #self.Window_Quit.triggered.connect()

        self.TableParameter = 'InventoryList' # Sets Current Table Tempporarily
        self.ManagementSys_RFAR() #Run This Function After UI Initialization

    #Function Definitions for Route88_InventoryDesign
    def ManagementSys_RenderExplicitElem(self):
        currentRow = 0
        self.InventoryStatus = QtWidgets.QStatusBar()
        self.setStatusBar(self.InventoryStatus)
        self.InventoryTable_View.setRowCount(currentRow + 1)
        for SetCellFixedElem in range(10):
            self.InventoryTable_View.horizontalHeader().setSectionResizeMode(SetCellFixedElem, QtWidgets.QHeaderView.ResizeToContents)
        
        self.Query_ColumnOpt.model().item(1).setEnabled(False)

        self.InventoryTable_View.horizontalHeader().setSectionResizeMode(2, QtWidgets.QHeaderView.Stretch)
        self.InventoryTable_View.horizontalHeader().setSectionResizeMode(9, QtWidgets.QHeaderView.Stretch)

    def ManagementSys_RFAR(self):
        try:
            self.MySQL_ConnectDatabase(SQL_UCredential='Route_TempUser', SQL_PCredential='123456789', SQLDatabase_Target='Route88_Inventory')
            self.MySQL_CursorSet(MySQL.cursors.DictCursor)
            self.MySQLDataWireCursor.execute('set session transaction isolation level READ COMMITTED')
            #Set All Parameters Without User Touching it for straight searching...
            self.ManagementSys_PatternEnabler()
            self.ManagementSys_SearchFieldSet()
            self.ManagementSys_OperatorSet()
            self.ManagementSys_PatternSet()
            self.ManagementSys_LoadData()
        except (Exception, MySQL.OperationalError) as FunctionErrorMsg:
            self.InventoryStatus.showMessage('Application Error: {0}'.format(FunctionErrorMsg))
            print('[Exception Thrown @ ManagementSys_RFAR] -> {0}'.format(FunctionErrorMsg))

    def ManagementSys_LoadData(self):
        try:
            #Setups
            currentRow = 0
            self.MySQLDataWireCursor.execute("SELECT * FROM InventoryList")
            InventoryDataFetch = self.MySQLDataWireCursor.fetchall()
            #print(InventoryDataFetch)
            # Fill Query_ColumnOpt First.
            #Fill Inventory Menu
            for InventoryData in InventoryDataFetch:
                self.InventoryTable_View.setRowCount(currentRow + 1)
                self.InventoryTable_View.setItem(currentRow, 0, QtWidgets.QTableWidgetItem('{0}'.format(InventoryData['IL_ItemCode'])))
                self.InventoryTable_View.setItem(currentRow, 1, QtWidgets.QTableWidgetItem('{0}'.format(InventoryData['IL_SupplierCode'])))
                self.InventoryTable_View.setItem(currentRow, 2, QtWidgets.QTableWidgetItem('{0}'.format(InventoryData['IL_ItemName'])))
                self.InventoryTable_View.setItem(currentRow, 3, QtWidgets.QTableWidgetItem('{0}'.format(InventoryData['IL_ItemType'])))
                self.InventoryTable_View.setItem(currentRow, 4, QtWidgets.QTableWidgetItem('{0}'.format(InventoryData['IL_AvailableStock'])))
                self.InventoryTable_View.setItem(currentRow, 5, QtWidgets.QTableWidgetItem('{0}'.format(InventoryData['IL_ConsumerCost'])))
                self.InventoryTable_View.setItem(currentRow, 6, QtWidgets.QTableWidgetItem('{0}'.format(InventoryData['IL_ExpiryDate'])))
                self.InventoryTable_View.setItem(currentRow, 7, QtWidgets.QTableWidgetItem('{0}'.format(InventoryData['IL_MenuInclusion'])))
                self.InventoryTable_View.setItem(currentRow, 8, QtWidgets.QTableWidgetItem('{0}'.format(InventoryData['IL_CreationTime'])))
                self.InventoryTable_View.setItem(currentRow, 9, QtWidgets.QTableWidgetItem('{0}'.format(InventoryData['IL_LastUpdate'])))
                
                for SetCellFixedWidth in range(10):
                    self.ColumnPosFixer = self.InventoryTable_View.item(currentRow, SetCellFixedWidth)
                    self.ColumnPosFixer.setTextAlignment(QtCore.Qt.AlignCenter)
                currentRow += 1
            self.InventoryStatus.showMessage('Database Query Process: TableView Data Refreshed from MySQL Database Sucess! Ready!')
            print('[Database Query Process @ ManagementSys_LoadData] -> TableView Data Refreshed from MySQL Database Sucess! Ready!')

        except (Exception, MySQL.OperationalError, MySQL.Error) as FunctionErrorMsg:
            self.InventoryStatus.showMessage('Application Error: {0}'.format(FunctionErrorMsg))
            print('[Exception Thrown @ ManagementSys_LoadData] -> {0}'.format(FunctionErrorMsg))

    # Interactive Button to Function
    # Menu Bar Functions
    # Table Selection Functions
    def ManagementSys_SearchFieldSet(self):
        if self.Query_ColumnOpt.currentText() == 'None':
            self.Query_Operator.setEnabled(False)
            self.Query_ValueToSearch.setEnabled(False)
            self.SearchPattern_ContainOpt.setEnabled(False)
            self.SearchPattern_ExactOpt.setEnabled(False)
            self.SearchPattern_ComboBox.setEnabled(False)
            self.Query_ValueToSearch.clear()
        else:
            self.Query_Operator.setEnabled(True)
            self.Query_ValueToSearch.setEnabled(True)
            self.SearchPattern_ContainOpt.setEnabled(True)
            self.SearchPattern_ExactOpt.setEnabled(True)
            if self.SearchPattern_ContainOpt.isChecked():
                self.SearchPattern_ComboBox.setEnabled(True)

            if self.Query_ColumnOpt.currentText() == 'All Columns':
                self.FieldParameter = "CONCAT(IL_ItemCode, '', IL_SupplierCode ,'', IL_ItemName, '', IL_ItemType, '', IL_AvailableStock, '', IL_ExpiryDate, '', IL_MenuInclusion, '', IL_CreationTime, '', IL_LastUpdate)"
            elif self.Query_ColumnOpt.currentText() == 'Item Code':
                self.FieldParameter = 'IL_ItemCode'
            elif self.Query_ColumnOpt.currentText() == 'Supplier Code':
                self.FieldParameter = 'IL_SupplierCode'
            elif self.Query_ColumnOpt.currentText() == 'Item Name':
                self.FieldParameter = 'IL_ItemName'
            elif self.Query_ColumnOpt.currentText() == 'Type':
                self.FieldParameter = 'IL_ItemType'
            elif self.Query_ColumnOpt.currentText() == 'Cost':
                self.FieldParameter = 'IL_ConsumerCost'
            elif self.Query_ColumnOpt.currentText() == 'Quantity':
                self.FieldParameter = 'IL_AvailableStock'
            elif self.Query_ColumnOpt.currentText() == 'Expiry Date':
                self.FieldParameter = 'IL_ExpiryDate'
            elif self.Query_ColumnOpt.currentText() == 'Menu Inclusion':
                self.FieldParameter = 'IL_MenuInclusion'
            elif self.Query_ColumnOpt.currentText() == 'Data Created':
                self.FieldParameter = 'IL_CreationTime'
            elif self.Query_ColumnOpt.currentText() == 'Last Modified':
                self.FieldParameter = 'IL_LastUpdate'
            else:
                print('')
                raise ValueError('')

    def ManagementSys_OperatorSet(self):
        if self.SearchPattern_ExactOpt.isChecked():
            self.OperatorParameter = self.Query_Operator.currentText()
        elif self.SearchPattern_ContainOpt.isChecked():
            self.OperatorParameter = 'LIKE'
        else:
            raise ValueError()
            print()

    def ManagementSys_PatternEnabler(self):
        if self.SearchPattern_ExactOpt.isChecked():
            self.SearchPattern_ComboBox.setEnabled(False)
            self.Query_Operator.setEnabled(True)
            self.ManagementSys_OperatorSet()
            self.ManagementSys_PatternSet()
            self.InventoryStatus.showMessage('Search Pattern: Switched to Exact Mode...')
        elif self.SearchPattern_ContainOpt.isChecked():
            self.Query_Operator.setEnabled(False)
            self.ManagementSys_OperatorSet()
            self.ManagementSys_PatternSet()
            self.SearchPattern_ComboBox.setEnabled(True)
            self.InventoryStatus.showMessage('Search Pattern: Switched to Pattern String Mode...')
        else:
            self.InventoryStatus.showMessage('Application Error: No Other Radio Buttons has a state of Bool(True).')
            raise ValueError('[Exception Thrown @ ManagementSys_PatternSet] -> No Other Radio Buttons has a state of Bool(True).')

    def ManagementSys_PatternSet(self):
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
        else:
            raise ValueError()
            print()
            
        # Actual Search Function
    def ManagementSys_SearchVal(self): # This function is fired every time there will be changes on the QLineEdit -> Query_ValueToSearch
        currentRow = 0
        try:
            if len(self.Query_ValueToSearch.text()) < 1:
                self.InventoryStatus.showMessage('Query Empty... Resetting View...')
                self.ManagementSys_RefreshData()
            else:
                self.InventoryStatus.showMessage('Looking for {0}...'.format(str(self.Query_ValueToSearch.text())))
                self.InventoryTable_View.clearContents()
                for RowLeftOver in range(self.InventoryTable_View.rowCount()):
                    self.InventoryTable_View.removeRow(RowLeftOver)

                print('[Search Parameters] Field -> {} | Operator -> {} | Target Value -> {}'.format(self.FieldParameter, self.OperatorParameter, self.TargetParameter))
                print('[Search Query] SELECT * FROM {} WHERE {} {} {}'.format(self.TableParameter, self.FieldParameter, self.OperatorParameter, self.TargetParameter))

                self.MySQLDataWireCursor.execute("SELECT * FROM {} WHERE {} {} '{}'".format(self.TableParameter, self.FieldParameter, self.OperatorParameter, self.TargetParameter))
                InventoryTargetDataFetch = self.MySQLDataWireCursor.fetchall()

                for InventoryData in InventoryTargetDataFetch:
                    self.InventoryTable_View.setRowCount(currentRow + 1)
                    self.InventoryTable_View.setItem(currentRow, 0, QtWidgets.QTableWidgetItem('{0}'.format (InventoryData['IL_ItemCode'])))
                    self.InventoryTable_View.setItem(currentRow, 1, QtWidgets.QTableWidgetItem('{0}'.format (InventoryData['IL_SupplierCode'])))
                    self.InventoryTable_View.setItem(currentRow, 2, QtWidgets.QTableWidgetItem('{0}'.format (InventoryData['IL_ItemName'])))
                    self.InventoryTable_View.setItem(currentRow, 3, QtWidgets.QTableWidgetItem('{0}'.format (InventoryData['IL_ItemType'])))
                    self.InventoryTable_View.setItem(currentRow, 4, QtWidgets.QTableWidgetItem('{0}'.format (InventoryData['IL_AvailableStock'])))
                    self.InventoryTable_View.setItem(currentRow, 5, QtWidgets.QTableWidgetItem('{0}'.format (InventoryData['IL_ConsumerCost'])))
                    self.InventoryTable_View.setItem(currentRow, 6, QtWidgets.QTableWidgetItem('{0}'.format (InventoryData['IL_ExpiryDate'])))
                    self.InventoryTable_View.setItem(currentRow, 7, QtWidgets.QTableWidgetItem('{0}'.format (InventoryData['IL_MenuInclusion'])))
                    self.InventoryTable_View.setItem(currentRow, 8, QtWidgets.QTableWidgetItem('{0}'.format (InventoryData['IL_CreationTime'])))
                    self.InventoryTable_View.setItem(currentRow, 9, QtWidgets.QTableWidgetItem('{0}'.format (InventoryData['IL_LastUpdate'])))
                    
                    for SetCellFixedWidth in range(10):
                        self.ColumnPosFixer = self.InventoryTable_View.item(currentRow, SetCellFixedWidth)
                        self.ColumnPosFixer.setTextAlignment(QtCore.Qt.AlignCenter)
                    currentRow += 1

        except (Exception, MySQL.Error, MySQL.OperationalError) as SearchQueryError:
            self.InventoryStatus.showMessage('Application Error: {0}'.format(SearchQueryError))
            print('[Exception Thrown @ ManagementSys_SearchVal] -> {0}'.format(SearchQueryError))

    # Staff Action Functions

    def ManagementSys_ModifierInit(self):
        pass
    def ManagementSys_AddEntry(self):
        self.ModifierDialog = Route88_ModifierCore()
        self.ModifierDialog.show()

        print('done')
        #self.ModifierDialog = 

    def ManagementSys_EditEntry_Selected(self):
        pass

    def ManagementSys_DeleteEntry_Selected(self):
        try:
            if self.InventoryTable_View.rowCount == 0:
                self.StaffAct_Delete.setEnabled(False)
                self.InventoryStatus.showMessage('Table Data Error -> You cannot delete anymore.')
                raise ValueError('Table Data Error -> You cannot delete anymore.')
            else:
                self.selectedRow = self.InventoryTable_View.currentRow()
                self.selectedStatic_ItemCode = 0
                self.selectedData = self.InventoryTable_View.item(self.selectedRow, self.selectedStatic_ItemCode).text()
                # Make IL_ItemCode as Temporary here, change it into a variable next time.
                print('[Database Query Process: Deletion Query] -> DELETE FROM {} WHERE IL_ItemCode = {}'.format(self.TableParameter, self.selectedData))
                self.InventoryStatus.showMessage('Deletion Query: Processing to Delete Row {0}'.format(self.selectedRow))

                self.MySQLDataWireCursor.execute('DELETE FROM {} WHERE IL_ItemCode = {}'.format(self.TableParameter, self.selectedData))
                self.InventoryTable_View.removeRow(self.selectedRow)
                self.MySQLDataWire.commit()
                self.InventoryStatus.showMessage('Deletion Query Process Success! -> Row {} Deleted.'.format(self.selectedRow + 1))

        except (Exception, MySQL.Error, MySQL.OperationalError) as DelectionErrMsg:
            self.InventoryStatus.showMessage('Deletion Query Process Error -> {}'.format(DelectionErrMsg))
            print('[Exception Thrown @ ManagementSys_DeleteEntry_Selected] -> {0}'.format(str(DelectionErrMsg)))
            
    def ManagementSys_RefreshData(self):
        try:
           #self.MySQLDataWireCursor.close()
           #self.MySQL_ConnectDatabase(SQL_UCredential='RouteTemp_FirstTimer', SQL_PCredential='123456789', SQLDatabase_Target='route88_employeeinfo')
            self.InventoryTable_View.clearContents()
            for RowLeftOver in range(10):
                self.InventoryTable_View.removeRow(RowLeftOver)

            self.InventoryStatus.showMessage('[Data Query Process @ ManagementSys_RefreshData] -> Attempting To Refresh Data from MySQL Database...')
            self.InventoryStatus.showMessage('Database Query Process: Attempting To Refresh Data from MySQL Database...')
            QtTest.QTest.qWait(900)
            self.ManagementSys_LoadData()
        except (Exception, MySQL.Error, MySQL.OperationalError) as RefreshError:
            self.InventoryStatus.showMessage('Application Error: {0}'.format(str(RefreshError)))
            raise Exception('[Exception Thrown @ ManagementSys_RefreshData] -> {0}'.format(str(RefreshError)))

    # Event Handlers
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_F4 and (event.modifiers() & QtCore.Qt.AltModifier):
            print("EventKeyPressed: ALT F4")
            event.ignore()
        if event.key() == QtCore.Qt.Key_Space:
            print("EventKeyPressed: Space")

class Route88_ModifierCore(Ui_Route88_Management_Modifier, Route88_TechnicalCore):
    def __init__(self, Parent=None):
        super(Route88_ModifierCore, self).__init__(Parent=Parent)
        self.setupUi(self)
        self.ModifierCore_RenderExplicitElem()
        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowMaximizeButtonHint | QtCore.Qt.WindowShadeButtonHint)
        self.setWindowIcon(QtGui.QIcon('IcoDisplay/r_88.ico'))


    # Button Binds to Functions
        for SetDisability in range(1, 5):
            self.Tab_SelectionSelectives.setTabEnabled(SetDisability, False)
        
        self.Modifier_CloseWindow.clicked.connect(self.close)
        self.Modifier_AddEntry.clicked.connect(self.ModifierCore_AddEntry)
        self.Modifier_ClearEntry.clicked.connect(self.ModifierCore_ClearEntry)

        self.ModifierCore_RFAR()

    # Staff Action Function Declarations
    def ModifierCore_AddEntry(self):
        try:
            self.MySQL_CursorSet(None)
            QDateGet = self.AddEntry_DateExpiry.date() 
            formattedDate = QDateGet.toPyDate()
            #appendRowLast = self.InventoryTable_View.rowCount()
            if len(self.AddEntry_ItemCode.text()) == 0:
                self.ModifierCore_Status.showMessage('Adding Entry Error: Constraint (> 0 Characters) Not Met @ Item Code Entry.')
                raise Exception('Adding Entry Error: Constraint (> 0 Characters) Not Met @ Item Code Entry.')
            if len(self.AddEntry_SupplierCode.text()) == 0:
                self.ModifierCore_Status.showMessage('Adding Entry Error: Constraint (> 0 Characters) Not Met @ Supplier Code Entry')
                raise Exception('Adding Entry Error: Constraint (> 0 Characters) Not Met @ Supplier Code Entry')
            if len(self.AddEntry_ItemName.text()) < 2:
                self.ModifierCore_Status.showMessage('Adding Entry Error: Constraint (> 2 Characters) Not Met @ Item Name Entry')
                raise Exception('Adding Entry Error: Constraint (> 2 Characters) Not Met @ Item Name Entry')
            if len(self.AddEntry_ItemType.text()) < 2:
                self.ModifierCore_Status.showMessage('Adding Entry Error: Constraint (> 2 Characters) Not Met @ Item Type Entry')
                raise Exception('Adding Entry Error: Constraint (> 2 Characters) Not Met @ Item Type Entry')
            else:
                TargetTable_Param = self.ModifierCore_GetTargetTable()
                print('[Pushing Value to Table @ InventoryList] -> INSERT INTO {} VALUES ({}, {}, {}, {}, {}, {}, {}, {}, {}, {})'.format(TargetTable_Param, self.AddEntry_ItemCode.text(), self.AddEntry_SupplierCode.text(), self.AddEntry_ItemName.text(), self.AddEntry_ItemType.text(), self.AddEntry_Quantity.value(), self.AddEntry_Cost.value(), formattedDate, 1,formattedDate, formattedDate))

                self.MySQLDataWireCursor.execute("INSERT INTO {} VALUES ({}, {}, '{}', '{}', {}, {}, '{}', {}, '{}', '{}')".format(str(TargetTable_Param), str(self.AddEntry_ItemCode.text()), str(self.AddEntry_SupplierCode.text()), str(self.AddEntry_ItemName.text()), str(self.AddEntry_ItemType.text()), str(self.AddEntry_Quantity.value()), str(self.AddEntry_Cost.value()), str(formattedDate), 1,str(formattedDate), str(formattedDate)))
                self.MySQLDataWire.commit()
                self.ModifierCore_Status.showMessage('Success Execution -> Successfully Added to Inventory!')

        
        except (Exception, MySQL.Error, MySQL.OperationalError) as PushEntryErrMsg:
            self.ModifierCore_Status.showMessage('Add Entry Execution Error: Please check your fields!')
            print('[Technical Information @ ModifierCore_AddEntry] -> {}'.format(PushEntryErrMsg))
            QSound.play("SysSounds/LoginFailedNotify.wav")
    
    def ModifierCore_ClearEntry(self):
        if self.Tab_SelectionSelectives.currentIndex() == 0:
            self.AddEntry_ItemCode.clear()
            self.AddEntry_SupplierCode.clear()
            self.AddEntry_ItemName.clear()
            self.AddEntry_ItemType.clear()
            self.AddEntry_Quantity.setValue(0)
            self.AddEntry_Cost.setValue(0.0)
            self.AddEntry_DateExpiry.setDateTime(QtCore.QDateTime.currentDateTime())
            self.ModifierCore_Status.showMessage('Clear Fields @ {} is Finished. Ready!'.format(self.Tab_SelectionSelectives.tabText(self.Tab_SelectionSelectives.currentIndex())))
            print('[Execution @ ModifierCore_ClearEntry] -> Clear Fields @ {} is Finished. Ready!'.format(self.Tab_SelectionSelectives.tabText(self.Tab_SelectionSelectives.currentIndex())))
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
    
        # Technical Functions
    def ModifierCore_RenderExplicitElem(self):
        self.ModifierCore_Status = QtWidgets.QStatusBar()
        self.setStatusBar(self.ModifierCore_Status)
        self.AddEntry_DateExpiry.setDateTime(QtCore.QDateTime.currentDateTime())

    def ModifierCore_RFAR(self):
        self.MySQL_ConnectDatabase(SQL_UCredential='Route_TempUser', SQL_PCredential='123456789',SQLDatabase_Target='route88_inventory')
        self.MySQL_CursorSet(None)

    def GetManagementSys_ItemValue(self):
        pass

    # We use this one to identify which table are we going to push some actions.
    def ModifierCore_GetTargetTable(self):
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
            print('[Exception @ GetManagementSys_ItemValue] -> Selected Candidate does not exist from List of QTabWidgetItem Names')
            raise ValueError('[Exception @ GetManagementSys_ItemValue] -> Selected Candidate does not exist from List of QTabWidgetItem Names')



class Route88_WindowController(object):
    def __init__(self, Parent=None):
        #We cannot select initiate a subclass to variable here. So do manual initialization. Which is a standard as well.
        self.Route88_InventoryInstance = Route88_ManagementCore()

    def WindowSelectionHandler(self, WindowToHide, WindowToShow):
        WindowToHide.hide()
        WindowToShow.show()


    def ShowLoginCore(self):
        self.Route88_LoginInstance = Route88_LoginCore()
        self.Route88_LoginInstance.show()



# Literal Procedural Programming Part
if __name__ == "__main__":
    sysCmdArgumentHandler('CLS') # Clear Output Buffer so we can debug with dignity.
    print('[Application App Startup] Route88_Core Application Version 0, Debug Output')
    app = QtWidgets.QApplication(sys.argv)
    Route88_InstanceController = Route88_WindowController()
    Route88_InstanceController.ShowLoginCore()
    sys.exit(app.exec_())
    #print('[Application Shutdown] Terminating PyQt5 Engine...')