# -*- coding: utf-8 -*-
# @Time    : 2020/10/12 0012 19:15
# @Author  : zhengwei
# @File    : 31.py
# @Software: PyCharm

class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        pos1 = 0
        pos2 = 0
        for i in range(-2, -len(nums), -1):
            if nums[i-1] < nums[i+1]:
                pos1 = i
        if pos1 == 0:
            return sorted(nums)
        else:
            for j in range(-1, -len(nums), -1):
                if nums[j] > nums[pos1]:
                    pos2 = j
            nums[pos1], nums[pos2] = nums[pos2],nums[pos1]
            if len(nums[pos1+1:]) > 1:
                result = nums[:pos1+1] + sorted(nums[pos1+1:])
            else:
                result = nums
            return result
test = Solution()
result = test.nextPermutation([3,2,1])
print(result)



