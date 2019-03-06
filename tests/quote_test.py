import unittest
from App.models import Quote
Quote = quote.Quote

class QuoteTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Quote model
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_quote = Quote("Ash",2,'Python Must Be Crazy')
    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Quote))


if __name__ == '__main__':
    unittest.main()