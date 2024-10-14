import unittest
from ebay_parser.parser import parse_ebay

class TestEbayParser(unittest.TestCase):
    def test_parse_ebay(self):
        data = parse_ebay()
        self.assertTrue(len(data) > 0)
        self.assertIn("title", data.columns)

if __name__ == '__main__':
    unittest.main()
