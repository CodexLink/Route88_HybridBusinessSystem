# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Route88_DataViewerCmpnt.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Route88_DataViewer_Window(object):
    def setupUi(self, Route88_DataViewer_Window):
        Route88_DataViewer_Window.setObjectName("Route88_DataViewer_Window")
        Route88_DataViewer_Window.setWindowModality(QtCore.Qt.WindowModal)
        Route88_DataViewer_Window.resize(1137, 416)
        Route88_DataViewer_Window.setMouseTracking(True)
        Route88_DataViewer_Window.setFocusPolicy(QtCore.Qt.NoFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("IcoDisplay/r_88.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Route88_DataViewer_Window.setWindowIcon(icon)
        Route88_DataViewer_Window.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(Route88_DataViewer_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
        self.groupBox_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.TableSystem_Selection = QtWidgets.QComboBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TableSystem_Selection.sizePolicy().hasHeightForWidth())
        self.TableSystem_Selection.setSizePolicy(sizePolicy)
        self.TableSystem_Selection.setObjectName("TableSystem_Selection")
        self.TableSystem_Selection.addItem("")
        self.TableSystem_Selection.addItem("")
        self.TableSystem_Selection.addItem("")
        self.TableSystem_Selection.addItem("")
        self.TableSystem_Selection.addItem("")
        self.TableSystem_Selection.addItem("")
        self.TableSystem_Selection.addItem("")
        self.horizontalLayout_7.addWidget(self.TableSystem_Selection)
        self.horizontalLayout_6.addWidget(self.groupBox_5)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.Query_ColumnOpt = QtWidgets.QComboBox(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Query_ColumnOpt.sizePolicy().hasHeightForWidth())
        self.Query_ColumnOpt.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.Query_ColumnOpt.setFont(font)
        self.Query_ColumnOpt.setStatusTip("")
        self.Query_ColumnOpt.setObjectName("Query_ColumnOpt")
        self.Query_ColumnOpt.addItem("")
        self.Query_ColumnOpt.addItem("")
        self.Query_ColumnOpt.addItem("")
        self.Query_ColumnOpt.addItem("")
        self.Query_ColumnOpt.addItem("")
        self.Query_ColumnOpt.addItem("")
        self.Query_ColumnOpt.addItem("")
        self.Query_ColumnOpt.addItem("")
        self.Query_ColumnOpt.addItem("")
        self.Query_ColumnOpt.addItem("")
        self.Query_ColumnOpt.addItem("")
        self.Query_ColumnOpt.addItem("")
        self.horizontalLayout_2.addWidget(self.Query_ColumnOpt)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.Query_ValueToSearch = QtWidgets.QLineEdit(self.groupBox_3)
        self.Query_ValueToSearch.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Query_ValueToSearch.sizePolicy().hasHeightForWidth())
        self.Query_ValueToSearch.setSizePolicy(sizePolicy)
        self.Query_ValueToSearch.setClearButtonEnabled(True)
        self.Query_ValueToSearch.setObjectName("Query_ValueToSearch")
        self.horizontalLayout_2.addWidget(self.Query_ValueToSearch)
        self.Query_Operator = QtWidgets.QComboBox(self.groupBox_3)
        self.Query_Operator.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Query_Operator.sizePolicy().hasHeightForWidth())
        self.Query_Operator.setSizePolicy(sizePolicy)
        self.Query_Operator.setStatusTip("")
        self.Query_Operator.setObjectName("Query_Operator")
        self.Query_Operator.addItem("")
        self.Query_Operator.addItem("")
        self.Query_Operator.addItem("")
        self.Query_Operator.addItem("")
        self.Query_Operator.addItem("")
        self.Query_Operator.addItem("")
        self.horizontalLayout_2.addWidget(self.Query_Operator)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_6.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.SearchPattern_ExactOpt = QtWidgets.QRadioButton(self.groupBox_4)
        self.SearchPattern_ExactOpt.setEnabled(False)
        self.SearchPattern_ExactOpt.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.SearchPattern_ExactOpt.setFont(font)
        self.SearchPattern_ExactOpt.setChecked(True)
        self.SearchPattern_ExactOpt.setAutoExclusive(True)
        self.SearchPattern_ExactOpt.setObjectName("SearchPattern_ExactOpt")
        self.horizontalLayout_5.addWidget(self.SearchPattern_ExactOpt)
        self.SearchPattern_ContainOpt = QtWidgets.QRadioButton(self.groupBox_4)
        self.SearchPattern_ContainOpt.setEnabled(False)
        self.SearchPattern_ContainOpt.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.SearchPattern_ContainOpt.setFont(font)
        self.SearchPattern_ContainOpt.setObjectName("SearchPattern_ContainOpt")
        self.horizontalLayout_5.addWidget(self.SearchPattern_ContainOpt)
        self.SearchPattern_ComboBox = QtWidgets.QComboBox(self.groupBox_4)
        self.SearchPattern_ComboBox.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SearchPattern_ComboBox.sizePolicy().hasHeightForWidth())
        self.SearchPattern_ComboBox.setSizePolicy(sizePolicy)
        self.SearchPattern_ComboBox.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.SearchPattern_ComboBox.setFont(font)
        self.SearchPattern_ComboBox.setStatusTip("")
        self.SearchPattern_ComboBox.setObjectName("SearchPattern_ComboBox")
        self.SearchPattern_ComboBox.addItem("")
        self.SearchPattern_ComboBox.addItem("")
        self.SearchPattern_ComboBox.addItem("")
        self.horizontalLayout_5.addWidget(self.SearchPattern_ComboBox)
        self.horizontalLayout_6.addWidget(self.groupBox_4)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.InventoryTable_View = QtWidgets.QTableWidget(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(9)
        self.InventoryTable_View.setFont(font)
        self.InventoryTable_View.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.InventoryTable_View.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.InventoryTable_View.setAlternatingRowColors(True)
        self.InventoryTable_View.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.InventoryTable_View.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.InventoryTable_View.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.InventoryTable_View.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.InventoryTable_View.setShowGrid(True)
        self.InventoryTable_View.setGridStyle(QtCore.Qt.DashLine)
        self.InventoryTable_View.setCornerButtonEnabled(False)
        self.InventoryTable_View.setObjectName("InventoryTable_View")
        self.InventoryTable_View.setColumnCount(0)
        self.InventoryTable_View.setRowCount(0)
        self.InventoryTable_View.verticalHeader().setVisible(False)
        self.InventoryTable_View.verticalHeader().setSortIndicatorShown(True)
        self.InventoryTable_View.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout.addWidget(self.InventoryTable_View)
        self.verticalLayout.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Roboto Mono")
        font.setPointSize(10)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.StaffAct_Add = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StaffAct_Add.sizePolicy().hasHeightForWidth())
        self.StaffAct_Add.setSizePolicy(sizePolicy)
        self.StaffAct_Add.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.StaffAct_Add.setFont(font)
        self.StaffAct_Add.setStatusTip("")
        self.StaffAct_Add.setObjectName("StaffAct_Add")
        self.horizontalLayout_4.addWidget(self.StaffAct_Add)
        self.StaffAct_Edit = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StaffAct_Edit.sizePolicy().hasHeightForWidth())
        self.StaffAct_Edit.setSizePolicy(sizePolicy)
        self.StaffAct_Edit.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.StaffAct_Edit.setFont(font)
        self.StaffAct_Edit.setStatusTip("")
        self.StaffAct_Edit.setObjectName("StaffAct_Edit")
        self.horizontalLayout_4.addWidget(self.StaffAct_Edit)
        self.StaffAct_Delete = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StaffAct_Delete.sizePolicy().hasHeightForWidth())
        self.StaffAct_Delete.setSizePolicy(sizePolicy)
        self.StaffAct_Delete.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.StaffAct_Delete.setFont(font)
        self.StaffAct_Delete.setStatusTip("")
        self.StaffAct_Delete.setObjectName("StaffAct_Delete")
        self.horizontalLayout_4.addWidget(self.StaffAct_Delete)
        self.StaffAct_RefreshData = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StaffAct_RefreshData.sizePolicy().hasHeightForWidth())
        self.StaffAct_RefreshData.setSizePolicy(sizePolicy)
        self.StaffAct_RefreshData.setMinimumSize(QtCore.QSize(0, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.StaffAct_RefreshData.setFont(font)
        self.StaffAct_RefreshData.setStatusTip("")
        self.StaffAct_RefreshData.setObjectName("StaffAct_RefreshData")
        self.horizontalLayout_4.addWidget(self.StaffAct_RefreshData)
        self.verticalLayout.addWidget(self.groupBox_2)
        Route88_DataViewer_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Route88_DataViewer_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1137, 21))
        self.menubar.setObjectName("menubar")
        self.menuWindow = QtWidgets.QMenu(self.menubar)
        self.menuWindow.setObjectName("menuWindow")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        Route88_DataViewer_Window.setMenuBar(self.menubar)
        self.About_InfoSystem = QtWidgets.QAction(Route88_DataViewer_Window)
        self.About_InfoSystem.setEnabled(False)
        self.About_InfoSystem.setMenuRole(QtWidgets.QAction.AboutRole)
        self.About_InfoSystem.setObjectName("About_InfoSystem")
        self.Staff_SwitchTo = QtWidgets.QAction(Route88_DataViewer_Window)
        self.Staff_SwitchTo.setObjectName("Staff_SwitchTo")
        self.Staff_Manage = QtWidgets.QAction(Route88_DataViewer_Window)
        self.Staff_Manage.setObjectName("Staff_Manage")
        self.Window_SwitchSystemView = QtWidgets.QAction(Route88_DataViewer_Window)
        self.Window_SwitchSystemView.setMenuRole(QtWidgets.QAction.ApplicationSpecificRole)
        self.Window_SwitchSystemView.setObjectName("Window_SwitchSystemView")
        self.Window_Quit = QtWidgets.QAction(Route88_DataViewer_Window)
        self.Window_Quit.setStatusTip("")
        self.Window_Quit.setShortcutContext(QtCore.Qt.WindowShortcut)
        self.Window_Quit.setMenuRole(QtWidgets.QAction.QuitRole)
        self.Window_Quit.setShortcutVisibleInContextMenu(True)
        self.Window_Quit.setObjectName("Window_Quit")
        self.menuWindow.addAction(self.Window_Quit)
        self.menuAbout.addAction(self.About_InfoSystem)
        self.menubar.addAction(self.menuWindow.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(Route88_DataViewer_Window)
        QtCore.QMetaObject.connectSlotsByName(Route88_DataViewer_Window)

    def retranslateUi(self, Route88_DataViewer_Window):
        _translate = QtCore.QCoreApplication.translate
        Route88_DataViewer_Window.setWindowTitle(_translate("Route88_DataViewer_Window", "Route88 System | Data Management View"))
        self.groupBox_5.setTitle(_translate("Route88_DataViewer_Window", "Data Table Selection"))
        self.TableSystem_Selection.setItemText(0, _translate("Route88_DataViewer_Window", "Inventory Data"))
        self.TableSystem_Selection.setItemText(1, _translate("Route88_DataViewer_Window", "Transaction Item Data"))
        self.TableSystem_Selection.setItemText(2, _translate("Route88_DataViewer_Window", "Supplier Data"))
        self.TableSystem_Selection.setItemText(3, _translate("Route88_DataViewer_Window", "Supplier Transaction Data"))
        self.TableSystem_Selection.setItemText(4, _translate("Route88_DataViewer_Window", "Receipt Data"))
        self.TableSystem_Selection.setItemText(5, _translate("Route88_DataViewer_Window", "Employee Data"))
        self.TableSystem_Selection.setItemText(6, _translate("Route88_DataViewer_Window", "Position Data"))
        self.groupBox_3.setTitle(_translate("Route88_DataViewer_Window", "Search Query"))
        self.label.setText(_translate("Route88_DataViewer_Window", "By"))
        self.Query_ColumnOpt.setCurrentText(_translate("Route88_DataViewer_Window", "None"))
        self.Query_ColumnOpt.setItemText(0, _translate("Route88_DataViewer_Window", "None"))
        self.Query_ColumnOpt.setItemText(1, _translate("Route88_DataViewer_Window", "All Columns"))
        self.Query_ColumnOpt.setItemText(2, _translate("Route88_DataViewer_Window", "Item Code"))
        self.Query_ColumnOpt.setItemText(3, _translate("Route88_DataViewer_Window", "Supplier Code"))
        self.Query_ColumnOpt.setItemText(4, _translate("Route88_DataViewer_Window", "Item Name"))
        self.Query_ColumnOpt.setItemText(5, _translate("Route88_DataViewer_Window", "Type"))
        self.Query_ColumnOpt.setItemText(6, _translate("Route88_DataViewer_Window", "Quantity"))
        self.Query_ColumnOpt.setItemText(7, _translate("Route88_DataViewer_Window", "Cost"))
        self.Query_ColumnOpt.setItemText(8, _translate("Route88_DataViewer_Window", "Expiry Date"))
        self.Query_ColumnOpt.setItemText(9, _translate("Route88_DataViewer_Window", "Menu Inclusion"))
        self.Query_ColumnOpt.setItemText(10, _translate("Route88_DataViewer_Window", "Data Created"))
        self.Query_ColumnOpt.setItemText(11, _translate("Route88_DataViewer_Window", "Last Modified"))
        self.label_2.setText(_translate("Route88_DataViewer_Window", "Look For"))
        self.Query_ValueToSearch.setPlaceholderText(_translate("Route88_DataViewer_Window", "Value Search..."))
        self.Query_Operator.setItemText(0, _translate("Route88_DataViewer_Window", "="))
        self.Query_Operator.setItemText(1, _translate("Route88_DataViewer_Window", "<>"))
        self.Query_Operator.setItemText(2, _translate("Route88_DataViewer_Window", ">"))
        self.Query_Operator.setItemText(3, _translate("Route88_DataViewer_Window", "<"))
        self.Query_Operator.setItemText(4, _translate("Route88_DataViewer_Window", ">="))
        self.Query_Operator.setItemText(5, _translate("Route88_DataViewer_Window", "<="))
        self.groupBox_4.setTitle(_translate("Route88_DataViewer_Window", "Search Patterns"))
        self.SearchPattern_ExactOpt.setText(_translate("Route88_DataViewer_Window", "Exact"))
        self.SearchPattern_ContainOpt.setText(_translate("Route88_DataViewer_Window", "Contains"))
        self.SearchPattern_ComboBox.setItemText(0, _translate("Route88_DataViewer_Window", "Between"))
        self.SearchPattern_ComboBox.setItemText(1, _translate("Route88_DataViewer_Window", "Starting With"))
        self.SearchPattern_ComboBox.setItemText(2, _translate("Route88_DataViewer_Window", "Ends With"))
        self.groupBox.setTitle(_translate("Route88_DataViewer_Window", "Data Table View"))
        self.InventoryTable_View.setSortingEnabled(True)
        self.groupBox_2.setTitle(_translate("Route88_DataViewer_Window", "Staff Actions"))
        self.StaffAct_Add.setText(_translate("Route88_DataViewer_Window", "Add Entry"))
        self.StaffAct_Edit.setText(_translate("Route88_DataViewer_Window", "Edit / Modify Selected Entry"))
        self.StaffAct_Delete.setText(_translate("Route88_DataViewer_Window", "Delete Selected Entry"))
        self.StaffAct_RefreshData.setText(_translate("Route88_DataViewer_Window", "Refresh Database"))
        self.menuWindow.setTitle(_translate("Route88_DataViewer_Window", "System Options"))
        self.menuAbout.setTitle(_translate("Route88_DataViewer_Window", "About"))
        self.About_InfoSystem.setText(_translate("Route88_DataViewer_Window", "About This System..."))
        self.Staff_SwitchTo.setText(_translate("Route88_DataViewer_Window", "Logout / Switch To..."))
        self.Staff_SwitchTo.setStatusTip(_translate("Route88_DataViewer_Window", "Go Back To Login Menu"))
        self.Staff_Manage.setText(_translate("Route88_DataViewer_Window", "Manage Staffs..."))
        self.Staff_Manage.setStatusTip(_translate("Route88_DataViewer_Window", "Manage Staff from the Window."))
        self.Window_SwitchSystemView.setText(_translate("Route88_DataViewer_Window", "Switch System..."))
        self.Window_SwitchSystemView.setStatusTip(_translate("Route88_DataViewer_Window", "Switches Window to a Candidate Window to Switch."))
        self.Window_Quit.setText(_translate("Route88_DataViewer_Window", "Switch System / User..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Route88_DataViewer_Window = QtWidgets.QMainWindow()
    ui = Ui_Route88_DataViewer_Window()
    ui.setupUi(Route88_DataViewer_Window)
    Route88_DataViewer_Window.show()
    sys.exit(app.exec_())
