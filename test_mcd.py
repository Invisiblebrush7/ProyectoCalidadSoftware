''' test_mcd.py '''
import unittest
from mcd import mcd

class TestStringMethods(unittest.TestCase):
    ''' class to test mcd.py '''
    def test_case_1(self):
        ''' Negative input '''
        self.assertEqual(mcd(-1, 10), -1)
    def test_case_2(self):
        ''' input as 1 '''
        self.assertEqual(mcd(1, 10), 1)
    def test_case_3(self):
        ''' Same input '''
        self.assertEqual(mcd(10, 10), 10)
    def test_case_4(self):
        ''' x > y '''
        self.assertEqual(mcd(10, 5), 5)
    def test_case_5(self):
        ''' y > x '''
        self.assertEqual(mcd(5, 10), 5)

if __name__ == '__main__':
    unittest.main()
