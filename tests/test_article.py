import unittest
from app.models import Article


class TestArticle(unittest.TestCase):
    '''
    Test Class to test the behaviours we want in our application
    '''

def setUp(self):
    '''
    Test Function that runs before every Test. Which is built in unittest 
    function.
    '''
    self.new_article = Artilce('cnbc',
                                'CNBC',
                                'CNBC',
                                'samsung switches mid-tier smartphone strategy to boost growth',
                                'Samsung is packing more tech into its mid-priced smartphones to appeal to millennials',
                                'https://www.cnbc.com/2018/09/03/samsung-switches-mid-tier-smartphone-strategy-to-boost-growth.html',
                                'https://fm.cnbc.com/applications/cnbc.com/resources/img/editorial/2018/08/13/105392844-1534155878558gettyimages-1014049982.1910x1000.jpeg?v=1534159196',
                                '2018-09-03T10:38:55Z') 

def test_instance(self):
    self.assertTrue(isinstance(self.new_article,Article))
