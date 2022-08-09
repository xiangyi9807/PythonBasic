#! /usr/bin/env python
# author: vin

from calculator import Count
import unittest

class TestCount(unittest.TestCase):

    def setUp(self) -> None:
        print('test start')

    def test_add01(self):
        a = Count(1, 2)
        self.assertEqual(a.add(), 3)

    def test_add02(self):
        b = Count(2, 2)
        self.assertEqual(b.add(), 3)

    def tearDown(self) -> None:
        print('test done')

if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(TestCount('test_add01'))
    suit.addTest(TestCount('test_add02'))

    runner = unittest.TextTestRunner()
    runner.run(suit)