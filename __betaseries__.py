#!/usr/bin/python
from sys import exit
import os
import ast

class Show:
    'class for a show on BetaSeries'

    def __init__(self, id = 0, title = '', description = '', seasons = '', episodes = '', followers = '', creation = '', genres = [], length = '', rating = '', network = '', language = '', user = {}):
        self.id = id
        self.title = title
        self.description = description
        self.seasons = seasons
        self.episodes = episodes
        self.followers = followers
        self.creation = creation
        self.genres = genres
        self.length = length
        self.rating = rating
        self.network = network
        self.language = language
        self.user = user

    def convertDict(self, res):
        self.id = res['id']
        self.title = res['title']
        self.description = res['description']
        self.seasons = res['seasons']
        self.episodes = res['episodes']
        self.followers = res['followers']
        self.creation = res['creation']
        self.genres = res['genres']
        self.length = res['length']
        self.rating = res['rating']
        self.network = res['network']
        self.language = res['language']
        self.user = UserShow().convertDict(res['user'])
        return self

    def display(self):
        if not self.user.status:
            msg = self.title +  " (" + self.creation + ") [season: " + self.seasons + " episodes: " + self.episodes + "]"
        else:
            msg = self.title +  " (" + self.creation + ") [season: " + self.seasons + " episodes: " + self.episodes + "] - User Completion : " + str(self.user.status) + "%"

        return msg

class UserLogin:
    def __init__(self, id=0, login = '', password = '', token = ''):
        self.id = id
        self.login = login
        self.password = password
        self.token = token
        self.whip = ()

    def reading(self):
        if os.path.isfile("data.txt") == False or os.stat("data.txt").st_size == 0:
            return
        with open('data.txt', 'r') as f:
            s = f.read()
            self.whip = ast.literal_eval(s)
        self.id = self.whip[0]
        self.login = self.whip[1]
        self.password = self.whip[2]
        self.token = self.whip[3]

    def writing(self):
        self.whip = self.id, self.login, self.password, self.token
        target = open('data.txt', 'a')
        target.seek(0)
        target.truncate()
        target.write(str(self.whip))
        print self.whip

    def convertDict(self, res):
        print res
        self.id = res['user']['id']
        self.login = res['user']['login']
        self.token = res['token']
        print res
        return self

class UserShow:
    'class for user information on a show on BetaSeries'

    def __init__(self, archived = '', favorited = '', remaining = 0, status = 0, last = ''):
        self.archived = archived
        self.favorited = favorited
        self.remaining = remaining
        self.status = status
        self.last = last

    def convertDict(self, res):
        self.archived = res['archived']
        self.favorited = res['favorited']
        self.remaining = res['remaining']
        self.status = res['status']
        self.last = res['last']
        return self

class Episode:
    'class for user information on a show on BetaSeries'

    def __init__(self, id = 0, show = '', code = '', title = ''):
        self.id = id
        self.show = show
        self.code = code
        self.title = title

    def convertDict(self, res):
        self.id = res['id']
        self.show = res['show']['title']
        self.code = res['code']
        self.title = res['title']
        return self

    def display(self):
        msg = self.show +  " (" + self.code + "): " + self.title
        return msg
