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
'''

from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from PyQt5.QtMultimedia import QSound
import MySQLdb as MySQL
import sys
from Route88_LoginForm import Ui_Route88_LoginWindow
from Route88_InventorySystem import Ui_Route88_InventorySystemView 
#from Route88_POSSystem import ???

# This class contains all technical function that would be used by these multiple class of multiple window.
class Route88_TechnicalCore(object):
    def __init__(self, Parent=None):
        super().__init__()

    # MySQL Mainstream Functions, Functions That Requires Calling MySQLdb Library
    # Initialize MySQL Server Twice, One for Login and Last.... ???
    def MySQL_ConnectDatabase(self, HostServerIP='localhost', SQL_UCredentials='root', SQL_PCredential='', SQLDatabase_Target='Route88_Staff'):
        try:
            self.MySQLDataWire = MySQL.connect(host=HostServerIP, user=SQL_UCredentials, passwd=SQL_PCredential, db=SQLDatabase_Target)
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
        self.MySQL_ConnectDatabase()
        self.MySQL_CursorSet(MySQL.cursors.DictCursor)
        self.LoginForm_RunFuncAfterRender("Route88_LoginForm")
    # Technical Functions
    # Load Function After UI Rendering.
    def LoginForm_RunFuncAfterRender(self, WindowUI_Name):
        try:
            if WindowUI_Name == 'Route88_LoginForm':
                self.LoginForm_ParseUserEnlisted()
        except Exception as ErrorHandler:
            print(ErrorHandler)

    #Route88_LoginForm UI Window Functions - StartPoint
    def LoginForm_ParseUserEnlisted(self):
        try:
            currentRow = 0
            self.MySQL_CursorSet(MySQL.cursors.DictCursor)
            self.MySQLDataWireCursor.execute("SELECT * FROM Employees")
            UserDataTable = self.MySQLDataWireCursor.fetchall()

            for UserData in UserDataTable:
                self.UserAcc_Enlisted.setRowCount(currentRow + 1)
                self.UserAcc_Enlisted.setItem(currentRow, 0, QtWidgets.QTableWidgetItem('{0}, {1}'.format(UserData['lname'], UserData['fname'])))
                self.UserColumn_1 = self.UserAcc_Enlisted.item(currentRow, 0)
                self.UserColumn_1.setTextAlignment(QtCore.Qt.AlignCenter)
                self.UserAcc_Enlisted.setItem(currentRow, 1, QtWidgets.QTableWidgetItem(UserData['JobPosition']))
                self.UserColumn_2 = self.UserAcc_Enlisted.item(currentRow, 1)
                self.UserColumn_2.setTextAlignment(QtCore.Qt.AlignCenter)
                currentRow += 1

            self.StatusLabel.setText("Database Loaded: Ready!")

        except MySQL.OperationalError as LoginQueryErrorMsg:
            print('MySQL.OperationalError -> {0}'.format(str(LoginQueryErrorMsg)))
            self.StatusLabel.setText("Database Error: Failed to Load User Data. Please restart the program.")

    def LoginForm_DataSubmission(self):
        try:
            self.MySQL_CursorSet(None)
            RowIndexSelected = self.UserAcc_Enlisted.selectionModel().selectedRows()
            for RowIndexQuery in sorted(RowIndexSelected):
                QueryReturn = self.MySQLDataWireCursor.execute("SELECT fname, lname FROM Employees WHERE concat(lname, ', ', fname) = %s AND password = %s", (
                    RowIndexQuery.data(), self.UserAcc_Password.text()))
                # After query we need to check if QueryReturn contains non-zero values. If it contains non-zero we proceed. Else not...

                # We need to store the credentials that is equalled to what we expect.
                if QueryReturn:
                    self.StatusLabel.setText("Login Success: Credential Input Matched!")
                    QSound.play("SysSounds/LoginSuccessNotify.wav")
                    QtTest.QTest.qWait(1500)
                    self.StatusLabel.setText("Successfully Logged in as ...".format("Unknown User..."))
                    QtTest.QTest.qWait(1500)
                    self.MySQLDataWire.close() # Reconnect to Anothe SQ: Usage with Specific User Parameters
                    self.close()
                    self.InventorySys_Init()

                else:
                    self.StatusLabel.setText("Login Error: Credential Input Not Matched! Check your Password!")
                    QSound.play("SysSounds/LoginFailedNotify.wav")

        except Exception as LoginSubmissionErrorMsg:
            print(LoginSubmissionErrorMsg)
            self.StatusLabel.setText(str(LoginSubmissionErrorMsg))
            QSound.play("SysSounds/LoginFailedNotify.wav")
    # Route88_LoginForm UI Window Functions - EndPoint





'''
class Route88_InventoryCore(QtWidgets.QMainWindow, Route88_TechnicalCore):
    def __init__(self):
        super().__init__()
        self.Route88_LoginWindow = Ui_Route88_LoginWindow()
        self.Route88_LoginWindow.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('IcoDisplay/r_88.ico'))

        self.setWindowFlags(QtCore.Qt.Dialog | QtCore.Qt.WindowTitleHint | QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowMinimizeButtonHint | QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.WindowShadeButtonHint | QtCore.Qt.WindowStaysOnTopHint | QtCore.Qt.CustomizeWindowHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        # Button Binds for Window 'Route88_LoginForm'
        self.Route88_LoginWindow.UserAcc_Password.returnPressed.connect(self.Route88_LoginWindow.UserAcc_SubmitData.click)
        self.Route88_LoginWindow.UserAcc_SubmitData.clicked.connect(self.LoginForm_DataSubmission)
        #Run The Following Functions for Initializing User Data @ Window 'Route88_LoginForm'
        #self.MySQL_ConnectDatabase()
        #self.MySQL_CursorSet(MySQL.cursors.DictCursor)
        #self.LoginForm_RunFuncAfterRender("Route88_LoginForm")
    #Function Definitions for Route88_InventoryDesign
    def InventorySys_Init(self):
        super().__init__()
        self.Route88_InventorySystemView = Ui_Route88_InventorySystemView()
        self.Route88_InventorySystemView.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('IcoDisplay/r_88.ico'))
        self.Route88_InventorySystemView.show()

        # Button Binds for Window 'Route88_InventoryDesign'
        #self.Route88_LoginWindow.UserAcc_Password.returnPressed.connect(self.Route88_LoginWindow.UserAcc_SubmitData.click)
        #self.Route88_LoginWindow.UserAcc_SubmitData.clicked.connect(self.LoginForm_DataSubmission)
        #Run The Following Functions for Initializing User Data @ Window 'Route88_InventoryDesign'
        self.MySQL_ConnectDatabase()
        self.MySQL_CursorSet(MySQL.cursors.DictCursor)
        self.LoginForm_RunFuncAfterRender("")
'''

# Literal Procedural Programming Part
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Route88_Instance = Route88_LoginCore()
    Route88_Instance.show()
    sys.exit(app.exec_())