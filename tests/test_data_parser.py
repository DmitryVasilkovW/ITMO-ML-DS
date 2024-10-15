import unittest

from ebay_parser.service.data_parser import DataParser


class TestDataParser(unittest.TestCase):
    def test_fetch_page(self):
        parser = DataParser("https://www.ebay.com/b/Electronics/bn_7000259124")
        html = parser.fetch_page("https://www.ebay.com/b/Electronics/bn_7000259124")
        self.assertIn('<html', html)


if __name__ == '__main__':
    unittest.main()
