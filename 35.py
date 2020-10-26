# -*- coding: utf-8 -*-
# @Time    : 2020/10/18 0018 16:46
# @Author  : zhengwei
# @File    : 35.py
# @Software: PyCharm

class Solution:
    def searchInsert(self, nums, target):
        if len(nums) == 0:
            return 0
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start+end) // 2
            if target > nums[mid]:
                start = mid + 1
            elif target < nums[mid]:
                end = mid - 1
            else:
                return mid
        if nums[mid] < target:
            return mid+1
        else:
            return mid


test = Solution()
result = test.searchInsert([1,3,5,8], 2)
print(result)



