#! /usr/bin/env python
# author: vin

from parameterized import parameterized,param
import unittest

def add(a, b):
    return a+b

class TestAdd(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @parameterized.expand(
        [
            param(1, 1, 2),
            param(2, 3, 4),
            param('a', 'b', 'ab')
        ]
    )
    def test_001(self, a, b, result):
        self.assertEqual(add(a, b), result)


if __name__ == '__main__':
    unittest.main()