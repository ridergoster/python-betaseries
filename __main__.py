from PyQt4 import QtCore, QtGui
import window
import hashlib
import sys
from __betaseries__ import Show, UserLogin, UserShow, Episode
from __betaseriesAPI__ import BetaSeriesAPI

API_KEY_PARAM    = '26f734f5598b'

class MainWindow(QtGui.QDialog, window.Ui_BetaSeries):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.searchBtn.clicked.connect(self.searchShow)
        self.loginBtn.clicked.connect(self.login)
        self.planningBtn.clicked.connect(self.searchPlanning)
        self.showsBtn.clicked.connect(self.searchCollectionShow)
        self.postBtn.clicked.connect(self.postAction)
        self.isLogged = False
        self.shows = []
        self.episodes = []
        user = UserLogin()
        user.reading()
        if user.id > 0:
            self.isLogged = True
            self.loginTxt.setText(user.login)
            self.pwdTxt.setText(user.password)
            self.API = BetaSeriesAPI(API_KEY_PARAM, user.token)
            self.loginLabel.setText('Login as: ' + user.login)
        else:
            self.API = BetaSeriesAPI(API_KEY_PARAM)

    def login(self):
        self.isLogged = False
        user = UserLogin()
        user.login = str(self.loginTxt.text())
        m = hashlib.md5()
        m.update(str(self.pwdTxt.text()))
        user.password = m.hexdigest()
        email = str(self.emailTxt.text())
        if len(email) > 0:
            request = self.API.subscribe(user.login, user.password, email)
        else:
            request = self.API.login(user.login, user.password)
        if len(request['errors']) > 0:
            msg = request['errors'][0]['text']
            print msg
        else:
            self.isLogged = True
            newUser = UserLogin().convertDict(request)
            newUser.password = user.password
            newUser.writing()
            self.API.setAccessToken(newUser.token)
            if len(email) > 0:
                msg = 'Login as new user: ' + newUser.login
            else:
                msg = 'Login as: ' + newUser.login
        self.loginLabel.setText(msg)

    def searchShow(self):
        txt = str(self.searchTxt.text())
        if len(txt) < 1:
            return
        request = self.API.getShows(txt)
        if len(request['errors']) > 0:
            msg = request['errors'][0]['text']
            self.loginLabel.setText(msg)
        else:
            self.cleanTable()
            for show in request['shows']:
                show = Show().convertDict(show)
                self.shows.append(show)
                self.resultList.addItem(QtGui.QListWidgetItem(show.display()))
            self.postBtn.setText("Add show to Collection")

    def searchCollectionShow(self):
        if self.isLogged == False:
            return
        request = self.API.getMemberInformation()
        if len(request['errors']) > 0:
            msg = request['errors'][0]['text']
            self.loginLabel.setText(msg)
        else:
            self.cleanTable()
            for show in request['member']['shows']:
                show = Show().convertDict(show)
                self.resultList.addItem(QtGui.QListWidgetItem(show.display()))
            self.postBtn.setText("")

    def searchPlanning(self):
        if self.isLogged == False:
            return
        request = self.API.getEpisodes()
        if len(request['errors']) > 0:
            msg = request['errors'][0]['text']
            self.loginLabel.setText(msg)
        else:
            self.cleanTable()
            for show in request['shows']:
                i = 0
                for episode in show['unseen']:
                    i += 1
                    episode = Episode().convertDict(episode)
                    self.episodes.append(episode)
                    self.resultList.addItem(QtGui.QListWidgetItem(episode.display()))
                    if i == 10:
                        break
            self.postBtn.setText("Check episode as seen")

    def postAction(self):
        if len(self.shows) > 0 and self.resultList.currentRow() > -1:
            self.postShow(self.resultList.currentRow())
            self.searchShow()
        elif len(self.episodes) > 0 and self.resultList.currentRow() > -1:
            self.postEpisode(self.resultList.currentRow())
            self.searchPlanning()

    def postShow(self, item):
        show = self.shows[item];
        request = self.API.postShow(show.id)
        if len(request['errors']) > 0:
            msg = request['errors'][0]['text']
            self.postLabel.setText(msg)
        else:
            self.postLabel.setText("Show " + show.title + " added !" )


    def postEpisode(self, item):
        episode = self.episodes[item];
        request = self.API.postEpisode(episode.id)
        if len(request['errors']) > 0:
            msg = request['errors'][0]['text']
            self.postLabel.setText(msg)
        else:
            self.postLabel.setText("[" + episode.show + "]: " + episode.title + " mark as seen !" )

    def cleanTable(self):
        self.shows = []
        self.episodes = []
        while self.resultList.count() > 0:
            self.resultList.takeItem(0)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec_()
