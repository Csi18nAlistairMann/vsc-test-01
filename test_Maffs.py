# 
# Simple unit tests of the 'Maffs' class elsewhere. 
# Based on https://docs.python.org/3/library/unittest.html

import unittest
from class_Maffs import Maffs

class TestMaffsMethods(unittest.TestCase):
    def test_most_common(self):
        maffs = Maffs
        self.assertEqual(maffs.average_of_three_non_zeroes(maffs, 3, 3, 3),
                        3)

    def test_v1_zero(self):
        maffs = Maffs
        self.assertEqual(maffs.average_of_three_non_zeroes(maffs, 0, 3, 3),
                        -1)

    def test_v2_zero(self):
        maffs = Maffs
        self.assertEqual(maffs.average_of_three_non_zeroes(maffs, 3, 0, 3),
                        -1)

    def test_v3_zero(self):
        maffs = Maffs
        self.assertEqual(maffs.average_of_three_non_zeroes(maffs, 3, 3, 0),
                        -1)

    def test_v1v2_zero(self):
        maffs = Maffs
        self.assertEqual(maffs.average_of_three_non_zeroes(maffs, 0, 0, 3),
                        -1)

    def test_v2v3_zero(self):
        maffs = Maffs
        self.assertEqual(maffs.average_of_three_non_zeroes(maffs, 3, 0, 0),
                        -1)

    def test_v1v3_zero(self):
        maffs = Maffs
        self.assertEqual(maffs.average_of_three_non_zeroes(maffs, 0, 3, 0),
                        -1)

    def test_v1v2v3_zero(self):
        maffs = Maffs
        self.assertEqual(maffs.average_of_three_non_zeroes(maffs, 0, 0, 0),
                        -1)

    def test_v1v2v3_zero(self):
        maffs = Maffs
        self.assertEqual(maffs.average_of_three_non_zeroes(maffs, 0, 0, 0),
                        -1)

if __name__ == '__main__':
    unittest.main()