# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI_Check.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Route88_MainWindow(object):
    def setupUi(self, Route88_MainWindow):
        Route88_MainWindow.setObjectName("Route88_MainWindow")
        Route88_MainWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        Route88_MainWindow.resize(400, 500)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Route88_MainWindow.sizePolicy().hasHeightForWidth())
        Route88_MainWindow.setSizePolicy(sizePolicy)
        Route88_MainWindow.setMinimumSize(QtCore.QSize(400, 500))
        Route88_MainWindow.setMaximumSize(QtCore.QSize(400, 500))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setBold(False)
        font.setWeight(50)
        Route88_MainWindow.setFont(font)
        Route88_MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        Route88_MainWindow.setTabletTracking(False)
        Route88_MainWindow.setToolTip("")
        Route88_MainWindow.setWhatsThis("")
        Route88_MainWindow.setSizeGripEnabled(True)
        Route88_MainWindow.setModal(True)
        self.groupBox = QtWidgets.QGroupBox(Route88_MainWindow)
        self.groupBox.setGeometry(QtCore.QRect(40, 310, 321, 141))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.groupBox)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(70, 40, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.plainTextEdit_2.setFont(font)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.Login_Submit = QtWidgets.QPushButton(self.groupBox)
        self.Login_Submit.setGeometry(QtCore.QRect(70, 90, 101, 31))
        self.Login_Submit.setObjectName("Login_Submit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(200, 90, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.frame = QtWidgets.QFrame(Route88_MainWindow)
        self.frame.setGeometry(QtCore.QRect(-10, 0, 511, 101))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(85, 170, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.frame.setPalette(palette)
        self.frame.setAutoFillBackground(True)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.listWidget = QtWidgets.QListWidget(Route88_MainWindow)
        self.listWidget.setGeometry(QtCore.QRect(40, 130, 321, 161))
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)

        self.retranslateUi(Route88_MainWindow)
        QtCore.QMetaObject.connectSlotsByName(Route88_MainWindow)

    def retranslateUi(self, Route88_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        Route88_MainWindow.setWindowTitle(_translate("Route88_MainWindow", "Route88 System | Login"))
        self.groupBox.setTitle(_translate("Route88_MainWindow", "Credentials"))
        self.Login_Submit.setText(_translate("Route88_MainWindow", "Clear Entry"))
        self.pushButton.setText(_translate("Route88_MainWindow", "Submit Data"))
        self.listWidget.setSortingEnabled(True)
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Route88_MainWindow", "Janrey Licas | Manager"))
        item = self.listWidget.item(1)
        item.setText(_translate("Route88_MainWindow", "root"))
        self.listWidget.setSortingEnabled(__sortingEnabled)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Route88_MainWindow = QtWidgets.QDialog()
    ui = Ui_Route88_MainWindow()
    ui.setupUi(Route88_MainWindow)
    Route88_MainWindow.show()
    sys.exit(app.exec_())
