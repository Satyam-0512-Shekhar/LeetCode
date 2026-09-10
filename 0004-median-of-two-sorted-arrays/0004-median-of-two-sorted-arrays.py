class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        result = (nums1 + nums2)
        result.sort()
        n = len(result)
        if n % 2 == 1:
            median = result[n // 2]
        else:
            median = (result[n // 2 - 1] + result[n // 2])/ 2.0
        return median
        