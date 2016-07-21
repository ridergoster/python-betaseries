from PyQt4 import QtCore, QtGui
import window
import hashlib
import requests
import sys
from __betaseries__ import Show, UserLogin, UserShow

API_KEY_PARAM    = '26f734f5598b';
USER_LOGIN_PARAM = "";
USER_PWD_PARAM   = "";
TOKEN_PARAM      = "";

class MainWindow(QtGui.QDialog, window.Ui_BetaSeries):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.searchBtn.clicked.connect(self.searchShow)
        self.loginBtn.clicked.connect(self.login)
        user = UserLogin()
        user.reading()
        if user.id > 0:
            self.loadUser(user)

    def loadUser(self, user):
        self.mailTxt.setText(user.login)
        self.pwdTxt.setText(user.password)
        msg = self.connexion(user)
        self.loginLabel.setText(msg)

    def login(self):
        user = UserLogin()
        user.login = str(self.mailTxt.text())
        m = hashlib.md5()
        m.update(str(self.pwdTxt.text()))
        user.password = m.hexdigest()
        msg = self.connexion(user)
        self.loginLabel.setText(msg)

    def connexion(self, user):
        USER_LOGIN_PARAM = user.login
        USER_PWD_PARAM = user.password
        if len(user.token) > 0:
            TOKEN_PARAM = user.token
            return 'Login as: ' + user.login
        else:
            headers = {'X-BetaSeries-Key': API_KEY_PARAM}
            payload = {'login': USER_LOGIN_PARAM, 'password': USER_PWD_PARAM}
            url = 'https://api.betaseries.com/members/auth'
            r = requests.post(url, params=payload, headers=headers)
            res = r.json()
            if len(res['errors']) > 0:
                return res['errors'][0]['text']
            else:
                newUser = UserLogin().convertDict(res)
                newUser.password = user.password
                newUser.writing()
                return 'Login as: ' + newUser.login

    def searchShow(self):
        txt = str(self.searchTxt.text())
        if len(txt) > 0:
            payload = {'title': txt}
            url = 'https://api.betaseries.com/shows/search'
            headers = {'X-BetaSeries-Key': API_KEY_PARAM}
            r = requests.get(url, params=payload, headers=headers)
            res = r.json()
            print r.json()
            while self.resultList.count() > 0:
                self.resultList.takeItem(0)
            for show in res['shows']:
                show = Show().convertDict(show)
                self.resultList.addItem(QtGui.QListWidgetItem(show.displayShow()))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec_()
