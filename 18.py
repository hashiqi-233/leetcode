# -*- coding: utf-8 -*-
# @Time    : 2020/9/16 0016 22:18
# @Author  : zhengwei
# @File    : 18.py
# @Software: PyCharm

class Solution:
    def fourSum(self, nums, target):
        nums = sorted(nums)
        results = []
        for i in range(len(nums)):
            if nums[i] == nums[i-1] and i!= 0:
                continue
            for j in range(i+1, len(nums)):
                if nums[j] == nums[j-1] and j!=i+1:
                    continue
                left = j + 1
                right = len(nums) - 1
                while left < right and left <= len(nums) - 1:
                    if nums[i] + nums[j] + nums[left] + nums[right] > target:
                        right = right - 1
                    elif nums[i]+ nums[j] + nums[left] + nums[right] < target:
                        left = left + 1
                    else:
                        results.append([nums[i], nums[j], nums[left], nums[right]])
                        right = right - 1
                        left = left + 1
                        while right > left and nums[right] == nums[right + 1]:
                            right = right - 1
                        while right > left and nums[left] == nums[left - 1]:
                            left = left + 1
        return results
test = Solution()
result = test.fourSum([-1,-5,-5,-3,2,5,0,4], -7)
print(result)



