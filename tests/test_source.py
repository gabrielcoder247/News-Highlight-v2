import unittest
from app.models import Source


class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behavour of the Source class
    '''
    def setUp(self):
        self.new_source = Source(123,'gabriel','business news','/source','general')