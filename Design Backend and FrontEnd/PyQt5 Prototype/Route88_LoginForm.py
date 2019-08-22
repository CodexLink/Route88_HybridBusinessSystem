# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Route88_LoginForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtMultimedia import QSound
import MySQLdb

class Ui_Route88_LoginWindow(QtWidgets.QMainWindow):
    def setupUi(self, Route88_LoginWindow):
        Route88_LoginWindow.setObjectName("Route88_LoginWindow")
        self.setWindowFlags(QtCore.Qt.WindowCloseButtonHint | QtCore.Qt.MSWindowsFixedSizeDialogHint)
        Route88_LoginWindow.setFixedSize(430, 420)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setBold(False)
        font.setWeight(50)
        Route88_LoginWindow.setFont(font)
        Route88_LoginWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Route88_LoginWindow.setTabletTracking(False)
        Route88_LoginWindow.setWindowTitle("Route88 System | Login")
        Route88_LoginWindow.setSizeGripEnabled(True)
        Route88_LoginWindow.setModal(True)
        self.GroupContainer_PassCred = QtWidgets.QGroupBox(Route88_LoginWindow)
        self.GroupContainer_PassCred.setGeometry(
            QtCore.QRect(30, 320, 361, 51))

        self.GroupContainer_PassCred.setFlat(False)
        self.GroupContainer_PassCred.setObjectName("GroupContainer_PassCred")
        self.UserAcc_Password = QtWidgets.QLineEdit(
            self.GroupContainer_PassCred)
        self.UserAcc_Password.setGeometry(QtCore.QRect(0, 20, 241, 31))
        self.UserAcc_Password.setInputMask("")
        self.UserAcc_Password.setMaxLength(50)
        self.UserAcc_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.UserAcc_Password.setClearButtonEnabled(True)
        self.UserAcc_Password.setObjectName("UserAcc_Password")
        self.UserAcc_SubmitData = QtWidgets.QPushButton(
            self.GroupContainer_PassCred)
        self.UserAcc_SubmitData.setGeometry(QtCore.QRect(260, 20, 101, 31))
        self.UserAcc_SubmitData.setObjectName("UserAcc_SubmitData")
        self.UserAcc_SubmitData.clicked.connect(self.R88GUI_DataSubmission)
        self.GroupContainer_StaffAccount = QtWidgets.QGroupBox(
            Route88_LoginWindow)
        self.GroupContainer_StaffAccount.setGeometry(
            QtCore.QRect(30, 120, 361, 181))
        self.GroupContainer_StaffAccount.setObjectName(
            "GroupContainer_StaffAccount")
        self.UserAcc_Enlisted = QtWidgets.QTableWidget(
            self.GroupContainer_StaffAccount)
        self.UserAcc_Enlisted.setGeometry(QtCore.QRect(0, 20, 361, 161))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.UserAcc_Enlisted.sizePolicy().hasHeightForWidth())
        self.UserAcc_Enlisted.setSizePolicy(sizePolicy)
        self.UserAcc_Enlisted.setMinimumSize(QtCore.QSize(321, 161))
        self.UserAcc_Enlisted.setMaximumSize(QtCore.QSize(361, 161))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.UserAcc_Enlisted.setFont(font)
        self.UserAcc_Enlisted.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.UserAcc_Enlisted.setWhatsThis("")
        self.UserAcc_Enlisted.setLineWidth(0)
        self.UserAcc_Enlisted.setMidLineWidth(0)
        self.UserAcc_Enlisted.setSizeAdjustPolicy(
            QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.UserAcc_Enlisted.setEditTriggers(
            QtWidgets.QAbstractItemView.AnyKeyPressed)
        self.UserAcc_Enlisted.setDragDropOverwriteMode(False)
        self.UserAcc_Enlisted.setAlternatingRowColors(True)
        self.UserAcc_Enlisted.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.UserAcc_Enlisted.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.UserAcc_Enlisted.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.UserAcc_Enlisted.setVerticalScrollMode(
            QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.UserAcc_Enlisted.setHorizontalScrollMode(
            QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.UserAcc_Enlisted.setGridStyle(QtCore.Qt.DashLine)
        self.UserAcc_Enlisted.setWordWrap(True)
        self.UserAcc_Enlisted.setObjectName("UserAcc_Enlisted")
        self.UserAcc_Enlisted.setColumnCount(2)
        self.UserAcc_Enlisted.setRowCount(2)
        item = QtWidgets.QTableWidgetItem()
        self.UserAcc_Enlisted.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.UserAcc_Enlisted.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.UserAcc_Enlisted.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.UserAcc_Enlisted.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.UserAcc_Enlisted.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.UserAcc_Enlisted.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.UserAcc_Enlisted.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.UserAcc_Enlisted.setItem(1, 1, item)
        self.UserAcc_Enlisted.horizontalHeader().setVisible(True)
        self.UserAcc_Enlisted.horizontalHeader().setCascadingSectionResizes(True)
        self.UserAcc_Enlisted.horizontalHeader().setHighlightSections(True)
        self.UserAcc_Enlisted.horizontalHeader().setSortIndicatorShown(True)
        self.UserAcc_Enlisted.horizontalHeader().setStretchLastSection(True)
        self.UserAcc_Enlisted.horizontalHeader().setSectionResizeMode(
            0, QtWidgets.QHeaderView.Stretch)
        self.UserAcc_Enlisted.horizontalHeader().setSectionResizeMode(
            1, QtWidgets.QHeaderView.ResizeToContents)
        self.UserAcc_Enlisted.verticalHeader().setVisible(True)
        self.UserAcc_Enlisted.verticalHeader().setCascadingSectionResizes(True)
        self.UserAcc_Enlisted.verticalHeader().setSortIndicatorShown(True)
        self.UserAcc_Enlisted.verticalHeader().setStretchLastSection(False)
        self.frame = QtWidgets.QFrame(Route88_LoginWindow)
        self.frame.setGeometry(QtCore.QRect(0, 0, 431, 101))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(401, 101))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.NoRole, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.NoRole, brush)
        self.frame.setPalette(palette)
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(120, 30, 241, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(113, 60, 201, 18))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(20, 20, 71, 71))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap(
            "../../Design Component Experimentations/PyQt5 Design Attempt/r_88.ico"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(1, 1, 2, 2))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(
            self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.StatusLabel = QtWidgets.QLabel(Route88_LoginWindow)
        self.StatusLabel.setGeometry(QtCore.QRect(10, 389, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.StatusLabel.setFont(font)
        self.StatusLabel.setObjectName("StatusLabel")
        self.GroupContainer_StaffAccount.raise_()
        self.GroupContainer_PassCred.raise_()
        self.frame.raise_()
        self.StatusLabel.raise_()

        self.retranslateUi(Route88_LoginWindow)
        QtCore.QMetaObject.connectSlotsByName(Route88_LoginWindow)
        Route88_LoginWindow.setTabOrder(
            self.UserAcc_Password, self.UserAcc_SubmitData)
        self.RunInstance_OnLoad() # After GUI Processing, Run Functions that is needed to run for loading data, specifically for Table Data Initialization with Database.

    def retranslateUi(self, Route88_LoginWindow):
        _translate = QtCore.QCoreApplication.translate
        self.GroupContainer_PassCred.setTitle(_translate(
            "Route88_LoginWindow", "Password Credentials"))
        self.UserAcc_SubmitData.setText(
            _translate("Route88_LoginWindow", "Submit Data"))
        self.GroupContainer_StaffAccount.setTitle(
            _translate("Route88_LoginWindow", "Select Staff Account"))
        self.UserAcc_Enlisted.setSortingEnabled(True)
        item = self.UserAcc_Enlisted.verticalHeaderItem(0)
        item.setText(_translate("Route88_LoginWindow", "1"))
        item = self.UserAcc_Enlisted.verticalHeaderItem(1)
        item.setText(_translate("Route88_LoginWindow", "2"))
        item = self.UserAcc_Enlisted.horizontalHeaderItem(0)
        item.setText(_translate("Route88_LoginWindow", "Staff Name"))
        item = self.UserAcc_Enlisted.horizontalHeaderItem(1)
        item.setText(_translate("Route88_LoginWindow", "Staff Job Position"))
        __sortingEnabled = self.UserAcc_Enlisted.isSortingEnabled()
        self.UserAcc_Enlisted.setSortingEnabled(False)
        item = self.UserAcc_Enlisted.item(0, 0)
        item.setText(_translate("Route88_LoginWindow", "root"))
        item = self.UserAcc_Enlisted.item(0, 1)
        item.setText(_translate("Route88_LoginWindow", "Database User"))
        item = self.UserAcc_Enlisted.item(1, 0)
        item.setText(_translate("Route88_LoginWindow",
                                "Charles Ian Mascarenas"))
        item = self.UserAcc_Enlisted.item(1, 1)
        item.setText(_translate("Route88_LoginWindow", "Database Designer"))
        self.UserAcc_Enlisted.setSortingEnabled(__sortingEnabled)
        self.label.setText(_translate(
            "Route88_LoginWindow", "Route88 Bike Cafe"))
        self.label_2.setText(_translate(
            "Route88_LoginWindow", " POS and Inventory System"))
        self.StatusLabel.setText("Unknown: No Submission Detected.")

    def RunInstance_OnLoad(self):
        try:
            currentRow = 0
            self.con = MySQLdb.connect(host='localhost', user='root', passwd='', db='Route88_Staff')
            cur = self.con.cursor(MySQLdb.cursors.DictCursor)
            cur.execute("SELECT * FROM Employees")
            rows = cur.fetchall()
            for row in rows:
                self.UserAcc_Enlisted.setRowCount(currentRow + 1)
                self.UserAcc_Enlisted.setItem(currentRow, 0, QtWidgets.QTableWidgetItem('{0}, {1}'.format(row['lname'], row['fname'])))
                self.UserAcc_Enlisted.setItem(currentRow, 1, QtWidgets.QTableWidgetItem(row['JobPosition']))  
                currentRow += 1
        except Exception as Error:
                print(Error)

    def R88GUI_DataSubmission(self):
        try:
            cur = self.con.cursor()
            cur.execute("SELECT concat(lname, ', ', fname) As FullName FROM Employees")
            rows = cur.fetchall()
            indexes = self.UserAcc_Enlisted.selectionModel().selectedRows()
            for index in sorted(indexes):
                userhandler = cur.execute("SELECT fname, lname FROM Employees WHERE concat(lname, ', ', fname) = '{0}' AND password = '{1}'".format(str(index.data()),self.UserAcc_Password.text()))
                
                if userhandler == 1:
                    self.StatusLabel.setText("Success: Login Credentials Matched!")
                    QSound.play("SysSounds/LoginSuccessNotify.wav")
                else:
                    self.StatusLabel.setText("Error: Login Credentials is Not Matched! Check your Password!")
                    QSound.play("SysSounds/LoginFailedNotify.wav")

        except Exception as ErrorMessage:
            print(ErrorMessage)
            self.StatusLabel.setText(str(ErrorMessage))
            QSound.play("SysSounds/LoginFailedNotify.wav")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Route88_LoginWindow = QtWidgets.QDialog()
    ui = Ui_Route88_LoginWindow()
    ui.setupUi(Route88_LoginWindow)
    Route88_LoginWindow.show()
    sys.exit(app.exec_())
