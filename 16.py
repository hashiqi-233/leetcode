# -*- coding: utf-8 -*-
# @Time    : 2020/9/13 0013 9:35
# @Author  : zhengwei
# @File    : 16.py
# @Software: PyCharm
import numpy as np
class Solution:
    def threeSumClosest(self, nums, target):
        nums = sorted(nums)
        min_val = 1000000
        min_abs_value = 100000
        save_s = set()
        for i in range(len(nums)):
            if nums[i] in save_s:
                continue
            save_s.add(nums[i])
            left = i + 1
            right = len(nums) - 1
            while left < right and left <= len(nums) - 1:
                tmp = nums[i] + nums[left] + nums[right]
                if nums[i] + nums[left] + nums[right] > target:
                    if np.abs(tmp-target) <= min_abs_value:
                        min_val = tmp
                        min_abs_value = np.abs(tmp-target)
                    right = right - 1
                elif nums[i] + nums[left] + nums[right] < target:
                    if np.abs(tmp - target) <= min_abs_value:
                        min_val = tmp
                        min_abs_value = np.abs(tmp - target)
                    left = left + 1
                else:
                    if np.abs(tmp - target) <= min_abs_value:
                        min_val = tmp
                        min_abs_value = np.abs(tmp - target)
                        break
        return min_val

test = Solution()
results = test.threeSumClosest([1,1,-1,-1,3], 3)
print(results)


