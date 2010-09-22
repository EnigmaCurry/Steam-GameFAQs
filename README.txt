################################################################################
### 
### Steam GameFAQs
###
### An enhanced GameFAQs browser for searching within Steam games.
###
################################################################################


About
=====

Video Games are hard these days. GameFAQs used to be considered
cheating, but I can hardly play a game like Oblivion or Fallout 3
without looking _something_ up.

The problem: Alt-tabbing out of the game to go to your web browser is
living on the edge: sometimes it works... often it crashes the game.

Steam is great though and they've provided an in-game browser
seemingly for just this purpose. Press shift-tab and click web browser
and away you go.

But then you realize something: the in-game steam browser is _really_
basic and is missing one critical feature to make GameFAQs actually
useful: search.

This tool provides a proxy to GameFAQs and injects javascript search
functionality into the page, thus allowing you to search for that
specific uber-death-armor you've been dungeon crawling for the last
half hour for.

Usage
=====

This is just your standard a Pylons application. You'll need Python
(2.6+) and Setuptools installed. Then run:

   python setup.py develop

That will download the rest of the dependencies and install them for
you. Now you should be able to start the server:

   paster serve development.ini

Building an .exe
================

I wanted this to be easy to use for Steam gamers that are not
necessarily Pythonistas, nor even programmers. So, you may want a
standalone exe version of the app. 

This is one of those black-magic arts of Python. Py2exe used to work
great, but that was before setuptools really caught on. I've never
gotten it to work with Python eggs.

BBFreeze is an alternative, and so far I've had OK results. The one
(huge) caveat is I can't get it to find the right dependencies
auto-magically. Either it finds none of them or it copies my entire
site-packages directory. I've ended up just explicitly listing all the
dependencies, which is a pain, but it works.

Just run:

  python make.py

You'll end up with a target directory with a run_server.bat file.
For distribution, I just make a self-extracting 7zip archive of that directory.
