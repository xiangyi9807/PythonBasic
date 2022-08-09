#! /usr/bin/env python
# author: vin

from calculator import Count
import unittest

class MyTest(unittest.TestCase):
    def setUp(self) -> None:
        print(' test case start')

    def tearDown(self) -> None:
        print(' test case end')

class TestAdd(MyTest):
    def test_add01(self):
        a = Count(1,2)
        self.assertEqual(a.add(), 3, 'add test failed')

    def test_add02(self):
        b = Count(2,2)
        self.assertEqual(b.add(), 3, 'add test failed')

class TestSub(MyTest):
    def test_sbu01(self):
        c = Count(2,5)
        self.assertEqual(c.sub(), 3, 'sub test failed')

    def test_sbu02(self):
        d = Count(5,2)
        self.assertEqual(d.sub(), 4, 'sub test failed')

if __name__ == '__main__':
    unittest.main()