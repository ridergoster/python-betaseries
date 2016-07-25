#!/usr/bin/python
import requests
import sys
import ast

class BetaSeriesAPI:
    'class for a show on BetaSeries'

    def __init__(self, apiKey = "", accessToken = ""):
        self.apiKey = apiKey
        self.accessToken = accessToken

    def setAccessToken(self, accessToken = ""):
        self.accessToken = accessToken

    def setApiKey(self, apiKey = ""):
        self.apiKey = apiKey

    def getApiKey(self):
        return self.apiKey

    def getAccessToken(self):
        return self.accessToken

    def login(self, login, pwd):
        headers = {'X-BetaSeries-Key': self.apiKey}
        payload = {'login': login, 'password': pwd}
        url = 'https://api.betaseries.com/members/auth'
        r = requests.post(url, params=payload, headers=headers)
        res = r.json()
        return res

    def subscribe(self, login, pwd, email):
        headers = {'X-BetaSeries-Key': self.apiKey}
        payload = {'login': login, 'password': pwd, 'email': email}
        url = 'https://api.betaseries.com/members/signup'
        r = requests.post(url, params=payload, headers=headers)
        res = r.json()
        return res

    def getShows(self, search = ""):
        headers = {'X-BetaSeries-Key': self.apiKey}
        payload = {'title': search}
        if len(self.accessToken) > 0:
            payload = {'title': search, 'access_token': self.accessToken}
        url = 'https://api.betaseries.com/shows/search'
        r = requests.get(url, params=payload, headers=headers)
        res = r.json()
        return res

    def getMemberInformation(self):
        headers = {'X-BetaSeries-Key': self.apiKey}
        payload = {'access_token': self.accessToken}
        url = 'https://api.betaseries.com/members/infos'
        r = requests.get(url, params=payload, headers=headers)
        res = r.json()
        return res

    def getEpisodes(self):
        headers = {'X-BetaSeries-Key': self.apiKey}
        payload = {'access_token': self.accessToken}
        url = 'https://api.betaseries.com/episodes/list'
        r = requests.get(url, params=payload, headers=headers)
        res = r.json()
        return res

    def postShow(self, showId):
        headers = {'X-BetaSeries-Key': self.apiKey}
        payload = {'id': showId, 'access_token': self.accessToken}
        url = 'https://api.betaseries.com/shows/show'
        r = requests.post(url, params=payload, headers=headers)
        res = r.json()
        return res

    def postEpisode(self, episodeId):
        headers = {'X-BetaSeries-Key': self.apiKey}
        payload = {'id': episodeId, 'access_token': self.accessToken}
        url = 'https://api.betaseries.com/episodes/watched'
        r = requests.post(url, params=payload, headers=headers)
        res = r.json()
        return res
