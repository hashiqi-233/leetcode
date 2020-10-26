# -*- coding: utf-8 -*-
# @Time    : 2020/10/18 0018 16:13
# @Author  : zhengwei
# @File    : 34.py
# @Software: PyCharm

class Solution:
    def searchRange(self, nums, target):
        if len(nums) == 0:
            return [-1,-1]
        start, end = 0, len(nums)-1
        results = []
        while start <= end:
            mid = (start+end) // 2
            if target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                results.append(mid)
                break
        if len(results) == 0:
            return [-1,-1]
        results = []
        while mid-1 >=0 and nums[mid-1] == nums[mid]:
            mid = mid - 1
        results.append(mid)
        while mid+1 <= len(nums)-1 and nums[mid + 1] == nums[mid]:
            mid = mid + 1
        results.append(mid)
        return results



test = Solution()
result = test.searchRange([1], 1)
print(result)