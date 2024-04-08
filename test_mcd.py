''' test_mcd.py '''
import unittest
from mcd import mcd

class TestStringMethods(unittest.TestCase):
    ''' class to test mcd.py '''
    def test_case_1(self):
        ''' X = 0 input '''
        self.assertEqual(mcd(0, 10), -1)
    def test_case_2(self):
        ''' y = 0 input '''
        self.assertEqual(mcd(10, 0), -1)
    def test_case_3(self):
        ''' x = 1 input '''
        self.assertEqual(mcd(1, 10), 1)
    def test_case_4(self):
        ''' y = 1 input '''
        self.assertEqual(mcd(10, 1), 1)
    def test_case_5(self):
        ''' x = y input '''
        self.assertEqual(mcd(10, 10), 10)
    def test_case_6(self):
        ''' x > y input '''
        self.assertEqual(mcd(10, 5), 5)
    def test_case_7(self):
        ''' y > x input '''
        self.assertEqual(mcd(5, 10), 5)

if __name__ == '__main__':
    unittest.main()
