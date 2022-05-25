# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/view/ui_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 600)
        MainWindow.setMinimumSize(QtCore.QSize(400, 600))
        MainWindow.setMaximumSize(QtCore.QSize(400, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.lw_notification = QtWidgets.QListWidget(self.centralwidget)
        self.lw_notification.setDefaultDropAction(QtCore.Qt.CopyAction)
        self.lw_notification.setAlternatingRowColors(True)
        self.lw_notification.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.lw_notification.setProperty("isWrapping", True)
        self.lw_notification.setObjectName("lw_notification")
        self.gridLayout.addWidget(self.lw_notification, 2, 0, 1, 1)
        self.le_ip = QtWidgets.QLineEdit(self.centralwidget)
        self.le_ip.setAlignment(QtCore.Qt.AlignCenter)
        self.le_ip.setObjectName("le_ip")
        self.gridLayout.addWidget(self.le_ip, 0, 0, 1, 1)
        self.sb_port = QtWidgets.QSpinBox(self.centralwidget)
        self.sb_port.setAlignment(QtCore.Qt.AlignCenter)
        self.sb_port.setAccelerated(True)
        self.sb_port.setMinimum(3505)
        self.sb_port.setMaximum(19600)
        self.sb_port.setObjectName("sb_port")
        self.gridLayout.addWidget(self.sb_port, 1, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_start = QtWidgets.QPushButton(self.centralwidget)
        self.btn_start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_start.setObjectName("btn_start")
        self.horizontalLayout.addWidget(self.btn_start)
        self.btn_stop = QtWidgets.QPushButton(self.centralwidget)
        self.btn_stop.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_stop.setObjectName("btn_stop")
        self.horizontalLayout.addWidget(self.btn_stop)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 22))
        self.menubar.setObjectName("menubar")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionAbout_author = QtWidgets.QAction(MainWindow)
        self.actionAbout_author.setObjectName("actionAbout_author")
        self.actionAbout_application = QtWidgets.QAction(MainWindow)
        self.actionAbout_application.setObjectName("actionAbout_application")
        self.menuAbout.addAction(self.actionAbout_author)
        self.menuAbout.addAction(self.actionAbout_application)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Modbus Server"))
        MainWindow.setStatusTip(_translate("MainWindow", "Ready ..."))
        self.lw_notification.setStatusTip(_translate("MainWindow", "Notification"))
        self.le_ip.setStatusTip(_translate("MainWindow", "Enter IP address"))
        self.le_ip.setText(_translate("MainWindow", "127.0.0.1"))
        self.le_ip.setPlaceholderText(_translate("MainWindow", "Enter IP address"))
        self.btn_start.setStatusTip(_translate("MainWindow", "Start server"))
        self.btn_start.setText(_translate("MainWindow", "Start"))
        self.btn_stop.setStatusTip(_translate("MainWindow", "Stop server"))
        self.btn_stop.setText(_translate("MainWindow", "Stop"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionAbout_author.setText(_translate("MainWindow", "About author"))
        self.actionAbout_application.setText(_translate("MainWindow", "About application"))
