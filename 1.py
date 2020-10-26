# -*- coding: utf-8 -*-
# @Time    : 2020/8/5 0005 19:21
# @Author  : zhengwei
# @File    : 1.py
# @Software: PyCharm

class Solution:
    def twoSum(self, nums, target):
        sort_nums = sorted(nums)
        i = 0
        j = len(sort_nums) - 1
        save_list = []
        while i < j:
            if sort_nums[i] + sort_nums[j] == target:
                save_list.extend([sort_nums[i], sort_nums[j]])
                i = i + 1
                j = j - 1
            elif sort_nums[i] + sort_nums[j] > target:
                j = j - 1
            else:
                i = i + 1
        result = []
        if len(save_list) > 0:
            if save_list[0] == save_list[1]:
                for k in range(len(nums)):
                    if nums[k] == save_list[0]:
                        result.append(k)
            else:
                result.extend([nums.index(save_list[0]), nums.index(save_list[1])])
        return result



test = Solution()
result = test.twoSum([3, 3], 6)
print(result)
