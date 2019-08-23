from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QSound
import MySQLdb as MySQL
import sys
from Route88_LoginForm import Ui_Route88_LoginWindow

class Route88_CoreClass(QtWidgets.QMainWindow):

    def __init__(self):
        super().__init__()
        self.MySQL_ConnectDatabase()
        self.Route88_LoginWindow = Ui_Route88_LoginWindow()
        self.Route88_LoginWindow.setupUi(self)
        self.RunFunction_AfterRender("Route88_LoginForm")
        self.Route88_LoginWindow.UserAcc_Password.returnPressed.connect(
            self.Route88_LoginWindow.UserAcc_SubmitData.click)
        self.Route88_LoginWindow.UserAcc_SubmitData.clicked.connect(
            self.LoginForm_DataSubmission)

    # Load Function After UI Rendering.
    def RunFunction_AfterRender(self, WindowUI_Name):
        try:
            currentRow = 0
            self.con = MySQL.connect(
                host='localhost', user='root', passwd='', db='Route88_Staff')
            cur = self.con.cursor(MySQL.cursors.DictCursor)
            cur.execute("SELECT * FROM Employees")
            rows = cur.fetchall()
            for row in rows:
                self.Route88_LoginWindow.UserAcc_Enlisted.setRowCount(
                    currentRow + 1)
                self.Route88_LoginWindow.UserAcc_Enlisted.setItem(
                    currentRow, 0, QtWidgets.QTableWidgetItem('{0}, {1}'.format(row['lname'], row['fname'])))
                self.Route88_LoginWindow.UserAcc_Enlisted.setItem(
                    currentRow, 1, QtWidgets.QTableWidgetItem(row['JobPosition']))
                currentRow += 1

        except (Exception, MySQL.OperationalError) as Error:
            self.Route88_LoginWindow.StatusLabel.setText(str(Error))
            print('MySQL.OperationalError -> {0}'.format(str(Error)))

    def LoginForm_DataSubmission(self):
        try:
            cur = self.con.cursor()
            indexes = self.Route88_LoginWindow.UserAcc_Enlisted.selectionModel().selectedRows()
            for index in sorted(indexes):
                QueryReturn = cur.execute("SELECT fname, lname FROM Employees WHERE concat(lname, ', ', fname) = %s AND password = %s", (
                    index.data(), self.Route88_LoginWindow.UserAcc_Password.text()))
                if QueryReturn:
                    self.Route88_LoginWindow.StatusLabel.setText(
                        "Success: Login Credentials Matched!")
                    QSound.play("SysSounds/LoginSuccessNotify.wav")
                else:
                    self.Route88_LoginWindow.StatusLabel.setText(
                        "Error: Login Credentials is Not Matched! Check your Password!")
                    QSound.play("SysSounds/LoginFailedNotify.wav")
        except Exception as ErrorMessage:
            print(ErrorMessage)
            self.Route88_LoginWindow.StatusLabel.setText(str(ErrorMessage))
            QSound.play("SysSounds/LoginFailedNotify.wav")

    # MySQL-Related Functions
    def LoginForm_ReadData(self):
        try:
            currentRow = 0
            self.MySQL_ConnectDatabase()
            cur = self.MySQLDataWire.cursor(MySQL.cursors.DictCursor)
            cur.execute("SELECT * FROM Employees")
            rows = cur.fetchall()
            for row in rows:
                self.Route88_LoginWindow.UserAcc_Enlisted.setRowCount(currentRow + 1)
                self.Route88_LoginWindow.UserAcc_Enlisted.setItem(currentRow, 0, QtWidgets.QTableWidgetItem('{0}, {1}'.format(row['lname'], row['fname'])))
                self.Route88_LoginWindow.UserAcc_Enlisted.setItem(currentRow, 1, QtWidgets.QTableWidgetItem(row['JobPosition']))
                currentRow += 1
        except (Exception, MySQL.OperationalError) as Error:
            self.Route88_LoginWindow.StatusLabel.setText(str(Error))
            print('MySQL.OperationalError -> {0}'.format(str(Error)))

    def MySQL_ConnectDatabase(self, HostServerIP='localhost', UserName='root', Password='', Database_Target='Route88_Staff'):
        self.MySQLDataWire = MySQL.connect(host=HostServerIP, user=UserName, passwd=Password, db=Database_Target)

    def MySQL_CursorSet(self):
        pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Route88_CoreLoad = Route88_CoreClass()
    Route88_CoreLoad.show()
    sys.exit(app.exec_())
