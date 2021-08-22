import unittest
from Binary_Search.Binary_Search import Solution


class MyTestCase(unittest.TestCase):

    def test_something(self):
        MySolution = Solution()
        self.assertEqual(MySolution.search(nums=list(range(10)), target=3), 3)
        self.assertEqual(MySolution.search(nums=[1, 3, 4, 6], target=4), 2)
        self.assertEqual(MySolution.search(nums=[1], target=4), -1)


if __name__ == '__main__':
    unittest.main()
