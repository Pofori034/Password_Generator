# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'passwordgen.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(400, 300)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 401, 281))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 40, 241, 171))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.passLine = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.passLine.setObjectName("passLine")
        self.verticalLayout.addWidget(self.passLine)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.generateButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.generateButton.setObjectName("generateButton")
        self.horizontalLayout.addWidget(self.generateButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.password = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.password.setObjectName("password")
        self.verticalLayout.addWidget(self.password)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.copyButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.copyButton.setObjectName("copyButton")
        self.horizontalLayout_2.addWidget(self.copyButton)
        self.filesaveButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.filesaveButton.setObjectName("filesaveButton")
        self.horizontalLayout_2.addWidget(self.filesaveButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 391, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.editaccountButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.editaccountButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.editaccountButton.setObjectName("editaccountButton")
        self.horizontalLayout_3.addWidget(self.editaccountButton)
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 100, 391, 151))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.openURLButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.openURLButton.setObjectName("openURLButton")
        self.gridLayout.addWidget(self.openURLButton, 0, 2, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.copyusernameButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.copyusernameButton.setObjectName("copyusernameButton")
        self.gridLayout.addWidget(self.copyusernameButton, 2, 2, 1, 1)
        self.usernameLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.usernameLine.setObjectName("usernameLine")
        self.gridLayout.addWidget(self.usernameLine, 2, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.websiteURLLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.websiteURLLine.setObjectName("websiteURLLine")
        self.gridLayout.addWidget(self.websiteURLLine, 0, 1, 1, 1)
        self.passwordLine = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.passwordLine.setObjectName("passwordLine")
        self.gridLayout.addWidget(self.passwordLine, 3, 1, 1, 1)
        self.copypasswordButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.copypasswordButton.setObjectName("copypasswordButton")
        self.gridLayout.addWidget(self.copypasswordButton, 3, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        mainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Password Generator"))
        self.label_5.setText(_translate("mainWindow", "Enter length of Password"))
        self.generateButton.setText(_translate("mainWindow", "Generate Password"))
        self.copyButton.setText(_translate("mainWindow", "Copy to Clipboard"))
        self.filesaveButton.setText(_translate("mainWindow", "Copy to File"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("mainWindow", "New Password"))
        self.label.setText(_translate("mainWindow", "Select Type of Account"))
        self.comboBox.setPlaceholderText(_translate("mainWindow", "Select Type of Account"))
        self.editaccountButton.setText(_translate("mainWindow", "Edit"))
        self.openURLButton.setText(_translate("mainWindow", "Open"))
        self.label_3.setText(_translate("mainWindow", "Username or Email:"))
        self.copyusernameButton.setText(_translate("mainWindow", "Copy"))
        self.label_2.setText(_translate("mainWindow", "Website login URL:"))
        self.copypasswordButton.setText(_translate("mainWindow", "Copy"))
        self.label_4.setText(_translate("mainWindow", "Password"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("mainWindow", "Manage Passwords"))
