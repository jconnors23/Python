# test_first_pilot.py
# Description: This file contains the tests for the first pilot study.
import unittest
import time 
from first_pilot import sum_list

class TestFirstPilot(unittest.TestCase):
    def test_sum_list(self):
        self.assertEqual(sum_list([1, 2, 3, 4, 5]), 15)
        self.assertEqual(sum_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 55)
        self.assertEqual(sum_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), 120)
        self.assertEqual(sum_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), 210)
        self.assertEqual(sum_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]), 325)

if __name__ == '__main__':
    unittest.main()