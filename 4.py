# -*- coding: utf-8 -*-
# @Time    : 2020/8/9 0009 21:51
# @Author  : zhengwei
# @File    : 4.py
# @Software: PyCharm

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        l1 = len(nums1)
        l2 = len(nums2)
        results = []
        i = 0
        j = 0
        while i <= l1-1 or j <= l2-1:
            if i <= l1-1 and j <= l2-1:
                if nums1[i] > nums2[j]:
                    results.append(nums2[j])
                    j = j+1
                else:
                    results.append(nums1[i])
                    i = i+1
            elif i <= l1-1 and j > l2-1:
                results.append(nums1[i])
                i = i+1
            elif i >l1-1 and j <= l2-1:
                results.append(nums2[j])
                j = j+1
        m = len(results)
        if m % 2 == 0:
            return (results[int(m/2)]+results[int(m/2-1)])/2
        else:
            return results[int(m//2)]
test = Solution()
results = test.findMedianSortedArrays([1,3], [2,4])
print(results)






