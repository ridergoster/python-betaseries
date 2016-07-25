# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_BetaSeries(object):
    def setupUi(self, BetaSeries):
        BetaSeries.setObjectName(_fromUtf8("BetaSeries"))
        BetaSeries.resize(780, 530)
        BetaSeries.setMinimumSize(QtCore.QSize(780, 530))
        BetaSeries.setMaximumSize(QtCore.QSize(780, 530))
        self.searchTxt = QtGui.QLineEdit(BetaSeries)
        self.searchTxt.setGeometry(QtCore.QRect(80, 90, 501, 21))
        self.searchTxt.setObjectName(_fromUtf8("searchTxt"))
        self.searchBtn = QtGui.QPushButton(BetaSeries)
        self.searchBtn.setGeometry(QtCore.QRect(590, 90, 121, 21))
        self.searchBtn.setObjectName(_fromUtf8("searchBtn"))
        self.loginTxt = QtGui.QLineEdit(BetaSeries)
        self.loginTxt.setGeometry(QtCore.QRect(80, 20, 131, 21))
        self.loginTxt.setText(_fromUtf8(""))
        self.loginTxt.setObjectName(_fromUtf8("loginTxt"))
        self.pwdTxt = QtGui.QLineEdit(BetaSeries)
        self.pwdTxt.setGeometry(QtCore.QRect(220, 20, 151, 21))
        self.pwdTxt.setEchoMode(QtGui.QLineEdit.Password)
        self.pwdTxt.setObjectName(_fromUtf8("pwdTxt"))
        self.loginLabel = QtGui.QLabel(BetaSeries)
        self.loginLabel.setEnabled(True)
        self.loginLabel.setGeometry(QtCore.QRect(80, 60, 371, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.loginLabel.setFont(font)
        self.loginLabel.setText(_fromUtf8(""))
        self.loginLabel.setObjectName(_fromUtf8("loginLabel"))
        self.loginBtn = QtGui.QPushButton(BetaSeries)
        self.loginBtn.setGeometry(QtCore.QRect(590, 20, 121, 21))
        self.loginBtn.setObjectName(_fromUtf8("loginBtn"))
        self.resultList = QtGui.QListWidget(BetaSeries)
        self.resultList.setGeometry(QtCore.QRect(70, 121, 641, 351))
        self.resultList.setObjectName(_fromUtf8("resultList"))
        self.planningBtn = QtGui.QPushButton(BetaSeries)
        self.planningBtn.setGeometry(QtCore.QRect(590, 60, 121, 21))
        self.planningBtn.setObjectName(_fromUtf8("planningBtn"))
        self.showsBtn = QtGui.QPushButton(BetaSeries)
        self.showsBtn.setGeometry(QtCore.QRect(460, 60, 121, 21))
        self.showsBtn.setObjectName(_fromUtf8("showsBtn"))
        self.postBtn = QtGui.QPushButton(BetaSeries)
        self.postBtn.setGeometry(QtCore.QRect(80, 480, 191, 21))
        self.postBtn.setText(_fromUtf8(""))
        self.postBtn.setObjectName(_fromUtf8("postBtn"))
        self.emailTxt = QtGui.QLineEdit(BetaSeries)
        self.emailTxt.setGeometry(QtCore.QRect(380, 20, 201, 21))
        self.emailTxt.setText(_fromUtf8(""))
        self.emailTxt.setObjectName(_fromUtf8("emailTxt"))
        self.postLabel = QtGui.QLabel(BetaSeries)
        self.postLabel.setEnabled(True)
        self.postLabel.setGeometry(QtCore.QRect(280, 480, 431, 20))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.postLabel.setFont(font)
        self.postLabel.setText(_fromUtf8(""))
        self.postLabel.setObjectName(_fromUtf8("postLabel"))

        self.retranslateUi(BetaSeries)
        QtCore.QMetaObject.connectSlotsByName(BetaSeries)

    def retranslateUi(self, BetaSeries):
        BetaSeries.setWindowTitle(_translate("BetaSeries", "BetaSeries Python", None))
        self.searchTxt.setPlaceholderText(_translate("BetaSeries", "Search Show...", None))
        self.searchBtn.setText(_translate("BetaSeries", "Search", None))
        self.loginTxt.setPlaceholderText(_translate("BetaSeries", "Username", None))
        self.pwdTxt.setPlaceholderText(_translate("BetaSeries", "Password", None))
        self.loginBtn.setText(_translate("BetaSeries", "Login-Subscribe", None))
        self.planningBtn.setText(_translate("BetaSeries", "My Planning", None))
        self.showsBtn.setText(_translate("BetaSeries", "My Shows", None))
        self.emailTxt.setPlaceholderText(_translate("BetaSeries", "Email (for subscribe only)", None))

