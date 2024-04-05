''' test_mcd.py '''
import unittest
from num_max import main

class TestNumMax(unittest.TestCase):
    ''' class to test mcd.py '''
    def test_case_1(self):
        ''' input x is greater that y and z '''
        self.assertEqual(main(5, 3, 1), 5)
    def test_case_2(self):
        ''' input y is greater that x and z '''
        self.assertEqual(main(3, 6, 1), 6)
    def test_case_3(self):
        ''' input z is greater that x and y '''
        self.assertEqual(main(1, 1, 4), 4)



if __name__ == '__main__':
    unittest.main()
