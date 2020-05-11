# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWinMeanTool.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 798, 23))
        self.menubar.setObjectName("menubar")
        self.menunew = QtWidgets.QMenu(self.menubar)
        self.menunew.setObjectName("menunew")
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionopen = QtWidgets.QAction(MainWindow)
        self.actionopen.setObjectName("actionopen")
        self.actionchose = QtWidgets.QAction(MainWindow)
        self.actionchose.setObjectName("actionchose")
        self.actionclose = QtWidgets.QAction(MainWindow)
        self.actionclose.setObjectName("actionclose")
        self.actionopen_2 = QtWidgets.QAction(MainWindow)
        self.actionopen_2.setObjectName("actionopen_2")
        self.menunew.addAction(self.actionopen)
        self.menunew.addAction(self.actionchose)
        self.menunew.addAction(self.actionclose)
        self.menubar.addAction(self.menunew.menuAction())
        self.toolBar.addAction(self.actionopen)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionchose)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionclose)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menunew.setTitle(_translate("MainWindow", "File"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionopen.setText(_translate("MainWindow", "open"))
        self.actionopen.setToolTip(_translate("MainWindow", "打开新文件"))
        self.actionopen.setShortcut(_translate("MainWindow", "Ctrl+A"))
        self.actionchose.setText(_translate("MainWindow", "chose"))
        self.actionclose.setText(_translate("MainWindow", "close"))
        self.actionopen_2.setText(_translate("MainWindow", "open"))
