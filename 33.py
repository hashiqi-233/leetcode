# -*- coding: utf-8 -*-
# @Time    : 2020/10/18 0018 14:58
# @Author  : zhengwei
# @File    : 33.py
# @Software: PyCharm

class Solution:
    def search(self, nums, target):
        if len(nums) == 0:
            return -1
        start, end = 0, len(nums)-1
        while start <= end:
            mid = (start+end) // 2
            if target == nums[mid]:
                return mid
            # 左边是有序的
            if nums[0] <= nums[mid]:
                if nums[0] <= target < nums[mid]:
                    end = mid-1
                else:
                    start = mid+1
            # 右边是有序的
            else:
                if nums[mid] < target <= nums[len(nums)-1]:
                    start = mid+1
                else:
                    end = mid-1
        return -1

test = Solution()
result = test.search([4,5,6,7,0,1,2], 0)
print(result)




