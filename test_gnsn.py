import unittest
from gnsn import gnsn


class GnsnTestCase(unittest.TestCase):
    def test_gnsn_1(self):
        values = gnsn(13, 101)
        length = len(values)
        sum = values.sum()
        result = (length == 13) and (sum == 101)
        self.assertEqual(result, True)

    def test_gnsn_2(self):
        values = gnsn(10, 94)
        length = len(values)
        sum = values.sum()
        result = (length == 10) and (sum == 94)
        self.assertEqual(result, True)


if __name__ == '__main__':
    unittest.main()
