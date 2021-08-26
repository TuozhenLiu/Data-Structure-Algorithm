import unittest
from typing import List
from Binary_Search.Find_First_and_Last_Position_of_Element_in_Sorted_Array import Solution


# def findKthSortedArrays(nums1: List[int], nums2: List[int], k) -> int:
#     left, right = 0, k
#     while True:
#         pointer1 = (left + right) // 2
#         pointer2 = k - pointer1
#         if nums1[pointer1 + 1] < nums2[pointer2]:
#             left = pointer1
#         elif nums1[pointer1] > nums2[pointer2 + 1]:
#             right = pointer1
#         else:
#             return max(nums1[pointer1], nums2[pointer2])


class MyTestCase(unittest.TestCase):
    def test_something(self):
        MySolution = Solution()
        self.assertEqual(MySolution.searchRange(nums=[5, 7, 7, 8, 8, 10], target=6), [-1, -1])
        # self.assertEqual(MySolution.searchRange(nums=[1], target=1), [0, 0])
        # self.assertEqual(MySolution.searchRange(nums=[1], target=4), -1)
    # def test(self):
    #     nums1 = [1, 3, 5]
    #     nums2 = [2, 4, 6]
    #     k = 3
    #     self.assertEqual(findKthSortedArrays(nums1,  nums2, k), 3)


if __name__ == '__main__':
    unittest.main()
