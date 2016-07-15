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
        BetaSeries.resize(532, 377)
        self.searchTxt = QtGui.QLineEdit(BetaSeries)
        self.searchTxt.setGeometry(QtCore.QRect(20, 90, 341, 21))
        self.searchTxt.setObjectName(_fromUtf8("searchTxt"))
        self.searchBtn = QtGui.QPushButton(BetaSeries)
        self.searchBtn.setGeometry(QtCore.QRect(389, 90, 101, 21))
        self.searchBtn.setObjectName(_fromUtf8("searchBtn"))
        self.mailTxt = QtGui.QLineEdit(BetaSeries)
        self.mailTxt.setGeometry(QtCore.QRect(20, 20, 171, 21))
        self.mailTxt.setObjectName(_fromUtf8("mailTxt"))
        self.pwdTxt = QtGui.QLineEdit(BetaSeries)
        self.pwdTxt.setGeometry(QtCore.QRect(210, 20, 141, 21))
        self.pwdTxt.setEchoMode(QtGui.QLineEdit.Password)
        self.pwdTxt.setObjectName(_fromUtf8("pwdTxt"))
        self.loginLabel = QtGui.QLabel(BetaSeries)
        self.loginLabel.setEnabled(True)
        self.loginLabel.setGeometry(QtCore.QRect(20, 60, 361, 16))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.loginLabel.setFont(font)
        self.loginLabel.setText(_fromUtf8(""))
        self.loginLabel.setObjectName(_fromUtf8("loginLabel"))
        self.loginBtn = QtGui.QPushButton(BetaSeries)
        self.loginBtn.setGeometry(QtCore.QRect(390, 20, 101, 21))
        self.loginBtn.setObjectName(_fromUtf8("loginBtn"))
        self.resultList = QtGui.QListWidget(BetaSeries)
        self.resultList.setGeometry(QtCore.QRect(-5, 121, 541, 281))
        self.resultList.setObjectName(_fromUtf8("resultList"))

        self.retranslateUi(BetaSeries)
        QtCore.QMetaObject.connectSlotsByName(BetaSeries)

    def retranslateUi(self, BetaSeries):
        BetaSeries.setWindowTitle(_translate("BetaSeries", "Dialog", None))
        self.searchBtn.setText(_translate("BetaSeries", "Search", None))
        self.loginBtn.setText(_translate("BetaSeries", "Login", None))

