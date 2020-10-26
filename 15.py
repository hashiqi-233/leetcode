# -*- coding: utf-8 -*-
# @Time    : 2020/9/6 0006 12:28
# @Author  : zhengwei
# @File    : 15.py
# @Software: PyCharm

class Solution:
    def threeSum(self, nums):
        nums = sorted(nums)
        results = []
        save_s = set()
        for i in range(len(nums)):
            if nums[i] in save_s:
                continue
            save_s.add(nums[i])
            left = i + 1
            right = len(nums) - 1
            while left < right and left <= len(nums) - 1:
                if nums[i] + nums[left] + nums[right] > 0:
                    right = right - 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left = left + 1
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    right = right - 1
                    left = left + 1
                    while right > left and nums[right] == nums[right + 1]:
                        right = right - 1
                    while right > left and nums[left] == nums[left - 1]:
                        left = left + 1
        return results


test = Solution()
results = test.threeSum([-2,0,1,1,2])
print(results)
