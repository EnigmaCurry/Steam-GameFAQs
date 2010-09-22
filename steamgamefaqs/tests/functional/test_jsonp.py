from steamgamefaqs.tests import *

class TestJsonpController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='jsonp', action='index'))
        # Test response...
