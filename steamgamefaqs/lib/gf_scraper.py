"""Service to scrape GameFAQs for the urls to the FAQs"""

import urllib2
from pyquery import PyQuery as pq
import urlparse

base_url = "http://www.gamefaqs.com"
title_search_path = "/search/index.html?game=%s"


class Game(object):
    def __init__(self, title, url, pod=None):
        self.title = title
        self.url = urlparse.urljoin(base_url,url)
        if not self.url.endswith("/"):
            self.url = self.url + "/"
        self.pod = None
        try:
            self.platform = urlparse.urlparse(self.url).path.split("/")[1]
        except IndexError:
            self.platform = None
    def __repr__(self):
        return "<Game title='%s' url='%s'>" % (self.title,self.url)
    def __json__(self):
        d = {}
        d['title'] = self.title
        d['url'] = self.url
        d['pod'] = self.pod
        d['platform'] = self.platform
        return d

class FAQ(object):
    def __init__(self, title, url, date=None, author=None, version=None, 
                 size=None, pod=None):
        self.title = title
        self.url = urlparse.urljoin(base_url,url)
        self.date = date
        self.author = author
        self.version = version
        self.size = size
        self.pod = pod
    def __repr__(self):
        return "<FAQ title='%s' url='%s'>" % (self.title, self.url)
    def __json__(self):
        d = {}
        d['title'] = self.title
        d['url'] = self.url
        d['date'] = self.date
        d['author'] = self.author
        d['version'] = self.version
        d['size'] = self.size
        d['pod'] = self.pod
        return d

def search_games(title):
    query = (base_url + title_search_path) % (urllib2.quote(title))
    src = urllib2.urlopen(query).read()
    #Results are divided into "pods": Best Matches, Good Matches etc.
    candidates = []
    page = pq(src)
    for pod in page("div.pod"):
        pod = pq(pod)
        pod_title = pod("h2.title").text()
        for tr in pod("tr"):
            tr = pq(tr)
            try:
                td = pq(tr("td")[1])
            except IndexError:
                continue
            a = td("a:first")
            if len(a) < 1:
                continue
            game = Game(a.text(),a.attr("href"), pod_title)
            candidates.append(game)
    return candidates

def game_faqs(game_url):
    query = urlparse.urljoin(game_url,"faqs")
    print query
    src = urllib2.urlopen(query).read()
    page = pq(src)
    faqs = []
    for pod in page("div.pod"):
        pod = pq(pod)
        pod_title = pod("h2.title").text()
        for tr in pod("tr"):
            tr = pq(tr)
            print tr.html()
            td = tr("td")
            try:
                title_td = pq(td[0])
            except IndexError:
                continue
            title = title_td.text()
            url = title_td("a:first").attr("href")
            try:
                date = pq(td[1]).text()
            except IndexError:
                date = None
            try:
                author = pq(td[2]).text()
            except IndexError:
                author = None
            try:
                version = pq(td[3]).text()
            except IndexError:
                version = None
            try:
                size = pq(td[4]).text()
            except IndexError:
                size = None
            faq = FAQ(title, url, date, author, version, size, pod_title)
            faqs.append(faq)
    return faqs
