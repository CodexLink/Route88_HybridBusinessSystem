from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QSound
import MySQLdb
import sys
from Route88_LoginForm import Ui_Route88_LoginWindow

class Route88_CoreClass(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.Route88_LoginWindow = Ui_Route88_LoginWindow()
        self.Route88_LoginWindow.setupUi(self)
        self.RunInstance_OnLoad()
        self.Route88_LoginWindow.UserAcc_Password.returnPressed.connect(self.Route88_LoginWindow.UserAcc_SubmitData.click)
        self.Route88_LoginWindow.UserAcc_SubmitData.clicked.connect(self.R88GUI_DataSubmission)

    def RunInstance_OnLoad(self):
        try:
            currentRow = 0
            self.con = MySQLdb.connect(host='localhost', user='root', passwd='', db='Route88_Staff')
            cur = self.con.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT * FROM Employees")
            rows = cur.fetchall()
            for row in rows:
                self.Route88_LoginWindow.UserAcc_Enlisted.setRowCount(currentRow + 1)
                self.Route88_LoginWindow.UserAcc_Enlisted.setItem(currentRow, 0, QtWidgets.QTableWidgetItem('{0}, {1}'.format(row['lname'], row['fname'])))
                self.Route88_LoginWindow.UserAcc_Enlisted.setItem(currentRow, 1, QtWidgets.QTableWidgetItem(row['JobPosition']))  
                currentRow += 1
        except Exception as Error:
                print(Error)

    def R88GUI_DataSubmission(self):
        try:
            cur = self.con.cursor()
            indexes = self.Route88_LoginWindow.UserAcc_Enlisted.selectionModel().selectedRows()
            for index in sorted(indexes):
                userhandler = cur.execute("SELECT fname, lname FROM Employees WHERE concat(lname, ', ', fname) = %s AND password = %s", (index.data(),self.Route88_LoginWindow.UserAcc_Password.text()))
                if userhandler:
                    self.Route88_LoginWindow.StatusLabel.setText("Success: Login Credentials Matched!")
                    QSound.play("SysSounds/LoginSuccessNotify.wav")
                else:
                    self.Route88_LoginWindow.StatusLabel.setText("Error: Login Credentials is Not Matched! Check your Password!")
                    QSound.play("SysSounds/LoginFailedNotify.wav")

        except Exception as ErrorMessage:
            print(ErrorMessage)
            self.Route88_LoginWindow.StatusLabel.setText(str(ErrorMessage))
            QSound.play("SysSounds/LoginFailedNotify.wav")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Route88_CoreLoad = Route88_CoreClass()
    Route88_CoreLoad.show()
    sys.exit(app.exec_())
