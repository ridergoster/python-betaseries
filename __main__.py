from PyQt4 import QtCore, QtGui
import window
import hashlib
import requests
import sys
from __betaseries__ import Show, UserShow

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

    def login(self):
        USER_LOGIN_PARAM = str(self.mailTxt.text())
        m = hashlib.md5()
        m.update(self.pwdTxt.text().toUtf8())
        print m.hexdigest()
        USER_PWD_PARAM = m.hexdigest()
        headers = {'X-BetaSeries-Key': API_KEY_PARAM}
        payload = {'login': USER_LOGIN_PARAM, 'password': USER_PWD_PARAM}
        url = 'https://api.betaseries.com/members/auth'
        r = requests.post(url, params=payload, headers=headers)
        res = r.json()
        if len(res['errors']) > 0:
            error = res['errors'][0]
            msg = "ERROR " + str(error['code']) + ": " + error['text']
        elif len(res['token']) > 0:
            user = res['user']
            TOKEN_PARAM = res['token']
            msg = "Login as " + user['login']
        self.loginLabel.setText(msg)

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
                show = Show().convertJson(show)
                self.resultList.addItem(QtGui.QListWidgetItem(show.displayShow()))

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec_()
