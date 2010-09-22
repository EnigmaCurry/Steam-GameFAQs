import logging

from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from steamgamefaqs.lib.decorators import jsonify

import urllib2
from steamgamefaqs.lib.base import BaseController, render
from steamgamefaqs.lib import gf_scraper as scraper

log = logging.getLogger(__name__)

class GamefaqsController(BaseController):

    def index(self):
        # Return a rendered template
        #return render('/gamefaqs.mako')
        # or, return a string
        return render("/gamefaqs.mako")

    def get_remote_page(self):
        """Get the contents of a remote HTTP page"""
        url = request.params['url']
        
        #Get the page
        u = urllib2.urlopen(url)
        page = u.read()
        #Get the encoding
        for p in u.info().plist:
            if p.startswith("charset="):
                enc = p.split("charset=")[-1]
                break
        else:
            enc = "utf-8"
        page = page.decode(enc)
        response.headers['Content-type'] = "text/html; charset=utf-8"
        return page

    @jsonify
    def search_games(self):
        name = request.params['name']
        return {"games": scraper.search_games(name)}

    @jsonify
    def search_faqs(self):
        game_url = request.params['game_url']
        return {"faqs": scraper.game_faqs(game_url)}
