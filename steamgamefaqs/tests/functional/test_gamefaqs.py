from steamgamefaqs.tests import *

class TestGamefaqsController(TestController):

    def test_index(self):
        response = self.app.get(url(controller='gamefaqs', action='index'))
        # Test response...
