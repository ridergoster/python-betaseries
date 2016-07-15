#!/usr/bin/python

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

    def convertJson(self, res):
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
        self.user = UserShow().convertJson(res['user'])
        return self

    def displayShow(self):
        msg = self.title +  " (" + self.creation + ") [season: " + self.seasons + " episodes: " + self.episodes + "]"
        return msg

class UserShow:
    'class for user information on a show on BetaSeries'

    def __init__(self, archived = '', favorited = '', remaining = 0, status = 0, last = ''):
        self.archived = archived
        self.favorited = favorited
        self.remaining = remaining
        self.status = status
        self.last = last

    def convertJson(self, res):
        self.archived = res['archived']
        self.favorited = res['favorited']
        self.remaining = res['remaining']
        self.status = res['status']
        self.last = res['last']
