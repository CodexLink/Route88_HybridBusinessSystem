from PyQt5 import QtGui,QtCore
import sys


class MainWindow(QtGui.QMainWindow):
    
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)

        self.bt = QtGui.QPushButton('crash')
        self.lbl = QtGui.QLabel('count')

        self.cnt = 0
        self.running = False

        self.bt.clicked.connect(self.count) # new style signal/slot connection

        # http://doc.qt.nokia.com/4.7-snapshot/qmainwindow.html#statusBar
        self.statusBar().showMessage("System Status | Normal") 

        #Layout
        vert_layout = QtGui.QHBoxLayout()
        vert_layout.addWidget(self.bt)
        self.main_widget = QtGui.QWidget(self)
        self.main_widget.setLayout(vert_layout)
        self.setCentralWidget(self.main_widget)

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.count)
        # check every second
        self.timer.start(1000*1)


    def count(self):
        a = open("connection_cpu.txt", "r").read()
        if a == "CPU Overclocked":
            abnormal_label = QtGui.QLabel("System Status | Normal")  
            abnormal_label.setStyleSheet(' QLabel {color: red}')
            self.statusBar().addWidget(abnormal_label)
            self.repaint()
        else:
            normal_label = QtGui.QLabel("System Status | Normal")
            self.statusBar().addWidget(normal_label)
            self.repaint()